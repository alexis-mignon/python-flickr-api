# -*- encoding: utf-8 -*-
"""
    Object Oriented implementation of Flickr API.

    Important notes:
    - For consistency, the naming of methods might differ from the name
      in the official API. Please check the method "docstring" to know
      what is the implemented method.

    - For methods which expect an object "id", either the 'id' string
      or the object itself can be used as argument. Similar consideration
      holds for lists of id's.

      For instance if "photo_id" is expected you can give call the function
      with named argument "photo=PhotoObject" or with the id string
      "photo_id=id_string".

    Author: Alexis Mignon (c)
    email: alexis.mignon_at_gmail.com
    Date: 05/08/2011
"""
# pylint: disable=method-name-lower-case

from . import method_call
from .flickrerrors import FlickrError
from .reflection import caller, static_caller, FlickrAutoDoc
from six import text_type, iteritems, with_metaclass
from six.moves import UserList, urllib, cStringIO, range
from . import auth
import warnings
from itertools import groupby
import os.path

try:
    from PIL import Image
except ImportError:
    class Image(object):
        @staticmethod
        def open(*args, **kwargs):
            image_module_404 = "\nThe PIL package was not found on this system. Images cannot be displayed." \
                "\nConsider installing PIL or Pillow."
            warnings.warn(image_module_404)
            raise RuntimeError("Image module not found.")



_SIZES_LABEL = {
    'sq': 'Square',
    'q': 'Large Square',
    't': 'Thumbnail',
    's': 'Small',
    'n': 'Small 320',
    'm': 'Medium',
    'z': 'Medium 640',
    'c': 'Medium 800',
    'l': 'Large',
    'h': 'Large 1600',
    'k': 'Large 2048',
    'o': 'Original'
}

def dict_converter(keys, func):
    def convert(dict_):
        for k in keys:
            try:
                dict_[k] = func(dict_[k])
            except KeyError:
                pass
    return convert


class FlickrObject(with_metaclass(FlickrAutoDoc, object)):
    """
        Base Object for Flickr API Objects.
        Flickr Objects are dynamically created from the
        named arguments given to the constructor.
    """

    __converters__ = []  # some functions used to convert some result field
    __display__ = []  # The attribute to display when the object is converted
                      # to a string

    def __init__(self, **params):
        params["loaded"] = False
        self._set_properties(**params)

    def _set_properties(self, **params):
        for c in self.__class__.__converters__:
            c(params)
        self.__dict__.update(params)

    def setToken(self, filename=None, token=None, token_key=None,
                 token_secret=None):
        """
            Set the authentication token to use with the object.
        """
        if token is None:
            token = auth.token_factory(filename=filename, token_key=token_key,
                                       token_secret=token_secret)
        self.__dict__["token"] = token

    def getToken(self):
        """
            Get the authentication token is any.
        """
        return self.__dict__.get("token", None)

    def __getattr__(self, name):
        if name == 'id' and name not in self.__dict__:
            raise AttributeError(
              "'%s' object has no attribute '%s'" % (
                    self.__class__.__name__, name)
              )
        if name not in self.__dict__:
            if not self.loaded:
                self.load()
        try:
            return self.__dict__[name]
        except KeyError:
            raise AttributeError(
                "'%s' object has no attribute '%s'" % (
                     self.__class__.__name__, name
                    )
                )

    def __setattr__(self, name, values):
        raise FlickrError("Readonly attribute")

    def get(self, key, *args, **kwargs):
        return self.__dict__.get(key, *args, **kwargs)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        raise FlickrError("Read-only attribute")

    def __str__(self):
        vals = []
        for k in self.__class__.__display__:
            val_found = False
            try:
                value = self.__dict__[k]
                val_found = True
            except KeyError:
                self.load()
                try:
                    value = self.__dict__[k]
                    val_found = True
                except KeyError:
                    pass
            if not val_found:
                continue
            if isinstance(value, text_type):
                value = value.encode("utf8")
            if isinstance(value, str):
                value = "'%s'" % value
            else:
                value = str(value)
            if len(value) > 20:
                value = value[:20] + "..."
            vals.append("%s=%s" % (k, value))
        return "%s(%s)" % (self.__class__.__name__, ", ".join(vals))

    def __repr__(self):
        return str(self)

    def getInfo(self):
        """
            Returns object information as a dictionary.
            Should be overriden.
        """
        return {}

    def load(self):
        props = self.getInfo()
        self.__dict__["loaded"] = True
        self._set_properties(**props)


class FlickrList(UserList):
    def __init__(self, data=[], info=None):
        UserList.__init__(self, data)
        self.info = info

    def __str__(self):
        return '%s;%s' % (str(self.data), str(self.info))

    def __repr__(self):
        return '%s;%s' % (repr(self.data), repr(self.info))


class Activity(FlickrObject):
    @static_caller("flickr.activity.userPhotos")
    def userPhotos(**args):
        return args, _extract_activity_list

    @static_caller("flickr.activity.userComments")
    def userComments(**args):
        return args, _extract_activity_list


class Blog(FlickrObject):
    __display__ = ["id", "name"]
    __converters__ = [
        dict_converter(["needspassword"], bool),
    ]
    __self_name__ = "blog_id"

    @caller("flickr.blogs.postPhoto")
    def postPhoto(self, **args):
        return _format_id("photo", args), lambda r: None


class BlogService(FlickrObject):
    __display__ = ["id", "text"]
    __self_name__ = "service"

    @caller("flickr.blogs.getList")
    def getList(self, **args):
        try:
            args["service"] = args["service"].id
        except (KeyError, AttributeError):
            pass

        def format_result(r, token=None):
            return [Blog(token=token, **b)
                       for b in _check_list(r["blogs"]["blog"])]

        return args, format_result

    @caller("flickr.blogs.postPhoto")
    def postPhoto(self, **args):
        return _format_id(args), _none

    @static_caller("flickr.blogs.getServices")
    def getServices():
        return ({},
                lambda r: [BlogService(**s)
                          for s in _check_list(r["services"]["service"])]
               )


class Camera(FlickrObject):
    __display__ = ["name"]
    __self_name__ = "camera"

    class Brand(FlickrObject):
        __display__ = ["name"]
        __self_name__ = "brand"

        @static_caller("flickr.cameras.getBrands")
        def getList():
            return ({},
                    lambda r: [Camera.Brand(**b) for b in r["brands"]["brand"]]
            )

        @caller("flickr.cameras.getBrandModels")
        def getModels(self):
            return ({},
                   lambda r: [Camera(**m) for m in r["cameras"]["camera"]]
            )


class Collection(FlickrObject):
    __display__ = ["id", "title"]
    __self_name__ = "collection_id"

    @caller("flickr.collections.getInfo")
    def getInfo(self, **args):
        def format_result(r):
            collection = r["collection"]
            icon_photos = _check_list(collection["iconphotos"]["photo"])
            photos = []
            for p in photos:
                p["owner"] = Person(p["owner"])
                photos.append(Photo(**p))
            collection["iconphotos"] = photos
            return collection
        return args, format_result

    @caller("flickr.stats.getCollectionStats")
    def getStats(self, date, **args):
        args["date"] = date
        return args, lambda r: int(r["stats"]["views"])

    @caller("flickr.collections.getTree")
    def getTree(self, **args):
        def format_result(r, token=None):
            collections = _check_list(r["collections"])
            collections_ = []
            for c in collections:
                sets = _check_list(c.pop("set"))
                sets_ = [Photoset(token=token, **s) for s in sets]
                collections_.append(Collection(token=token, sets=sets_, **c))
            return collections_
        return _format_id("user", args), format_result


class CommonInstitution(FlickrObject):
    __display__ = ["id", "name"]

    @static_caller("flickr.commons.getInstitutions")
    def getInstitutions():
        def format_result(r):
            institutions = _check_list(r["institutions"]["institution"])
            institutions_ = []
            for i in institutions:
                urls = _check_list(i['urls']['url'])
                urls_ = []
                for u in urls:
                    u["url"] = u.pop("text")
                    urls_.append(CommonInstitutionUrl(**u))
                i["urls"] = urls_
                institutions_.append(CommonInstitution(id=i["nsid"], **i))
            return institutions_
        return {}, format_result


class CommonInstitutionUrl(FlickrObject):
    pass


class Contact(FlickrObject):
    @static_caller("flickr.contacts.getList")
    def getList(self, **args):
        def format_result(r):
            info = r["contacts"]
            contacts = [Person(id=c["nsid"], **c)
                         for c in _check_list(info["contact"])]
            return FlickrList(contacts, Info(**info))
        return args, format_result

    @static_caller("flickr.contacts.getListRecentlyUploaded")
    def getListRecentlyUploaded(self, **args):
        def format_result(r):
            info = r["contacts"]
            contacts = [Person(id=c["nsid"], **c)
                         for c in _check_list(info["contact"])]
            return FlickrList(contacts, Info(**info))
        return args, format_result

    @static_caller("flickr.contacts.getTaggingSuggestions")
    def getTaggingSuggestions(self, **args):
        def format_result(r):
            info = r["contacts"]
            contacts = [Person(id=c["nsid"], **c)
                         for c in _check_list(info["contact"])]
            return FlickrList(contacts, Info(**info))
        return args, format_result


class Gallery(FlickrObject):
    __display__ = ["id", "title"]
    __converters__ = [
        dict_converter(["date_create", "date_update", "count_photos",
                        "count_videos"], int),
    ]
    __self_name__ = "gallery_id"

    @caller("flickr.galleries.addPhoto")
    def addPhoto(self, **args):
        return _format_id("photo", args), _none

    @static_caller("flickr.galleries.create")
    def create(**args):
        return _format_id("primary_photo", args), lambda r: Gallery(**r["gallery"])

    @caller("flickr.galleries.editMeta")
    def editMedia(self, **args):
        return args, _none

    @caller("flickr.galleries.editPhoto")
    def editPhoto(self, **args):
        return _format_id("photo", args), _none

    @caller("flickr.galleries.editPhotos")
    def editPhotos(self, **args):
        if "photos" in args:
            args["photo_ids"] = [p.id for p in args.pop("photos")]
        photo_ids = args["photo_ids"]
        if isinstance(photo_ids, list):
            args["photo_ids"] = ", ".join(photo_ids)
        return _format_id("primary_photo", args), _none

    @static_caller("flickr.urls.lookupGallery")
    def getByUrl(url):
        def format_result(r):
            gallery = r["gallery"]
            gallery["owner"] = Person(id=gallery["owner"])
            return Gallery(**gallery)
        return {'url': url}, format_result

    @caller("flickr.galleries.getInfo")
    def getInfo(self):
        def format_result(r, token=None):
            gallery = r["gallery"]
            gallery["owner"] = Person(id=gallery["owner"])
            try:
                pp_id = gallery.pop("primary_photo_id")
                pp_secret = gallery.pop("primary_photo_secret")
                pp_farm = gallery.pop("primary_photo_farm")
                pp_server = gallery.pop("primary_photo_server")
                gallery["primary_photo"] = Photo(id=pp_id, secret=pp_secret,
                                                 server=pp_server, farm=pp_farm,
                                                 token=token)
            except KeyError:
                pass
            return gallery
        return {}, format_result

    @caller("flickr.galleries.getPhotos")
    def getPhotos(self, **args):
        return _format_extras(args), _extract_photo_list


class Category(FlickrObject):
    __display__ = ["id", "name"]


class Info(FlickrObject):
    __converters__ = [
        dict_converter(["page", "perpage", "pages", "total", "count"], int)

    ]
    __display__ = ["page", "perpage", "pages", "total", "count"]
    pass


class Group(FlickrObject):
    __converters__ = [
        dict_converter(["members", "privacy"], int),
        dict_converter(["admin", "eighteenplus", "invistation_only"], bool)
    ]
    __display__ = ["id", "name"]
    __self_name__ = "group_id"

    class Topic(FlickrObject):
        __display__ = ["id", "subject"]
        __self_name__ = "topic_id"

        class Reply(FlickrObject):
            __display__ = ["id"]
            __self_name__ = "reply_id"

            def getToken(self):
                return self.topic.getToken()

            @staticmethod
            def _format_reply(reply):
                author = {
                    'id': reply.pop("author"),
                    'role': reply.pop("role"),
                    'is_pro': bool(reply.pop("is_pro")),
                }
                reply["author"] = Person(**author)
                return reply

            @caller("flickr.groups.discuss.replies.getInfo")
            def getInfo(self, **args):
                return args, lambda r: self._format_reply(r["reply"])

            @caller("flickr.groups.discuss.replies.delete")
            def delete(self, **args):
                args["topic_id"] = self.topic.id

        def getToken(self):
            return self.group.getToken()

        @caller("flickr.groups.discuss.replies.add")
        def addReply(self, **args):
            return args, _none

        @staticmethod
        def _format_topic(topic):
            """ reformat a topic dict
            """

            author = {
                'id': topic.pop("author"),
                'is_pro': bool(topic.pop('is_pro')),
                'role': topic.pop("role"),
            }
            topic["author"] = Person(**author)
            return topic

        @caller("flickr.groups.discuss.topics.getInfo")
        def getInfo(self, **args):
            def format_result(r):
                return self._format_topic(r["topic"])
            return args, format_result

        @caller("flickr.groups.discuss.replies.getList")
        def getReplies(self, **args):
            def format_result(r):
                info = r["replies"]
                return FlickrList(
                    [Group.Topic.Reply(topic=self,
                                       **Group.Topic.Reply._format_reply(rep))
                            for rep in info.pop("reply", [])],
                     Info(**info)
                )
            return args, format_result

        @caller("flickr.groups.discuss.replies.delete")
        def delete(self, **args):
            args["topic_id"] = self.topic.id
            return args, _none

        @caller("flickr.groups.discuss.replies.edit")
        def edit(self, **args):
            args["topic_id"] = self.topic.id
            return args, _none

    @caller("flickr.groups.discuss.topics.add")
    def addDiscussTopic(**args):
        return args, _none

    @static_caller("flickr.groups.browse")
    def browse(**args):
        def format_result(r, token):
            cat = r["category"]
            subcats = [Category(**c) for c in _check_list(cat.pop("subcats"))]
            groups = [Group(id=g["nsid"], **g)
                       for g in _check_list(cat.pop("group"))]
            return Category(id=args["cat_id"], subcats=subcats, groups=groups,
                            **cat)
        return _format_id("cat", args), format_result

    @caller("flickr.groups.getInfo")
    def getInfo(self, **args):
        return args, lambda r: r["group"]

    @caller("flickr.urls.getGroup")
    def getUrl(self, **args):
        return args, lambda r: r["group"]["url"]

    @static_caller("flickr.urls.lookupGroup")
    def getByUrl(url, **args):
        args["url"] = url

        def format_result(r):
            group = r["group"]
            group["name"] = group.pop("groupname")
            return Group(**group)
        return args, format_result

    @static_caller("flickr.groups.search")
    def search(**args):
        def format_result(r, token):
            info = r["groups"]
            groups = [Group(id=g["nsid"], **g) for g in info.pop("group")]
            return FlickrList(groups, Info(**info))
        return args, format_result

    @caller("flickr.groups.members.getList")
    def getMembers(self, **args):
        try:
            membertypes = args["membertypes"]
            if isinstance(membertypes, list):
                args["membertypes"] = ", ".join([str(i) for i in membertypes])
        except KeyError:
            pass

        def format_result(r):
            info = r["members"]
            return FlickrList(
                [Person(**p) for p in _check_list(info.pop("member"))],
                 Info(**info)
            )
        return args, format_result

    @caller("flickr.groups.pools.add")
    def addPhoto(self, **args):
        return _format_id("photo", args), _none

    @caller("flickr.groups.pools.getContext")
    def getPoolContext(self, **args):
        return (_format_id("photo", args),
                lambda r: (Photo(**r["prevphoto"]), Photo(r["nextphoto"]))
        )

    @caller("flickr.groups.discuss.topics.getList")
    def getDiscussTopics(self, **args):
        def format_result(r):
            info = r["topics"]
            return FlickrList(
                [Group.Topic(group=self, **Group.Topic._format_topic(t))
                    for t in info.pop("topic", [])],
                Info(**info)
            )
        return args, format_result

    @static_caller("flickr.groups.pools.getGroups")
    def getGroups(**args):
        def format_result(r, token):
            info = r["groups"]
            return FlickrList(
                [Group(token=token, **g) for g in info.pop("group", [])],
                 Info(**info)
            )
        return args, format_result

    @static_caller("flickr.people.getGroups")
    def getMemberGroups(**args):
        def format_result(r, token):
            info = r["groups"]
            return FlickrList(
                [Group(token=token, **g) for g in info.pop("group", [])],
                 Info(**info)
            )
        return args, format_result

    @caller("flickr.groups.pools.getPhotos")
    def getPhotos(self, **args):
        return _format_extras(args), _extract_photo_list

    @caller("flickr.groups.pools.remove")
    def removePhoto(self, **args):
        return _format_id("photo", args), _none

    @caller("flickr.groups.join")
    def join(self, **args):
        return args, _none

    @caller("flickr.groups.joinRequest")
    def joinRequest(self, **args):
        return args, _none

    @caller("flickr.groups.leave")
    def leave(self, **args):
        return args, _none


class License(FlickrObject):
    __display__ = ["id", "name"]
    __self_name__ = "license_id"

    @static_caller("flickr.photos.licenses.getInfo")
    def getList():
        def format_result(r):
            licenses = r["licenses"]["license"]
            if not isinstance(licenses, list):
                licenses = [licenses]
            return [License(**l) for l in licenses]
        return {}, format_result


class Location(FlickrObject):
    __display__ = ["latitude", "longitude", "accuracy"]
    __converters__ = [
        dict_converter(["latitude", "longitude"], float),
        dict_converter(["accuracy"], int),
    ]


class MachineTag(FlickrObject):

    class Namespace(FlickrObject):
        __display__ = ["text", "usage", "predicate"]

    class Pair(FlickrObject):
        __display__ = ["namespace", "text", "usage", "predicate"]

    class Predicate(FlickrObject):
        __display__ = ["usage", "text", "namespaces"]

    class Value(FlickrObject):
        __display__ = ["usage", "namespace", "predicate", "text"]

    @static_caller("flickr.machinetags.getNamespaces")
    def getNamespaces(**args):
        def format_result(r):
            info = r["namespaces"]
            return FlickrList(
                [MachineTag.Namespace(**ns)
                    for ns in _check_list(info.pop("namespace"))],
                Info(**info)
            )
        return args, format_result

    @static_caller("flickr.machinetags.getPairs")
    def getPairs(**args):
        def format_result(r):
            info = r["pairs"]
            return FlickrList(
                [MachineTag.Pair(**p) for p in _check_list(info.pop("pair"))],
                 Info(**info)
            )
        return args, format_result

    @static_caller("flickr.machinetags.getPredicates")
    def getPredicates(**args):
        def format_result(r):
            info = r["predicates"]
            return FlickrList(
                [MachineTag.Predicate(**p)
                    for p in _check_list(info.pop("predicate"))],
                Info(**info)
            )
        return args, format_result

    @static_caller("flickr.machinetags.getRecentValues")
    def getRecentValues(**args):
        def format_result(r):
            info = r["values"]
            return FlickrList(
                [MachineTag.Value(**v)
                    for v in _check_list(info.pop("value"))],
                Info(**info)
            )
        return args, format_result

    @static_caller("flickr.machinetags.getValues")
    def getValues(**args):
        def format_result(r):
            info = r["values"]
            return FlickrList(
                [MachineTag.Value(**v)
                    for v in _check_list(info.pop("value"))],
                Info(**info)
            )
        return args, format_result


class Panda(FlickrObject):
    __display__ = ["name"]
    __self_name__ = 'panda_name'

    @static_caller("flickr.panda.getList")
    def getList():
        return (
            {},
            lambda r: [Panda(name=p, id=p) for p in r["pandas"]["panda"]]
        )

    @caller("flickr.panda.getPhotos")
    def getPhotos(self, **args):
        return _format_extras(args), _extract_photo_list


class Person(FlickrObject):
    __converters__ = [
        dict_converter(["ispro"], bool),
    ]
    __display__ = ["id", "username"]
    __self_name__ = "user_id"

    def __init__(self, **params):
        if not "id" in params:
            if "nsid" in params:
                params["id"] = params["nsid"]
            else:
                raise ValueError("The 'id' or 'nsid' parameter is required")
        FlickrObject.__init__(self, **params)

    @caller("flickr.photos.geo.batchCorrectLocation")
    def batchCorrectLocation(self, **args):
        return _format_id("place", args), _none

    @staticmethod
    def getFromToken(token=None, filename=None, token_key=None,
                     token_secret=None):
        """
            Retrieve the person corresponding to the authentication token.
        """
        if token is None:
            token = auth.token_factory(filename=filename, token_key=token_key,
                                       token_secret=token_secret)
        return test.login(token=token)

    @static_caller("flickr.people.findByEmail")
    def findByEmail(find_email):
        return {'find_email': find_email}, lambda r: Person(**r["user"])

    @static_caller("flickr.people.findByUsername")
    def findByUserName(username):
        return {'username': username}, lambda r: Person(**r["user"])

    @static_caller("flickr.urls.lookupUser")
    def findByUrl(url):
        return {'url': url}, lambda r: Person(**r["user"])

    @caller("flickr.favorites.getContext")
    def getFavoriteContext(self, **args):
        def format_result(r, token=None):
            return (Photo(token=token, **r["prevphoto"]),
                    Photo(token=token, **r["nextphoto"]))
        return _format_id("photo", args), format_result

    @caller("flickr.favorites.getList")
    def getFavorites(self, **args):
        return _format_extras(args), _extract_photo_list

    @caller("flickr.photosets.getList")
    def getPhotosets(self, **args):
        def format_result(r, token=None):
            info = r["photosets"]
            photosets = info.pop("photoset")
            if not isinstance(photosets, list):
                photosets = [photosets]
            return FlickrList(
                [Photoset(token=token, **ps) for ps in photosets],
                 Info(**info)
            )
        return args, format_result

    @caller("flickr.favorites.getPublicList")
    def getPublicFavorites(self, **args):
        return _format_extras(args), _extract_photo_list

    @caller("flickr.people.getInfo")
    def getInfo(self, **args):
        def format_result(r):
            user = r["person"]
            user["photos_info"] = user.pop("photos")
            return user
        return args, format_result

    @caller("flickr.galleries.getList")
    def getGalleries(self, **args):
        def format_result(r, token=True):
            info = r["galleries"]
            galleries = _check_list(info.pop("gallery"))
            galleries_ = []

            for g in galleries:
                g["owner"] = Person(id=g["owner"])
                galleries_.append(g)
            return FlickrList(galleries_, Info(**info))
        return args, format_result

    @caller("flickr.people.getLimits")
    def getLimits(self):
        return {}, lambda r: r

    @caller("flickr.photos.getCounts")
    def getPhotoCounts(self, **args):
        return args, lambda r: r["photocounts"]["photocount"]

    @caller("flickr.people.getPhotos")
    def getPhotos(self, **args):
        return args, _extract_photo_list

    @caller("flickr.urls.getUserPhotos")
    def getPhotosUrl(self):
        return {}, lambda r: r["user"]["url"]

    @caller("flickr.urls.getUserProfile")
    def getProfileUrl(self):
        return {}, lambda r: r["user"]["url"]

    @caller("flickr.people.getPublicPhotos")
    def getPublicPhotos(self, **args):
        return args, _extract_photo_list

    @caller("flickr.people.getPhotosOf")
    def getPhotosOf(self, **args):
        return (_format_id("owner", _format_extras(args)),
               lambda r: _extract_photo_list(r, token=self.getToken()))

    @caller("flickr.contacts.getPublicList")
    def getPublicContacts(self, **args):
        def format_result(r, token=None):
            info = r["contacts"]
            contacts = [Person(id=c["nsid"], token=token, **c)
                                for c in _check_list(info["contact"])]
            return FlickrList(contacts, Info(**info))
        return args, format_result

    @caller("flickr.people.getPublicGroups")
    def getPublicGroups(self, **args):
        def format_result(r, token=None):
            groups = r["groups"]["group"]
            groups_ = []
            for gr in groups:
                gr["id"] = gr["nsid"]
                groups_.append(Group(token=token, **gr))
            return groups_
        return args, format_result

    @static_caller("flickr.people.getUploadStatus")
    def getUploadStatus(**args):
        return args, lambda r: r["user"]

    @caller("flickr.collections.getTree")
    def getCollectionTree(self, **args):
        def format_result(r, token=None):
            collections = _check_list(r["collections"])
            collections_ = []
            for c in collections[0]["collection"]:
                sets = _check_list(c.pop("set"))
                sets_ = [Photoset(token=token, **s) for s in sets]
                collections_.append(Collection(token=token, sets=sets_, **c))
            return collections_
        return _format_id("collection", args), format_result

    @caller("flickr.photos.getContactsPublicPhotos")
    def getContactsPublicPhotos(self, **args):
        return (_format_extras(args),
                lambda r: _extract_photo_list(r, token=self.getToken())
                )

    @caller("flickr.tags.getListUser")
    def getTags(self):
        return {}, lambda r: [Tag(text=t) for t in r["who"]["tags"]["tag"]]

    @caller("flickr.tags.getListUserPopular")
    def getPopularTags(**args):
        return args, lambda r: [Tag(**t) for t in r["who"]["tags"]["tag"]]

    @caller("flickr.favorites.remove")
    def removeFromFavorites(self, **args):
        return _format_id("photo", args), _none

    @static_caller("flickr.photos.getNotInSet")
    def getNotInSetPhotos(**args):
        return _format_extras(args), _extract_photo_list


class Photo(FlickrObject):
    __converters__ = [
        dict_converter(["isfamily", "ispublic", "isfriend", "cancomment",
                        "canaddmeta", "permcomment", "permmeta", "isfavorite"],
                        bool),
        dict_converter(["posted", "lastupdate"], int),
        dict_converter(["views", "comments"], int),
    ]
    __display__ = ["id", "title"]
    __self_name__ = "photo_id"

    class Comment(FlickrObject):
        __display__ = ["id", "author"]
        __self_name__ = "comment_id"

        @caller("flickr.photos.comments.deleteComment")
        def delete(self, **args):
            return args, _none

        @caller("flickr.photos.comments.editComment")
        def edit(self, **args):
            return args, _none

        @static_caller("flickr.photos.comments.getRecentForContacts")
        def getRecentForContacts(**args):
            return _format_extras(args), _extract_photo_list

    class Exif(FlickrObject):
        __display__ = ["tag", "raw"]

    class Note(FlickrObject):
        __display__ = ["id", "text"]
        __self_name__ = "note_id"

        @caller("flickr.photos.notes.edit")
        def edit(self, **args):
            return args, _none

        @caller("flickr.photos.notes.delete")
        def delete(self, **args):
            return args, _none

    class Suggestion(FlickrObject):
        __display__ = ["id"]
        __self_name__ = "suggestion_id"

        @caller("flickr.photos.suggestions.approveSuggestion")
        def approve(self):
            return {}, _none

        @caller("flickr.photos.suggestions.rejectSuggestion")
        def reject(self):
            return {}, _none

        @caller("flickr.photos.suggestions.removeSuggestion")
        def remove(self):
            return {}, _none

    @caller("flickr.photos.people.delete")
    def deletePerson(self, **args):
        return _format_id("user", args), _none

    @caller("flickr.photos.people.deleteCoords")
    def deletePersonCoords(self, **args):
        return _format_id("user", args), _none

    @caller("flickr.photos.people.editCoords")
    def editPersonCoords(self, **args):
        return _format_id("user", args), _none

    @caller("flickr.photos.comments.addComment")
    def addComment(self, **args):
        def format_result(r, token=None):
            args["id"] = r["comment"]["id"]
            args["photo"] = self
            return Photo.Comment(**args)
        return args, format_result

    @caller("flickr.photos.notes.add")
    def addNote(self, **args):
        def format_result(r, token=None):
            args["id"] = r["note"]["id"]
            args["photo"] = self
            return Photo.Note(**args)
        return args, format_result

    @caller("flickr.photos.people.add")
    def addPerson(self, **args):
        return _format_id("user", args), _none

    @caller("flickr.photos.addTags")
    def addTags(self, tags, **args):
        if isinstance(tags, list):
            tags = ", ".join(tags)
        args["tags"] = tags
        return args, _none

    @caller("flickr.favorites.add")
    def addToFavorites(self):
        return {}, _none

    @caller("flickr.photos.geo.correctLocation")
    def correctLocation(self, **args):
        return _format_id("place", args), _none

    @static_caller("flickr.photos.upload.checkTickets")
    def checkUploadTickets(tickets, **args):
        def format_result(r, token=None):
            tickets = r["uploader"]["ticket"]
            if not isinstance(tickets, list):
                tickets = [tickets]
            return [UploadTicket(**t) for t in tickets]
        args["tickets"] = ','.join(tickets)
        return args, format_result

    @caller("flickr.photos.delete")
    def delete(self, **args):
        return args, _none

    @caller("flickr.photos.getAllContexts")
    def getAllContexts(self, **args):
        def format_result(r, token=None):
            photosets = []
            if "set" in r:
                for s in r["set"]:
                    photosets.append(Photoset(token=token, **s))
            pools = []
            if "pool" in r:
                for p in r["pool"]:
                    pools.append(Group(token=token, **p))
            return photosets, pools
        return args, format_result

    @caller("flickr.photos.comments.getList")
    def getComments(self, **args):
        def format_result(r, token=None):
            try:
                comments = r["comments"]["comment"]
            except KeyError:
                comments = []

            comments_ = []
            if not isinstance(comments, list):
                comments = [comments]
            for c in comments:
                author = c["author"]
                authorname = c.pop("authorname")
                c["author"] = Person(id=author, username=authorname,
                                        token=token)
                comments_.append(Photo.Comment(token=token, photo=self, **c))
            return comments_
        return args, format_result

    @caller("flickr.photos.getInfo")
    def getInfo(self, **args):
        def format_result(r, token=None):
            photo = r["photo"]

            owner = photo["owner"]
            owner["id"] = owner["nsid"]
            photo["owner"] = Person(token=token, **owner)

            photo.update(photo.pop("usage"))
            photo.update(photo.pop("visibility"))
            photo.update(photo.pop("publiceditability"))
            photo.update(photo.pop("dates"))

            tags = []
            for t in _check_list(photo["tags"]["tag"]):
                t["author"] = Person(token=token, id=t.pop("author"))
                tags.append(Tag(token=token, **t))
            photo["tags"] = tags
            photo["notes"] = [
                Photo.Note(token=token, **n)
                    for n in _check_list(photo["notes"]["note"])
            ]

            sizes = photo.pop("sizes", None)
            if sizes:
                photo["sizes"] = dict([(s['label'], s) for s in sizes["size"]])

            return photo
        return args, format_result

    @caller("flickr.photos.getContactsPhotos")
    def getContactsPhotos(self, **args):
        def format_result(r, token=None):
            photos = r["photos"]["photo"]
            photos_ = []
            for p in photos:
                photos_.append(Photo(token=token, **p))
            return photos_
        return args, format_result

    @caller("flickr.photos.getContext")
    def getContext(self, **args):
        def format_result(r, token):
            return (Photo(token=token, **r["prevphoto"]),
                    Photo(token=token, **r["nextphoto"]))
        return args, format_result

    @caller("flickr.photos.getExif")
    def getExif(self, **args):
        if hasattr(self, "secret"):
            args["secret"] = self.secret

        def format_result(r):
            try:
                return [Photo.Exif(**e) for e in r["photo"]["exif"]]
            except KeyError:
                return []
        return args, format_result

    @caller("flickr.favorites.getContext")
    def getFavoriteContext(self, **args):
        def format_result(r, token):
            return (Photo(token=token, **r["prevphoto"]),
                    Photo(token=token, **r["nextphoto"]))
        return _format_id("user", args), format_result

    @caller("flickr.photos.getFavorites")
    def getFavorites(self, **args):
        def format_result(r, token):
            photo = r["photo"]
            persons = photo.pop("person")
            persons_ = []
            if not isinstance(persons, list):
                persons = [persons]

            for p in persons:
                p["id"] = p["nsid"]
                persons_.append(Person(token=token, **p))
            infos = Info(**photo)
            return FlickrList(persons_, infos)
        return args, format_result

    @caller("flickr.galleries.getListForPhoto")
    def getGalleries(self, **args):
        def format_result(r):
            info = r["galleries"]
            galleries = _check_list(info.pop("gallery"))
            galleries_ = []

            for g in galleries_:
                g["owner"] = Person(g["owner"])
                pp_id = g.pop("primary_photo_id")
                pp_secret = g.pop("primary_photo_secret")
                pp_farm = g.pop("primary_photo_farm")
                pp_server = g.pop("primary_photo_server")

                g["primary_photo"] = Gallery(
                    id=pp_id, secret=pp_secret,
                    server=pp_server, farm=pp_farm
                )

                galleries_.append(g)

            return FlickrList(galleries_, Info(**info))
        return args, format_result

    @caller("flickr.photos.geo.getPerms")
    def getGeoPerms(self, **args):
        return args, lambda r, token: PhotoGeoPerms(token=token, **r["perms"])

    @caller("flickr.photos.geo.getLocation")
    def getLocation(self, **args):
        def format_result(r, token):
            loc = r["photo"]["location"]
            return Location(token=token, photo=self, **loc)
        return args, format_result

    def getNotes(self):
        """
            Returns the list of notes for a photograph
        """
        return self.notes

    @static_caller("flickr.interestingness.getList")
    def getInteresting(**args):
        return _format_extras(args), _extract_photo_list

    @static_caller("flickr.photos.getRecent")
    def getRecent(**args):
        return _format_extras(args), _extract_photo_list

    @caller("flickr.photos.suggestions.getList")
    def getSuggestions(self, **args):
        def format_result(r):
            info = r["suggestions"]
            suggestions_ = _check_list(info.pop("suggestion"))
            suggestions = []
            for s in suggestions_:
                if "photo_id" in s:
                    s["photo"] = s.pop(Photo(id=s.pop("photo_id")))
                if "suggested_by" in s:
                    s["suggested_by"] = Person(id=s["suggested_by"])
                suggestions.append(Photo.Suggestion(**s))
            return FlickrList(suggestions, info=Info(**info))
        return args, format_result

    @caller("flickr.photos.getSizes")
    def _getSizes(self, **args):
        def format_result(r):
            return dict([(s["label"], s) for s in r["sizes"]["size"]])
        return args, format_result

    def getSizes(self, force=False, **args):
        if force or "sizes" not in self.__dict__:
            self.__dict__["sizes"] = self._getSizes(**args)
        return self.sizes

    @caller("flickr.stats.getPhotoStats")
    def getStats(self, date, **args):
        args["date"] = date
        return (
            args,
            lambda r: dict([(k, int(v)) for k, v in iteritems(r["stats"])])
        )

    @caller("flickr.tags.getListPhoto")
    def getTags(self, **args):
        return args, lambda r: [Tag(**t) for t in r["photo"]["tags"]["tag"]]

    def getPageUrl(self):
        """
            returns the URL to the photo's page.
        """
        return "http://www.flickr.com/photos/%s/%s" % (self.owner.id, self.id)

    @caller("flickr.photos.getPerms")
    def getPerms(self):
        return {}, lambda r: r

    def _getLargestSizeLabel(self):
        """
            returns the largest size for the current photo.
        """
        sizes = {k:v for k,v in self.getSizes().items() if v["media"] == self.media}
        max_size = None
        max_area = None
        for sl, s in iteritems(sizes):
            try:
                area = int(s["height"]) * int(s["width"])
            except TypeError:
                # Video entries have None width and/or height entries sometimes
                continue
            if max_area is None or area > max_area:
                max_size = sl
                max_area = area
        return max_size

    def getPhotoUrl(self, size_label=None):
        """
            returns the URL to the photo page corresponding to the
            given size.

        Arguments:
            size_label: The label corresponding to the photo size

                'Square': 75x75
                'Thumbnail': 100 on longest side
                'Small': 240 on  longest side
                'Medium': 500 on longest side
                'Medium 640': 640 on longest side
                'Large': 1024 on longest side
                'Original': original photo (not always available)
        """
        if size_label is None:
            size_label = self._getLargestSizeLabel()
        try:
            return self.getSizes()[size_label]["url"]
        except KeyError:
            raise FlickrError("The requested size is not available")

    def getPhotoFile(self, size_label=None):
        """
            returns the URL to the photo file corresponding to the
            given size.

        Arguments:
            size_label: The label corresponding to the photo size

                'Square': 75x75
                'Thumbnail': 100 on longest side
                'Small': 240 on  longest side
                'Medium': 500 on longest side
                'Medium 640': 640 on longest side
                'Large': 1024 on longest side
                'Original': original photo (not always available)
        """
        if size_label is None:
            size_label = self._getLargestSizeLabel()
        try:
            return self.getSizes()[size_label]["source"]
        except KeyError:
            raise FlickrError("The requested size is not available")

    def _getOutputFilename(self, filename, size_label):
        photo_file = self.getPhotoFile(size_label)
        file_ext = ('.' + photo_file.split('.')[-1]) if self.media == "photo" else ".mp4"

        output_filename = filename
        if os.path.splitext(filename)[1] == '':
            output_filename = filename + file_ext

        return output_filename


    def save(self, filename, size_label=None):
        """
            saves the photo corresponding to the
            given size.

        Arguments:
            filename: target file name (without extension)

            size_label: The label corresponding to the photo size

                'Square': 75x75
                'Thumbnail': 100 on longest side
                'Small': 240 on  longest side
                'Medium': 500 on longest side
                'Medium 640': 640 on longest side
                'Large': 1024 on longest side
                'Original': original photo (not always available)
        """
        if size_label is None:
            size_label = self._getLargestSizeLabel()
        output_filename = self._getOutputFilename(filename, size_label)

        photo_file = self.getPhotoFile(size_label)
        r = urllib.request.urlopen(photo_file)
        with open(output_filename, 'wb') as f:
            f.write(r.read())
            f.close()

        return output_filename

    def show(self, size_label=None):
        """
            Shows the photo corresponding to the
            given size.

        Note: This methods uses PIL

        Arguments:
            filename: target file name

            size_label: The label corresponding to the photo size

                'Square': 75x75
                'Thumbnail': 100 on longest side
                'Small': 240 on  longest side
                'Medium': 500 on longest side
                'Medium 640': 640 on longest side
                'Large': 1024 on longest side
                'Original': original photo (not always available)
        """
        if size_label is None:
            size_label = self._getLargestSizeLabel()
        r = urllib.request.urlopen(self.getPhotoFile(size_label))
        b = cStringIO(r.read())
        Image.open(b).show()

    @static_caller("flickr.photos.getUntagged")
    def getUntagged(**args):
        return _format_extras(args), _extract_photo_list

    @static_caller("flickr.photos.getWithGeoData")
    def getWithGeoData(**args):
        return _format_extras(args), _extract_photo_list

    @static_caller("flickr.photos.getWithoutGeoData")
    def getWithoutGeoData(**args):
        return _format_extras(args), _extract_photo_list

    @caller("flickr.photos.people.getList")
    def getPeople(self, **args):
        def format_result(r, token):
            info = r["people"]
            people = info.pop("person")
            people_ = []
            if isinstance(people, Person):
                people = [people]
            for p in people:
                p["id"] = p["nsid"]
                p["photo"] = self
                people_.append(Person(**p))
            return people_
        return args, format_result

    @static_caller("flickr.photos.geo.photosForLocation")
    def photosForLocation(**args):
        return args, _extract_photo_list

    @static_caller("flickr.photos.recentlyUpdated")
    def recentlyUpdated(**args):
        return _format_extras(args), _extract_photo_list

    @caller("flickr.favorites.remove")
    def removeFromFavorites(self, **args):
        return args, _none

    @caller("flickr.photos.geo.removeLocation")
    def removeLocation(self, **args):
        return args, _none

    @caller("flickr.photos.transform.rotate")
    def rotate(self, degrees, **args):
        args["degrees"] = degrees

        def format_result(r, token):
            photo_id = r["photo_id"]["_content"]
            photo_secret = r["photo_id"]["secret"]
            return Photo(token=token, id=photo_id, secret=photo_secret)
        return args, format_result

    @static_caller("flickr.photos.search")
    def search(**args):
        if "extras" not in args:
            args["extras"] = []
        if not isinstance(args["extras"], list):
            args["extras"] = [args["extras"]]
        args["extras"] += "media,url_sq, url_t, url_s, url_q, url_m, url_n, url_z, url_c, url_l, url_o".split(", ")

        args = _format_id("user", args)
        args = _format_extras(args)
        return args, _extract_photo_list

    @caller("flickr.photos.geo.setContext")
    def setContext(self, context, **args):
        args["context"] = context
        return args, _none

    @caller("flickr.photos.setContentType")
    def setContentType(self, **args):
        return args, _none

    @caller("flickr.photos.setDates")
    def setDates(self, **args):
        return args, _none

    @caller("flickr.photos.geo.setPerms")
    def setGeoPerms(self, **args):
        return args, _none

    @caller("flickr.photos.licenses.setLicense")
    def setLicence(self, license, **args):
        return _format_id("licence", args), _none

    @caller("flickr.photos.geo.setLocation")
    def setLocation(self, **args):
        return args, _none

    @caller("flickr.photos.setMeta")
    def setMeta(self, **args):
        return args, _none

    @caller("flickr.photos.setPerms")
    def setPerms(self, **args):
        return args, _none

    @caller("flickr.photos.setSafetyLevel")
    def setSafetyLevel(self, **args):
        return args, _none

    @caller("flickr.photos.setTags")
    def setTags(self, tags, **args):
        args["tags"] = tags
        return args, _none

    @caller("flickr.photos.suggestions.suggestLocation")
    def suggestLocation(self, **args):
        _format_id("place", args)

        def format_result(r):
            info = r["suggestions"]
            suggestions_ = _check_list(info.pop("suggestion"))
            suggestions = []
            for s in suggestions_:
                if "photo_id" in s:
                    s["photo"] = Photo(id=s.pop("photo_id"))
                if "suggested_by" in s:
                    s["suggested_by"] = Person(id=s["suggested_by"])
                suggestions.append(Photo.Suggestion(**s))
            return FlickrList(suggestions, info=Info(**info))
        return args, format_result


class PhotoGeoPerms(FlickrObject):
    __converters__ = [
        dict_converter(["ispublic", "iscontact", "isfamily", "isfriend"], bool)
    ]
    __display__ = ["id", "ispublic", "iscontact", "isfamily", "isfriend"]


class Photoset(FlickrObject):
    __converters__ = [
        dict_converter(["photos"], int),
    ]
    __display__ = ["id", "title"]
    __self_name__ = "photoset_id"

    class Comment(FlickrObject):
        __display__ = ["id"]
        __self_name__ = "comment_id"

        @caller("flickr.photosets.comments.deleteComment")
        def delete(self, **args):
            return args, _none

        @caller("flickr.photosets.comments.editComment")
        def edit(self, **args):
            self._set_properties(**args)
            return args, _none

    @caller("flickr.photosets.addPhoto")
    def addPhoto(self, **args):
        return _format_id("photo", args), _none

    @caller("flickr.photosets.comments.addComment")
    def addComment(self, **args):
        return (
            args,
            lambda r, token: Photoset.Comment(token=token, photoset=self, **r)
        )

    @static_caller("flickr.photosets.create")
    def create(**args):
        try:
            pphoto = args.pop("primary_photo")
            pphoto_id = pphoto.id
        except KeyError:
            pphoto_id = args.pop("primary_photo_id")
            pphoto = Photo(id=pphoto_id)
        args["primary_photo_id"] = pphoto_id

        def format_result(r, token):
            photoset = r["photoset"]
            photoset["primary"] = pphoto
            return Photoset(token=token, **photoset)
        return args, format_result

    @caller("flickr.photosets.delete")
    def delete(self, **args):
        return args, _none

    @caller("flickr.photosets.editMeta")
    def editMeta(self, **args):
        return args, _none

    @caller("flickr.photosets.editPhotos")
    def editPhotos(self, **args):
        try:
            args["primary_photo_id"] = args.pop("primary_photo").id
        except KeyError:
            pass
        try:
            args["photo_ids"] = [p.id for p in args["photos"]]
        except KeyError:
            pass

        photo_ids = args["photo_ids"]
        if isinstance(photo_ids, list):
            args["photo_ids"] = ", ".join(photo_ids)
        return args, _none

    @caller("flickr.photosets.comments.getList")
    def getComments(self, **args):
        def format_result(r, token):
            comments = r["comments"]["comment"]
            comments_ = []
            if not isinstance(comments, list):
                comments = [comments]
            for c in comments:
                author = c["author"]
                authorname = c.pop("authorname")
                c["author"] = Person(id=author, username=authorname)
                comments_.append(
                    Photoset.Comment(token=token, photo=self, **c)
                )
            return comments_
        return args, format_result

    @caller("flickr.photosets.getContext")
    def getContext(self, **args):
        def format_result(r, token):
            return (Photo(token=token, **r["prevphoto"]),
                    Photo(token=token, **r["nextphoto"]))
        return _format_id("photo", args), format_result

    @caller("flickr.photosets.getInfo")
    def getInfo(self, **args):
        def format_result(r, token):
            photoset = r["photoset"]
            photoset["owner"] = Person(token=token, id=photoset["owner"])
            return photoset
        return args, format_result

    @caller("flickr.photosets.getPhotos")
    def getPhotos(self, **args):
        def format_result(r):
            ps = r["photoset"]
            return FlickrList([Photo(**p) for p in ps["photo"]],
                               Info(pages=ps["pages"],
                                    page=ps["page"],
                                    perpage=ps["perpage"],
                                    total=ps["total"]))
        return _format_extras(args), format_result

    @caller("flickr.stats.getPhotosetStats")
    def getStats(self, date, **args):
        args["date"] = date
        return (
            args,
            lambda r: dict([(k, int(v)) for k, v in iteritems(r["stats"])])
        )

    @static_caller("flickr.photosets.orderSets")
    def orderSets(**args):
        try:
            photosets = args.pop("photosets")
            args["photoset_ids"] = [ps.id for ps in photosets]
        except KeyError:
            pass

        photoset_ids = args["photoset_ids"]
        if isinstance(photoset_ids, list):
            args["photoset_ids"] = ", ".join(photoset_ids)

        return args, _none

    @caller("flickr.photosets.removePhoto")
    def removePhoto(self, **args):
        return _format_id("photo", args), _none

    @caller("flickr.photosets.removePhotos")
    def removePhotos(self, **args):
        try:
            args["photo_ids"] = [p.id for p in args.pop("photos")]
        except KeyError:
            pass

        photo_ids = args["photo_ids"]
        if isinstance(photo_ids, list):
            args["photo_ids"] = u", ".join(photo_ids)

        return args, _none

    @caller("flickr.photosets.reorderPhotos")
    def reorderPhotos(self, **args):
        try:
            args["photo_ids"] = [p.id for p in args.pop("photos")]
        except KeyError:
            pass

        photo_ids = args["photo_ids"]
        if isinstance(photo_ids, list):
            args["photo_ids"] = u",".join(photo_ids)

        return args, _none

    @caller("flickr.photosets.setPrimaryPhoto")
    def setPrimaryPhoto(self, **args):
        return _format_id("photo", args), _none


class Place(FlickrObject):
    __display__ = ["id", "name", "woeid", "latitude", "longitude"]
    __converters__ = [
        dict_converter(["latitude", "longitude"], float),
    ]
    __self_name__ = 'place_id'

    class ShapeData(FlickrObject):
        class Polyline(FlickrObject):
            pass

    class Type(FlickrObject):
        __display__ = ["id", "text"]

    class Tag(FlickrObject):
        __display__ = ["text", "count"]
        __converters__ = [
            dict_converter(["count"], int),
        ]

    @static_caller("flickr.places.find")
    def find(**args):
        return args, _extract_place_list

    @static_caller("flickr.places.findByLatLon")
    def findByLatLon(**args):
        return args, _extract_place_list

    @caller("flickr.places.getChildrenWithPhotosPublic")
    def getChildrenWithPhotoPublic(self, **args):
        return args, _extract_place_list

    @caller("flickr.places.getInfo")
    def getInfo(self, **args):
        def format_result(r):
            return Place.parse_place(r["place"])
        return args, format_result

    @staticmethod
    def parse_shapedata(shape_data_dict):
        shapedata = shape_data_dict.copy()
        shapedata["polylines"] = [
            Place.ShapeData.Polyline(coords=p.split(" "))
                for p in shapedata["polylines"]["polyline"]
        ]
        if "url" in shapedata:
            shapedata["shapefile"] = shapedata.pop("urls")["shapefile"].text
        return shapedata

    @staticmethod
    def parse_place(place_dict):
        place = place_dict.copy()
        if "locality" in place:
            place["locality"] = Place(**Place.parse_place(place["locality"]))

        if "county" in place:
            place["county"] = Place(**Place.parse_place(place["county"]))

        if "region" in place:
            place["region"] = Place(**Place.parse_place(place["region"]))

        if "country" in place:
            place["country"] = Place(**Place.parse_place(place["country"]))

        if "shapedata" in place:
            shapedata = Place.parse_shapedata(place["shapedata"])
            place["shapedata"] = Place.ShapeData(**shapedata)

        if "text" in place:
            place["name"] = place.pop("text")

        place["id"] = place.pop("place_id")
        return place

    @static_caller("flickr.places.getInfoByUrl")
    def getByUrl(url):
        return {'url': url}, lambda r: Place(**Place.parse_place(r["place"]))

    @static_caller("flickr.places.getPlaceTypes")
    def getPlaceTypes(**args):
        def format_result(r):
            places_types = r["place_types"]["place_type"]
            return [Place.Type(id=pt.pop("place_type_id"), **pt)
                     for pt in places_types]
        return args, format_result

    @static_caller("flickr.places.getShapeHistory")
    def getShapeHistory(**args):
        def format_result(r):
            info = r["shapes"]
            return [Place.ShapeData(**Place.parse_shapedata(sd))
                    for sd in _check_list(info.pop("shapedata"))]
        return args, format_result

    @caller("flickr.places.getTopPlacesList")
    def getTopPlaces(self, **args):
        return args, _extract_place_list

    @static_caller("flickr.places.placesForBoundingBox")
    def placesForBoundingBox(**args):
        def format_result(r):
            info = r["places"]
            return [
                Place(Place.parse_place(place))
                    for place in info.pop("place")]
        return args, format_result

    @static_caller("flickr.places.placesForContacts")
    def placesForContacts(**args):
        def format_result(r):
            info = r["places"]
            return [
                Place(Place.parse_place(place))
                    for place in info.pop("place")]
        return args, format_result

    @static_caller("flickr.places.placesForTags")
    def placesForTags(**args):
        return args, _extract_place_list

    @static_caller("flickr.places.placesForUser")
    def placesForUser(**args):
        return args, _extract_place_list

    @static_caller("flickr.places.tagsForPlace")
    def tagsForPlace(**args):
        args = _format_id("place", args)
        args = _format_id("woe", args)
        return args, lambda r: [Place.Tag(**t) for t in r["tags"]["tag"]]

    @caller("flickr.places.tagsForPlace")
    def getTags(self, **args):
        return args, lambda r: [Place.Tag(**t) for t in r["tags"]["tag"]]


class prefs(FlickrObject):
    @static_caller("flickr.prefs.getContentType")
    def getContentType(**args):
        return args, lambda r: r["person"]["content_type"]

    @static_caller("flickr.prefs.getGeoPerms")
    def getGeoPerms(**args):
        return args, lambda r: r["person"]

    @static_caller("flickr.prefs.getHidden")
    def getHidden(**args):
        return args, lambda r: bool(r["person"]["hidden"])

    @static_caller("flickr.prefs.getPrivacy")
    def getPrivacy(**args):
        return args, lambda r: r["person"]["privacy"]

    @static_caller("flickr.prefs.getSafetyLevel")
    def getSafetyLevel(**args):
        return args, lambda r: r["person"]["safety_level"]


class Reflection(FlickrObject):
    @static_caller("flickr.reflection.getMethodInfo")
    def getMethodInfo(method_name):
        return {"method_name": method_name}, lambda r: r["method"]

    @static_caller("flickr.reflection.getMethods")
    def getMethods():
        return {}, lambda r: r["methods"]["method"]


class stats(FlickrObject):
    class Domain(FlickrObject):
        __display__ = ["name"]

    class Referrer(FlickrObject):
        __display__ = ["url", "views"]
        __converters__ = [
            dict_converter(["views"], int),
        ]

    @static_caller("flickr.stats.getCollectionDomains")
    def getCollectionDomains(**args):
        def format_result(r):
            info = r["domains"]
            domains = [stats.Domain(**d) for d in info.pop("domain")]
            return FlickrList(domains, Info(**info))
        return _format_id("collection", args), format_result

    @static_caller("flickr.stats.getCollectionReferrers")
    def getCollectionReferrers(**args):
        def format_result(r):
            info = r["domain"]
            referrers = [stats.Referrer(**r) for r in info.pop("referrer")]
            return FlickrList(referrers, Info(**info))
        return _format_id("collection", args), format_result

    @static_caller("flickr.stats.getCSVFiles")
    def getCSVFiles():
        return {}, lambda r: r["stats"]["csvfiles"]["csv"]

    @static_caller("flickr.stats.getPhotoDomains")
    def getPhotoDomains(**args):
        def format_result(r):
            info = r["domains"]
            domains = [stats.Domain(**d) for d in info.pop("domain")]
            return FlickrList(domains, Info(**info))
        return _format_id("photo", args), format_result

    @static_caller("flickr.stats.getPhotoReferrers")
    def getPhotoReferrers(**args):
        def format_result(r):
            info = r["domain"]
            referrers = [stats.Referrer(**r) for r in info.pop("referrer")]
            return FlickrList(referrers, Info(**info))
        return _format_id("photo", args), format_result

    @static_caller("flickr.stats.getPhotosetDomains")
    def getPhotosetDomains(**args):
        def format_result(r):
            info = r["domains"]
            domains = [stats.Domain(**d) for d in info.pop("domain")]
            return FlickrList(domains, Info(**info))
        return _format_id("photoset", args), format_result

    @static_caller("flickr.stats.getPhotosetReferrers")
    def getPhotosetReferrers(**args):
        def format_result(r):
            info = r["domain"]
            referrers = [stats.Referrer(**r) for r in info.pop("referrer")]
            return FlickrList(referrers, Info(**info))
        return _format_id("photoset", args), format_result

    @static_caller("flickr.stats.getPhotostreamDomains")
    def getPhotostreamDomains(**args):
        def format_result(r):
            info = r["domains"]
            domains = [stats.Domain(**d) for d in info.pop("domain")]
            return FlickrList(domains, Info(**info))
        return args, format_result

    @static_caller("flickr.stats.getPhotostreamReferrers")
    def getPhotostreamReferrers(**args):
        def format_result(r):
            info = r["domain"]
            referrers = [stats.Referrer(**r) for r in info.pop("referrer")]
            return FlickrList(referrers, Info(**info))
        return args, format_result

    @static_caller("flickr.stats.getPhotostreamStats")
    def getPhotostreamStats(date, **args):
        args["date"] = date
        return args, lambda r: int(r["stats"]["views"])

    @static_caller("flickr.stats.getPopularPhotos")
    def getPopularPhotos():
        def format_result(r):
            info = r["photos"]
            photos = []
            for p in info.pop("photo"):
                pstat = p.pop("stats")
                photos.append((Photo(**p), pstat))
            return FlickrList(photos, Info(**info))
        return {}, format_result

    @static_caller("flickr.stats.getTotalViews")
    def getTotalViews(**args):
        return args, lambda r: r["stats"]


class Tag(FlickrObject):
    __display__ = ["id", "text"]
    __self_name__ = "tag_id"

    class Cluster(FlickrObject):
        __display__ = ["total"]
        __self_name__ = "cluster_id"

        @caller("flickr.tags.getClusterPhotos")
        def getPhotos(self, **args):
            return args, _extract_photo_list

    @caller("flickr.photos.removeTag")
    def remove(self, **args):
        return args, _none

    @static_caller("flickr.tags.getClusters")
    def getClusters(**args):
        def format_result(r):
            clusters = r["clusters"]["cluster"]
            return [
                Tag.Cluster(tag=args["tag"],
                            tags=[Tag(text=t) for t in c["tag"]],
                            total=c["total"]
                ) for c in clusters
            ]
        return args, format_result

    @static_caller("flickr.tags.getHotList")
    def getHotList(**args):
        return args, lambda r: [Tag(**t) for t in r["hottags"]["tag"]]

    @static_caller("flickr.tags.getListUser")
    def getListUser(**args):
        return (
            _format_id("user", args),
            lambda r: [Tag(**t) for t in r["who"]["tags"]["tag"]]
        )

    @static_caller("flickr.tags.getListUserPopular")
    def getListUserPopular(**args):
        return (_format_id("user", args),
                lambda r: [Tag(**t) for t in r["who"]["tags"]["tag"]])

    @static_caller("flickr.tags.getListUserRaw")
    def getListUserRaw(**args):
        def format_result(r):
            tags = r["who"]["tags"]["tag"]
            return [{'clean': t["clean"], "raws": t["raw"]} for t in tags]
        return args, format_result

    @static_caller("flickr.tags.getRelated")
    def getRelated(tag, **args):
        args["tag"] = tag
        return args, lambda r: r["tags"]["tag"]


class test(FlickrObject):
    @static_caller("flickr.test.echo")
    def echo(**args):
        return args, lambda r: r

    @static_caller("flickr.test.login")
    def login(token=None, **args):
        return args, lambda r: Person(token=token, **r["user"])

    @static_caller("flickr.test.null")
    def null():
        return {}, _none


class UploadTicket(FlickrObject):
    pass


def _extract_activity_list(r):
    items = _check_list(r["items"]["item"])
    activities = []
    for item in items:
        activity = item.pop("activity")
        item_type = item.pop(["type"])
        if item_type == "photo":
            item = Photo(**item)
        elif item_type == "photoset":
            item = Photoset(**item)
        events_ = []
        events = _check_list(activity["event"])
        for e in events:
            user = e["user"]
            username = e.pop("username")
            e["user"] = Person(id=user, username=username)
            e_type = e.pop("type")
            if e_type == "comment":
                if item_type == "photo":
                    events_.append(Photo.Comment(photo=item, **e))
                elif item_type == "photoset":
                    events_.append(Photoset.Comment(photoset=item, **e))
            elif e_type == 'note':
                events_.append(Photo.Note(photo=item, **e))
        activities.append(Activity(item=item, events=events))
    return activities


def _format_id(name, args):
    try:
        args[name + "_id"] = args.pop(name).id
    except KeyError:
        pass
    return args


def _format_extras(args):
    try:
        extras = args["extras"]
        if isinstance(extras, list):
            args["extras"] = ", ".join(extras)
    except KeyError:
        pass
    return args


def _new(cls):
    def _newobject(**args):
        return cls(**args)
    return _newobject


def _none(r):
    return None


def _extract_place_list(r):
    info = r["places"]
    return FlickrList(
        [Place(id=place.pop("place_id"), **place)
            for place in info.pop("place")],
        Info(**info)
    )


def _extract_photo_list(r, token=None):
    photos = []
    infos = r["photos"]
    pp = infos.pop("photo")
    if not isinstance(pp, list):
        pp = [pp]
    for p in pp:
        owner = Person(id=p["owner"], token=token)
        p["owner"] = owner
        p["token"] = token

        # only check sizes for photo as there's no way to ask for video url on extras
        if "media" in p and p["media"] == "photo":
            sizes = _parse_inline_sizes(p)
            if sizes:
                p["sizes"] = sizes

        photos.append(Photo(**p))
    return FlickrList(photos, Info(**infos))

def _parse_inline_sizes(p):
    keys = [k for k in p.keys() if k.startswith("url_")]
    size_keys = set(k.split("_")[-1] for k in keys)

    sizes = {}
    for s in size_keys:
        w = p["width_"+s]
        h = p["height_"+s]
        url = "https://www.flickr.com/photos/%s/%s/sizes/%s/" % (p["owner"].id, p["id"], s)
        source = p["url_"+s]
        label = _SIZES_LABEL[s]
        media = p["media"]

        sizes[label] = dict(width=w, height=h, url=url, source=source, label=label, media=media)

    return sizes


def _check_list(obj):
    if isinstance(obj, list):
        return obj
    else:
        return [obj]


class Walker(object):
    """
        Object to walk along paginated results. This allows
        to loop on all the results corresponding to a query
        regardless pagination.

        w = Walker(method,*args, **kwargs)

        arguments:
        - method: a method returning a FlickrList object.
        - *args: positional arguments to call 'method' with
        - **kwargs: named arguments to call 'method' with

        ex:
        >>> w = Walker(Photo.search, tags="animals")
        >>> for photo in w:
        >>>     print photo.title

        You can also use slices:
        ex:
        >>> w = Walker(Photo.search, tags="animals")
        >>> for photo in w[:20]:
        >>>     print photo.title

        but be aware that if a starting index is given all the items
        till the wanted one will be iterated, so using a large
        starting value might be slow.
    """
    def __init__(self, method, *args, **kwargs):
        """
            Constructor

        arguments:
        - method: a method returning a FlickrList object.
        - *args: positional arguments to call 'method' with
        - **kwargs: named arguments to call 'method' with

        """
        self.method = method
        self.args = args
        self.kwargs = kwargs

        self._curr_list = self.method(*self.args, **self.kwargs)
        self._info = self._curr_list.info
        self._curr_index = 0
        self._page = 1
        self.stop = None

    def __len__(self):
        return self._info.total

    def __iter__(self):
        return self

    def __getitem__(self, slice_):
        if isinstance(slice_, slice):
            return SlicedWalker(self,
                slice_.start,
                slice_.stop,
                slice_.step)
        else:
            raise ValueError("Only slices can be used as subscript")

    def __next__(self):
        return self.next()

    def next(self):
        if self._curr_index == len(self._curr_list):
            if self._page < self._info.pages:
                self._page += 1
                self.kwargs["page"] = self._page

                self._curr_list = self.method(*self.args, **self.kwargs)
                self._info = self._curr_list.info
                self._curr_index = 0

            else:
                raise StopIteration()

        curr = self._curr_list[self._curr_index]
        self._curr_index += 1
        return curr


class SlicedWalker(object):
    """ Used to apply slices on objects.
        Starting at a large index might be slow since all items till
        the start one will be iterated.
    """
    def __init__(self, walker, start, stop, step):
        self.walker = walker
        self.start = start or 0
        self.stop = stop or len(walker)
        self.step = step or 1

        self._begin = True
        self._total = 0

    def __len__(self):
        return (self.stop - self.start) // self.step

    def __iter__(self):
        return self

    def next(self):
        if self._begin:
            for i in range(self.start):
                self.walker.next()
                self._total += 1
            self._begin = False
        else:
            for i in range(self.step - 1):
                self._total += 1
                self.walker.next()

        if self._total < self.stop:
            self._total += 1
            return self.walker.next()
        else:
            raise StopIteration()
