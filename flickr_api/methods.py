__methods__ = {
    "flickr.photos.notes.delete": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The note id passed was not a valid note id",
                "message": "Note not found",
                "code": "1",
            },
            {
                "text": "The calling user does not have permission to delete the specified note",
                "message": "User cannot delete note",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the note to delete",
                "optional": "0",
                "name": "note_id",
            },
        ],
        "description": "Delete a note from a photo.",
        "needslogin": True,
        "name": "flickr.photos.notes.delete",
    },
    "flickr.photos.comments.addComment": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id",
                "message": "Photo not found.",
                "code": "1",
            },
            {
                "text": "Comment text can not be blank",
                "message": "Blank comment.",
                "code": "8",
            },
            {
                "text": "The user has reached the limit for number of comments posted during a specific time period.  Wait a bit and try again.",
                "message": "User is posting comments too fast.",
                "code": "9",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Add comment to a photo as the currently authenticated user.",
        "needssigning": True,
        "requiredperms": "write",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to add a comment to.",
                "optional": "0",
                "name": "photo_id",
            },
            {"text": "Text of the comment", "optional": "0", "name": "comment_text"},
        ],
        "needslogin": True,
        "response": '<comment id="97777-72057594037941949-72057594037942602" />',
        "name": "flickr.photos.comments.addComment",
    },
    "flickr.activity.userPhotos": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns a list of recent activity on photos belonging to the calling user. <b>Do not poll this method more than once an hour</b>.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The timeframe in which to return updates for. This can be specified in days (<code>'2d'</code>) or hours (<code>'4h'</code>). The default behavoir is to return changes since the beginning of the previous user session.",
                "optional": "1",
                "name": "timeframe",
            },
            {
                "text": "Number of items to return per page. If this argument is omitted, it defaults to 10. The maximum allowed value is 50.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<items>\r\n\t<item type="photoset" id="395" owner="12037949754@N01" \r\n\t\tprimary="6521" secret="5a3cc65d72" server="2" \r\n\t\tcommentsold="1" commentsnew="1"\r\n\t\tviews="33" photos="7" more="0">\r\n\t\t<title>A set of photos</title>\r\n\t\t<activity>\r\n\t\t\t<event type="comment"\r\n\t\t\tuser="12037949754@N01" username="Bees"\r\n\t\t\tdateadded="1144086424">yay</event>\r\n\t\t</activity>\r\n\t</item>\r\n\r\n\t<item type="photo" id="10289" owner="12037949754@N01"\r\n\t\tsecret="34da0d3891" server="2"\r\n\t\tcommentsold="1" commentsnew="1"\r\n\t\tnotesold="0" notesnew="1"\r\n\t\tviews="47" faves="0" more="0">\r\n\t\t<title>A photo</title>\r\n\t\t<activity>\r\n\t\t\t<event type="comment"\r\n\t\t\tuser="12037949754@N01" username="Bees"\r\n\t\t\tdateadded="1133806604">test</event>\r\n\t\t\t<event type="note"\r\n\t\t\tuser="12037949754@N01" username="Bees"\r\n\t\t\tdateadded="1118785229">nice</event>\r\n\t\t</activity>\r\n\t</item>\r\n</items>',
        "name": "flickr.activity.userPhotos",
    },
    "flickr.groups.pools.getContext": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id, or was the id of a photo that the calling user does not have permission to view.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The specified photo is not in the specified group's pool.",
                "message": "Photo not in pool",
                "code": "2",
            },
            {
                "text": "The specified group nsid was not a valid group or the caller does not have permission to view the group's pool.",
                "message": "Group not found",
                "code": "3",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.groups.pools.getContext",
        "explanation": '<p>See <a href="/services/api/flickr.photos.getContext.html">flickr.photos.getContext</a></p>',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to fetch the context for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The nsid of the group who's pool to fetch the photo's context for.",
                "optional": "0",
                "name": "group_id",
            },
            {"text": "", "optional": "1", "name": "num_prev"},
            {"text": "", "optional": "1", "name": "num_next"},
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: description, license, date_upload, date_taken, owner_name, icon_server, original_format, last_update, geo, tags, machine_tags, o_dims, views, media, path_alias, url_sq, url_t, url_s, url_m, url_z, url_l, url_o",
                "optional": "1",
                "name": "extras",
            },
        ],
        "needslogin": False,
        "response": '<prevphoto id="2980" secret="973da1e709"\r\n\ttitle="boo!" url="/photos/bees/2980/" /> \r\n<nextphoto id="2985" secret="059b664012"\r\n\ttitle="Amsterdam Amstel" url="/photos/bees/2985/" /> ',
        "description": "Returns next and previous photos for a photo in a group pool.",
    },
    "flickr.photosets.getContext": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id, or was the id of a photo that the calling user does not have permission to view.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The specified photo is not in the specified set.",
                "message": "Photo not in set",
                "code": "2",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.photosets.getContext",
        "explanation": '<p>See <a href="/services/api/flickr.photos.getContext.html">flickr.photos.getContext</a></p>',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to fetch the context for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The id of the photoset for which to fetch the photo's context.",
                "optional": "0",
                "name": "photoset_id",
            },
            {"text": "", "optional": "1", "name": "num_prev"},
            {"text": "", "optional": "1", "name": "num_next"},
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: description, license, date_upload, date_taken, owner_name, icon_server, original_format, last_update, geo, tags, machine_tags, o_dims, views, media, path_alias, url_sq, url_t, url_s, url_m, url_z, url_l, url_o",
                "optional": "1",
                "name": "extras",
            },
        ],
        "needslogin": False,
        "response": '<prevphoto id="2980" secret="973da1e709"\r\n\ttitle="boo!" url="/photos/bees/2980/" /> \r\n<nextphoto id="2985" secret="059b664012"\r\n\ttitle="Amsterdam Amstel" url="/photos/bees/2985/" /> ',
        "description": "Returns next and previous photos for a photo in a set.",
    },
    "flickr.people.getPublicGroups": {
        "errors": [
            {
                "text": "The user id passed did not match a Flickr user.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.people.getPublicGroups",
        "explanation": "<p>The <code>admin</code> attribute indicates whether the user is an administrator of the group. The <code>eighteenplus</code> attribute indicates if the group is visible to members over 18 only. The <code>invite_only</code> attribute indicates whether a user can join the group without administrator approval.</p>",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user to fetch groups for.",
                "optional": "0",
                "name": "user_id",
            },
            {
                "text": 'Include public groups that require <a href="http://www.flickr.com/help/groups/#10">an invitation</a> or administrator approval to join.',
                "optional": "1",
                "name": "invitation_only",
            },
        ],
        "needslogin": False,
        "response": '<groups>\r\n\t<group nsid="34427469792@N01" name="FlickrCentral"\r\n\t\tadmin="0" eighteenplus="0" invitation_only="0" /> \r\n\t<group nsid="37114057624@N01" name="Cal\'s Test Group"\r\n\t\tadmin="1" eighteenplus="0" invitation_only="1" /> \r\n\t<group nsid="34955637532@N01" name="18+ Group"\r\n\t\tadmin="1" eighteenplus="1" invitation_only="0" /> \r\n</groups>',
        "description": "Returns the list of public groups a user is a member of.",
    },
    "flickr.tags.getClusters": {
        "errors": [
            {
                "text": "The tag was invalid or no cluster exists for that tag.",
                "message": "Tag cluster not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Gives you a list of tag clusters for the given tag.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {"text": "The tag to fetch clusters for.", "optional": "0", "name": "tag"},
        ],
        "needslogin": False,
        "response": '<clusters source="cows" total="2">\r\n\t<cluster total="3">\r\n\t\t<tag>farm</tag>\r\n\t\t<tag>animals</tag>\r\n\t\t<tag>cattle</tag>\r\n\t</cluster>\r\n\t<cluster total="3">\r\n\t\t<tag>green</tag>\r\n\t\t<tag>landscape</tag>\r\n\t\t<tag>countryside</tag>\r\n\t</cluster>\r\n</clusters>',
        "name": "flickr.tags.getClusters",
    },
    "flickr.photos.geo.photosForLocation": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {
                "text": "One or more required arguments was missing from the method call.",
                "message": "Required arguments missing",
                "code": "1",
            },
            {
                "text": "The latitude argument failed validation.",
                "message": "Not a valid latitude",
                "code": "2",
            },
            {
                "text": "The longitude argument failed validation.",
                "message": "Not a valid longitude",
                "code": "3",
            },
            {
                "text": "The accuracy argument failed validation.",
                "message": "Not a valid accuracy",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The latitude whose valid range is -90 to 90. Anything more than 6 decimal places will be truncated.",
                "optional": "0",
                "name": "lat",
            },
            {
                "text": "The longitude whose valid range is -180 to 180. Anything more than 6 decimal places will be truncated.",
                "optional": "0",
                "name": "lon",
            },
            {
                "text": "Recorded accuracy level of the location information. World level is 1, Country is ~3, Region ~6, City ~11, Street ~16. Current range is 1-16. Defaults to 16 if not specified.",
                "optional": "1",
                "name": "accuracy",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "description": "Return a list of photos for the calling user at a specific latitude, longitude and accuracy",
        "needslogin": True,
        "name": "flickr.photos.geo.photosForLocation",
    },
    "flickr.places.placesForUser": {
        "errors": [
            {
                "text": "Places for user have been disabled or are otherwise not available.",
                "message": "Places for user are not available at this time",
                "code": "1",
            },
            {
                "text": "One or more of the required parameters was not included with your request.",
                "message": "Required parameter missing",
                "code": "2",
            },
            {
                "text": "An invalid place type was included with your request.",
                "message": "Not a valid place type",
                "code": "3",
            },
            {
                "text": "An invalid Places (or WOE) identifier was included with your request.",
                "message": "Not a valid Place ID",
                "code": "4",
            },
            {
                "text": "The threshold passed was invalid. ",
                "message": "Not a valid threshold",
                "code": "5",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return a list of the top 100 unique places clustered by a given placetype for a user. ",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": 'The numeric ID for a specific place type to cluster photos by. <br /><br />\r\n\r\nValid place type IDs are :\r\n\r\n<ul>\r\n<li><strong>22</strong>: neighbourhood</li>\r\n<li><strong>7</strong>: locality</li>\r\n<li><strong>8</strong>: region</li>\r\n<li><strong>12</strong>: country</li>\r\n<li><strong>29</strong>: continent</li>\r\n</ul>\r\n<br />\r\n<span style="font-style:italic;">The "place_type" argument has been deprecated in favor of the "place_type_id" argument. It won\'t go away but it will not be added to new methods. A complete list of place type IDs is available using the <a href="http://www.flickr.com/services/api/flickr.places.getPlaceTypes.html">flickr.places.getPlaceTypes</a> method. (While optional, you must pass either a valid place type or place type ID.)</span>',
                "optional": "1",
                "name": "place_type_id",
            },
            {
                "text": 'A specific place type to cluster photos by. <br /><br />\r\n\r\nValid place types are :\r\n\r\n<ul>\r\n<li><strong>neighbourhood</strong> (and neighborhood)</li>\r\n<li><strong>locality</strong></li>\r\n<li><strong>region</strong></li>\r\n<li><strong>country</strong></li>\r\n<li><strong>continent</strong></li>\r\n</ul>\r\n<br /><span style="font-style:italic;">(While optional, you must pass either a valid place type or place type ID.)</span>',
                "optional": "1",
                "name": "place_type",
            },
            {
                "text": 'A Where on Earth identifier to use to filter photo clusters. For example all the photos clustered by <strong>locality</strong> in the United States (WOE ID <strong>23424977</strong>).<br /><br />\r\n<span style="font-style:italic;">(While optional, you must pass either a valid Places ID or a WOE ID.)</span>',
                "optional": "1",
                "name": "woe_id",
            },
            {
                "text": 'A Flickr Places identifier to use to filter photo clusters. For example all the photos clustered by <strong>locality</strong> in the United States (Place ID <strong>4KO02SibApitvSBieQ</strong>).<br /><br />\r\n<span style="font-style:italic;">(While optional, you must pass either a valid Places ID or a WOE ID.)</span>',
                "optional": "1",
                "name": "place_id",
            },
            {
                "text": 'The minimum number of photos that a place type must have to be included. If the number of photos is lowered then the parent place type for that place will be used.<br /><br />\r\n\r\nFor example if you only have <strong>3</strong> photos taken in the locality of Montreal</strong> (WOE ID 3534) but your threshold is set to <strong>5</strong> then those photos will be "rolled up" and included instead with a place record for the region of Quebec (WOE ID 2344924).',
                "optional": "1",
                "name": "threshold",
            },
            {
                "text": "Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "min_upload_date",
            },
            {
                "text": "Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "max_upload_date",
            },
            {
                "text": "Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date should be in the form of a mysql datetime.",
                "optional": "1",
                "name": "min_taken_date",
            },
            {
                "text": "Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date should be in the form of a mysql datetime.",
                "optional": "1",
                "name": "max_taken_date",
            },
        ],
        "needslogin": True,
        "response": '<places total="1">\r\n   <place place_id="kH8dLOubBZRvX_YZ" woeid="2487956"\r\n               latitude="37.779" longitude="-122.420"\r\n               place_url="/United+States/California/San+Francisco"\r\n               place_type="locality"\r\n               photo_count="156">San Francisco, California</place>\r\n</places>',
        "name": "flickr.places.placesForUser",
    },
    "flickr.photos.getAllContexts": {
        "errors": [
            {
                "text": "The photo id passed was not the id of a valid photo.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns all visible sets and pools the photo belongs to.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The photo to return information for.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "needslogin": False,
        "response": '<set id="392" title="\u8bb0\u5fc6\u7fa4\u7ec4" />\r\n<pool id="34427465471@N01" title="FlickrDiscuss" />',
        "name": "flickr.photos.getAllContexts",
    },
    "flickr.urls.getUserProfile": {
        "errors": [
            {
                "text": "The NSID specified was not a valid user.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "No user_id was passed and the calling user was not logged in.",
                "message": "No user specified",
                "code": "2",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns the url to a user's profile.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user to fetch the url for. If omitted, the calling user is assumed.",
                "optional": "1",
                "name": "user_id",
            },
        ],
        "needslogin": False,
        "response": '<user nsid="12037949754@N01" url="http://www.flickr.com/people/bees/" />',
        "name": "flickr.urls.getUserProfile",
    },
    "flickr.photos.getPerms": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id of a photo belonging to the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get permissions for a photo.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to get permissions for.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "needslogin": True,
        "response": '<perms id="2733" ispublic="1" isfriend="1" isfamily="0" permcomment="0" permaddmeta="1" /> ',
        "name": "flickr.photos.getPerms",
    },
    "flickr.tags.getListUserPopular": {
        "errors": [
            {
                "text": "The user NSID passed was not a valid user NSID and the calling user was not logged in.\r\n",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get the popular tags for a given user (or the currently logged in user).",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user to fetch the tag list for. If this argument is not specified, the currently logged in user (if any) is assumed.",
                "optional": "1",
                "name": "user_id",
            },
            {
                "text": "Number of popular tags to return. defaults to 10 when this argument is not present.",
                "optional": "1",
                "name": "count",
            },
        ],
        "needslogin": False,
        "response": '<who id="12037949754@N01">\r\n\t<tags>\r\n\t\t<tag count="10">bar</tag> \r\n\t\t<tag count="11">foo</tag> \r\n\t\t<tag count="147">gull</tag> \r\n\t\t<tag count="3">tags</tag> \r\n\t\t<tag count="3">test</tag> \r\n\t</tags>\r\n</who>',
        "name": "flickr.tags.getListUserPopular",
    },
    "flickr.photos.geo.correctLocation": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": 'Before users may assign location data to a photo they must define who, by default, may view that information. Users can edit this preference at <a href="http://www.flickr.com/account/geo/privacy/">http://www.flickr.com/account/geo/privacy/</a>',
                "message": "User has not configured default viewing settings for location data.",
                "code": "1",
            },
            {
                "text": "No place ID was passed to the method",
                "message": "Missing place ID",
                "code": "2",
            },
            {
                "text": "The place ID passed to the method could not be identified",
                "message": "Not a valid place ID",
                "code": "3",
            },
            {
                "text": "There was an error trying to correct the location.",
                "message": "Server error correcting location.",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the photo whose WOE location is being corrected.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "A Flickr Places ID. (While optional, you must pass either a valid Places ID or a WOE ID.)",
                "optional": "1",
                "name": "place_id",
            },
            {
                "text": "A Where On Earth (WOE) ID. (While optional, you must pass either a valid Places ID or a WOE ID.)",
                "optional": "1",
                "name": "woe_id",
            },
            {
                "text": "The venue ID for a Foursquare location. (If not passed in with correction, any existing foursquare venue will be removed).",
                "optional": "0",
                "name": "foursquare_id",
            },
        ],
        "description": "",
        "needslogin": True,
        "name": "flickr.photos.geo.correctLocation",
    },
    "flickr.photosets.getInfo": {
        "errors": [
            {
                "text": "The photoset id was not valid.",
                "message": "Photoset not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Gets information about a photoset.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the photoset to fetch information for.",
                "optional": "0",
                "name": "photoset_id",
            },
        ],
        "needslogin": False,
        "response": '<photoset id="72157624618609504" owner="34427469121@N01" primary="4847770787" secret="6abd09a292" server="4153" farm="5" photos="55" count_views="523" count_comments="1" count_photos="43" count_videos="12" can_comment="1" date_create="1280530593" date_update="1308091378">\r\n    <title>Mah Kittehs</title>\r\n    <description>Sixty and Niner. Born on the 3rd of May, 2010, or thereabouts. Came to my place on Thursday, July 29, 2010.</description>\r\n</photoset>',
        "name": "flickr.photosets.getInfo",
    },
    "flickr.places.getInfoByUrl": {
        "errors": [
            {
                "text": "The flickr.com/places URL was not passed with the API method.",
                "message": "Place URL required.",
                "code": "2",
            },
            {
                "text": "Unable to find a valid place for the places URL.",
                "message": "Place not found.",
                "code": "3",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Lookup information about a place, by its flickr.com/places URL.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "A flickr.com/places URL in the form of /country/region/city. For example: /Canada/Quebec/Montreal",
                "optional": "0",
                "name": "url",
            },
        ],
        "needslogin": False,
        "response": '<place place_id="4hLQygSaBJ92" woeid="3534"\r\n   latitude="45.512" longitude="-73.554"\r\n   place_url="/Canada/Quebec/Montreal" place_type="locality"\r\n   has_shapedata="1">\r\n   <locality place_id="4hLQygSaBJ92" woeid="3534"\r\n      latitude="45.512" longitude="-73.554"\r\n      place_url="/Canada/Quebec/Montreal">Montreal</locality>\r\n   <county place_id="cFBi9x6bCJ8D5rba1g" woeid="29375198"\r\n      latitude="45.551" longitude="-73.600" \r\n      place_url="/cFBi9x6bCJ8D5rba1g">Montr\xe9al</county>\r\n   <region place_id="CrZUvXebApjI0.72" woeid="2344924" \r\n      latitude="53.890" longitude="-68.429"\r\n      place_url="/Canada/Quebec">Quebec</region>\r\n   <country place_id="EESRy8qbApgaeIkbsA" woeid="23424775"\r\n      latitude="62.358" longitude="-96.582" \r\n      place_url="/Canada">Canada</country>\r\n   <shapedata created="1223513357" alpha="0.012359619140625"\r\n      count_points="34778" count_edges="52">\r\n      <polylines>\r\n         <polyline>\r\n            45.427627563477,-73.589645385742 45.428966522217,-73.587898254395, etc...\r\n         </polyline>\r\n      </polylines>\r\n   </shapedata>\r\n</place>',
        "name": "flickr.places.getInfoByUrl",
    },
    "flickr.places.getChildrenWithPhotosPublic": {
        "errors": [
            {
                "text": "One or more required parameter is missing from the API call.",
                "message": "Required parameter missing",
                "code": "1",
            },
            {
                "text": "An invalid Places (or WOE) ID was passed with the API call.",
                "message": "Not a valid Places ID",
                "code": "2",
            },
            {
                "text": "No place could be found for the Places (or WOE) ID passed to the API call.",
                "message": "Place not found",
                "code": "3",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return a list of locations with public photos that are parented by a Where on Earth (WOE) or Places ID.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "A Flickr Places ID. (While optional, you must pass either a valid Places ID or a WOE ID.)",
                "optional": "1",
                "name": "place_id",
            },
            {
                "text": "A Where On Earth (WOE) ID. (While optional, you must pass either a valid Places ID or a WOE ID.)",
                "optional": "1",
                "name": "woe_id",
            },
        ],
        "needslogin": False,
        "response": '<places total="79">\r\n   <place place_id="HznQfdKbB58biy8sdA" woeid="26332794"\r\n      latitude="45.498" longitude="-73.575"\r\n      place_url="/Canada/Quebec/Montreal  /Montreal+Golden+Square+Mile"\r\n      place_type="neighbourhood" photo_count="2717">\r\n      Montreal Golden Square Mile, Montreal, QC, CA, Canada\r\n   </place>\r\n   <place place_id="K1rYWmGbB59rwn7lOA" woeid="26332799"\r\n      latitude="45.502" longitude="-73.578"\r\n      place_url="/Canada/Quebec/Montreal/Downtown+Montr%C3%A9al"\r\n      place_type="neighbourhood" photo_count="2317">\r\n      Downtown Montr\xe9al, Montreal, QC, CA, Canada\r\n  </place>\r\n\r\n   <!-- and so on... -->\r\n\r\n</places>',
        "name": "flickr.places.getChildrenWithPhotosPublic",
    },
    "flickr.photos.geo.removeLocation": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photo id was either invalid or was for a photo not viewable by the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The specified photo has not been geotagged - there is nothing to remove.",
                "message": "Photo has no location information",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo you want to remove location data from.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "description": "Removes the geo data associated with a photo.",
        "needslogin": True,
        "name": "flickr.photos.geo.removeLocation",
    },
    "flickr.contacts.getListRecentlyUploaded": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Limits the resultset to contacts that have uploaded photos since this date. The date should be in the form of a Unix timestamp.\r\n\r\nThe default offset is (1) hour and the maximum (24) hours. ",
                "optional": "1",
                "name": "date_lastupload",
            },
            {
                "text": 'Limit the result set to all contacts or only those who are friends or family. Valid options are:\r\n\r\n<ul>\r\n<li><strong>ff</strong> friends and family</li>\r\n<li><strong>all</strong> all your contacts</li>\r\n</ul>\r\nDefault value is "all".',
                "optional": "1",
                "name": "filter",
            },
        ],
        "description": "Return a list of contacts for a user who have recently uploaded photos along with the total count of photos uploaded.<br /><br />\r\n\r\nThis method is still considered experimental. We don't plan for it to change or to go away but so long as this notice is present you should write your code accordingly.",
        "needslogin": True,
        "name": "flickr.contacts.getListRecentlyUploaded",
    },
    "flickr.groups.members.getList": {
        "errors": [
            {"text": "", "message": "Group not found", "code": "1"},
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get a list of the members of a group.  The call must be signed on behalf of a Flickr member, and the ability to see the group membership will be determined by the Flickr member's group privileges.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Return a list of members for this group.  The group must be viewable by the Flickr member on whose behalf the API call is made.",
                "optional": "0",
                "name": "group_id",
            },
            {
                "text": 'Comma separated list of member types\r\n<ul>\r\n<li>2: member</li>\r\n<li>3: moderator</li>\r\n<li>4: admin</li>\r\n</ul>\r\nBy default returns all types.  (Returning super rare member type "1: narwhal" isn\'t supported by this API method)',
                "optional": "1",
                "name": "membertypes",
            },
            {
                "text": "Number of members to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<members page="1" pages="1" perpage="100" total="33">\r\n<member nsid="123456@N01" username="foo" iconserver="1" iconfarm="1" membertype="2"/>\r\n<member nsid="118210@N07" username="kewlchops666" iconserver="0" iconfarm="0" membertype="4"/>\r\n<member nsid="119377@N07" username="Alpha Shanan" iconserver="0" iconfarm="0" membertype="2"/>\r\n<member nsid="67783977@N00" username="fakedunstanp1" iconserver="1003" iconfarm="2" membertype="3"/>\r\n...\r\n</members>',
        "name": "flickr.groups.members.getList",
    },
    "flickr.stats.getPhotoReferrers": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The photo id was either invalid or was for a photo not owned by the calling user.",
                "message": "Photo not found",
                "code": "4",
            },
            {
                "text": "The domain provided is not in the expected format.",
                "message": "Invalid domain",
                "code": "5",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.stats.getPhotoReferrers",
        "explanation": "<p>There is one <code>&lt;referrer&gt;</code> element for each referring page, with attributes for the url and the number of views.</p>\r\n\r\n<p>Where the referring page is a search engine and we have identified the search term it will be given in the searchterm attribute.</p>",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format.\r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.",
                "optional": "0",
                "name": "date",
            },
            {
                "text": 'The domain to return referrers for. This should be a hostname (eg: "flickr.com") with no protocol or pathname.',
                "optional": "0",
                "name": "domain",
            },
            {
                "text": "The id of the photo to get stats for. If not provided, stats for all photos will be returned.",
                "optional": "1",
                "name": "photo_id",
            },
            {
                "text": "Number of referrers to return per page. If this argument is omitted, it defaults to 25. The maximum allowed value is 100.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<domain page="1" perpage="25" pages="1" total="3" name="flickr.com">\r\n\t<referrer url="http://flickr.com/" views="11"/>\r\n\t<referrer url="http://flickr.com/photos/friends/" views="8"/>\r\n\t<referrer url="http://flickr.com/search/?q=stats+api" views="2" searchterm="stats api"/>\r\n</domain>',
        "description": "Get a list of referrers from a given domain to a photo",
    },
    "flickr.contacts.getList": {
        "errors": [
            {
                "text": "The possible values are: name and time.",
                "message": "Invalid sort parameter.",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get a list of contacts for the calling user.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "An optional filter of the results. The following values are valid:<br />\r\n&nbsp;\r\n<dl>\r\n\t<dt><b><code>friends</code></b></dt>\r\n\t<dl>Only contacts who are friends (and not family)</dl>\r\n\r\n\t<dt><b><code>family</code></b></dt>\r\n\t<dl>Only contacts who are family (and not friends)</dl>\r\n\r\n\t<dt><b><code>both</code></b></dt>\r\n\t<dl>Only contacts who are both friends and family</dl>\r\n\r\n\t<dt><b><code>neither</code></b></dt>\r\n\t<dl>Only contacts who are neither friends nor family</dl>\r\n</dl>",
                "optional": "1",
                "name": "filter",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 1000. The maximum allowed value is 1000.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The order in which to sort the returned contacts. Defaults to name. The possible values are: name and time.",
                "optional": "1",
                "name": "sort",
            },
        ],
        "needslogin": True,
        "response": '<contacts page="1" pages="1" perpage="1000" total="3">\r\n\t<contact nsid="12037949629@N01" username="Eric" iconserver="1"\r\n\t\trealname="Eric Costello"\r\n\t\tfriend="1" family="0" ignored="1" /> \r\n\t<contact nsid="12037949631@N01" username="neb" iconserver="1"\r\n\t\trealname="Ben Cerveny"\r\n\t\tfriend="0" family="0" ignored="0" /> \r\n\t<contact nsid="41578656547@N01" username="cal_abc" iconserver="1"\r\n\t\trealname="Cal Henderson"\r\n\t\tfriend="1" family="1" ignored="0" />\r\n</contacts>',
        "name": "flickr.contacts.getList",
    },
    "flickr.stats.getPhotosetStats": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The photoset id was either invalid or was for a set not owned by the calling user.",
                "message": "Photoset not found",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get the number of views on a photoset for a given date.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format.\r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.",
                "optional": "0",
                "name": "date",
            },
            {
                "text": "The id of the photoset to get stats for.",
                "optional": "0",
                "name": "photoset_id",
            },
        ],
        "needslogin": True,
        "response": '<stats views="24" comments="1" />',
        "name": "flickr.stats.getPhotosetStats",
    },
    "flickr.places.placesForTags": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return a list of the top 100 unique places clustered by a given placetype for set of tags or machine tags. ",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The numeric ID for a specific place type to cluster photos by. <br /><br />\r\n\r\nValid place type IDs are :\r\n\r\n<ul>\r\n<li><strong>22</strong>: neighbourhood</li>\r\n<li><strong>7</strong>: locality</li>\r\n<li><strong>8</strong>: region</li>\r\n<li><strong>12</strong>: country</li>\r\n<li><strong>29</strong>: continent</li>\r\n</ul>",
                "optional": "0",
                "name": "place_type_id",
            },
            {
                "text": 'A Where on Earth identifier to use to filter photo clusters. For example all the photos clustered by <strong>locality</strong> in the United States (WOE ID <strong>23424977</strong>).\r\n<br /><br />\r\n<span style="font-style:italic;">(While optional, you must pass either a valid Places ID or a WOE ID.)</span>',
                "optional": "1",
                "name": "woe_id",
            },
            {
                "text": 'A Flickr Places identifier to use to filter photo clusters. For example all the photos clustered by <strong>locality</strong> in the United States (Place ID <strong>4KO02SibApitvSBieQ</strong>).\r\n<br /><br />\r\n<span style="font-style:italic;">(While optional, you must pass either a valid Places ID or a WOE ID.)</span>',
                "optional": "1",
                "name": "place_id",
            },
            {
                "text": 'The minimum number of photos that a place type must have to be included. If the number of photos is lowered then the parent place type for that place will be used.<br /><br />\r\n\r\nFor example if you only have <strong>3</strong> photos taken in the locality of Montreal</strong> (WOE ID 3534) but your threshold is set to <strong>5</strong> then those photos will be "rolled up" and included instead with a place record for the region of Quebec (WOE ID 2344924).',
                "optional": "1",
                "name": "threshold",
            },
            {
                "text": "A comma-delimited list of tags. Photos with one or more of the tags listed will be returned.",
                "optional": "1",
                "name": "tags",
            },
            {
                "text": "Either 'any' for an OR combination of tags, or 'all' for an AND combination. Defaults to 'any' if not specified.",
                "optional": "1",
                "name": "tag_mode",
            },
            {
                "text": 'Aside from passing in a fully formed machine tag, there is a special syntax for searching on specific properties :\r\n\r\n<ul>\r\n  <li>Find photos using the \'dc\' namespace :    <code>"machine_tags" => "dc:"</code></li>\r\n\r\n  <li> Find photos with a title in the \'dc\' namespace : <code>"machine_tags" => "dc:title="</code></li>\r\n\r\n  <li>Find photos titled "mr. camera" in the \'dc\' namespace : <code>"machine_tags" => "dc:title=\\"mr. camera\\"</code></li>\r\n\r\n  <li>Find photos whose value is "mr. camera" : <code>"machine_tags" => "*:*=\\"mr. camera\\""</code></li>\r\n\r\n  <li>Find photos that have a title, in any namespace : <code>"machine_tags" => "*:title="</code></li>\r\n\r\n  <li>Find photos that have a title, in any namespace, whose value is "mr. camera" : <code>"machine_tags" => "*:title=\\"mr. camera\\""</code></li>\r\n\r\n  <li>Find photos, in the \'dc\' namespace whose value is "mr. camera" : <code>"machine_tags" => "dc:*=\\"mr. camera\\""</code></li>\r\n\r\n </ul>\r\n\r\nMultiple machine tags may be queried by passing a comma-separated list. The number of machine tags you can pass in a single query depends on the tag mode (AND or OR) that you are querying with. "AND" queries are limited to (16) machine tags. "OR" queries are limited\r\nto (8).',
                "optional": "1",
                "name": "machine_tags",
            },
            {
                "text": "Either 'any' for an OR combination of tags, or 'all' for an AND combination. Defaults to 'any' if not specified.",
                "optional": "1",
                "name": "machine_tag_mode",
            },
            {
                "text": "Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "min_upload_date",
            },
            {
                "text": "Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "max_upload_date",
            },
            {
                "text": "Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date should be in the form of a mysql datetime.",
                "optional": "1",
                "name": "min_taken_date",
            },
            {
                "text": "Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date should be in the form of a mysql datetime.",
                "optional": "1",
                "name": "max_taken_date",
            },
        ],
        "needslogin": False,
        "response": '<places total="1">\r\n   <place place_id="kH8dLOubBZRvX_YZ" woeid="2487956"\r\n               latitude="37.779" longitude="-122.420"\r\n               place_url="/United+States/California/San+Francisco"\r\n               place_type="locality"\r\n               photo_count="156">San Francisco, California</place>\r\n</places>',
        "name": "flickr.places.placesForTags",
    },
    "flickr.photosets.addPhoto": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photoset id passed was not the id of avalid photoset owned by the calling user.",
                "message": "Photoset not found",
                "code": "1",
            },
            {
                "text": "The photo id passed was not the id of a valid photo owned by the calling user.",
                "message": "Photo not found",
                "code": "2",
            },
            {
                "text": "The photo is already a member of the photoset.",
                "message": "Photo already in set",
                "code": "3",
            },
            {
                "text": "A set has reached the upper limit for the number of photos allowed.",
                "message": "Maximum number of photos in set",
                "code": "10",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photoset to add a photo to.",
                "optional": "0",
                "name": "photoset_id",
            },
            {
                "text": "The id of the photo to add to the set.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "description": "Add a photo to the end of an existing photoset.",
        "needslogin": True,
        "name": "flickr.photosets.addPhoto",
    },
    "flickr.photos.geo.setPerms": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photo id was either invalid or was for a photo not viewable by the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The photo requested has no location data or is not viewable by the calling user.",
                "message": "Photo has no location information",
                "code": "2",
            },
            {
                "text": "Some or all of the required arguments were not supplied.",
                "message": "Required arguments missing.",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "1 to set viewing permissions for the photo's location data to public, 0 to set it to private.",
                "optional": "0",
                "name": "is_public",
            },
            {
                "text": "1 to set viewing permissions for the photo's location data to contacts, 0 to set it to private.",
                "optional": "0",
                "name": "is_contact",
            },
            {
                "text": "1 to set viewing permissions for the photo's location data to friends, 0 to set it to private.",
                "optional": "0",
                "name": "is_friend",
            },
            {
                "text": "1 to set viewing permissions for the photo's location data to family, 0 to set it to private.",
                "optional": "0",
                "name": "is_family",
            },
            {
                "text": "The id of the photo to get permissions for.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "description": "Set the permission for who may view the geo data associated with a photo.",
        "needslogin": True,
        "name": "flickr.photos.geo.setPerms",
    },
    "flickr.favorites.remove": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photo id passed was not in the user's favorites.",
                "message": "Photo not in favorites",
                "code": "1",
            },
            {
                "text": "user_id was passed as an argument, but photo_id is not owned by the authenticated user.",
                "message": "Cannot remove photo from that user's favorites",
                "code": "2",
            },
            {
                "text": "Invalid user_id argument.",
                "message": "User not found",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to remove from the user's favorites.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "NSID of the user whose favorites the photo should be removed from. This only works if the calling user owns the photo.",
                "optional": "1",
                "name": "user_id",
            },
        ],
        "description": "Removes a photo from a user's favorites list.",
        "needslogin": True,
        "name": "flickr.favorites.remove",
    },
    "flickr.groups.pools.remove": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The group_id passed did not refer to a valid group.",
                "message": "Group not found",
                "code": "1",
            },
            {
                "text": "The photo_id passed was not a valid id of a photo in the group pool.",
                "message": "Photo not in pool",
                "code": "2",
            },
            {
                "text": "The calling user doesn't own the photo and is not an administrator of the group, so may not remove the photo from the pool.",
                "message": "Insufficient permission to remove photo",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to remove from the group pool. The photo must either be owned by the calling user of the calling user must be an administrator of the group.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The NSID of the group who's pool the photo is to removed from.",
                "optional": "0",
                "name": "group_id",
            },
        ],
        "description": "Remove a photo from a group pool.",
        "needslogin": True,
        "name": "flickr.groups.pools.remove",
    },
    "flickr.photos.notes.edit": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The note id passed was not a valid note id",
                "message": "Note not found",
                "code": "1",
            },
            {
                "text": "The calling user does not have permission to edit the specified note",
                "message": "User cannot edit note",
                "code": "2",
            },
            {
                "text": "One or more of the required arguments were not supplied.",
                "message": "Missing required arguments",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {"text": "The id of the note to edit", "optional": "0", "name": "note_id"},
            {
                "text": "The left coordinate of the note",
                "optional": "0",
                "name": "note_x",
            },
            {
                "text": "The top coordinate of the note",
                "optional": "0",
                "name": "note_y",
            },
            {"text": "The width of the note", "optional": "0", "name": "note_w"},
            {"text": "The height of the note", "optional": "0", "name": "note_h"},
            {
                "text": "The description of the note",
                "optional": "0",
                "name": "note_text",
            },
        ],
        "description": "Edit a note on a photo. Coordinates and sizes are in pixels, based on the 500px image size shown on individual photo pages.\r\n",
        "needslogin": True,
        "name": "flickr.photos.notes.edit",
    },
    "flickr.groups.pools.getGroups": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.groups.pools.getGroups",
        "explanation": "<p>The <code>privacy</code> attribute is 1 for private groups, 2 for invite-only public groups and 3 for open public groups.</p>",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
            {
                "text": "Number of groups to return per page. If this argument is omitted, it defaults to 400. The maximum allowed value is 400.",
                "optional": "1",
                "name": "per_page",
            },
        ],
        "needslogin": True,
        "response": '<groups page="1" pages="1" per_page="400" total="3">\r\n\t<group nsid="33853651696@N01" name="Art and Literature Hoedown"\r\n\t\tadmin="0" privacy="3" photos="2" iconserver="1" /> \r\n\t<group nsid="34427465446@N01" name="FlickrIdeas"\r\n\t\tadmin="1" privacy="3" photos="20" iconserver="1" /> \r\n\t<group nsid="34427465497@N01" name="GNEverybody"\r\n\t\tadmin="0" privacy="3" photos="4" iconserver="1" /> \r\n</groups>',
        "description": "Returns a list of groups to which you can add photos.",
    },
    "flickr.photos.people.getList": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.photos.people.getList",
        "explanation": 'x, y, w and h correspond to the coordinates of the "bounding box" around a person in a photo. Since these co-ordinates are optional, these elements may not be present for every person.',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to get a list of people for.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "needslogin": False,
        "response": '<people total="1">\r\n  <person nsid="87944415@N00" username="hitherto" iconserver="1" iconfarm="1"\r\n          realname="Simon Batistoni" added_by="12037949754@N01" x="50" y="50"\r\n          w="100" h="100"/>\r\n</people>',
        "description": "Get a list of people in a given photo.",
    },
    "flickr.people.findByUsername": {
        "errors": [
            {
                "text": "No user with the supplied username was found.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return a user's NSID, given their username.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The username of the user to lookup.",
                "optional": "0",
                "name": "username",
            },
        ],
        "needslogin": False,
        "response": '<user nsid="12037949632@N01">\r\n\t<username>Stewart</username> \r\n</user>',
        "name": "flickr.people.findByUsername",
    },
    "flickr.people.getInfo": {
        "errors": [
            {
                "text": "The user id passed did not match a Flickr user.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.people.getInfo",
        "explanation": '<p>The <code>firstdate</code> element contains the unix timestamp of the first photo uploaded by the user. The <code>firstdatetaken</code> element contains the mysql datetime of the first photo taken by the user.</p>\r\n<p>The <code>iconserver</code> element is used to build the url to the users\' buddyicon - for more information please read the <a href="/services/api/misc.buddyicons.html">buddyicon guide</a>.</p>\r\n<p>\r\nIf the API call is authenticated contact information will also be returned as attributes on the person element.  <code>contact</code>, <code>friend</code>, and <code>family</code> are boolean flags describing the relationship between the <a href="/services/api/auth.spec.html">authenticated</a> user, and the person currently being inspected.   <code>revcontact</code>, <code>revfriend</code>, and <code>revfamily</code> is the reciprocal relationship.\r\n</p>',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user to fetch information about.",
                "optional": "0",
                "name": "user_id",
            },
            {
                "text": "As an alternative to user_id, load a member based on URL, either photos or people URL.",
                "optional": "0",
                "name": "url",
            },
            {
                "text": "If set to 1, it checks if the user is connected to Facebook and returns that information back.",
                "optional": "1",
                "name": "fb_connected",
            },
            {
                "text": "If set to 1, it returns the storage information about the user, like the storage used and storage available.",
                "optional": "1",
                "name": "storage",
            },
        ],
        "needslogin": False,
        "response": '<person nsid="12037949754@N01" ispro="0" iconserver="122" iconfarm="1">\r\n\t<username>bees</username>\r\n\t<realname>Cal Henderson</realname>\r\n        <mbox_sha1sum>eea6cd28e3d0003ab51b0058a684d94980b727ac</mbox_sha1sum>\r\n\t<location>Vancouver, Canada</location>\r\n\t<photosurl>http://www.flickr.com/photos/bees/</photosurl> \r\n\t<profileurl>http://www.flickr.com/people/bees/</profileurl> \r\n\t<photos>\r\n\t\t<firstdate>1071510391</firstdate>\r\n\t\t<firstdatetaken>1900-09-02 09:11:24</firstdatetaken>\r\n\t\t<count>449</count>\r\n\t</photos>\r\n</person>',
        "description": "Get information about a user.",
    },
    "flickr.photos.geo.batchCorrectLocation": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "Some or all of the required arguments were not supplied.",
                "message": "Required arguments missing",
                "code": "1",
            },
            {
                "text": "The latitude argument failed validation.",
                "message": "Not a valid latitude",
                "code": "2",
            },
            {
                "text": "The longitude argument failed validation.",
                "message": "Not a valid longitude",
                "code": "3",
            },
            {
                "text": "The accuracy argument failed validation.",
                "message": "Not a valid accuracy",
                "code": "4",
            },
            {
                "text": "An invalid Places (or WOE) ID was passed with the API call.",
                "message": "Not a valid Places ID",
                "code": "5",
            },
            {
                "text": "There were no geotagged photos found for the authed user at the supplied latitude, longitude and accuracy.",
                "message": "No photos geotagged at that location",
                "code": "6",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The latitude of the photos to be update whose valid range is -90 to 90. Anything more than 6 decimal places will be truncated.",
                "optional": "0",
                "name": "lat",
            },
            {
                "text": "The longitude of the photos to be updated whose valid range is -180 to 180. Anything more than 6 decimal places will be truncated.",
                "optional": "0",
                "name": "lon",
            },
            {
                "text": "Recorded accuracy level of the photos to be updated. World level is 1, Country is ~3, Region ~6, City ~11, Street ~16. Current range is 1-16. Defaults to 16 if not specified.",
                "optional": "0",
                "name": "accuracy",
            },
            {
                "text": "A Flickr Places ID. (While optional, you must pass either a valid Places ID or a WOE ID.)",
                "optional": "1",
                "name": "place_id",
            },
            {
                "text": "A Where On Earth (WOE) ID. (While optional, you must pass either a valid Places ID or a WOE ID.)",
                "optional": "1",
                "name": "woe_id",
            },
        ],
        "description": "Correct the places hierarchy for all the photos for a user at a given latitude, longitude and accuracy.<br /><br />\r\n\r\nBatch corrections are processed in a delayed queue so it may take a few minutes before the changes are reflected in a user's photos.",
        "needslogin": True,
        "name": "flickr.photos.geo.batchCorrectLocation",
    },
    "flickr.collections.getTree": {
        "errors": [
            {
                "text": "The specified user could not be found.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The specified collection does not exist.",
                "message": "Collection not found",
                "code": "2",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.collections.getTree",
        "explanation": "A nested tree of collections, and the collections and sets they contain.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the collection to fetch a tree for, or zero to fetch the root collection. Defaults to zero.",
                "optional": "1",
                "name": "collection_id",
            },
            {
                "text": "The ID of the account to fetch the collection tree for. Deafults to the calling user.",
                "optional": "1",
                "name": "user_id",
            },
        ],
        "needslogin": False,
        "response": '<collections>\r\n<collection id="12-72157594586579649" title="All My Photos" description="a collection" iconlarge="http://farm1.static.flickr.com/187/cols/37_43fac2cf79_l.jpg" \r\niconsmall="http://farm1.static.flickr.com/187/cols/56_43fac2cf79_s.jpg">\r\n<set id="92157594171298291" title="kitesurfing" description="a set"/>\r\n<set id="72157594247596158" title="faves" description="some favorites."/>\r\n</collection>\r\n</collections>',
        "description": "Returns a tree (or sub tree) of collections belonging to a given user.",
    },
    "flickr.stats.getCollectionDomains": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The collection id was either invalid or was for a collection not owned by the calling user.",
                "message": "Collection not found",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.stats.getCollectionDomains",
        "explanation": '<p>There is one <code>&lt;domain&gt;</code> element for each referring domain, with attributes for the domain name and the number of views.</p>\r\n\r\n<p>For details on the referrers coming from each domain listed you can call <a href="/services/api/flickr.stats.getCollectionReferrers.html">flickr.stats.getCollectionReferrers</a></p>',
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format.\r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.",
                "optional": "0",
                "name": "date",
            },
            {
                "text": "The id of the collection to get stats for. If not provided, stats for all collections will be returned.",
                "optional": "1",
                "name": "collection_id",
            },
            {
                "text": "Number of domains to return per page. If this argument is omitted, it defaults to 25. The maximum allowed value is 100.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<domains page="1" perpage="25" pages="1" total="3">\r\n\t<domain name="images.search.yahoo.com" views="127" />\r\n\t<domain name="flickr.com" views="122" />\r\n\t<domain name="images.google.com" views="70" />\r\n</domains>\r\n',
        "description": "Get a list of referring domains for a collection",
    },
    "flickr.photos.comments.deleteComment": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The requested comment is against a photo which no longer exists.",
                "message": "Photo not found.",
                "code": "1",
            },
            {
                "text": "The comment id passed was not a valid comment id",
                "message": "Comment not found.",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the comment to edit.",
                "optional": "0",
                "name": "comment_id",
            },
        ],
        "description": "Delete a comment as the currently authenticated user.",
        "needslogin": True,
        "name": "flickr.photos.comments.deleteComment",
    },
    "flickr.blogs.getList": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.blogs.getList",
        "explanation": "<p>The <code>needspassword</code> attribute indicates whether a call to <code>flickr.blogs.postPhoto</code> for this blog will require a password to be sent. When flickr has a password already stored, <code>needspassword</code> is 0</p>",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": 'Optionally only return blogs for a given service id.  You can get a list of from <a href="/services/api/flickr.blogs.getServices.html">flickr.blogs.getServices()</a>.',
                "optional": "1",
                "name": "service",
            },
        ],
        "needslogin": True,
        "response": '<blogs>\r\n\t<blog id="73" name="Bloxus test" needspassword="0"\r\n\t\turl="http://remote.bloxus.com/" /> \r\n\t<blog id="74" name="Manila Test" needspassword="1"\r\n\t\turl="http://flickrtest1.userland.com/" /> \r\n</blogs>',
        "description": "Get a list of configured blogs for the calling user.",
    },
    "flickr.panda.getPhotos": {
        "errors": [
            {
                "text": "One or more required parameters was not included with your request.",
                "message": "Required parameter missing.",
                "code": "1",
            },
            {
                "text": "You requested a panda we haven't met yet.",
                "message": "Unknown panda",
                "code": "2",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.panda.getPhotos",
        "explanation": "When calling this API method please ensure that your code uses the <strong>lastupdate</strong> and <strong>interval</strong> attributes to determine when to request new photos. <em>lastupdate</em> is a Unix timestamp indicating when the list of photos was generated and <em>interval</em> is the number of seconds to wait before polling the Flickr API again.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": 'The name of the panda to ask for photos from. There are currently three pandas named:<br /><br />\r\n\r\n<ul>\r\n<li><strong><a href="http://flickr.com/photos/ucumari/126073203/">ling ling</a></strong></li>\r\n<li><strong><a href="http://flickr.com/photos/lynnehicks/136407353">hsing hsing</a></strong></li>\r\n<li><strong><a href="http://flickr.com/photos/perfectpandas/1597067182/">wang wang</a></strong></li>\r\n</ul>\r\n\r\n<br />You can fetch a list of all the current pandas using the <a href="/services/api/flickr.panda.getList.html">flickr.panda.getList</a> API method.',
                "optional": "0",
                "name": "panda_name",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "needslogin": False,
        "response": '<photos interval="60000" lastupdate="1235765058272" total="120" panda="ling ling">\r\n    <photo title="Shorebirds at Pillar Point" id="3313428913" secret="2cd3cb44cb"\r\n        server="3609" farm="4" owner="72442527@N00" ownername="Pat Ulrich"/>\r\n    <photo title="Battle of the sky" id="3313713993" secret="3f7f51500f"\r\n        server="3382" farm="4" owner="10459691@N05" ownername="Sven Ericsson"/>\r\n    <!-- and so on -->\r\n</photos>',
        "description": 'Ask the <a href="http://www.flickr.com/explore/panda">Flickr Pandas</a> for a list of recent public (and "safe") photos.\r\n<br/><br/>\r\nMore information about the pandas can be found on the <a href="http://code.flickr.com/blog/2009/03/03/panda-tuesday-the-history-of-the-panda-new-apis-explore-and-you/">dev blog</a>.',
    },
    "flickr.machinetags.getNamespaces": {
        "errors": [
            {
                "text": "Missing or invalid predicate argument.",
                "message": "Not a valid predicate.",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.machinetags.getNamespaces",
        "explanation": '"Usage" gives you roughly how popular a machine tags, while "predicates" is the count of distinct predicates a namespace has.',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Limit the list of namespaces returned to those that have the following predicate.",
                "optional": "1",
                "name": "predicate",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": False,
        "response": '<namespaces page="1" total="5" perpage="500" pages="1">\r\n  <namespace usage="6538" predicates="13">aero</namespace>\r\n  <namespace usage="9072" predicates="24">flickr</namespace>\r\n  <namespace usage="670270" predicates="35">geo</namespace>\r\n  <namespace usage="23903" predicates="36">taxonomy</namespace>\r\n  <namespace usage="50449" predicates="4">upcoming</namespace>\r\n</namespaces>\r\n',
        "description": "Return a list of unique namespaces, optionally limited by a given predicate, in alphabetical order.",
    },
    "flickr.groups.pools.getPhotos": {
        "errors": [
            {
                "text": "The group id passed was not a valid group id.",
                "message": "Group not found",
                "code": "1",
            },
            {
                "text": "The logged in user (if any) does not have permission to view the pool for this group.",
                "message": "You don't have permission to view this pool",
                "code": "2",
            },
            {
                "text": "The user specified by user_id does not exist.",
                "message": "Unknown user",
                "code": "3",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns a list of pool photos for a given group, based on the permissions of the group and the user logged in (if any).",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the group who's pool you which to get the photo list for.",
                "optional": "0",
                "name": "group_id",
            },
            {
                "text": "A tag to filter the pool with. At the moment only one tag at a time is supported.",
                "optional": "1",
                "name": "tags",
            },
            {
                "text": "The nsid of a user. Specifiying this parameter will retrieve for you only those photos that the user has contributed to the group pool.",
                "optional": "1",
                "name": "user_id",
            },
            {"text": "", "optional": "1", "name": "jump_to"},
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "needslogin": False,
        "response": '<photos page="1" pages="1" perpage="1" total="1">\r\n\t<photo id="2645" owner="12037949754@N01" title="36679_o"\r\n\tsecret="a9f4a06091" server="2"\r\n\tispublic="1" isfriend="0" isfamily="0"\r\n\townername="Bees / ?" dateadded="1089918707" /> \r\n</photos>',
        "name": "flickr.groups.pools.getPhotos",
    },
    "flickr.stats.getPhotostreamReferrers": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The domain provided is not in the expected format.",
                "message": "Invalid domain",
                "code": "5",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.stats.getPhotostreamReferrers",
        "explanation": "<p>There is one <code>&lt;referrer&gt;</code> element for each referring page, with attributes for the url and the number of views.</p>\r\n\r\n<p>Where the referring page is a search engine and we have identified the search term it will be given in the searchterm attribute.</p>",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format. \r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.",
                "optional": "0",
                "name": "date",
            },
            {
                "text": 'The domain to return referrers for. This should be a hostname (eg: "flickr.com") with no protocol or pathname.',
                "optional": "0",
                "name": "domain",
            },
            {
                "text": "Number of referrers to return per page. If this argument is omitted, it defaults to 25. The maximum allowed value is 100.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<domain page="1" perpage="25" pages="1" total="3" name="flickr.com">\r\n\t<referrer url="http://flickr.com/" views="11"/>\r\n\t<referrer url="http://flickr.com/photos/friends/" views="8"/>\r\n\t<referrer url="http://flickr.com/search/?q=stats+api" views="2" searchterm="stats api"/>\r\n</domain>',
        "description": "Get a list of referrers from a given domain to a user's photostream",
    },
    "flickr.photos.getUntagged": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.",
                "optional": "1",
                "name": "min_upload_date",
            },
            {
                "text": "Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.",
                "optional": "1",
                "name": "max_upload_date",
            },
            {
                "text": "Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date should be in the form of a mysql datetime or unix timestamp.",
                "optional": "1",
                "name": "min_taken_date",
            },
            {
                "text": "Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.",
                "optional": "1",
                "name": "max_taken_date",
            },
            {
                "text": "Return photos only matching a certain privacy level. Valid values are:\r\n<ul>\r\n<li>1 public photos</li>\r\n<li>2 private photos visible to friends</li>\r\n<li>3 private photos visible to family</li>\r\n<li>4 private photos visible to friends &amp; family</li>\r\n<li>5 completely private photos</li>\r\n</ul>\r\n",
                "optional": "1",
                "name": "privacy_filter",
            },
            {
                "text": "Filter results by media type. Possible values are <code>all</code> (default), <code>photos</code> or <code>videos</code>",
                "optional": "1",
                "name": "media",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "description": "Returns a list of your photos with no tags.",
        "needslogin": True,
        "name": "flickr.photos.getUntagged",
    },
    "flickr.groups.search": {
        "errors": [
            {
                "text": "The required text argument was ommited.",
                "message": "No text passed",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Search for groups. 18+ groups will only be returned for authenticated calls where the authenticated user is over 18.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {"text": "The text to search for.", "optional": "0", "name": "text"},
            {
                "text": "Number of groups to return per page. If this argument is ommited, it defaults to 100. The maximum allowed value is 500.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is ommited, it defaults to 1. ",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": False,
        "response": '<groups page="1" pages="14" perpage="5" total="67">\r\n\t<group nsid="3000@N02"\r\n\t\tname="Frito\'s Test Group" eighteenplus="0" /> \r\n\t<group nsid="32825757@N00"\r\n\t\tname="Free for All" eighteenplus="0" /> \r\n\t<group nsid="33335981560@N01"\r\n\t\tname="joly\'s mothers" eighteenplus="0" /> \r\n\t<group nsid="33853651681@N01"\r\n\t\tname="Wintermute tower" eighteenplus="0" /> \r\n\t<group nsid="33853651696@N01"\r\n\t\tname="Art and Literature Hoedown" eighteenplus="0" /> \r\n</groups>',
        "name": "flickr.groups.search",
    },
    "flickr.push.subscribe": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {
                "text": "One of the required arguments for the method was not provided.",
                "message": "Required parameter missing",
                "code": "1",
            },
            {
                "text": "One of the arguments was specified with an illegal value.",
                "message": "Invalid parameter value",
                "code": "2",
            },
            {
                "text": "A different subscription already exists that uses the same callback URL.",
                "message": "Callback URL already in use for a different subscription",
                "code": "3",
            },
            {
                "text": "The verification callback failed, or failed to return the expected response to confirm the subscription.",
                "message": "Callback failed or invalid response",
                "code": "4",
            },
            {
                "text": "PuSH subscriptions are currently restricted to Pro account holders.",
                "message": "Service currently available only to pro accounts",
                "code": "5",
            },
            {
                "text": "A subscription with those details exists already, but it is in a pending (non-verified) state. Please wait a bit for the verification callback to complete before attempting to update the subscription.",
                "message": "Subscription awaiting verification callback response - try again later",
                "code": "6",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": 'The type of subscription. See <a href="http://www.flickr.com/services/api/flickr.push.getTopics.htm">flickr.push.getTopics</a>.',
                "optional": "0",
                "name": "topic",
            },
            {
                "text": "The url for the subscription endpoint. Limited to 255 bytes, and must be unique for this user, i.e. no two subscriptions for a given user may use the same callback url.",
                "optional": "0",
                "name": "callback",
            },
            {
                "text": 'The verification mode, either <code>sync</code> or <code>async</code>. See the <a href="http://pubsubhubbub.googlecode.com/svn/trunk/pubsubhubbub-core-0.3.html#subscribingl">Google PubSubHubbub spec</a> for details.',
                "optional": "0",
                "name": "verify",
            },
            {
                "text": 'The verification token to be echoed back to the subscriber during the verification callback, as per the <a href="http://pubsubhubbub.googlecode.com/svn/trunk/pubsubhubbub-core-0.3.html#subscribing">Google PubSubHubbub spec</a>. Limited to 200 bytes.',
                "optional": "1",
                "name": "verify_token",
            },
            {
                "text": "Number of seconds for which the subscription will be valid. Legal values are 60 to 86400 (1 minute to 1 day). If not present, the subscription will be auto-renewing.",
                "optional": "1",
                "name": "lease_seconds",
            },
            {
                "text": 'A 32-bit integer for a <a href="http://developer.yahoo.com/geo/geoplanet/">Where on Earth ID</a>. Only valid if <code>topic</code> is <code>geo</code>.\r\n<br/><br/>\r\nThe order of precedence for geo subscriptions is : woe ids, place ids, radial i.e. the <code>lat, lon</code> parameters will be ignored if <code>place_ids</code> is present, which will be ignored if <code>woe_ids</code> is present.',
                "optional": "1",
                "name": "woe_ids",
            },
            {
                "text": "A comma-separated list of Flickr place IDs. Only valid if <code>topic</code> is <code>geo</code>.\r\n<br/><br/>\r\nThe order of precedence for geo subscriptions is : woe ids, place ids, radial i.e. the <code>lat, lon</code> parameters will be ignored if <code>place_ids</code> is present, which will be ignored if <code>woe_ids</code> is present.",
                "optional": "1",
                "name": "place_ids",
            },
            {
                "text": "A latitude value, in decimal format. Only valid if <code>topic</code> is <code>geo</code>. Defines the latitude for a radial query centered around (lat, lon).\r\n<br/><br/>\r\nThe order of precedence for geo subscriptions is : woe ids, place ids, radial i.e. the <code>lat, lon</code> parameters will be ignored if <code>place_ids</code> is present, which will be ignored if <code>woe_ids</code> is present.",
                "optional": "1",
                "name": "lat",
            },
            {
                "text": "A longitude value, in decimal format. Only valid if <code>topic</code> is <code>geo</code>. Defines the longitude for a radial query centered around (lat, lon).\r\n<br/><br/>\r\nThe order of precedence for geo subscriptions is : woe ids, place ids, radial i.e. the <code>lat, lon</code> parameters will be ignored if <code>place_ids</code> is present, which will be ignored if <code>woe_ids</code> is present.",
                "optional": "1",
                "name": "lon",
            },
            {
                "text": "A radius value, in the units defined by radius_units. Only valid if <code>topic</code> is <code>geo</code>. Defines the radius of a circle for a radial query centered around (lat, lon). Default is 5 km.\r\n<br/><br/>\r\nThe order of precedence for geo subscriptions is : woe ids, place ids, radial i.e. the <code>lat, lon</code> parameters will be ignored if <code>place_ids</code> is present, which will be ignored if <code>woe_ids</code> is present.",
                "optional": "1",
                "name": "radius",
            },
            {
                "text": "Defines the units for the radius parameter. Only valid if <code>topic</code> is <code>geo</code>. Options are <code>mi</code> and <code>km</code>. Default is <code>km</code>.\r\n<br/><br/>\r\nThe order of precedence for geo subscriptions is : woe ids, place ids, radial i.e. the <code>lat, lon</code> parameters will be ignored if <code>place_ids</code> is present, which will be ignored if <code>woe_ids</code> is present.",
                "optional": "1",
                "name": "radius_units",
            },
            {
                "text": "Defines the minimum accuracy required for photos to be included in a subscription. Only valid if <code>topic</code> is <code>geo</code> Legal values are 1-16, default is 1 (i.e. any accuracy level).\r\n<ul>\r\n<li>World level is 1</li>\r\n<li>Country is ~3</li>\r\n<li>Region is ~6</li>\r\n<li>City is ~11</li>\r\n<li>Street is ~16</li>\r\n</ul>",
                "optional": "1",
                "name": "accuracy",
            },
            {
                "text": 'A comma-separated list of nsids representing Flickr Commons institutions (see <a href="http://www.flickr.com/services/api/flickr.commons.getInstitutions.html">flickr.commons.getInstitutions</a>). Only valid if <code>topic</code> is <code>commons</code>. If not present this argument defaults to all Flickr Commons institutions.',
                "optional": "1",
                "name": "nsids",
            },
            {
                "text": "A comma-separated list of strings to be used for tag subscriptions. Photos with one or more of the tags listed will be included in the subscription. Only valid if the <code>topic</code> is <code>tags</code>.",
                "optional": "1",
                "name": "tags",
            },
            {
                "text": "A comma-separated list of strings to be used for machine tag subscriptions. Photos with one or more of the machine tags listed will be included in the subscription. Currently the format must be <code>namespace:tag_name=value</code> Only valid if the <code>topic</code> is <code>tags</code>.",
                "optional": "1",
                "name": "machine_tags",
            },
            {"text": "", "optional": "1", "name": "update_type"},
            {"text": "", "optional": "1", "name": "output_format"},
            {"text": "", "optional": "1", "name": "mailto"},
        ],
        "description": "In ur pandas, tickling ur unicorn\r\n<br><br>\r\n<i>(this method is experimental and may change)</i>",
        "needslogin": True,
        "name": "flickr.push.subscribe",
    },
    "flickr.photos.suggestions.suggestLocation": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The photo whose location you are suggesting.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The latitude whose valid range is -90 to 90. Anything more than 6 decimal places will be truncated.",
                "optional": "0",
                "name": "lat",
            },
            {
                "text": "The longitude whose valid range is -180 to 180. Anything more than 6 decimal places will be truncated.",
                "optional": "0",
                "name": "lon",
            },
            {
                "text": "Recorded accuracy level of the location information. World level is 1, Country is ~3, Region ~6, City ~11, Street ~16. Current range is 1-16. Defaults to 16 if not specified.",
                "optional": "1",
                "name": "accuracy",
            },
            {
                "text": "The WOE ID of the location used to build the location hierarchy for the photo.",
                "optional": "1",
                "name": "woe_id",
            },
            {
                "text": "The Flickr Places ID of the location used to build the location hierarchy for the photo.",
                "optional": "1",
                "name": "place_id",
            },
            {
                "text": "A short note or history to include with the suggestion.",
                "optional": "1",
                "name": "note",
            },
        ],
        "description": "Suggest a geotagged location for a photo.",
        "needslogin": True,
        "name": "flickr.photos.suggestions.suggestLocation",
    },
    "flickr.people.getGroups": {
        "errors": [
            {
                "text": "The user id passed did not match a Flickr user.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.people.getGroups",
        "explanation": "The admin attribute indicates whether the user is an administrator of the group. The eighteenplus attribute indicates if the group is visible to members over 18 only. The invite_only attribute indicates whether a user can join the group without administrator approval.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user to fetch groups for.",
                "optional": "0",
                "name": "user_id",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>privacy</code>, <code>throttle</code>, <code>restrictions</code>",
                "optional": "1",
                "name": "extras",
            },
        ],
        "needslogin": True,
        "response": '<groups>\r\n  <group nsid="17274427@N00" name="Cream of the Crop - Please read the rules" iconfarm="1" iconserver="1" admin="0" eighteenplus="0" invitation_only="0" members="11935" pool_count="12522" />\r\n  <group nsid="20083316@N00" name="Apple" iconfarm="1" iconserver="1" admin="0" eighteenplus="0" invitation_only="0" members="11776" pool_count="62438" />\r\n  <group nsid="34427469792@N01" name="FlickrCentral" iconfarm="1" iconserver="1" admin="0" eighteenplus="0" invitation_only="0" members="168055" pool_count="5280930" />\r\n  <group nsid="37718678610@N01" name="Typography and Lettering" iconfarm="1" iconserver="1" admin="0" eighteenplus="0" invitation_only="0" members="17318" pool_count="130169" />\r\n</groups>',
        "description": "Returns the list of groups a user is a member of.",
    },
    "flickr.places.getTopPlacesList": {
        "errors": [
            {
                "text": "One or more required parameters with missing from your request.",
                "message": "Required parameter missing",
                "code": "1",
            },
            {
                "text": "An unknown or unsupported place type ID was passed with your request.",
                "message": "Not a valid place type.",
                "code": "2",
            },
            {
                "text": "The date argument passed with your request is invalid.",
                "message": "Not a valid date.",
                "code": "3",
            },
            {
                "text": "An invalid Places (or WOE) identifier was included with your request.",
                "message": "Not a valid Place ID",
                "code": "4",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return the top 100 most geotagged places for a day.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The numeric ID for a specific place type to cluster photos by. <br /><br />\r\n\r\nValid place type IDs are :\r\n\r\n<ul>\r\n<li><strong>22</strong>: neighbourhood</li>\r\n<li><strong>7</strong>: locality</li>\r\n<li><strong>8</strong>: region</li>\r\n<li><strong>12</strong>: country</li>\r\n<li><strong>29</strong>: continent</li>\r\n</ul>",
                "optional": "0",
                "name": "place_type_id",
            },
            {
                "text": "A valid date in YYYY-MM-DD format. The default is yesterday.",
                "optional": "1",
                "name": "date",
            },
            {
                "text": "Limit your query to only those top places belonging to a specific Where on Earth (WOE) identifier.",
                "optional": "1",
                "name": "woe_id",
            },
            {
                "text": "Limit your query to only those top places belonging to a specific Flickr Places identifier.",
                "optional": "1",
                "name": "place_id",
            },
        ],
        "needslogin": False,
        "response": '<places total="100" date_start="1246320000" date_stop="1246406399">\r\n   <place place_id="4KO02SibApitvSBieQ" woeid="23424977"\r\n       latitude="48.890" longitude="-116.982" \r\n       place_url="/United+States" place_type="country" \r\n       place_type_id="12" photo_count="23371">United States</place>\r\n   <!-- and so on... -->\r\n</places>',
        "name": "flickr.places.getTopPlacesList",
    },
    "flickr.photos.getInfo": {
        "errors": [
            {
                "text": "The photo id was either invalid or was for a photo not viewable by the calling user.",
                "message": "Photo not found.",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.photos.getInfo",
        "explanation": "<p>The <code>&lt;permissions&gt;</code> element is only returned for photos owned by the calling user. The <code>isfavorite</code> attribute only makes sense for logged in users who don't own the photo. The <code>rotation</code> attribute is the current clockwise rotation, in degrees, by which the smaller image sizes differ from the original image.</p>\r\n\r\n<p>The <code>&lt;date&gt;</code> element's <code>lastupdate</code> attribute is a Unix timestamp indicating the last time the photo, or any of its metadata (tags, comments, etc.) was modified.</p>",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to get information for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The secret for the photo. If the correct secret is passed then permissions checking is skipped. This enables the 'sharing' of individual photos by passing around the id and secret.",
                "optional": "1",
                "name": "secret",
            },
            {"text": "", "optional": "1", "name": "humandates"},
            {"text": "", "optional": "1", "name": "privacy_filter"},
            {"text": "", "optional": "1", "name": "get_contexts"},
            {
                "text": "Return geofence information in the photo's location property",
                "optional": "1",
                "name": "get_geofences",
            },
            {"text": "", "optional": "1", "name": "extras"},
        ],
        "needslogin": False,
        "response": '<photo id="2733" secret="123456" server="12"\r\n\tisfavorite="0" license="3" rotation="90" \r\n\toriginalsecret="1bc09ce34a" originalformat="png">\r\n\t<owner nsid="12037949754@N01" username="Bees"\r\n\t\trealname="Cal Henderson" location="Bedford, UK" />\r\n\t<title>orford_castle_taster</title>\r\n\t<description>hello!</description>\r\n\t<visibility ispublic="1" isfriend="0" isfamily="0" />\r\n\t<dates posted="1100897479" taken="2004-11-19 12:51:19"\r\n\t\ttakengranularity="0" lastupdate="1093022469" />\r\n\t<permissions permcomment="3" permaddmeta="2" />\r\n\t<editability cancomment="1" canaddmeta="1" />\r\n\t<comments>1</comments>\r\n\t<notes>\r\n\t\t<note id="313" author="12037949754@N01"\r\n\t\t\tauthorname="Bees" x="10" y="10"\r\n\t\t\tw="50" h="50">foo</note>\r\n\t</notes>\r\n\t<tags>\r\n\t\t<tag id="1234" author="12037949754@N01" raw="woo yay">wooyay</tag>\r\n\t\t<tag id="1235" author="12037949754@N01" raw="hoopla">hoopla</tag>\r\n\t</tags>\r\n\t<urls>\r\n\t\t<url type="photopage">http://www.flickr.com/photos/bees/2733/</url> \r\n\t</urls>\r\n</photo>',
        "description": "Get information about a photo. The calling user must have permission to view the photo.",
    },
    "flickr.photos.getSizes": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The calling user does not have permission to view the photo.",
                "message": "Permission denied",
                "code": "2",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns the available sizes for a photo.  The calling user must have permission to view the photo.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to fetch size information for.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "needslogin": False,
        "response": '<sizes canblog="1" canprint="1" candownload="1">\r\n    <size label="Square" width="75" height="75" source="http://farm2.staticflickr.com/1103/567229075_2cf8456f01_s.jpg" url="http://www.flickr.com/photos/stewart/567229075/sizes/sq/" media="photo" />\r\n    <size label="Large Square" width="150" height="150" source="http://farm2.staticflickr.com/1103/567229075_2cf8456f01_q.jpg" url="http://www.flickr.com/photos/stewart/567229075/sizes/q/" media="photo" />\r\n    <size label="Thumbnail" width="100" height="75" source="http://farm2.staticflickr.com/1103/567229075_2cf8456f01_t.jpg" url="http://www.flickr.com/photos/stewart/567229075/sizes/t/" media="photo" />\r\n    <size label="Small" width="240" height="180" source="http://farm2.staticflickr.com/1103/567229075_2cf8456f01_m.jpg" url="http://www.flickr.com/photos/stewart/567229075/sizes/s/" media="photo" />\r\n    <size label="Small 320" width="320" height="240" source="http://farm2.staticflickr.com/1103/567229075_2cf8456f01_n.jpg" url="http://www.flickr.com/photos/stewart/567229075/sizes/n/" media="photo" />\r\n    <size label="Medium" width="500" height="375" source="http://farm2.staticflickr.com/1103/567229075_2cf8456f01.jpg" url="http://www.flickr.com/photos/stewart/567229075/sizes/m/" media="photo" />\r\n    <size label="Medium 640" width="640" height="480" source="http://farm2.staticflickr.com/1103/567229075_2cf8456f01_z.jpg?zz=1" url="http://www.flickr.com/photos/stewart/567229075/sizes/z/" media="photo" />\r\n    <size label="Medium 800" width="800" height="600" source="http://farm2.staticflickr.com/1103/567229075_2cf8456f01_c.jpg" url="http://www.flickr.com/photos/stewart/567229075/sizes/c/" media="photo" />\r\n    <size label="Large" width="1024" height="768" source="http://farm2.staticflickr.com/1103/567229075_2cf8456f01_b.jpg" url="http://www.flickr.com/photos/stewart/567229075/sizes/l/" media="photo" />\r\n    <size label="Original" width="2400" height="1800" source="http://farm2.staticflickr.com/1103/567229075_6dc09dc6da_o.jpg" url="http://www.flickr.com/photos/stewart/567229075/sizes/o/" media="photo" />\r\n</sizes>\r\n',
        "name": "flickr.photos.getSizes",
    },
    "flickr.prefs.getSafetyLevel": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns the default safety level preference for the user.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": True,
        "response": '<rsp stat="ok">\r\n<person nsid="12037949754@N01" safety_level="1" />\r\n</rsp>',
        "name": "flickr.prefs.getSafetyLevel",
    },
    "flickr.galleries.create": {
        "errors": [
            {
                "text": "One or more of the required parameters was missing from your API call.",
                "message": "Required parameter missing",
                "code": "1",
            },
            {
                "text": "The title or the description could not be validated.",
                "message": "Invalid title or description",
                "code": "2",
            },
            {
                "text": "There was a problem creating the gallery.",
                "message": "Failed to add gallery",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.galleries.create",
        "explanation": "The ID of the newly created gallery, and its URL.",
        "needssigning": True,
        "requiredperms": "write",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {"text": "The name of the gallery", "optional": "0", "name": "title"},
            {
                "text": "A short description for the gallery",
                "optional": "0",
                "name": "description",
            },
            {
                "text": "The first photo to add to your gallery",
                "optional": "1",
                "name": "primary_photo_id",
            },
        ],
        "needslogin": True,
        "response": '  <gallery id="50736-72157623680420409" url="http://www.flickr.com/photos/kellan/galleries/72157623680420409" /> \r\n',
        "description": "Create a new gallery for the calling user.",
    },
    "flickr.cameras.getBrandModels": {
        "errors": [
            {
                "text": "Unable to find the given brand ID.",
                "message": "Brand not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Retrieve all the models for a given camera brand.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the requested brand (as returned from flickr.cameras.getBrands).",
                "optional": "0",
                "name": "brand",
            },
        ],
        "needslogin": False,
        "response": '<rsp stat="ok">\r\n  <cameras brand="apple">\r\n    <camera id="iphone_9000">\r\n      <name>iPhone 9000</name>\r\n      <details>\r\n        <megapixels>22.0</megapixels>\r\n        <zoom>3.0</zoom>\r\n        <lcd_size>40.5</lcd_size>\r\n        <storage_type>Flash</storage_type>\r\n      </details>\r\n      <images>\r\n        <small>http://farm3.staticflickr.com/1234/cameras/123456_model_small_123456.jpg</small>\r\n        <large>http://farm3.staticflickr.com/1234/cameras/123456_model_large_123456.jpg</large>\r\n      </images>\r\n    </camera>\r\n  </cameras>\r\n</rsp>',
        "name": "flickr.cameras.getBrandModels",
    },
    "flickr.groups.discuss.topics.getList": {
        "errors": [
            {
                "text": "The group_id is invalid",
                "message": "Group not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get a list of discussion topics in a group.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the group to fetch information for.",
                "optional": "0",
                "name": "group_id",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": False,
        "response": '<rsp stat="ok">\r\n  <topics group_id="46744914@N00" iconserver="1" iconfarm="1" name="Tell a story in 5 frames (Visual story telling)" members="12428" privacy="3" lang="en-us" ispoolmoderated="1" total="4621" page="1" per_page="2" pages="2310">\r\n    <topic id="72157625038324579" subject="A long time ago in a galaxy far, far away..." author="53930889@N04" authorname="Smallportfolio_jm08" role="member" iconserver="5169" iconfarm="6" count_replies="8" can_edit="0" can_delete="0" can_reply="0" is_sticky="0" is_locked="" datecreate="1287070965" datelastpost="1336905518">\r\n      <message>&lt;div&gt;&lt;span class=&quot;photo_container pc_m bbml_img&quot;&gt;&lt;a href=&quot;/photos/53930889@N04/5080874079/&quot; title=&quot;Star Wars 1 by Smallportfolio_jm08&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm5.staticflickr.com/4035/5080874079_684cf874e0_m.jpg&quot; width=&quot;240&quot; height=&quot;180&quot; alt=&quot;Star Wars 1 by Smallportfolio_jm08&quot;  class=&quot;pc_img&quot; border=&quot;0&quot; /&gt;&lt;/a&gt;&lt;/span&gt;&lt;/div&gt;\r\n\r\n&lt;div&gt;&lt;span class=&quot;photo_container pc_m bbml_img&quot;&gt;&lt;a href=&quot;/photos/53930889@N04/5081467846/&quot; title=&quot;Star Wars 2 by Smallportfolio_jm08&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm5.staticflickr.com/4071/5081467846_2eec86176d_m.jpg&quot; width=&quot;240&quot; height=&quot;180&quot; alt=&quot;Star Wars 2 by Smallportfolio_jm08&quot;  class=&quot;pc_img&quot; border=&quot;0&quot; /&gt;&lt;/a&gt;&lt;/span&gt;&lt;/div&gt;\r\n\r\n&lt;div&gt;&lt;span class=&quot;photo_container pc_m bbml_img&quot;&gt;&lt;a href=&quot;/photos/53930889@N04/5081467886/&quot; title=&quot;Star Wars 3 by Smallportfolio_jm08&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm5.staticflickr.com/4021/5081467886_d8cca6c8e8_m.jpg&quot; width=&quot;240&quot; height=&quot;180&quot; alt=&quot;Star Wars 3 by Smallportfolio_jm08&quot;  class=&quot;pc_img&quot; border=&quot;0&quot; /&gt;&lt;/a&gt;&lt;/span&gt;&lt;/div&gt;\r\n\r\n&lt;div&gt;&lt;span class=&quot;photo_container pc_m bbml_img&quot;&gt;&lt;a href=&quot;/photos/53930889@N04/5081467910/&quot; title=&quot;Star Wars 4 by Smallportfolio_jm08&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm5.staticflickr.com/4084/5081467910_274bb11fdc_m.jpg&quot; width=&quot;240&quot; height=&quot;180&quot; alt=&quot;Star Wars 4 by Smallportfolio_jm08&quot;  class=&quot;pc_img&quot; border=&quot;0&quot; /&gt;&lt;/a&gt;&lt;/span&gt;&lt;/div&gt;\r\n\r\n&lt;div&gt;&lt;span class=&quot;photo_container pc_m bbml_img&quot;&gt;&lt;a href=&quot;/photos/53930889@N04/5081467948/&quot; title=&quot;Star Wars 5 by Smallportfolio_jm08&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm5.staticflickr.com/4154/5081467948_1a5f200bc0_m.jpg&quot; width=&quot;240&quot; height=&quot;180&quot; alt=&quot;Star Wars 5 by Smallportfolio_jm08&quot;  class=&quot;pc_img&quot; border=&quot;0&quot; /&gt;&lt;/a&gt;&lt;/span&gt;&lt;/div&gt;</message>\r\n    </topic>\r\n    <topic id="72157629635119774" subject="Where The Fish Are" author="75240402@N04" authorname="Nokinrocks" role="member" iconserver="7027" iconfarm="8" count_replies="0" can_edit="0" can_delete="0" can_reply="0" is_sticky="0" is_locked="" datecreate="1336485653" datelastpost="1336485653">\r\n      <message>&lt;a href=&quot;http://www.flickr.com/photos/nokinrocks/7120495637/&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm9.staticflickr.com/8005/7120495637_fec0382b4b_n.jpg&quot; width=&quot;320&quot; height=&quot;256&quot; alt=&quot;Step It Up&quot; /&gt;&lt;/a&gt;\r\n\r\n&lt;a href=&quot;http://www.flickr.com/photos/nokinrocks/7122908705/&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm8.staticflickr.com/7259/7122908705_3bef338378_n.jpg&quot; width=&quot;240&quot; height=&quot;320&quot; alt=&quot;P1050351&quot; /&gt;&lt;/a&gt;\r\n\r\n&lt;a href=&quot;http://www.flickr.com/photos/nokinrocks/7122922123/&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm8.staticflickr.com/7052/7122922123_2bfcb6707c_n.jpg&quot; width=&quot;214&quot; height=&quot;320&quot; alt=&quot;Frog On A Log&quot; /&gt;&lt;/a&gt;\r\n\r\n&lt;a href=&quot;http://www.flickr.com/photos/nokinrocks/7122929521/&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm8.staticflickr.com/7047/7122929521_8ffebdd424_n.jpg&quot; width=&quot;320&quot; height=&quot;200&quot; alt=&quot;P1050397&quot; /&gt;&lt;/a&gt;\r\n\r\n&lt;a href=&quot;http://www.flickr.com/photos/nokinrocks/7122916999/&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm8.staticflickr.com/7200/7122916999_a7328f9dcc_n.jpg&quot; width=&quot;320&quot; height=&quot;261&quot; alt=&quot;P1050361&quot; /&gt;&lt;/a&gt;</message>\r\n    </topic>\r\n  </topics>\r\n</rsp>',
        "name": "flickr.groups.discuss.topics.getList",
    },
    "flickr.stats.getPopularPhotos": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The sort provided is not valid",
                "message": "Invalid sort",
                "code": "5",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.stats.getPopularPhotos",
        "explanation": '<p>This method returns the standard photo list xml.</p>\r\n\r\n<p>In addition each photo element contains a <code>&lt;stats&gt;</code> element. This has attributes for the view, comment and favorite counts for the requested day.</p>\r\n\r\n<p>To map <code>&lt;photo&gt;</code> elements to urls, please read the <a href="misc.urls.html">url documentation</a>.</p>\r\n',
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format. \r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.\r\n\r\nIf no date is provided, all time view counts will be returned.",
                "optional": "1",
                "name": "date",
            },
            {
                "text": 'The order in which to sort returned photos. Defaults to views. The possible values are views, comments and favorites. \r\n\r\nOther sort options are available through <a href="/services/api/flickr.photos.search.html">flickr.photos.search</a>.',
                "optional": "1",
                "name": "sort",
            },
            {
                "text": "Number of referrers to return per page. If this argument is omitted, it defaults to 25. The maximum allowed value is 100.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<photos page="2" pages="89" perpage="10" total="881">\r\n\t<photo id="2636" owner="47058503995@N01" \r\n\t\tsecret="a123456" server="2" title="test_04"\r\n\t\tispublic="1" isfriend="0" isfamily="0">\r\n\t\t<stats views="941" comments="18" favorites="2"/>\r\n\t</photo>\r\n\t<photo id="2635" owner="47058503995@N01"\r\n\t\tsecret="b123456" server="2" title="test_03"\r\n\t\tispublic="0" isfriend="1" isfamily="1">\r\n\t\t<stats views="141" comments="1" favorites="2"/>\r\n\t</photo>\r\n</photos>',
        "description": "List the photos with the most views, comments or favorites",
    },
    "flickr.photos.people.delete": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The NSID passed was not a valid user id.",
                "message": "Person not found",
                "code": "1",
            },
            {
                "text": "The photo id passed was not a valid photo id.",
                "message": "Photo not found",
                "code": "2",
            },
            {
                "text": "The calling user did not have permission to remove this person from this photo.",
                "message": "User cannot remove that person",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to remove a person from.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The NSID of the person to remove from the photo.",
                "optional": "0",
                "name": "user_id",
            },
            {
                "text": "An email address for an invited user.",
                "optional": "1",
                "name": "email",
            },
        ],
        "description": "Remove a person from a photo.",
        "needslogin": True,
        "name": "flickr.photos.people.delete",
    },
    "flickr.commons.getInstitutions": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Retrieves a list of the current Commons institutions.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": False,
        "response": '<rsp stat="ok">\r\n <institutions>\r\n  <institution nsid="123456@N01" date_launch="1232000000">\r\n   <name>Institution</name>\r\n    <urls>\r\n     <url type="site">http://example.com/</url>\r\n     <url type="license">http://example.com/commons/license</url>\r\n     <url type="flickr">http://flickr.com/photos/institution</url>\r\n    </urls>\r\n   </institution>\r\n  </institutions>\r\n</rsp>',
        "name": "flickr.commons.getInstitutions",
    },
    "flickr.photosets.create": {
        "errors": [
            {
                "text": "No title parameter was passed in the request.",
                "message": "No title specified",
                "code": "1",
            },
            {
                "text": "The primary photo id passed was not a valid photo id or does not belong to the calling user.",
                "message": "Photo not found",
                "code": "2",
            },
            {
                "text": "The user has reached their maximum number of photosets limit.",
                "message": "Can't create any more sets",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.photosets.create",
        "explanation": "<p>New photosets are automatically put first in the photoset ordering for the user. Use <a href=\"/services/api/flickr.photosets.orderSets.html\">flickr.photosets.orderSets</a> if you don't want the new set to appear first on the user's photoset list.</p>",
        "needssigning": True,
        "requiredperms": "write",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {"text": "A title for the photoset.", "optional": "0", "name": "title"},
            {
                "text": "A description of the photoset. May contain limited html.",
                "optional": "1",
                "name": "description",
            },
            {
                "text": "The id of the photo to represent this set. The photo must belong to the calling user.",
                "optional": "0",
                "name": "primary_photo_id",
            },
        ],
        "needslogin": True,
        "response": '<photoset id="1234" url="http://www.flickr.com/photos/bees/sets/1234/" />',
        "description": "Create a new photoset for the calling user.",
    },
    "flickr.people.getLimits": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.people.getLimits",
        "explanation": '<ul>\r\n<li>photos/@maxdisplaypx: maximum size in pixels for photos displayed on the site (0 means that no limit is in place). No limit is placed on the dimension of photos uploaded.</li>\r\n<li>photos/@maxupload: maximum file size in bytes for photo uploads.</li>\r\n<li>videos/@maxduration: maximum duration in seconds of a video.</li>\r\n<li>videos/@maxupload: maximum file size in bytes for video uploads.</li>\r\n</ul>\r\n\r\n<p>For more details, see the documentation about <a href="http://www.flickr.com/help/limits/">limits</a>.</p>',
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": True,
        "response": '<person nsid="30135021@N05">\r\n\t<photos maxdisplaypx="1024" maxupload="15728640" />\r\n\t<videos maxduration="90" maxupload="157286400" />\r\n</person>',
        "description": "Returns the photo and video limits that apply to the calling user account.",
    },
    "flickr.collections.getInfo": {
        "errors": [
            {
                "text": "The requested collection could not be found or is not visible to the calling user.",
                "message": "Collection not found",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns information for a single collection.  Currently can only be called by the collection owner, this may change.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the collection to fetch information for.",
                "optional": "0",
                "name": "collection_id",
            },
        ],
        "needslogin": True,
        "response": '<collection id="12-72157594586579649" child_count="6" datecreate="1173812218" iconlarge="http://farm1.static.flickr.com/187/cols/73743fac2cf79_l.jpg" iconsmall="http://farm1.static.flickr.com/187/cols/72157594586579649_43fac2cf79_s.jpg" server="187" secret="36">\r\n<title>All My Photos</title>\r\n<description>Photos!</description>\r\n<iconphotos>\r\n<photo id="14" owner="12@N01" secret="b57ba5c" server="51" farm="1" title="in full cap and gown" ispublic="1" isfriend="0" isfamily="0"/>\r\n<photo id="15" owner="12@N01" secret="ba1c2a8" server="58" farm="1" title="Just beyond the door" ispublic="0" isfriend="1" isfamily="0"/>\r\n<photo id="17" owner="12@N01" secret="0001969" server="73" farm="1" title="IMG_3787.JPG" ispublic="1" isfriend="0" isfamily="0"/>\r\n....\r\n</iconphotos>\r\n</collection>',
        "name": "flickr.collections.getInfo",
    },
    "flickr.stats.getCSVFiles": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": 'Returns a list of URLs for text files containing <i>all</i> your stats data (from November 26th 2007 onwards) for the currently auth\'d user.\r\n\r\n<b>Please note, these files will only be available until June 1, 2010 Noon PDT.</b> \r\nFor more information <a href="/help/stats/#1369409">please check out this FAQ</a>, or just <a href="/photos/me/stats/downloads/">go download your files</a>.',
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": True,
        "response": '<stats> \r\n   <csvfiles> \r\n      <csv href="http://farm4.static.flickr.com/3496/stats/72157623902771865_faaa.csv" type="daily" date="2010-04-01" /> \r\n      <csv href="http://farm4.static.flickr.com/3376/stats/72157624027152370_fbbb.csv" type="monthly" date="2010-04-01" /> \r\n      <csv href="http://farm5.static.flickr.com/4006/stats/72157623627769689_fccc.csv" type="daily" date="2010-03-01" /> \r\n      ....\r\n    </csvfiles> \r\n</stats>',
        "name": "flickr.stats.getCSVFiles",
    },
    "flickr.urls.lookupUser": {
        "errors": [
            {
                "text": "The passed URL was not a valid user profile or photos url.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns a user NSID, given the url to a user's photos or profile.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The url to the user's profile or photos page.",
                "optional": "0",
                "name": "url",
            },
        ],
        "needslogin": False,
        "response": '<user id="12037949632@N01">\r\n\t<username>Stewart</username> \r\n</user>',
        "name": "flickr.urls.lookupUser",
    },
    "flickr.urls.getUserPhotos": {
        "errors": [
            {
                "text": "The NSID specified was not a valid user.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "No user_id was passed and the calling user was not logged in.",
                "message": "No user specified",
                "code": "2",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns the url to a user's photos.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user to fetch the url for. If omitted, the calling user is assumed.",
                "optional": "1",
                "name": "user_id",
            },
        ],
        "needslogin": False,
        "response": '<user nsid="12037949754@N01" url="http://www.flickr.com/photos/bees/" />',
        "name": "flickr.urls.getUserPhotos",
    },
    "flickr.photos.getContactsPhotos": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Fetch a list of recent photos from the calling users' contacts.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Number of photos to return. Defaults to 10, maximum 50. This is only used if <code>single_photo</code> is not passed.",
                "optional": "1",
                "name": "count",
            },
            {
                "text": "set as 1 to only show photos from friends and family (excluding regular contacts).",
                "optional": "1",
                "name": "just_friends",
            },
            {
                "text": "Only fetch one photo (the latest) per contact, instead of all photos in chronological order.",
                "optional": "1",
                "name": "single_photo",
            },
            {
                "text": "Set to 1 to include photos from the calling user.",
                "optional": "1",
                "name": "include_self",
            },
            {
                "text": 'A comma-delimited list of extra information to fetch for each returned record. Currently supported fields include: license, date_upload, date_taken, owner_name, icon_server, original_format, last_update. For more information see extras under <a href="/services/api/flickr.photos.search.html">flickr.photos.search</a>.',
                "optional": "1",
                "name": "extras",
            },
        ],
        "needslogin": True,
        "response": '<photos>\r\n\t<photo id="2801" owner="12037949629@N01"\r\n\t\tsecret="123456" server="1"\r\n\t\tusername="Eric is the best" title="grease" /> \r\n\t<photo id="2499" owner="33853651809@N01"\r\n\t\tsecret="123456" server="1"\r\n\t\tusername="cal18" title="36679_o" /> \r\n\t<photo id="2437" owner="12037951898@N01"\r\n\t\tsecret="123456" server="1"\r\n\t\tusername="georgie parker" title="phoenix9_stewart" /> \r\n</photos>',
        "name": "flickr.photos.getContactsPhotos",
    },
    "flickr.groups.discuss.replies.edit": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The topic_id is invalid",
                "message": "Topic not found",
                "code": "1",
            },
            {
                "text": "The reply_id is invalid.",
                "message": "Reply not found",
                "code": "2",
            },
            {
                "text": "The topic_id and reply_id are required.",
                "message": "Missing required arguments",
                "code": "3",
            },
            {
                "text": "Replies can only be edited by their owner.",
                "message": "Cannot edit reply",
                "code": "4",
            },
            {
                "text": "Either this account is not a member of the group, or discussion in this group is disabled.",
                "message": "Cannot post to group",
                "code": "5",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the topic the post is in.",
                "optional": "0",
                "name": "topic_id",
            },
            {
                "text": "The ID of the reply post to edit.",
                "optional": "0",
                "name": "reply_id",
            },
            {
                "text": "The message to edit the post with.",
                "optional": "0",
                "name": "message",
            },
        ],
        "description": "Edit a topic reply.",
        "needslogin": True,
        "name": "flickr.groups.discuss.replies.edit",
    },
    "flickr.tags.getListUser": {
        "errors": [
            {
                "text": "The user NSID passed was not a valid user NSID and the calling user was not logged in.\r\n",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get the tag list for a given user (or the currently logged in user).",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user to fetch the tag list for. If this argument is not specified, the currently logged in user (if any) is assumed.",
                "optional": "1",
                "name": "user_id",
            },
        ],
        "needslogin": False,
        "response": '<who id="12037949754@N01">\r\n\t<tags>\r\n\t\t<tag>gull</tag> \r\n\t\t<tag>tag1</tag> \r\n\t\t<tag>tag2</tag> \r\n\t\t<tag>tags</tag> \r\n\t\t<tag>test</tag> \r\n\t</tags>\r\n</who>',
        "name": "flickr.tags.getListUser",
    },
    "flickr.photos.upload.checkTickets": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.photos.upload.checkTickets",
        "explanation": '<p>There is one <code>&lt;ticket&gt;</code> element for each ticket id supplied. The <code>id</code> attribute contains the corresponding ticket id. If the ticket wasn\'t found, the <code>invalid</code> attribute is set. The status of the ticket is passed in the <code>status</code> attribute; 0 means not completed, 1 means completed and 2 means the ticket failed (indicating there was a problem converting the file). When the status is 1, the photo id is passed in the <code>photoid</code> attribute. The photo id can then be used as with the <a href="/services/api/upload.api.html">synchronous upload API</a>.',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "A comma-delimited list of ticket ids",
                "optional": "0",
                "name": "tickets",
            },
            {"text": "", "optional": "1", "name": "batch_id"},
        ],
        "needslogin": False,
        "response": '<uploader>\r\n\t<ticket id="128" complete="1" photoid="2995" />\r\n\t<ticket id="129" complete="0" />\r\n\t<ticket id="130" complete="2" />\r\n\t<ticket id="131" invalid="1" />\r\n</uploader>\r\n',
        "description": "Checks the status of one or more asynchronous photo upload tickets.",
    },
    "flickr.photosets.comments.getList": {
        "errors": [
            {
                "text": "The photoset id was invalid.",
                "message": "Photoset not found.",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns the comments for a photoset.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photoset to fetch comments for.",
                "optional": "0",
                "name": "photoset_id",
            },
        ],
        "needslogin": False,
        "response": '<comments photoset_id="109722179">\r\n    <comment id="6065-109722179-72057594077818641"\r\n         author="35468159852@N01" authorname="Rev Dan Catt" date_create="1141841470"\r\n         permalink="http://www.flickr.com/photos/straup/109722179/#comment72057594077818641"\r\n         >Umm, I\'m not sure, can I get back to you on that one?</comment>\r\n</comments>',
        "name": "flickr.photosets.comments.getList",
    },
    "flickr.places.getInfo": {
        "errors": [
            {
                "text": "One or more required parameter is missing from the API call.",
                "message": "Required parameter missing",
                "code": "1",
            },
            {
                "text": "An invalid Places (or WOE) ID was passed with the API call.",
                "message": "Not a valid Places ID",
                "code": "2",
            },
            {
                "text": "No place could be found for the Places (or WOE) ID passed to the API call.",
                "message": "Place not found",
                "code": "3",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.places.getInfo",
        "explanation": "  ",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": 'A Flickr Places ID. <span style="font-style:italic;">(While optional, you must pass either a valid Places ID or a WOE ID.)</span>',
                "optional": "1",
                "name": "place_id",
            },
            {
                "text": 'A Where On Earth (WOE) ID. <span style="font-style:italic;">(While optional, you must pass either a valid Places ID or a WOE ID.)</span>',
                "optional": "1",
                "name": "woe_id",
            },
        ],
        "needslogin": False,
        "response": '<place place_id="4hLQygSaBJ92" woeid="3534"\r\n   latitude="45.512" longitude="-73.554"\r\n   place_url="/Canada/Quebec/Montreal" place_type="locality"\r\n   has_shapedata="1" timezone="America/Toronto">\r\n   <locality place_id="4hLQygSaBJ92" woeid="3534"\r\n      latitude="45.512" longitude="-73.554"\r\n      place_url="/Canada/Quebec/Montreal">Montreal</locality>\r\n   <county place_id="cFBi9x6bCJ8D5rba1g" woeid="29375198"\r\n      latitude="45.551" longitude="-73.600" \r\n      place_url="/cFBi9x6bCJ8D5rba1g">Montr\xe9al</county>\r\n   <region place_id="CrZUvXebApjI0.72" woeid="2344924" \r\n      latitude="53.890" longitude="-68.429"\r\n      place_url="/Canada/Quebec">Quebec</region>\r\n   <country place_id="EESRy8qbApgaeIkbsA" woeid="23424775"\r\n      latitude="62.358" longitude="-96.582" \r\n      place_url="/Canada">Canada</country>\r\n   <shapedata created="1223513357" alpha="0.012359619140625"\r\n      count_points="34778" count_edges="52"\r\n      has_donuthole="1" is_donuthole="1">\r\n      <polylines>\r\n         <polyline>\r\n            45.427627563477,-73.589645385742 45.428966522217,-73.587898254395, etc...\r\n         </polyline>\r\n      </polylines>\r\n      <urls>\r\n         <shapefile>\r\n         http://farm4.static.flickr.com/3228/shapefiles/3534_20081111_0a8afe03c5.tar.gz\r\n         </shapefile>\r\n      </urls>\r\n   </shapedata>\r\n</place>',
        "description": "Get informations about a place.",
    },
    "flickr.photos.people.deleteCoords": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The NSID passed was not a valid user id.",
                "message": "Person not found",
                "code": "1",
            },
            {
                "text": "The photo id passed was not a valid photo id.",
                "message": "Photo not found",
                "code": "2",
            },
            {
                "text": "The calling user is neither the person depicted in the photo nor the person who added the bounding box.",
                "message": "User cannot edit that person in that photo",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to edit a person in.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The NSID of the person whose bounding box you want to remove.",
                "optional": "0",
                "name": "user_id",
            },
        ],
        "description": "Remove the bounding box from a person in a photo",
        "needslogin": True,
        "name": "flickr.photos.people.deleteCoords",
    },
    "flickr.photos.geo.setLocation": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photo id was either invalid or was for a photo not viewable by the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "Some or all of the required arguments were not supplied.",
                "message": "Required arguments missing.",
                "code": "2",
            },
            {
                "text": "The latitude argument failed validation.",
                "message": "Not a valid latitude.",
                "code": "3",
            },
            {
                "text": "The longitude argument failed validation.",
                "message": "Not a valid longitude.",
                "code": "4",
            },
            {
                "text": "The accuracy argument failed validation.",
                "message": "Not a valid accuracy.",
                "code": "5",
            },
            {
                "text": "There was an unexpected problem setting location information to the photo.",
                "message": "Server error.",
                "code": "6",
            },
            {
                "text": 'Before users may assign location data to a photo they must define who, by default, may view that information. Users can edit this preference at <a href="http://www.flickr.com/account/geo/privacy/">http://www.flickr.com/account/geo/privacy/</a>',
                "message": "User has not configured default viewing settings for location data.",
                "code": "7",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to set location data for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The latitude whose valid range is -90 to 90. Anything more than 6 decimal places will be truncated.",
                "optional": "0",
                "name": "lat",
            },
            {
                "text": "The longitude whose valid range is -180 to 180. Anything more than 6 decimal places will be truncated.",
                "optional": "0",
                "name": "lon",
            },
            {
                "text": "Recorded accuracy level of the location information. World level is 1, Country is ~3, Region ~6, City ~11, Street ~16. Current range is 1-16. Defaults to 16 if not specified.",
                "optional": "1",
                "name": "accuracy",
            },
            {
                "text": 'Context is a numeric value representing the photo\'s geotagginess beyond latitude and longitude. For example, you may wish to indicate that a photo was taken "indoors" or "outdoors". <br /><br />\r\nThe current list of context IDs is :<br /><br/>\r\n<ul>\r\n<li><strong>0</strong>, not defined.</li>\r\n<li><strong>1</strong>, indoors.</li>\r\n<li><strong>2</strong>, outdoors.</li>\r\n</ul><br />\r\nThe default context for geotagged photos is 0, or "not defined"\r\n',
                "optional": "1",
                "name": "context",
            },
            {
                "text": "Associate a geo bookmark with this photo.",
                "optional": "1",
                "name": "bookmark_id",
            },
            {"text": "", "optional": "1", "name": "is_public"},
            {"text": "", "optional": "1", "name": "is_contact"},
            {"text": "", "optional": "1", "name": "is_friend"},
            {"text": "", "optional": "1", "name": "is_family"},
            {
                "text": "The venue ID for a Foursquare location.",
                "optional": "1",
                "name": "foursquare_id",
            },
            {
                "text": "A Where On Earth (WOE) ID. (If passed in, will override the default venue based on the lat/lon.)",
                "optional": "1",
                "name": "woeid",
            },
        ],
        "description": 'Sets the geo data (latitude and longitude and, optionally, the accuracy level) for a photo.\r\n\r\nBefore users may assign location data to a photo they must define who, by default, may view that information. Users can edit this preference at <a href="http://www.flickr.com/account/geo/privacy/">http://www.flickr.com/account/geo/privacy/</a>. If a user has not set this preference, the API method will return an error.',
        "needslogin": True,
        "name": "flickr.photos.geo.setLocation",
    },
    "flickr.push.getTopics": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "All the different flavours of anteater.\r\n<br><br>\r\n<i>(this method is experimental and may change)</i>",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": False,
        "response": '<rsp stat="ok">\r\n  <topics>\r\n    <topic name="contacts_photos" />\r\n    <topic name="contacts_faves" />\r\n  </topics>\r\n</rsp>',
        "name": "flickr.push.getTopics",
    },
    "flickr.tags.getRelated": {
        "errors": [
            {
                "text": "The tag argument was missing.",
                "message": "Tag not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns a list of tags 'related' to the given tag, based on clustered usage analysis.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The tag to fetch related tags for.",
                "optional": "0",
                "name": "tag",
            },
        ],
        "needslogin": False,
        "response": '<tags source="london">\r\n\t<tag>england</tag>\r\n\t<tag>thames</tag>\r\n\t<tag>tube</tag>\r\n\t<tag>bigben</tag>\r\n\t<tag>uk</tag>\r\n</tags>\r\n',
        "name": "flickr.tags.getRelated",
    },
    "flickr.favorites.getContext": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id, or was the id of a photo that the calling user does not have permission to view.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The specified user was not found.",
                "message": "User not found",
                "code": "2",
            },
            {
                "text": "The specified photo is not a favorite of the specified user.",
                "message": "Photo not a favorite",
                "code": "3",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.favorites.getContext",
        "explanation": '<p>See <a href="/services/api/flickr.photos.getContext.html">flickr.photos.getContext</a></p>',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to fetch the context for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The user who counts the photo as a favorite.",
                "optional": "0",
                "name": "user_id",
            },
            {"text": "", "optional": "1", "name": "num_prev"},
            {"text": "", "optional": "1", "name": "num_next"},
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: description, license, date_upload, date_taken, owner_name, icon_server, original_format, last_update, geo, tags, machine_tags, o_dims, views, media, path_alias, url_sq, url_t, url_s, url_m, url_z, url_l, url_o",
                "optional": "1",
                "name": "extras",
            },
        ],
        "needslogin": False,
        "response": '<rsp stat=\'ok\'>\r\n<count>3</count>\r\n<prevphoto id="2980" secret="973da1e709"\r\n\ttitle="boo!" url="/photos/bees/2980/" /> \r\n<nextphoto id="2985" secret="059b664012"\r\n\ttitle="Amsterdam Amstel" url="/photos/bees/2985/" />\r\n</rsp>',
        "description": "Returns next and previous favorites for a photo in a user's favorites.",
    },
    "flickr.photosets.comments.deleteComment": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The comment id passed was not a valid comment id",
                "message": "Comment not found.",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the comment to delete from a photoset.",
                "optional": "0",
                "name": "comment_id",
            },
        ],
        "description": "Delete a photoset comment as the currently authenticated user.",
        "needslogin": True,
        "name": "flickr.photosets.comments.deleteComment",
    },
    "flickr.prefs.getPrivacy": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns the default privacy level preference for the user.\r\n\r\nPossible values are:\r\n<ul>\r\n<li>1 : Public</li>\r\n<li>2 : Friends only</li>\r\n<li>3 : Family only</li>\r\n<li>4 : Friends and Family</li>\r\n<li>5 : Private</li>\r\n</ul>",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": True,
        "response": '<rsp stat="ok">\r\n<person nsid="12037949754@N01" privacy="1" />\r\n</rsp>',
        "name": "flickr.prefs.getPrivacy",
    },
    "flickr.push.getSubscriptions": {
        "errors": [
            {
                "text": "PuSH subscriptions are currently restricted to Pro account holders.",
                "message": "Service currently available only to pro accounts",
                "code": "5",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns a list of the subscriptions for the logged-in user.\r\n<br><br>\r\n<i>(this method is experimental and may change)</i>",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": True,
        "response": '<rsp stat="ok">\r\n  <subscriptions>\r\n    <subscription topic="contacts_photos" callback="http://example.com/contacts_photos_endpoint?user=12345" pending="0" date_create="1309293755" lease_seconds="0" expiry="1309380155" verify_attempts="0" />\r\n    <subscription topic="contacts_faves" callback="http://example.com/contacts_faves_endpoint?user=12345" pending="0" date_create="1309293785" lease_seconds="0" expiry="1309380185" verify_attempts="0" />\r\n  </subscriptions>\r\n</rsp>',
        "name": "flickr.push.getSubscriptions",
    },
    "flickr.photos.suggestions.rejectSuggestion": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The unique ID of the suggestion to reject.",
                "optional": "0",
                "name": "suggestion_id",
            },
        ],
        "description": "Reject a suggestion for a photo.",
        "needslogin": True,
        "name": "flickr.photos.suggestions.rejectSuggestion",
    },
    "flickr.tags.getHotList": {
        "errors": [
            {
                "text": "The specified period was not understood.",
                "message": "Invalid period",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns a list of hot tags for the given period.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The period for which to fetch hot tags. Valid values are <code>day</code> and <code>week</code> (defaults to <code>day</code>).",
                "optional": "1",
                "name": "period",
            },
            {
                "text": "The number of tags to return. Defaults to 20. Maximum allowed value is 200.",
                "optional": "1",
                "name": "count",
            },
        ],
        "needslogin": False,
        "response": '<hottags period="day" count="6">\r\n\t<tag score="20">northerncalifornia</tag>\r\n\t<tag score="18">top20</tag>\r\n\t<tag score="15">keychain</tag>\r\n\t<tag score="10">zb</tag>\r\n\t<tag score="9">selfportraittuesday</tag>\r\n\t<tag score="4">jan06</tag>\r\n</hottags>',
        "name": "flickr.tags.getHotList",
    },
    "flickr.galleries.editPhoto": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "That gallery could not be found.",
                "message": "Invalid gallery ID",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the gallery to add a photo to. Note: this is the compound ID returned in methods like flickr.galleries.getList, and flickr.galleries.getListForPhoto.",
                "optional": "0",
                "name": "gallery_id",
            },
            {
                "text": "The photo ID to add to the gallery.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The updated comment the photo.",
                "optional": "0",
                "name": "comment",
            },
        ],
        "description": "Edit the comment for a gallery photo.",
        "needslogin": True,
        "name": "flickr.galleries.editPhoto",
    },
    "flickr.galleries.getList": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return the list of galleries created by a user.  Sorted from newest to oldest.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user to get a galleries list for. If none is specified, the calling user is assumed.",
                "optional": "0",
                "name": "user_id",
            },
            {
                "text": "Number of galleries to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": False,
        "response": '<galleries total="9" page="1" pages="1" per_page="100" user_id="34427469121@N01">\r\n   <gallery id="5704-72157622637971865" \r\n             url="http://www.flickr.com/photos/george/galleries/72157622637971865" \r\n             owner="34427469121@N01" date_create="1257711422" date_update="1260360756"\r\n             primary_photo_id="107391222"  primary_photo_server="39" \r\n             primary_photo_farm="1" primary_photo_secret="ffa"\r\n             count_photos="16" count_videos="2" >\r\n       <title>I like me some black &amp; white</title>\r\n       <description>black and whites</description>\r\n   </gallery>\r\n   <gallery id="5704-72157622566655097" \r\n            url="http://www.flickr.com/photos/george/galleries/72157622566655097" \r\n            owner="34427469121@N01" date_create="1256852229" date_update="1260462343" \r\n            primary_photo_id="497374910" primary_photo_server="231" \r\n            primary_photo_farm="1" primary_photo_secret="9ae0f"\r\n            count_photos="18" count_videos="0" >\r\n       <title>People Sleeping in Libraries</title>\r\n       <description />\r\n   </gallery>\r\n</galleries>',
        "name": "flickr.galleries.getList",
    },
    "flickr.groups.discuss.replies.add": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The topic_id is invalid.",
                "message": "Topic not found",
                "code": "1",
            },
            {
                "text": "Either this account is not a member of the group, or discussion in this group is disabled.\r\n",
                "message": "Cannot post to group",
                "code": "2",
            },
            {
                "text": "The topic_id and message are required.",
                "message": "Missing required arguments",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the topic to post a comment to.",
                "optional": "0",
                "name": "topic_id",
            },
            {
                "text": "The message to post to the topic.",
                "optional": "0",
                "name": "message",
            },
        ],
        "description": "Post a new reply to a group discussion topic.",
        "needslogin": True,
        "name": "flickr.groups.discuss.replies.add",
    },
    "flickr.favorites.getList": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {
                "text": "The specified user NSID was not a valid flickr user.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user to fetch the favorites list for. If this argument is omitted, the favorites list for the calling user is returned.",
                "optional": "1",
                "name": "user_id",
            },
            {"text": "", "optional": "1", "name": "jump_to"},
            {
                "text": "Minimum date that a photo was favorited on. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "min_fave_date",
            },
            {
                "text": "Maximum date that a photo was favorited on. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "max_fave_date",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "description": "Returns a list of the user's favorite photos. Only photos which the calling user has permission to see are returned.",
        "needslogin": True,
        "name": "flickr.favorites.getList",
    },
    "flickr.favorites.add": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The photo belongs to the user and so cannot be added to their favorites.",
                "message": "Photo is owned by you",
                "code": "2",
            },
            {
                "text": "The photo is already in the user's list of favorites.",
                "message": "Photo is already in favorites",
                "code": "3",
            },
            {
                "text": "The user does not have permission to add the photo to their favorites.",
                "message": "User cannot see photo",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to add to the user's favorites.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "description": "Adds a photo to a user's favorites list.",
        "needslogin": True,
        "name": "flickr.favorites.add",
    },
    "flickr.galleries.editPhotos": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the gallery to modify. The gallery must belong to the calling user.",
                "optional": "0",
                "name": "gallery_id",
            },
            {
                "text": "The id of the photo to use as the 'primary' photo for the gallery. This id must also be passed along in photo_ids list argument.",
                "optional": "0",
                "name": "primary_photo_id",
            },
            {
                "text": "A comma-delimited list of photo ids to include in the gallery. They will appear in the set in the order sent. This list must contain the primary photo id. This list of photos replaces the existing list.",
                "optional": "0",
                "name": "photo_ids",
            },
        ],
        "description": "Modify the photos in a gallery. Use this method to add, remove and re-order photos.",
        "needslogin": True,
        "name": "flickr.galleries.editPhotos",
    },
    "flickr.urls.lookupGroup": {
        "errors": [
            {
                "text": "The passed URL was not a valid group page or photo pool url.",
                "message": "Group not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns a group NSID, given the url to a group's page or photo pool.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The url to the group's page or photo pool.",
                "optional": "0",
                "name": "url",
            },
        ],
        "needslogin": False,
        "response": '<group id="34427469792@N01">\r\n\t<groupname>FlickrCentral</groupname> \r\n</group>',
        "name": "flickr.urls.lookupGroup",
    },
    "flickr.favorites.getPublicList": {
        "needssigning": False,
        "requiredperms": "none",
        "errors": [
            {
                "text": "The specified user NSID was not a valid flickr user.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The user to fetch the favorites list for.",
                "optional": "0",
                "name": "user_id",
            },
            {"text": "", "optional": "1", "name": "jump_to"},
            {
                "text": "Minimum date that a photo was favorited on. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "min_fave_date",
            },
            {
                "text": "Maximum date that a photo was favorited on. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "max_fave_date",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "description": "Returns a list of favorite public photos for the given user.",
        "needslogin": False,
        "name": "flickr.favorites.getPublicList",
    },
    "flickr.people.getPhotosOf": {
        "errors": [
            {
                "text": "A user_id was passed which did not match a valid flickr user.",
                "message": "User not found.",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.people.getPhotosOf",
        "explanation": '<p>This method returns a variant of the standard photo list xml.</p>\r\n\r\n<p>For queries about a member other than the currently authenticated one, pagination data ("total" and "pages" attributes) will not be available.</p>\r\n\r\n<p>Instead, the <photos> element will contain a boolean value \'has_next_page\' which will tell you whether or not there are more photos to fetch.</p>',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": 'The NSID of the user you want to find photos of. A value of "me" will search against photos of the calling user, for authenticated calls.',
                "optional": "0",
                "name": "user_id",
            },
            {
                "text": "An NSID of a Flickr member. This will restrict the list of photos to those taken by that member.",
                "optional": "1",
                "name": "owner_id",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>date_person_added</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "needslogin": False,
        "response": '<photos page="2" has_next_page="1" perpage="10">\r\n\t<photo id="2636" owner="47058503995@N01" \r\n\t\tsecret="a123456" server="2" title="test_04"\r\n\t\tispublic="1" isfriend="0" isfamily="0" />\r\n\t<photo id="2635" owner="47058503995@N01"\r\n\t\tsecret="b123456" server="2" title="test_03"\r\n\t\tispublic="0" isfriend="1" isfamily="1" />\r\n\t<photo id="2633" owner="47058503995@N01"\r\n\t\tsecret="c123456" server="2" title="test_01"\r\n\t\tispublic="1" isfriend="0" isfamily="0" />\r\n\t<photo id="2610" owner="12037949754@N01"\r\n\t\tsecret="d123456" server="2" title="00_tall"\r\n\t\tispublic="1" isfriend="0" isfamily="0" />\r\n</photos>',
        "description": "Returns a list of photos containing a particular Flickr member.",
    },
    "flickr.reflection.getMethodInfo": {
        "errors": [
            {
                "text": "The requested method was not found.",
                "message": "Method not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns information for a given flickr API method.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The name of the method to fetch information for.",
                "optional": "0",
                "name": "method_name",
            },
        ],
        "needslogin": False,
        "response": '<method name="flickr.fakeMethod" needslogin="1">\r\n\t<description>A fake method</description> \r\n\t<response>xml-response-example</response> \r\n\t<explanation>explanation of example response</explanation> \r\n\t<arguments>\r\n\t\t<argument name="api_key" optional="0">\r\n\t\t\tYou API application key.</argument> \r\n\t\t<argument name="color" optional="1">\r\n\t\t\tYour favorite color.</argument> \r\n\t</arguments>\r\n\t<errors>\r\n\t\t<error code="1" message="Photo not found">\r\n\t\t\tFull explanation...</error> \r\n\t\t<error code="100" message="Invalid API Key">\r\n\t\t\tFull explanation...</error> \r\n\t</errors>\r\n</method>\r\n',
        "name": "flickr.reflection.getMethodInfo",
    },
    "flickr.places.tagsForPlace": {
        "errors": [
            {
                "text": "One or more parameters was not included with the API request",
                "message": "Required parameter missing",
                "code": "1",
            },
            {
                "text": "An invalid Places (or WOE) identifier was included with your request.",
                "message": "Not a valid Places ID",
                "code": "2",
            },
            {
                "text": "An invalid Places (or WOE) identifier was included with your request.",
                "message": "Place not found",
                "code": "3",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return a list of the top 100 unique tags for a Flickr Places or Where on Earth (WOE) ID",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": 'A Where on Earth identifier to use to filter photo clusters.<br /><br />\r\n<span style="font-style:italic;">(While optional, you must pass either a valid Places ID or a WOE ID.)</span>',
                "optional": "1",
                "name": "woe_id",
            },
            {
                "text": 'A Flickr Places identifier to use to filter photo clusters.<br /><br />\r\n<span style="font-style:italic;">(While optional, you must pass either a valid Places ID or a WOE ID.)</span>',
                "optional": "1",
                "name": "place_id",
            },
            {
                "text": "Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "min_upload_date",
            },
            {
                "text": "Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "max_upload_date",
            },
            {
                "text": "Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date should be in the form of a mysql datetime.",
                "optional": "1",
                "name": "min_taken_date",
            },
            {
                "text": "Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date should be in the form of a mysql datetime.",
                "optional": "1",
                "name": "max_taken_date",
            },
        ],
        "needslogin": False,
        "response": '<tags total="100">\r\n   <tag count="31775">montreal</tag>\r\n   <tag count="20585">canada</tag>\r\n   <tag count="12319">montr\xe9al</tag>\r\n   <tag count="12154">quebec</tag>\r\n   <tag count="6471">qu\xe9bec</tag>\r\n   <tag count="2173">sylvainmichaud</tag>\r\n   <tag count="2091">nikon</tag>\r\n   <tag count="1541">lucbus</tag>\r\n   <tag count="1539">music</tag>\r\n   <tag count="1479">urban</tag>\r\n   <tag count="1425">lucbussieres</tag>\r\n   <tag count="1419">festival</tag>\r\n   <!-- and so on -->\r\n</tags>',
        "name": "flickr.places.tagsForPlace",
    },
    "flickr.groups.joinRequest": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The group_id or message argument are missing.",
                "message": "Required arguments missing",
                "code": "1",
            },
            {
                "text": "The Group does not exist",
                "message": "Group does not exist",
                "code": "2",
            },
            {
                "text": "The authed account does not have permission to view/join the group.",
                "message": "Group not available to the account",
                "code": "3",
            },
            {
                "text": "The authed account has previously joined this group",
                "message": "Account is already in that group",
                "code": "4",
            },
            {
                "text": "The group does not require an invitation to join, please use flickr.groups.join.",
                "message": "Group is public and open",
                "code": "5",
            },
            {
                "text": "The user must read and accept the rules before joining. Please see the accept_rules argument for this method.",
                "message": "User must accept the group rules before joining",
                "code": "6",
            },
            {
                "text": "A request has already been sent and is pending approval.",
                "message": "User has already requested to join that group",
                "code": "7",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the group to request joining.",
                "optional": "0",
                "name": "group_id",
            },
            {
                "text": "Message to the administrators.",
                "optional": "0",
                "name": "message",
            },
            {
                "text": "If the group has rules, they must be displayed to the user prior to joining. Passing a true value for this argument specifies that the application has displayed the group rules to the user, and that the user has agreed to them. (See flickr.groups.getInfo).",
                "optional": "0",
                "name": "accept_rules",
            },
        ],
        "description": "Request to join a group that is invitation-only.",
        "needslogin": True,
        "name": "flickr.groups.joinRequest",
    },
    "flickr.photos.setSafetyLevel": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id of a photo belonging to the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "Neither a valid safety level nor a hidden value were passed.",
                "message": "Invalid or missing arguments",
                "code": "2",
            },
            {
                "text": "Changing the safety level of this photo is not allowed.",
                "message": "Change not allowed",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Set the safety level of a photo.",
        "needssigning": True,
        "requiredperms": "write",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to set the adultness of.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The safety level of the photo.  Must be one of:\r\n\r\n1 for Safe, 2 for Moderate, and 3 for Restricted.",
                "optional": "1",
                "name": "safety_level",
            },
            {
                "text": "Whether or not to additionally hide the photo from public searches.  Must be either 1 for Yes or 0 for No.",
                "optional": "1",
                "name": "hidden",
            },
        ],
        "needslogin": True,
        "response": '<rsp stat="ok">\r\n<photo id="14814" safety_level="2" hidden="0"/>\r\n</rsp>',
        "name": "flickr.photos.setSafetyLevel",
    },
    "flickr.places.resolvePlaceURL": {
        "errors": [
            {"text": "", "message": "Place URL required.", "code": "2"},
            {"text": "", "message": "Place not found.", "code": "3"},
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": 'Find Flickr Places information by Place URL.<br /><br />\r\nThis method has been deprecated. It won\'t be removed but you should use <a href="/services/api/flickr.places.getInfoByUrl.html">flickr.places.getInfoByUrl</a> instead.\r\n',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "A Flickr Places URL.  \r\n<br /><br />\r\nFlickr Place URLs are of the form /country/region/city",
                "optional": "0",
                "name": "url",
            },
        ],
        "needslogin": False,
        "response": '<location place_id="kH8dLOubBZRvX_YZ" woeid="2487956" \r\n                latitude="37.779" longitude="-122.420"\r\n                place_url="/United+States/California/San+Francisco"\r\n                place_type="locality">\r\n   <locality place_id="kH8dLOubBZRvX_YZ" woeid="2487956"\r\n                 latitude="37.779" longitude="-122.420" \r\n                 place_url="/United+States/California/San+Francisco">San Francisco</locality>\r\n   <county place_id="hCca8XSYA5nn0X1Sfw" woeid="12587707"\r\n                 latitude="37.759" longitude="-122.435" \r\n                 place_url="/hCca8XSYA5nn0X1Sfw">San Francisco</county>\r\n   <region place_id="SVrAMtCbAphCLAtP" woeid="2347563" \r\n                latitude="37.271" longitude="-119.270" \r\n                place_url="/United+States/California">California</region>\r\n   <country place_id="4KO02SibApitvSBieQ" woeid="23424977"\r\n                  latitude="48.890" longitude="-116.982" \r\n                  place_url="/United+States">United States</country>\r\n</location>',
        "name": "flickr.places.resolvePlaceURL",
    },
    "flickr.contacts.getTaggingSuggestions": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get suggestions for tagging people in photos based on the calling user's contacts.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Return calling user in the list of suggestions. Default: true.",
                "optional": "1",
                "name": "include_self",
            },
            {
                "text": "Include suggestions from the user's address book. Default: false",
                "optional": "1",
                "name": "include_address_book",
            },
            {
                "text": "Number of contacts to return per page. If this argument is omitted, all contacts will be returned.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<rsp stat="ok">\r\n<contacts page="1" pages="1" perpage="1000" total="1">\r\n\t<contact nsid="30135021@N05" username="Hugo Haas" iconserver="1" iconfarm="1" realname="" friend="0" family="0" path_alias="" />\r\n</contacts>\r\n</rsp>',
        "name": "flickr.contacts.getTaggingSuggestions",
    },
    "flickr.tags.getListPhoto": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.tags.getListPhoto",
        "explanation": '<p>For an explanation of the <code>tag</code> element, please read the <a href="/services/api/misc.tags.html">tags documentation</a>.</p>',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to return tags for.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "needslogin": False,
        "response": '<photo id="2619">\r\n\t<tags>\r\n\t\t<tag id="156" author="12037949754@N01"\r\n\t\t\tauthorname="Bees" raw="tag 1">tag1</tag> \r\n\t\t<tag id="157" author="12037949754@N01"\r\n\t\t\tauthorname="Bees" raw="tag 2">tag2</tag> \r\n\t</tags>\r\n</photo>',
        "description": "Get the tag list for a given photo.",
    },
    "flickr.auth.oauth.checkToken": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns the credentials attached to an OAuth authentication token.",
        "needssigning": True,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The OAuth authentication token to check.",
                "optional": "0",
                "name": "oauth_token",
            },
        ],
        "needslogin": False,
        "response": '<oauth>\r\n    <token>72157627611980735-09e87c3024f733da</token>\r\n    <perms>write</perms>\r\n    <user nsid="1121451801@N07" username="jamalf" fullname="Jamal F"/>\r\n</oauth>',
        "name": "flickr.auth.oauth.checkToken",
    },
    "flickr.auth.oauth.getAccessToken": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Exchange an auth token from the old Authentication API, to an OAuth access token. Calling this method will delete the auth token used to make the request.",
        "needssigning": True,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": False,
        "response": '<auth> \r\n\t<access_token oauth_token="72157607082540144-8d5d7ea7696629bf" oauth_token_secret="f38bf58b2d95bc8b" /> \r\n</auth> ',
        "name": "flickr.auth.oauth.getAccessToken",
    },
    "flickr.groups.join": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The group_id doesn't exist",
                "message": "Required arguments missing",
                "code": "1",
            },
            {
                "text": "The Group does not exist",
                "message": "Group does not exist",
                "code": "2",
            },
            {
                "text": "The authed account does not have permission to view/join the group.",
                "message": "Group not availabie to the account",
                "code": "3",
            },
            {
                "text": "The authed account has previously joined this group",
                "message": "Account is already in that group",
                "code": "4",
            },
            {
                "text": "Use flickr.groups.joinRequest to contact the administrations for an invitation.",
                "message": "Membership in group is by invitation only.",
                "code": "5",
            },
            {
                "text": "The user must read and accept the rules before joining. Please see the accept_rules argument for this method.",
                "message": "User must accept the group rules before joining",
                "code": "6",
            },
            {
                "text": "The account is a member of the maximum number of groups.",
                "message": "Account in maximum number of groups",
                "code": "10",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the Group in question",
                "optional": "0",
                "name": "group_id",
            },
            {
                "text": "If the group has rules, they must be displayed to the user prior to joining. Passing a true value for this argument specifies that the application has displayed the group rules to the user, and that the user has agreed to them. (See flickr.groups.getInfo).",
                "optional": "1",
                "name": "accept_rules",
            },
        ],
        "description": "Join a public group as a member.",
        "needslogin": True,
        "name": "flickr.groups.join",
    },
    "flickr.photosets.setPrimaryPhoto": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photoset id passed was not the id of avalid photoset owned by the calling user.",
                "message": "Photoset not found",
                "code": "1",
            },
            {
                "text": "The photo id passed was not the id of a valid photo owned by the calling user.",
                "message": "Photo not found",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photoset to set primary photo to.",
                "optional": "0",
                "name": "photoset_id",
            },
            {
                "text": "The id of the photo to set as primary.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "description": "Set photoset primary photo",
        "needslogin": True,
        "name": "flickr.photosets.setPrimaryPhoto",
    },
    "flickr.people.findByEmail": {
        "errors": [
            {
                "text": "No user with the supplied email address was found.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return a user's NSID, given their email address",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The email address of the user to find  (may be primary or secondary).",
                "optional": "0",
                "name": "find_email",
            },
        ],
        "needslogin": False,
        "response": '<user nsid="12037949632@N01">\r\n\t<username>Stewart</username> \r\n</user>',
        "name": "flickr.people.findByEmail",
    },
    "flickr.auth.checkToken": {
        "errors": [
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.auth.checkToken",
        "explanation": '<p><code>perms</code> can have values of <code>none</code>, <code>read</code>, <code>write</code> or <code>delete</code>. For more information, see the <a href="/services/api/auth.spec.html">Auth API spec</a>.</p>',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The authentication token to check.",
                "optional": "0",
                "name": "auth_token",
            },
        ],
        "needslogin": False,
        "response": '<auth>\r\n\t<token>976598454353455</token>\r\n\t<perms>read</perms>\r\n\t<user nsid="12037949754@N01" username="Bees" fullname="Cal H" />\r\n</auth>',
        "description": 'Returns the credentials attached to an authentication token. This call <b>must</b> be signed, and is <b><a href="/services/api/auth.oauth.html">deprecated in favour of OAuth</a></b>.',
    },
    "flickr.stats.getPhotosetDomains": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The photoset id was either invalid or was for a set not owned by the calling user.",
                "message": "Photoset not found",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.stats.getPhotosetDomains",
        "explanation": '<p>There is one <code>&lt;domain&gt;</code> element for each referring domain, with attributes for the domain name and the number of views.</p>\r\n\r\n<p>For details on the referrers coming from each domain listed you can call <a href="/services/api/flickr.stats.getPhotosetReferrers.html">flickr.stats.getPhotosetReferrers</a></p>',
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format.\r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.",
                "optional": "0",
                "name": "date",
            },
            {
                "text": "The id of the photoset to get stats for. If not provided, stats for all sets will be returned.",
                "optional": "1",
                "name": "photoset_id",
            },
            {
                "text": "Number of domains to return per page. If this argument is omitted, it defaults to 25. The maximum allowed value is 100.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<domains page="1" perpage="25" pages="1" total="3">\r\n\t<domain name="images.search.yahoo.com" views="127" />\r\n\t<domain name="flickr.com" views="122" />\r\n\t<domain name="images.google.com" views="70" />\r\n</domains>\r\n',
        "description": "Get a list of referring domains for a photoset",
    },
    "flickr.photos.suggestions.getList": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Only show suggestions for a single photo.",
                "optional": "1",
                "name": "photo_id",
            },
            {
                "text": 'Only show suggestions with a given status.\r\n\r\n<ul>\r\n<li><strong>0</strong>, pending</li>\r\n<li><strong>1</strong>, approved</li>\r\n<li><strong>2</strong>, rejected</li>\r\n</ul>\r\n\r\nThe default is pending (or "0").',
                "optional": "1",
                "name": "status_id",
            },
        ],
        "description": "Return a list of suggestions for a user that are pending approval.",
        "needslogin": True,
        "name": "flickr.photos.suggestions.getList",
    },
    "flickr.photos.comments.getList": {
        "errors": [
            {
                "text": "The photo id was either invalid or was for a photo not viewable by the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns the comments for a photo",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to fetch comments for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "Minimum date that a a comment was added. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "min_comment_date",
            },
            {
                "text": "Maximum date that a comment was added. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "max_comment_date",
            },
            {"text": "", "optional": "1", "name": "page"},
            {"text": "", "optional": "1", "name": "per_page"},
            {"text": "", "optional": "1", "name": "include_faves"},
        ],
        "needslogin": False,
        "response": '<comments photo_id="109722179">\r\n        <comment id="6065-109722179-72057594077818641"\r\n         author="35468159852@N01" authorname="Rev Dan Catt" datecreate="1141841470"\r\n         permalink="http://www.flickr.com/photos/straup/109722179/#comment72057594077818641"\r\n         >Umm, I\'m not sure, can I get back to you on that one?</comment>\r\n</comments>',
        "name": "flickr.photos.comments.getList",
    },
    "flickr.photosets.orderSets": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "One of the photoset ids passed was not the id of a valid photoset belonging to the calling user.",
                "message": "Set not found",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "A comma delimited list of photoset IDs, ordered with the set to show first, first in the list. Any set IDs not given in the list will be set to appear at the end of the list, ordered by their IDs.",
                "optional": "0",
                "name": "photoset_ids",
            },
        ],
        "description": "Set the order of photosets for the calling user.",
        "needslogin": True,
        "name": "flickr.photosets.orderSets",
    },
    "flickr.photos.search": {
        "errors": [
            {
                "text": "When performing an 'all tags' search, you may not specify more than 20 tags to join together.",
                "message": "Too many tags in ALL query",
                "code": "1",
            },
            {
                "text": "A user_id was passed which did not match a valid flickr user.",
                "message": "Unknown user",
                "code": "2",
            },
            {
                "text": "To perform a search with no parameters (to get the latest public photos, please use flickr.photos.getRecent instead).",
                "message": "Parameterless searches have been disabled",
                "code": "3",
            },
            {
                "text": "The logged in user (if any) does not have permission to view the pool for this group.",
                "message": "You don't have permission to view this pool",
                "code": "4",
            },
            {
                "text": "The Flickr API search databases are temporarily unavailable.",
                "message": "Sorry, the Flickr search API is not currently available.",
                "code": "10",
            },
            {
                "text": "The query styntax for the machine_tags argument did not validate.",
                "message": "No valid machine tags",
                "code": "11",
            },
            {
                "text": "The maximum number of machine tags in a single query was exceeded.",
                "message": "Exceeded maximum allowable machine tags",
                "code": "12",
            },
            {
                "text": "jump_to only supported for some query types.",
                "message": "jump_to not avaiable for this query",
                "code": "13",
            },
            {
                "text": "jump_to must be valid photo ID.",
                "message": "Bad value for jump_to",
                "code": "14",
            },
            {"text": "", "message": "Photo not found", "code": "15"},
            {
                "text": "",
                "message": "You can only search within your own favorites",
                "code": "16",
            },
            {
                "text": "The call tried to use the contacts parameter with no user ID or a user ID other than that of the authenticated user.",
                "message": "You can only search within your own contacts",
                "code": "17",
            },
            {
                "text": "The request contained contradictory arguments.",
                "message": "Illogical arguments",
                "code": "18",
            },
            {
                "text": "The search requested photos beyond an allowable offset. Reduce the page number or number of results per page for this search.",
                "message": "Excessive photo offset in search",
                "code": "20",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.photos.search",
        "explanation": "Please note that Flickr will return at most the first 4,000 results for any given search query.  If this is an issue, we recommend trying a more specific query.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user who's photo to search. If this parameter isn't passed then everybody's public photos will be searched. A value of \"me\" will search against the calling user's photos for authenticated calls.",
                "optional": "1",
                "name": "user_id",
            },
            {
                "text": "A comma-delimited list of tags. Photos with one or more of the tags listed will be returned. You can exclude results that match a term by prepending it with a - character.",
                "optional": "1",
                "name": "tags",
            },
            {
                "text": "Either 'any' for an OR combination of tags, or 'all' for an AND combination. Defaults to 'any' if not specified.",
                "optional": "1",
                "name": "tag_mode",
            },
            {
                "text": "A free text search. Photos who's title, description or tags contain the text will be returned. You can exclude results that match a term by prepending it with a - character.",
                "optional": "1",
                "name": "text",
            },
            {
                "text": "Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.",
                "optional": "1",
                "name": "min_upload_date",
            },
            {
                "text": "Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.",
                "optional": "1",
                "name": "max_upload_date",
            },
            {
                "text": "Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.",
                "optional": "1",
                "name": "min_taken_date",
            },
            {
                "text": "Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.",
                "optional": "1",
                "name": "max_taken_date",
            },
            {
                "text": "The license id for photos (for possible values see the flickr.photos.licenses.getInfo method). Multiple licenses may be comma-separated.",
                "optional": "1",
                "name": "license",
            },
            {
                "text": "The order in which to sort returned photos. Deafults to date-posted-desc (unless you are doing a radial geo query, in which case the default sorting is by ascending distance from the point specified). The possible values are: date-posted-asc, date-posted-desc, date-taken-asc, date-taken-desc, interestingness-desc, interestingness-asc, and relevance.",
                "optional": "1",
                "name": "sort",
            },
            {
                "text": "Return photos only matching a certain privacy level. This only applies when making an authenticated call to view photos you own. Valid values are:\r\n<ul>\r\n<li>1 public photos</li>\r\n<li>2 private photos visible to friends</li>\r\n<li>3 private photos visible to family</li>\r\n<li>4 private photos visible to friends & family</li>\r\n<li>5 completely private photos</li>\r\n</ul>\r\n",
                "optional": "1",
                "name": "privacy_filter",
            },
            {
                "text": 'A comma-delimited list of 4 values defining the Bounding Box of the area that will be searched.\r\n<br /><br />\r\nThe 4 values represent the bottom-left corner of the box and the top-right corner, minimum_longitude, minimum_latitude, maximum_longitude, maximum_latitude.\r\n<br /><br />\r\nLongitude has a range of -180 to 180 , latitude of -90 to 90. Defaults to -180, -90, 180, 90 if not specified.\r\n<br /><br />\r\nUnlike standard photo queries, geo (or bounding box) queries will only return 250 results per page.\r\n<br /><br />\r\nGeo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against "parameterless searches" for queries without a geo component.\r\n<br /><br />\r\nA tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters &#8212; If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).',
                "optional": "1",
                "name": "bbox",
            },
            {
                "text": "Recorded accuracy level of the location information.  Current range is 1-16 : \r\n\r\n<ul>\r\n<li>World level is 1</li>\r\n<li>Country is ~3</li>\r\n<li>Region is ~6</li>\r\n<li>City is ~11</li>\r\n<li>Street is ~16</li>\r\n</ul>\r\n\r\nDefaults to maximum value if not specified.",
                "optional": "1",
                "name": "accuracy",
            },
            {
                "text": "Safe search setting:\r\n\r\n<ul>\r\n<li>1 for safe.</li>\r\n<li>2 for moderate.</li>\r\n<li>3 for restricted.</li>\r\n</ul>\r\n\r\n(Please note: Un-authed calls can only see Safe content.)",
                "optional": "1",
                "name": "safe_search",
            },
            {
                "text": "Content Type setting:\r\n<ul>\r\n<li>1 for photos only.</li>\r\n<li>2 for screenshots only.</li>\r\n<li>3 for 'other' only.</li>\r\n<li>4 for photos and screenshots.</li>\r\n<li>5 for screenshots and 'other'.</li>\r\n<li>6 for photos and 'other'.</li>\r\n<li>7 for photos, screenshots, and 'other' (all).</li>\r\n</ul>",
                "optional": "1",
                "name": "content_type",
            },
            {
                "text": 'Aside from passing in a fully formed machine tag, there is a special syntax for searching on specific properties :\r\n\r\n<ul>\r\n  <li>Find photos using the \'dc\' namespace :    <code>"machine_tags" => "dc:"</code></li>\r\n\r\n  <li> Find photos with a title in the \'dc\' namespace : <code>"machine_tags" => "dc:title="</code></li>\r\n\r\n  <li>Find photos titled "mr. camera" in the \'dc\' namespace : <code>"machine_tags" => "dc:title=\\"mr. camera\\"</code></li>\r\n\r\n  <li>Find photos whose value is "mr. camera" : <code>"machine_tags" => "*:*=\\"mr. camera\\""</code></li>\r\n\r\n  <li>Find photos that have a title, in any namespace : <code>"machine_tags" => "*:title="</code></li>\r\n\r\n  <li>Find photos that have a title, in any namespace, whose value is "mr. camera" : <code>"machine_tags" => "*:title=\\"mr. camera\\""</code></li>\r\n\r\n  <li>Find photos, in the \'dc\' namespace whose value is "mr. camera" : <code>"machine_tags" => "dc:*=\\"mr. camera\\""</code></li>\r\n\r\n </ul>\r\n\r\nMultiple machine tags may be queried by passing a comma-separated list. The number of machine tags you can pass in a single query depends on the tag mode (AND or OR) that you are querying with. "AND" queries are limited to (16) machine tags. "OR" queries are limited\r\nto (8).',
                "optional": "1",
                "name": "machine_tags",
            },
            {
                "text": "Either 'any' for an OR combination of tags, or 'all' for an AND combination. Defaults to 'any' if not specified.",
                "optional": "1",
                "name": "machine_tag_mode",
            },
            {
                "text": "The id of a group who's pool to search.  If specified, only matching photos posted to the group's pool will be returned.",
                "optional": "1",
                "name": "group_id",
            },
            {
                "text": "boolean. Pass faves=1 along with your user_id to search within your favorites",
                "optional": "1",
                "name": "faves",
            },
            {
                "text": 'Limit results by camera.  Camera names must be in the <a href="http://www.flickr.com/cameras">Camera Finder</a> normalized form.  <a href="http://flickr.com/services/api/flickr.cameras.getList">flickr.cameras.getList()</a> returns a list of searchable cameras.',
                "optional": "1",
                "name": "camera",
            },
            {"text": "Jump, jump!", "optional": "1", "name": "jump_to"},
            {
                "text": "Search your contacts. Either 'all' or 'ff' for just friends and family. (Experimental)",
                "optional": "1",
                "name": "contacts",
            },
            {
                "text": 'A 32-bit identifier that uniquely represents spatial entities. (not used if bbox argument is present). \r\n<br /><br />\r\nGeo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against "parameterless searches" for queries without a geo component.\r\n<br /><br />\r\nA tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters &mdash; If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).',
                "optional": "1",
                "name": "woe_id",
            },
            {
                "text": 'A Flickr place id.  (not used if bbox argument is present).\r\n<br /><br />\r\nGeo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against "parameterless searches" for queries without a geo component.\r\n<br /><br />\r\nA tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters &mdash; If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).',
                "optional": "1",
                "name": "place_id",
            },
            {
                "text": "Filter results by media type. Possible values are <code>all</code> (default), <code>photos</code> or <code>videos</code>",
                "optional": "1",
                "name": "media",
            },
            {
                "text": 'Any photo that has been geotagged, or if the value is "0" any photo that has <i>not</i> been geotagged.\r\n<br /><br />\r\nGeo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against "parameterless searches" for queries without a geo component.\r\n<br /><br />\r\nA tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters &mdash; If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).',
                "optional": "1",
                "name": "has_geo",
            },
            {
                "text": 'Geo context is a numeric value representing the photo\'s geotagginess beyond latitude and longitude. For example, you may wish to search for photos that were taken "indoors" or "outdoors". <br /><br />\r\nThe current list of context IDs is :<br /><br/>\r\n<ul>\r\n<li><strong>0</strong>, not defined.</li>\r\n<li><strong>1</strong>, indoors.</li>\r\n<li><strong>2</strong>, outdoors.</li>\r\n</ul>\r\n<br /><br />\r\nGeo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against "parameterless searches" for queries without a geo component.\r\n<br /><br />\r\nA tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters &mdash; If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).',
                "optional": "1",
                "name": "geo_context",
            },
            {
                "text": 'A valid latitude, in decimal format, for doing radial geo queries.\r\n<br /><br />\r\nGeo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against "parameterless searches" for queries without a geo component.\r\n<br /><br />\r\nA tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters &mdash; If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).',
                "optional": "1",
                "name": "lat",
            },
            {
                "text": 'A valid longitude, in decimal format, for doing radial geo queries.\r\n<br /><br />\r\nGeo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against "parameterless searches" for queries without a geo component.\r\n<br /><br />\r\nA tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters &mdash; If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).',
                "optional": "1",
                "name": "lon",
            },
            {
                "text": "A valid radius used for geo queries, greater than zero and less than 20 miles (or 32 kilometers), for use with point-based geo queries. The default value is 5 (km).",
                "optional": "1",
                "name": "radius",
            },
            {
                "text": 'The unit of measure when doing radial geo queries. Valid options are "mi" (miles) and "km" (kilometers). The default is "km".',
                "optional": "1",
                "name": "radius_units",
            },
            {
                "text": 'Limit the scope of the search to only photos that are part of the <a href="http://flickr.com/commons">Flickr Commons project</a>. Default is false.',
                "optional": "1",
                "name": "is_commons",
            },
            {
                "text": 'Limit the scope of the search to only photos that are in a <a href="http://www.flickr.com/help/galleries/">gallery</a>?  Default is false, search all photos.',
                "optional": "1",
                "name": "in_gallery",
            },
            {
                "text": "The id of a user.  Will return photos where the user has been people tagged.  A call signed as the person_id in question will return *all* photos the user in, otherwise returns public photos.",
                "optional": "1",
                "name": "person_id",
            },
            {
                "text": "Limit the scope of the search to only photos that are for sale on Getty. Default is false.",
                "optional": "1",
                "name": "is_getty",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "needslogin": False,
        "description": "Return a list of photos matching some criteria. Only photos visible to the calling user will be returned. To return private or semi-private photos, the caller must be authenticated with 'read' permissions, and have permission to view the photos. Unauthenticated calls will only return public photos.",
    },
    "flickr.stats.getCollectionReferrers": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The collection id was either invalid or was for a collection not owned by the calling user.",
                "message": "Collection not found",
                "code": "4",
            },
            {
                "text": "The domain provided is not in the expected format.",
                "message": "Invalid domain",
                "code": "5",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.stats.getCollectionReferrers",
        "explanation": "<p>There is one <code>&lt;referrer&gt;</code> element for each referring page, with attributes for the url and the number of views.</p>\r\n\r\n<p>Where the referring page is a search engine and we have identified the search term it will be given in the searchterm attribute.</p>",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format. \r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.",
                "optional": "0",
                "name": "date",
            },
            {
                "text": 'The domain to return referrers for. This should be a hostname (eg: "flickr.com") with no protocol or pathname.',
                "optional": "0",
                "name": "domain",
            },
            {
                "text": "The id of the collection to get stats for. If not provided, stats for all collections will be returned.",
                "optional": "1",
                "name": "collection_id",
            },
            {
                "text": "Number of referrers to return per page. If this argument is omitted, it defaults to 25. The maximum allowed value is 100.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<domain page="1" perpage="25" pages="1" total="3" name="flickr.com">\r\n\t<referrer url="http://flickr.com/" views="11"/>\r\n\t<referrer url="http://flickr.com/photos/friends/" views="8"/>\r\n\t<referrer url="http://flickr.com/search/?q=stats+api" views="2" searchterm="stats api"/>\r\n</domain>\r\n',
        "description": "Get a list of referrers from a given domain to a collection",
    },
    "flickr.groups.getInfo": {
        "errors": [
            {
                "text": "The group NSID passed did not refer to a group that the calling user can see - either an invalid group is or a group that can't be seen by the calling user.",
                "message": "Group not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get information about a group.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the group to fetch information for.",
                "optional": "0",
                "name": "group_id",
            },
            {
                "text": 'The language of the group name and description to fetch.  If the language is not found, the primary language of the group will be returned.\r\n\r\nValid values are the same as <a href="/services/feeds/">in feeds</a>.',
                "optional": "1",
                "name": "lang",
            },
        ],
        "needslogin": False,
        "response": '<group id="34427465497@N01" iconserver="1" iconfarm="1" lang="en-us" ispoolmoderated="0">\r\n\t<name>GNEverybody</name>\r\n\t<description>The group for GNE players</description>\r\n\t<members>69</members>\r\n\t<privacy>3</privacy>\r\n\t<throttle count="10" mode="month" remaining="3"/>\r\n        <restrictions photos_ok="1" videos_ok="1" images_ok="1" screens_ok="1" art_ok="1" safe_ok="1" moderate_ok="0" restricted_ok="0" has_geo="0" />\r\n</group>',
        "name": "flickr.groups.getInfo",
    },
    "flickr.machinetags.getPredicates": {
        "errors": [
            {
                "text": "Missing or invalid namespace argument.",
                "message": "Not a valid namespace",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return a list of unique predicates, optionally limited by a given namespace.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Limit the list of predicates returned to those that have the following namespace.",
                "optional": "1",
                "name": "namespace",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": False,
        "response": '<predicates page="1" pages="1" total="3" perpage="500">\r\n    <predicate usage="20" namespaces="1">elbow</predicate>\r\n    <predicate usage="52" namespaces="2">face</predicate>\r\n    <predicate usage="10" namespaces="1">hand</predicate>\r\n</predicates>\r\n',
        "name": "flickr.machinetags.getPredicates",
    },
    "flickr.photos.getCounts": {
        "errors": [
            {
                "text": "Neither dates nor taken_dates were specified.",
                "message": "No dates specified",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Gets a list of photo counts for the given date ranges for the calling user.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "A comma delimited list of unix timestamps, denoting the periods to return counts for. They should be specified <b>smallest first</b>.",
                "optional": "1",
                "name": "dates",
            },
            {
                "text": "A comma delimited list of mysql datetimes, denoting the periods to return counts for. They should be specified <b>smallest first</b>.",
                "optional": "1",
                "name": "taken_dates",
            },
        ],
        "needslogin": True,
        "response": '<photocounts>\r\n\t<photocount count="4" fromdate="1093566950" todate="1093653350" /> \r\n\t<photocount count="0" fromdate="1093653350" todate="1093739750" /> \r\n\t<photocount count="0" fromdate="1093739750" todate="1093826150" /> \r\n\t<photocount count="2" fromdate="1093826150" todate="1093912550" /> \r\n\t<photocount count="0" fromdate="1093912550" todate="1093998950" /> \r\n\t<photocount count="0" fromdate="1093998950" todate="1094085350" /> \r\n\t<photocount count="0" fromdate="1094085350" todate="1094171750" /> \r\n</photocounts>\r\n',
        "name": "flickr.photos.getCounts",
    },
    "flickr.photos.transform.rotate": {
        "errors": [
            {
                "text": "The photo id was invalid or did not belong to the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The rotation degrees were an invalid value.",
                "message": "Invalid rotation",
                "code": "2",
            },
            {
                "text": "There was a problem either rotating the image or storing the rotated versions.",
                "message": "Temporary failure",
                "code": "3",
            },
            {
                "text": "The rotation service is currently disabled.",
                "message": "Rotation disabled",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Rotate a photo.",
        "needssigning": True,
        "requiredperms": "write",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to rotate.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The amount of degrees by which to rotate the photo (clockwise) from it's current orientation. Valid values are 90, 180 and 270.",
                "optional": "0",
                "name": "degrees",
            },
        ],
        "needslogin": True,
        "response": '<photoid secret="abcdef" originalsecret="abcdef">1234</photoid>',
        "name": "flickr.photos.transform.rotate",
    },
    "flickr.photos.delete": {
        "needssigning": True,
        "requiredperms": "delete",
        "errors": [
            {
                "text": "The photo id was not the id of a photo belonging to the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to delete.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "description": "Delete a photo from flickr.",
        "needslogin": True,
        "name": "flickr.photos.delete",
    },
    "flickr.photos.setTags": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photo id passed was not the id of a photo belonging to the calling user. It might be an invalid id, or the photo might be owned by another user. ",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The number of tags specified exceeds the limit for the photo. No tags were modified.",
                "message": "Maximum number of tags reached",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to set tags for.\r\n",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "All tags for the photo (as a single space-delimited string).",
                "optional": "0",
                "name": "tags",
            },
        ],
        "description": "Set the tags for a photo.",
        "needslogin": True,
        "name": "flickr.photos.setTags",
    },
    "flickr.photos.addTags": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photo id passed was not the id of a photo that the calling user can add tags to. It could be an invalid id, or the user may not have permission to add tags to it.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The maximum number of tags for the photo has been reached - no more tags can be added. If the current count is less than the maximum, but adding all of the tags for this request would go over the limit, the whole request is ignored. I.E. when you get this message, none of the requested tags have been added.",
                "message": "Maximum number of tags reached",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to add tags to.",
                "optional": "0",
                "name": "photo_id",
            },
            {"text": "The tags to add to the photo.", "optional": "0", "name": "tags"},
        ],
        "description": "Add tags to a photo.",
        "needslogin": True,
        "name": "flickr.photos.addTags",
    },
    "flickr.stats.getPhotosetReferrers": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The photoset id was either invalid or was for a set not owned by the calling user.",
                "message": "Photoset not found",
                "code": "4",
            },
            {
                "text": "The domain provided is not in the expected format.",
                "message": "Invalid domain",
                "code": "5",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.stats.getPhotosetReferrers",
        "explanation": "<p>There is one <code>&lt;referrer&gt;</code> element for each referring page, with attributes for the url and the number of views.</p>\r\n\r\n<p>Where the referring page is a search engine and we have identified the search term it will be given in the searchterm attribute.</p>",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format. \r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.",
                "optional": "0",
                "name": "date",
            },
            {
                "text": 'The domain to return referrers for. This should be a hostname (eg: "flickr.com") with no protocol or pathname.',
                "optional": "0",
                "name": "domain",
            },
            {
                "text": "The id of the photoset to get stats for. If not provided, stats for all sets will be returned.",
                "optional": "1",
                "name": "photoset_id",
            },
            {
                "text": "Number of referrers to return per page. If this argument is omitted, it defaults to 25. The maximum allowed value is 100.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<domain page="1" perpage="25" pages="1" total="3" name="flickr.com">\r\n\t<referrer url="http://flickr.com/" views="11"/>\r\n\t<referrer url="http://flickr.com/photos/friends/" views="8"/>\r\n\t<referrer url="http://flickr.com/search/?q=stats+api" views="2" searchterm="stats api"/>\r\n</domain>',
        "description": "Get a list of referrers from a given domain to a photoset",
    },
    "flickr.places.getShapeHistory": {
        "errors": [
            {
                "text": "One or more required parameter is missing from the API call.",
                "message": "Required parameter missing",
                "code": "1",
            },
            {
                "text": "An invalid Places (or WOE) ID was passed with the API call.",
                "message": "Not a valid Places ID",
                "code": "2",
            },
            {
                "text": "No place could be found for the Places (or WOE) ID passed to the API call.",
                "message": "Place not found",
                "code": "3",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return an historical list of all the shape data generated for a Places or Where on Earth (WOE) ID.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": 'A Flickr Places ID. <span style="font-style:italic;">(While optional, you must pass either a valid Places ID or a WOE ID.)</span>',
                "optional": "1",
                "name": "place_id",
            },
            {
                "text": 'A Where On Earth (WOE) ID. <span style="font-style:italic;">(While optional, you must pass either a valid Places ID or a WOE ID.)</span>',
                "optional": "1",
                "name": "woe_id",
            },
        ],
        "needslogin": False,
        "response": '<shapes total="2" woe_id="3534" place_id="4hLQygSaBJ92" place_type="locality" place_type_id="7">\r\n   <shapedata created="1223513357" alpha="0.012359619140625"\r\n      count_points="34778" count_edges="52" is_donuthole="0">\r\n      <polylines>\r\n         <polyline>\r\n            45.427627563477,-73.589645385742 45.428966522217,-73.587898254395, etc...\r\n         </polyline>\r\n      </polylines>\r\n      <urls>\r\n         <shapefile>\r\n         http://farm4.static.flickr.com/3228/shapefiles/3534_20081111_0a8afe03c5.tar.gz\r\n         </shapefile>\r\n      </urls>\r\n   </shapedata>\r\n   <!-- and so on... -->\r\n</shapes>',
        "name": "flickr.places.getShapeHistory",
    },
    "flickr.places.placesForContacts": {
        "errors": [
            {
                "text": "Places for contacts have been disabled or are otherwise not available.",
                "message": "Places for contacts are not available at this time",
                "code": "1",
            },
            {
                "text": "One or more of the required parameters was not included with your request.",
                "message": "Required parameter missing",
                "code": "2",
            },
            {
                "text": "An invalid place type was included with your request.",
                "message": "Not a valid place type.",
                "code": "3",
            },
            {
                "text": "An invalid Places (or WOE) identifier was included with your request.",
                "message": "Not a valid Place ID",
                "code": "4",
            },
            {
                "text": "The threshold passed was invalid. ",
                "message": "Not a valid threshold",
                "code": "5",
            },
            {
                "text": 'Contacts must be either "all" or "ff" (friends and family).',
                "message": "Not a valid contacts type",
                "code": "6",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return a list of the top 100 unique places clustered by a given placetype for a user's contacts. ",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": 'A specific place type to cluster photos by. <br /><br />\r\n\r\nValid place types are :\r\n\r\n<ul>\r\n<li><strong>neighbourhood</strong> (and neighborhood)</li>\r\n<li><strong>locality</strong></li>\r\n<li><strong>region</strong></li>\r\n<li><strong>country</strong></li>\r\n<li><strong>continent</strong></li>\r\n</ul>\r\n<br />\r\n<span style="font-style:italic;">The "place_type" argument has been deprecated in favor of the "place_type_id" argument. It won\'t go away but it will not be added to new methods. A complete list of place type IDs is available using the <a href="http://www.flickr.com/services/api/flickr.places.getPlaceTypes.html">flickr.places.getPlaceTypes</a> method. (While optional, you must pass either a valid place type or place type ID.)</span>',
                "optional": "1",
                "name": "place_type",
            },
            {
                "text": 'The numeric ID for a specific place type to cluster photos by. <br /><br />\r\n\r\nValid place type IDs are :\r\n\r\n<ul>\r\n<li><strong>22</strong>: neighbourhood</li>\r\n<li><strong>7</strong>: locality</li>\r\n<li><strong>8</strong>: region</li>\r\n<li><strong>12</strong>: country</li>\r\n<li><strong>29</strong>: continent</li>\r\n</ul>\r\n<br /><span style="font-style:italic;">(While optional, you must pass either a valid place type or place type ID.)</span>',
                "optional": "1",
                "name": "place_type_id",
            },
            {
                "text": 'A Where on Earth identifier to use to filter photo clusters. For example all the photos clustered by <strong>locality</strong> in the United States (WOE ID <strong>23424977</strong>).<br /><br />\r\n<span style="font-style:italic;">(While optional, you must pass either a valid Places ID or a WOE ID.)</span>',
                "optional": "1",
                "name": "woe_id",
            },
            {
                "text": 'A Flickr Places identifier to use to filter photo clusters. For example all the photos clustered by <strong>locality</strong> in the United States (Place ID <strong>4KO02SibApitvSBieQ</strong>).\r\n<br /><br />\r\n<span style="font-style:italic;">(While optional, you must pass either a valid Places ID or a WOE ID.)</span>',
                "optional": "1",
                "name": "place_id",
            },
            {
                "text": 'The minimum number of photos that a place type must have to be included. If the number of photos is lowered then the parent place type for that place will be used.<br /><br />\r\n\r\nFor example if your contacts only have <strong>3</strong> photos taken in the locality of Montreal</strong> (WOE ID 3534) but your threshold is set to <strong>5</strong> then those photos will be "rolled up" and included instead with a place record for the region of Quebec (WOE ID 2344924).',
                "optional": "1",
                "name": "threshold",
            },
            {
                "text": "Search your contacts. Either 'all' or 'ff' for just friends and family. (Default is all)",
                "optional": "1",
                "name": "contacts",
            },
            {
                "text": "Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "min_upload_date",
            },
            {
                "text": "Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "max_upload_date",
            },
            {
                "text": "Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date should be in the form of a mysql datetime.",
                "optional": "1",
                "name": "min_taken_date",
            },
            {
                "text": "Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date should be in the form of a mysql datetime.",
                "optional": "1",
                "name": "max_taken_date",
            },
        ],
        "needslogin": True,
        "response": '<places total="1">\r\n   <place place_id="kH8dLOubBZRvX_YZ" woeid="2487956"\r\n               latitude="37.779" longitude="-122.420"\r\n               place_url="/United+States/California/San+Francisco"\r\n               place_type="locality"\r\n               photo_count="156">San Francisco, California</place>\r\n</places>',
        "name": "flickr.places.placesForContacts",
    },
    "flickr.photos.licenses.setLicense": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The specified id was not the id of a valif photo owner by the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The license id was not valid.",
                "message": "License not found",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The photo to update the license for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": 'The license to apply, or 0 (zero) to remove the current license. Note : as of this writing the "no known copyright restrictions" license (7) is not a valid argument.',
                "optional": "0",
                "name": "license_id",
            },
        ],
        "description": "Sets the license for a photo.",
        "needslogin": True,
        "name": "flickr.photos.licenses.setLicense",
    },
    "flickr.groups.discuss.topics.getInfo": {
        "errors": [
            {
                "text": "The topic_id is invalid",
                "message": "Topic not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get information about a group discussion topic.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID for the topic to edit.",
                "optional": "0",
                "name": "topic_id",
            },
        ],
        "needslogin": False,
        "response": '<?xml version="1.0" encoding="utf-8" ?>\r\n<rsp stat="ok">\r\n  <topic id="72157607082559966" subject="Who\'s still around?" author="30134652@N05" authorname="JAMAL\'S ACCOUNT" is_pro="0" role="admin" iconserver="0" iconfarm="0" count_replies="1" can_edit="1" can_delete="0" can_reply="0" is_sticky="0" is_locked="0" datecreate="1337975869" datelastpost="1337975921" last_reply="72157607082559968">\r\n    <message>Is anyone still around in this group?</message>\r\n  </topic>\r\n</rsp>',
        "name": "flickr.groups.discuss.topics.getInfo",
    },
    "flickr.photosets.editPhotos": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photoset id passed was not a valid photoset id or did not belong to the calling user.",
                "message": "Photoset not found",
                "code": "1",
            },
            {
                "text": "One or more of the photo ids passed was not a valid photo id or does not belong to the calling user.",
                "message": "Photo not found",
                "code": "2",
            },
            {
                "text": "The primary photo id passed was not a valid photo id or does not belong to the calling user.",
                "message": "Primary photo not found",
                "code": "3",
            },
            {
                "text": "The primary photo id passed did not appear in the photo id list.",
                "message": "Primary photo not in list",
                "code": "4",
            },
            {
                "text": "No photo ids were passed.",
                "message": "Empty photos list",
                "code": "5",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photoset to modify. The photoset must belong to the calling user.",
                "optional": "0",
                "name": "photoset_id",
            },
            {
                "text": "The id of the photo to use as the 'primary' photo for the set. This id must also be passed along in photo_ids list argument.",
                "optional": "0",
                "name": "primary_photo_id",
            },
            {
                "text": "A comma-delimited list of photo ids to include in the set. They will appear in the set in the order sent. This list <b>must</b> contain the primary photo id. All photos must belong to the owner of the set. This list of photos replaces the existing list. Call flickr.photosets.addPhoto to append a photo to a set.",
                "optional": "0",
                "name": "photo_ids",
            },
        ],
        "description": "Modify the photos in a photoset. Use this method to add, remove and re-order photos.",
        "needslogin": True,
        "name": "flickr.photosets.editPhotos",
    },
    "flickr.photos.geo.setContext": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photo id was either invalid or was for a photo not viewable by the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The context ID passed to the method is invalid.",
                "message": "Not a valid context",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to set context data for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": 'Context is a numeric value representing the photo\'s geotagginess beyond latitude and longitude. For example, you may wish to indicate that a photo was taken "indoors" or "outdoors". <br /><br />\r\nThe current list of context IDs is :<br /><br/>\r\n<ul>\r\n<li><strong>0</strong>, not defined.</li>\r\n<li><strong>1</strong>, indoors.</li>\r\n<li><strong>2</strong>, outdoors.</li>\r\n</ul>',
                "optional": "0",
                "name": "context",
            },
        ],
        "description": "Indicate the state of a photo's geotagginess beyond latitude and longitude.<br /><br />\r\nNote : photos passed to this method must already be geotagged (using the <q>flickr.photos.geo.setLocation</q> method).",
        "needslogin": True,
        "name": "flickr.photos.geo.setContext",
    },
    "flickr.places.findByLatLon": {
        "errors": [
            {
                "text": "One or more required parameters was not included with the API request.",
                "message": "Required arguments missing",
                "code": "1",
            },
            {
                "text": "The latitude argument failed validation.",
                "message": "Not a valid latitude",
                "code": "2",
            },
            {
                "text": "The longitude argument failed validation.",
                "message": "Not a valid longitude",
                "code": "3",
            },
            {
                "text": "The accuracy argument failed validation.",
                "message": "Not a valid accuracy",
                "code": "4",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": 'Return a place ID for a latitude, longitude and accuracy triple.<br /><br />\r\nThe flickr.places.findByLatLon method is not meant to be a (reverse) geocoder in the traditional sense. It is designed to allow users to find photos for "places" and will round up to the nearest place type to which corresponding place IDs apply.<br /><br />\r\nFor example, if you pass it a street level coordinate it will return the city that contains the point rather than the street, or building, itself.<br /><br />\r\nIt will also truncate latitudes and longitudes to three decimal points.\r\n\r\n',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The latitude whose valid range is -90 to 90. Anything more than 4 decimal places will be truncated.",
                "optional": "0",
                "name": "lat",
            },
            {
                "text": "The longitude whose valid range is -180 to 180. Anything more than 4 decimal places will be truncated.",
                "optional": "0",
                "name": "lon",
            },
            {
                "text": "Recorded accuracy level of the location information. World level is 1, Country is ~3, Region ~6, City ~11, Street ~16. Current range is 1-16. The default is 16.",
                "optional": "1",
                "name": "accuracy",
            },
        ],
        "needslogin": False,
        "response": '<places latitude="37.76513627957266" longitude="-122.42020770907402" accuracy="16" total="1">\r\n   <place place_id="Y12JWsKbApmnSQpbQg" woeid="23512048"\r\n      latitude="37.765" longitude="-122.424" \r\n      place_url="/United+States/California/San+Francisco/Mission+Dolores"\r\n      place_type="neighbourhood" place_type_id="22" \r\n      timezone="America/Los_Angeles"\r\n      name="Mission Dolores, San Francisco, CA, US, United States"/>\r\n</places>',
        "name": "flickr.places.findByLatLon",
    },
    "flickr.photosets.removePhoto": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photoset id passed was not the id of avalid photoset owned by the calling user.",
                "message": "Photoset not found",
                "code": "1",
            },
            {
                "text": "The photo id passed was not the id of a valid photo belonging to the calling user.",
                "message": "Photo not found",
                "code": "2",
            },
            {
                "text": "The photo is not a member of the photoset.",
                "message": "Photo not in set",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photoset to remove a photo from.",
                "optional": "0",
                "name": "photoset_id",
            },
            {
                "text": "The id of the photo to remove from the set.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "description": "Remove a photo from a photoset.",
        "needslogin": True,
        "name": "flickr.photosets.removePhoto",
    },
    "flickr.cameras.getBrands": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns all the brands of cameras that Flickr knows about.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": False,
        "response": '<rsp stat="ok">\r\n<brands>\r\n\t<brand id="canon">Canon</brand>\r\n\t<brand id="nikon">Nikon</brand>\r\n        <brand id="apple">Apple</brand>\r\n</brands>\r\n</rsp>',
        "name": "flickr.cameras.getBrands",
    },
    "flickr.photos.getWithoutGeoData": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "max_upload_date",
            },
            {
                "text": "Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.",
                "optional": "1",
                "name": "min_taken_date",
            },
            {
                "text": "Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.",
                "optional": "1",
                "name": "max_taken_date",
            },
            {
                "text": "Return photos only matching a certain privacy level. Valid values are:\r\n<ul>\r\n<li>1 public photos</li>\r\n<li>2 private photos visible to friends</li>\r\n<li>3 private photos visible to family</li>\r\n<li>4 private photos visible to friends &amp; family</li>\r\n<li>5 completely private photos</li>\r\n</ul>\r\n",
                "optional": "1",
                "name": "privacy_filter",
            },
            {
                "text": "The order in which to sort returned photos. Deafults to date-posted-desc. The possible values are: date-posted-asc, date-posted-desc, date-taken-asc, date-taken-desc, interestingness-desc, and interestingness-asc.",
                "optional": "1",
                "name": "sort",
            },
            {
                "text": "Filter results by media type. Possible values are <code>all</code> (default), <code>photos</code> or <code>videos</code>",
                "optional": "1",
                "name": "media",
            },
            {
                "text": "Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.",
                "optional": "1",
                "name": "min_upload_date",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "description": "Returns a list of your photos which haven't been geo-tagged.",
        "needslogin": True,
        "name": "flickr.photos.getWithoutGeoData",
    },
    "flickr.stats.getTotalViews": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get the overall view counts for an account",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format.\r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.\r\n\r\nIf no date is provided, all time view counts will be returned.",
                "optional": "1",
                "name": "date",
            },
        ],
        "needslogin": True,
        "response": '<stats>\r\n\t<total views="469" />\r\n\t<photos views="386" />\r\n\t<photostream views="72" />\r\n\t<sets views="11" />\r\n\t<collections views="0" />\r\n</stats>',
        "name": "flickr.stats.getTotalViews",
    },
    "flickr.photos.getNotInSet": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.",
                "optional": "1",
                "name": "max_upload_date",
            },
            {
                "text": "Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.",
                "optional": "1",
                "name": "min_taken_date",
            },
            {
                "text": "Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.",
                "optional": "1",
                "name": "max_taken_date",
            },
            {
                "text": "Return photos only matching a certain privacy level. Valid values are:\r\n<ul>\r\n<li>1 public photos</li>\r\n<li>2 private photos visible to friends</li>\r\n<li>3 private photos visible to family</li>\r\n<li>4 private photos visible to friends &amp; family</li>\r\n<li>5 completely private photos</li>\r\n</ul>\r\n",
                "optional": "1",
                "name": "privacy_filter",
            },
            {
                "text": "Filter results by media type. Possible values are <code>all</code> (default), <code>photos</code> or <code>videos</code>",
                "optional": "1",
                "name": "media",
            },
            {
                "text": "Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.",
                "optional": "1",
                "name": "min_upload_date",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "description": "Returns a list of your photos that are not part of any sets.",
        "needslogin": True,
        "name": "flickr.photos.getNotInSet",
    },
    "flickr.groups.discuss.replies.getList": {
        "errors": [
            {
                "text": "The topic_id is invalid.",
                "message": "Topic not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get a list of replies from a group discussion topic.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the topic to fetch replies for.",
                "optional": "0",
                "name": "topic_id",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": "0",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": False,
        "response": '<rsp stat="ok">\r\n  <replies>\r\n    <topic topic_id="72157625038324579" subject="A long time ago in a galaxy far, far away..." group_id="46744914@N00" iconserver="1" iconfarm="1" name="Tell a story in 5 frames (Visual story telling)" author="53930889@N04" authorname="Smallportfolio_jm08" role="member" author_iconserver="5169" author_iconfarm="6" can_edit="0" can_delete="0" can_reply="0" is_sticky="0" is_locked="" datecreate="1287070965" datelastpost="1336905518" total="8" page="1" per_page="3" pages="2">\r\n      <message>&lt;div&gt;&lt;span class=&quot;photo_container pc_m bbml_img&quot;&gt;&lt;a href=&quot;/photos/53930889@N04/5080874079/&quot; title=&quot;Star Wars 1 by Smallportfolio_jm08&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm5.staticflickr.com/4035/5080874079_684cf874e0_m.jpg&quot; width=&quot;240&quot; height=&quot;180&quot; alt=&quot;Star Wars 1 by Smallportfolio_jm08&quot;  class=&quot;pc_img&quot; border=&quot;0&quot; /&gt;&lt;/a&gt;&lt;/span&gt;&lt;/div&gt;\r\n\r\n&lt;div&gt;&lt;span class=&quot;photo_container pc_m bbml_img&quot;&gt;&lt;a href=&quot;/photos/53930889@N04/5081467846/&quot; title=&quot;Star Wars 2 by Smallportfolio_jm08&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm5.staticflickr.com/4071/5081467846_2eec86176d_m.jpg&quot; width=&quot;240&quot; height=&quot;180&quot; alt=&quot;Star Wars 2 by Smallportfolio_jm08&quot;  class=&quot;pc_img&quot; border=&quot;0&quot; /&gt;&lt;/a&gt;&lt;/span&gt;&lt;/div&gt;\r\n\r\n&lt;div&gt;&lt;span class=&quot;photo_container pc_m bbml_img&quot;&gt;&lt;a href=&quot;/photos/53930889@N04/5081467886/&quot; title=&quot;Star Wars 3 by Smallportfolio_jm08&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm5.staticflickr.com/4021/5081467886_d8cca6c8e8_m.jpg&quot; width=&quot;240&quot; height=&quot;180&quot; alt=&quot;Star Wars 3 by Smallportfolio_jm08&quot;  class=&quot;pc_img&quot; border=&quot;0&quot; /&gt;&lt;/a&gt;&lt;/span&gt;&lt;/div&gt;\r\n\r\n&lt;div&gt;&lt;span class=&quot;photo_container pc_m bbml_img&quot;&gt;&lt;a href=&quot;/photos/53930889@N04/5081467910/&quot; title=&quot;Star Wars 4 by Smallportfolio_jm08&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm5.staticflickr.com/4084/5081467910_274bb11fdc_m.jpg&quot; width=&quot;240&quot; height=&quot;180&quot; alt=&quot;Star Wars 4 by Smallportfolio_jm08&quot;  class=&quot;pc_img&quot; border=&quot;0&quot; /&gt;&lt;/a&gt;&lt;/span&gt;&lt;/div&gt;\r\n\r\n&lt;div&gt;&lt;span class=&quot;photo_container pc_m bbml_img&quot;&gt;&lt;a href=&quot;/photos/53930889@N04/5081467948/&quot; title=&quot;Star Wars 5 by Smallportfolio_jm08&quot;&gt;&lt;img class=&quot;notsowide&quot; src=&quot;http://farm5.staticflickr.com/4154/5081467948_1a5f200bc0_m.jpg&quot; width=&quot;240&quot; height=&quot;180&quot; alt=&quot;Star Wars 5 by Smallportfolio_jm08&quot;  class=&quot;pc_img&quot; border=&quot;0&quot; /&gt;&lt;/a&gt;&lt;/span&gt;&lt;/div&gt;</message>\r\n    </topic>\r\n    <reply id="72157625163054214" author="41380738@N05" authorname="BlueRidgeKitties" role="member" iconserver="2459" iconfarm="3" can_edit="0" can_delete="0" datecreate="1287071539" lastedit="0">\r\n      <message>*LOL* The universe is full of &lt;a href=&quot;http://www.flickr.com/groups/visualstory/discuss/72157622533160886/&quot;&gt;giant furry space monsters&lt;/a&gt; it seems! Love it.</message>\r\n    </reply>\r\n    <reply id="72157625163539300" author="52101018@N00" authorname="pterandon" role="admin" iconserver="1" iconfarm="1" can_edit="0" can_delete="0" datecreate="1287076748" lastedit="0">\r\n      <message>Great work. Good focus on different aspects of scene in each frame.  Funny ending-- even better that I didn\'t notice the cat right away!  Being a hopeless Trekkie, I was wondering why Han was doing the Vulcan death grip on one of his allies....</message>\r\n    </reply>\r\n    <reply id="72157625040116805" author="54830408@N02" authorname="tay.grisham" role="member" iconserver="0" iconfarm="0" can_edit="0" can_delete="0" datecreate="1287089858" lastedit="0">\r\n      <message>On a scale of 1 to 10 of awesome. This is a 15</message>\r\n    </reply>\r\n  </replies>\r\n</rsp>',
        "name": "flickr.groups.discuss.replies.getList",
    },
    "flickr.photos.getFavorites": {
        "errors": [
            {
                "text": "The specified photo does not exist, or the calling user does not have permission to view it.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns the list of people who have favorited a given photo.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the photo to fetch the favoriters list for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
            {
                "text": "Number of usres to return per page. If this argument is omitted, it defaults to 10. The maximum allowed value is 50.",
                "optional": "1",
                "name": "per_page",
            },
        ],
        "needslogin": False,
        "response": '<photo id="1253576" secret="81b96be690" server="1" farm="1"\r\n\tpage="1" pages="3" perpage="10" total="27">\r\n\t<person nsid="33939862@N00" username="Dementation" favedate="1166689690"/>\r\n\t<person nsid="49485425@N00" username="indigenous_prodigy" favedate="1166573724"/>\r\n\t<person nsid="46834205@N00" username="smaaz" favedate="1161874052"/>\r\n\t<person nsid="95626108@N00" username="chrome Foxpuppy" favedate="1160528154"/>\r\n\t<person nsid="44991966@N00" username="getnoid" favedate="1159828789"/>\r\n\t<person nsid="92544710@N00" username="miss_rogue" favedate="1158034266"/>\r\n\t<person nsid="50944224@N00" username="Infollatus" favedate="1155317436"/>\r\n\t<person nsid="80544408@N00" username="DafyddLlyr" favedate="1148511763"/>\r\n\t<person nsid="31154299@N00" username="c r i s" favedate="1143085224"/>\r\n\t<person nsid="54309070@N00" username="Shinayaker" favedate="1142584219"/>\r\n</photo>',
        "name": "flickr.photos.getFavorites",
    },
    "flickr.machinetags.getPairs": {
        "errors": [
            {
                "text": "Missing or invalid namespace argument.",
                "message": "Not a valid namespace",
                "code": "1",
            },
            {
                "text": "Missing or invalid predicate argument.",
                "message": "Not a valid predicate",
                "code": "2",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return a list of unique namespace and predicate pairs, optionally limited by predicate or namespace, in alphabetical order.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Limit the list of pairs returned to those that have the following namespace.",
                "optional": "1",
                "name": "namespace",
            },
            {
                "text": "Limit the list of pairs returned to those that have the following predicate.",
                "optional": "1",
                "name": "predicate",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": False,
        "response": '<pairs page="1" total="1228" perpage="500" pages="3">\r\n   <pair namespace="aero" predicate="airline" usage="1093">aero:airline</pair>\r\n   <pair namespace="aero" predicate="icao" usage="4">aero:icao</pair>\r\n   <pair namespace="aero" predicate="model" usage="1026">aero:model</pair>\r\n   <pair namespace="aero" predicate="tail" usage="1048">aero:tail</pair>\r\n</pairs>',
        "name": "flickr.machinetags.getPairs",
    },
    "flickr.urls.lookupGallery": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.urls.lookupGallery",
        "explanation": 'This is the same format returned by <a href="http://www.flickr.com/services/api/flickr.galleries.getInfo.html">flickr.galleries.getInfo</a>.',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {"text": "The gallery's URL.", "optional": "0", "name": "url"},
        ],
        "needslogin": False,
        "response": '<gallery id="6065-72157617483228192" url="/photos/straup/galleries/72157617483228192" owner="35034348999@N01" \r\nprimary_photo_id="292882708" \r\ndate_create="1241028772" date_update="1270111667" \r\ncount_photos="17" count_videos="0" server="112" farm="1" secret="7f29861bc4">\r\n\t<title>Cat Pictures I\'ve Sent To Kevin Collins</title>\r\n\t<description />\r\n</gallery>',
        "description": "Returns gallery info, by url.",
    },
    "flickr.test.echo": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "A testing method which echo's all parameters back in the response.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": False,
        "response": "<method>echo</method>\r\n<foo>bar</foo>",
        "name": "flickr.test.echo",
    },
    "flickr.photosets.editMeta": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photoset id passed was not a valid photoset id or did not belong to the calling user.",
                "message": "Photoset not found",
                "code": "1",
            },
            {
                "text": "No title parameter was passed in the request. ",
                "message": "No title specified",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photoset to modify.",
                "optional": "0",
                "name": "photoset_id",
            },
            {
                "text": "The new title for the photoset.",
                "optional": "0",
                "name": "title",
            },
            {
                "text": "A description of the photoset. May contain limited html.",
                "optional": "1",
                "name": "description",
            },
        ],
        "description": "Modify the meta-data for a photoset.",
        "needslogin": True,
        "name": "flickr.photosets.editMeta",
    },
    "flickr.photosets.removePhotos": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photoset id passed was not the id of available photosets owned by the calling user.",
                "message": "Photoset not found",
                "code": "1",
            },
            {
                "text": "The photo id passed was not the id of a valid photo belonging to the calling user.",
                "message": "Photo not found",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photoset to remove photos from.",
                "optional": "0",
                "name": "photoset_id",
            },
            {
                "text": "Comma-delimited list of photo ids to remove from the photoset.",
                "optional": "0",
                "name": "photo_ids",
            },
        ],
        "description": "Remove multiple photos from a photoset.",
        "needslogin": True,
        "name": "flickr.photosets.removePhotos",
    },
    "flickr.tags.getMostFrequentlyUsed": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns a list of most frequently used tags for a user.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": True,
        "response": '<rsp stat="ok">\r\n<who id="30135021@N05">\r\n\t<tags>\r\n\t\t<tag count="1">blah</tag>\r\n\t\t<tag count="5">publicdomain</tag>\r\n\t</tags>\r\n</who>\r\n</rsp>',
        "name": "flickr.tags.getMostFrequentlyUsed",
    },
    "flickr.prefs.getContentType": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns the default content type preference for the user.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": True,
        "response": '<rsp stat="ok">\r\n<person nsid="12037949754@N01" content_type="1" />\r\n</rsp>',
        "name": "flickr.prefs.getContentType",
    },
    "flickr.people.getPublicPhotos": {
        "needssigning": False,
        "requiredperms": "none",
        "errors": [
            {
                "text": "The user NSID passed was not a valid user NSID.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user who's photos to return.",
                "optional": "0",
                "name": "user_id",
            },
            {
                "text": "Safe search setting:\r\n\r\n<ul>\r\n<li>1 for safe.</li>\r\n<li>2 for moderate.</li>\r\n<li>3 for restricted.</li>\r\n</ul>\r\n\r\n(Please note: Un-authed calls can only see Safe content.)",
                "optional": "1",
                "name": "safe_search",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "description": "Get a list of public photos for the given user.",
        "needslogin": False,
        "name": "flickr.people.getPublicPhotos",
    },
    "flickr.groups.discuss.replies.delete": {
        "needssigning": True,
        "requiredperms": "delete",
        "errors": [
            {
                "text": "The topic_id is invalid.",
                "message": "Topic not found",
                "code": "1",
            },
            {
                "text": "The reply_id is invalid.",
                "message": "Reply not found",
                "code": "2",
            },
            {
                "text": "Replies can only be edited by their owner.",
                "message": "Cannot delete reply",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the topic the post is in.",
                "optional": "0",
                "name": "topic_id",
            },
            {
                "text": "The ID of the reply to delete.",
                "optional": "0",
                "name": "reply_id",
            },
        ],
        "description": "Delete a reply from a group topic.",
        "needslogin": True,
        "name": "flickr.groups.discuss.replies.delete",
    },
    "flickr.groups.browse": {
        "errors": [
            {
                "text": "The value passed for cat_id was not a valid category id.",
                "message": "Category not found",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.groups.browse",
        "explanation": "<p>The <code>count</code> attribute of the <code>subcat</code> element gives the number of groups inside the subcat.</p>\r\n\r\n<p>The <code>members</code> attribute of the <code>group</code> element gives the total number of members in the group. The <code>online</code> attribute gives a count of the members who are currently online. The <code>inchat</code> attribute gives a count of the number of people in the group's chat, regardless of whether they are members of the group.</p>",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The category id to fetch a list of groups and sub-categories for. If not specified, it defaults to zero, the root of the category tree.",
                "optional": "1",
                "name": "cat_id",
            },
        ],
        "needslogin": True,
        "response": '<category name="Alt" path="/Alt" pathids="/63">\r\n\t<subcat id="80" name="18+" count="0" /> \r\n\t<subcat id="82" name="Absurd" count="4" /> \r\n\t<group nsid="34955637532@N01" name="Cal\'s Public Test Group"\r\n\t\tmembers="13" online="1" chatnsid="34955637533@N01" inchat="0" /> \r\n\t<group nsid="34158032587@N01" name="Eric\'s Alt Group Test"\r\n\t\tmembers="3" online="0" chatnsid="34158032588@N01" inchat="0" /> \r\n</category>\r\n',
        "description": "Browse the group category tree, finding groups and sub-categories.",
    },
    "flickr.stats.getPhotostreamDomains": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.stats.getPhotostreamDomains",
        "explanation": '<p>There is one <code>&lt;domain&gt;</code> element for each referring domain, with attributes for the domain name and the number of views.</p>\r\n\r\n<p>For details on the referrers coming from each domain listed you can call <a href="/services/api/flickr.stats.getPhotostreamReferrers.html">flickr.stats.getPhotostreamReferrers</a></p>',
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format.\r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.",
                "optional": "0",
                "name": "date",
            },
            {
                "text": "Number of domains to return per page. If this argument is omitted, it defaults to 25. The maximum allowed value is 100",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<domains page="1" perpage="25" pages="1" total="3">\r\n\t<domain name="images.search.yahoo.com" views="127" />\r\n\t<domain name="flickr.com" views="122" />\r\n\t<domain name="images.google.com" views="70" />\r\n</domains>\r\n',
        "description": "Get a list of referring domains for a photostream",
    },
    "flickr.people.getUploadStatus": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.people.getUploadStatus",
        "explanation": '<p>Bandwidth and filesize numbers are provided in bytes and kilobytes. If you\'re using 32bit numbers, stick to using the kilobyte values - they shouldn\'t ever exceed 2/4 billion, while the byte values will.</p>\r\n\r\n<p>Bandwidth is specified in bytes/kb per month.</p>\r\n\r\n\r\n<p>All accounts display "lots" for the number of remaining sets, but remains in the response for backwards compatibility.</p>\r\n\r\n<p>Pro accounts display "lots" for the number of remaining videos, while free users will display 0, 1, or 2.</p>\r\n',
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": True,
        "response": '<user id="12037949754@N01" ispro="1">\r\n\t<username>Bees</username> \r\n\t<bandwidth\r\n\t\tmaxbytes="2147483648" maxkb="2097152"\r\n\t\tusedbytes="383724" usedkb="374"\r\n\t\tremainingbytes="2147099924" remainingkb="2096777"\r\n\t /> \r\n\t<filesize\r\n\t\tmaxbytes="10485760" maxkb="10240"\r\n\t/> \r\n\t<sets\r\n\t\tcreated="27"\r\n\t\tremaining="lots"\r\n\t/>\r\n\t<videos\r\n\t\tuploaded="5"\r\n\t\tremaining="lots"\r\n\t/>\r\n</user>',
        "description": "Returns information for the calling user related to photo uploads.",
    },
    "flickr.places.resolvePlaceId": {
        "errors": [
            {"text": "", "message": "Place ID required.", "code": "2"},
            {"text": "", "message": "Place not found.", "code": "3"},
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": 'Find Flickr Places information by Place ID.<br /><br />\r\nThis method has been deprecated. It won\'t be removed but you should use <a href="/services/api/flickr.places.getInfo.html">flickr.places.getInfo</a> instead.',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {"text": "A Flickr Places ID", "optional": "0", "name": "place_id"},
        ],
        "needslogin": False,
        "response": '<location place_id="kH8dLOubBZRvX_YZ" woeid="2487956" \r\n                latitude="37.779" longitude="-122.420"\r\n                place_url="/United+States/California/San+Francisco"\r\n                place_type="locality">\r\n   <locality place_id="kH8dLOubBZRvX_YZ" woeid="2487956"\r\n                 latitude="37.779" longitude="-122.420" \r\n                 place_url="/United+States/California/San+Francisco">San Francisco</locality>\r\n   <county place_id="hCca8XSYA5nn0X1Sfw" woeid="12587707"\r\n                 latitude="37.759" longitude="-122.435" \r\n                 place_url="/hCca8XSYA5nn0X1Sfw">San Francisco</county>\r\n   <region place_id="SVrAMtCbAphCLAtP" woeid="2347563" \r\n                latitude="37.271" longitude="-119.270" \r\n                place_url="/United+States/California">California</region>\r\n   <country place_id="4KO02SibApitvSBieQ" woeid="23424977"\r\n                  latitude="48.890" longitude="-116.982" \r\n                  place_url="/United+States">United States</country>\r\n</location>',
        "name": "flickr.places.resolvePlaceId",
    },
    "flickr.machinetags.getRecentValues": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Fetch recently used (or created) machine tags values.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "A namespace that all values should be restricted to.",
                "optional": "1",
                "name": "namespace",
            },
            {
                "text": "A predicate that all values should be restricted to.",
                "optional": "1",
                "name": "predicate",
            },
            {
                "text": "Only return machine tags values that have been added since this timestamp, in epoch seconds.  ",
                "optional": "1",
                "name": "added_since",
            },
        ],
        "needslogin": False,
        "response": '<values namespace="taxonomy" predicate="common" page="1" total="500" perpage="500" pages="1">\r\n    <value usage="4" namespace="taxonomy" predicate="common"\r\n           first_added="1244232796" last_added="1244232796">maui chaff flower</value>\r\n\r\n    <!-- and so on... -->\r\n</values>',
        "name": "flickr.machinetags.getRecentValues",
    },
    "flickr.panda.getList": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": 'Return a list of <a href="http://www.flickr.com/explore/panda">Flickr pandas</a>, from whom you can request photos using the <a href="/services/api/flickr.panda.getPhotos.htm">flickr.panda.getPhotos</a> API method.\r\n<br/><br/>\r\nMore information about the pandas can be found on the <a href="http://code.flickr.com/blog/2009/03/03/panda-tuesday-the-history-of-the-panda-new-apis-explore-and-you/">dev blog</a>.',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": False,
        "response": "<pandas>\r\n   <panda>ling ling</panda>\r\n   <panda>hsing hsing</panda>\r\n   <panda>wang wang</panda>\r\n</pandas>",
        "name": "flickr.panda.getList",
    },
    "flickr.photos.setContentType": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id of a photo belonging to the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "Some or all of the required arguments were not supplied.",
                "message": "Required arguments missing",
                "code": "2",
            },
            {
                "text": "Changing the content type of this photo is not allowed.",
                "message": "Change not allowed",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Set the content type of a photo.",
        "needssigning": True,
        "requiredperms": "write",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to set the adultness of.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The content type of the photo. Must be one of: 1 for Photo, 2 for Screenshot, and 3 for Other.",
                "optional": "0",
                "name": "content_type",
            },
        ],
        "needslogin": True,
        "response": '<rsp stat="ok">\r\n<photo id="14814" content_type="3"/>\r\n</rsp>',
        "name": "flickr.photos.setContentType",
    },
    "flickr.photos.setDates": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photo id was not the id of a valid photo belonging to the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "No dates were specified to be changed.",
                "message": "Not enough arguments",
                "code": "2",
            },
            {
                "text": "The value passed for 'granularity' was not a valid flickr date granularity.",
                "message": "Invalid granularity",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to edit dates for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": 'The date the photo was uploaded to flickr (see the <a href="/services/api/misc.dates.html">dates documentation</a>)',
                "optional": "1",
                "name": "date_posted",
            },
            {
                "text": 'The date the photo was taken (see the <a href="/services/api/misc.dates.html">dates documentation</a>)',
                "optional": "1",
                "name": "date_taken",
            },
            {
                "text": 'The granularity of the date the photo was taken (see the <a href="/services/api/misc.dates.html">dates documentation</a>)',
                "optional": "1",
                "name": "date_taken_granularity",
            },
        ],
        "description": "Set one or both of the dates for a photo.",
        "needslogin": True,
        "name": "flickr.photos.setDates",
    },
    "flickr.photos.geo.getPerms": {
        "errors": [
            {
                "text": "The photo id was either invalid or was for a photo not viewable by the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The photo requested has no location data or is not viewable by the calling user.",
                "message": "Photo has no location information",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get permissions for who may view geo data for a photo.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to get permissions for.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "needslogin": True,
        "response": '<perms id="10592" ispublic="0" iscontact="0" isfriend="0" isfamily="1" />',
        "name": "flickr.photos.geo.getPerms",
    },
    "flickr.test.null": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "description": "Null test",
        "needslogin": True,
        "name": "flickr.test.null",
    },
    "flickr.galleries.addPhoto": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "One or more required parameters was not included with your API call.",
                "message": "Required parameter missing",
                "code": "1",
            },
            {
                "text": "That gallery could not be found.",
                "message": "Invalid gallery ID",
                "code": "2",
            },
            {
                "text": "The requested photo could not be found.",
                "message": "Invalid photo ID",
                "code": "3",
            },
            {
                "text": "The comment body could not be validated.",
                "message": "Invalid comment",
                "code": "4",
            },
            {
                "text": "Unable to add the photo to the gallery.",
                "message": "Failed to add photo",
                "code": "5",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": 'The ID of the gallery to add a photo to.  Note: this is the compound ID returned in methods like <a href="/services/api/flickr.galleries.getList.html">flickr.galleries.getList</a>, and <a href="/services/api/flickr.galleries.getListForPhoto.html">flickr.galleries.getListForPhoto</a>.',
                "optional": "0",
                "name": "gallery_id",
            },
            {
                "text": "The photo ID to add to the gallery",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "A short comment or story to accompany the photo.",
                "optional": "1",
                "name": "comment",
            },
        ],
        "description": "Add a photo to a gallery.",
        "needslogin": True,
        "name": "flickr.galleries.addPhoto",
    },
    "flickr.interestingness.getList": {
        "needssigning": False,
        "requiredperms": "none",
        "errors": [
            {
                "text": "The date string passed did not validate. All dates must be formatted : YYYY-MM-DD",
                "message": "Not a valid date string.",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "A specific date, formatted as YYYY-MM-DD, to return interesting photos for.",
                "optional": "1",
                "name": "date",
            },
            {
                "text": "Always ask the pandas for interesting photos. This is a temporary argument to allow developers to update their code.",
                "optional": "1",
                "name": "use_panda",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "description": "Returns the list of interesting photos for the most recent day or a user-specified date.",
        "needslogin": False,
        "name": "flickr.interestingness.getList",
    },
    "flickr.photosets.comments.addComment": {
        "errors": [
            {"text": "", "message": "Photoset not found", "code": "1"},
            {"text": "", "message": "Blank comment", "code": "8"},
            {
                "text": "The user has reached the limit for number of comments posted during a specific time period. Wait a bit and try again.",
                "message": "User is posting comments too fast.",
                "code": "9",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Add a comment to a photoset.",
        "needssigning": True,
        "requiredperms": "write",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photoset to add a comment to.",
                "optional": "0",
                "name": "photoset_id",
            },
            {"text": "Text of the comment", "optional": "0", "name": "comment_text"},
        ],
        "needslogin": True,
        "response": '<comment id="97777-12492-72057594037942601" />',
        "name": "flickr.photosets.comments.addComment",
    },
    "flickr.photos.getContext": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id, or was the id of a photo that the calling user does not have permission to view.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.photos.getContext",
        "explanation": '<p>When either the previous of next photo is unavailable, the element is still returned, but contains <code>id="0"</code></p>',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to fetch the context for.",
                "optional": "0",
                "name": "photo_id",
            },
            {"text": "", "optional": "1", "name": "num_prev"},
            {"text": "", "optional": "1", "name": "num_next"},
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description, license, date_upload, date_taken, owner_name, icon_server, original_format, last_update, geo, tags, machine_tags, o_dims, views, media, path_alias, url_sq, url_t, url_s, url_m, url_z, url_l, url_o</code>",
                "optional": "1",
                "name": "extras",
            },
            {
                "text": "Accepts <code>datetaken</code> or <code>dateposted</code> and returns results in the proper order.",
                "optional": "1",
                "name": "order_by",
            },
        ],
        "needslogin": False,
        "response": '<prevphoto id="2980" secret="973da1e709"\r\n\ttitle="boo!" url="/photos/bees/2980/" /> \r\n<nextphoto id="2985" secret="059b664012"\r\n\ttitle="Amsterdam Amstel" url="/photos/bees/2985/" /> ',
        "description": "Returns next and previous photos for a photo in a photostream.",
    },
    "flickr.photos.recentlyUpdated": {
        "errors": [
            {
                "text": "Some or all of the required arguments were not supplied.",
                "message": "Required argument missing.",
                "code": "1",
            },
            {
                "text": "The date argument did not pass validation.",
                "message": "Not a valid date",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.photos.recentlyUpdated",
        "explanation": "<p>Photos are sorted by their date updated timestamp, in descending order.</p>",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "A Unix timestamp or any English textual datetime description indicating the date from which modifications should be compared.",
                "optional": "0",
                "name": "min_date",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<photos page="1" pages="1" perpage="100" total="2">\r\n        <photo id="169885459" owner="35034348999@N01" \r\n               secret="c85114c195" server="46" title="Doubting Michael"\r\n               ispublic="1" isfriend="0" isfamily="0" lastupdate="1150755888" />\r\n        <photo id="85022332" owner="35034348999@N01"\r\n               secret="23de6de0c0" server="41"\r\n               title="&quot;Do you think we\'re allowed to tape stuff to the walls?&quot;"\r\n               ispublic="1" isfriend="0" isfamily="0" lastupdate="1150564974" />\r\n</photos>',
        "description": "<p>Return a list of your photos that have been recently created or which have been recently modified.</p>\r\n\r\n<p>Recently modified may mean that the photo's metadata (title, description, tags) may have been changed or a comment has been added (or just modified somehow :-)</p>",
    },
    "flickr.photos.getWithGeoData": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "min_upload_date",
            },
            {
                "text": "Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "max_upload_date",
            },
            {
                "text": "Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date should be in the form of a mysql datetime.",
                "optional": "1",
                "name": "min_taken_date",
            },
            {
                "text": "Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date should be in the form of a mysql datetime.",
                "optional": "1",
                "name": "max_taken_date",
            },
            {
                "text": "Return photos only matching a certain privacy level. Valid values are:\r\n<ul>\r\n<li>1 public photos</li>\r\n<li>2 private photos visible to friends</li>\r\n<li>3 private photos visible to family</li>\r\n<li>4 private photos visible to friends & family</li>\r\n<li>5 completely private photos</li>\r\n</ul>\r\n",
                "optional": "1",
                "name": "privacy_filter",
            },
            {
                "text": "The order in which to sort returned photos. Deafults to date-posted-desc. The possible values are: date-posted-asc, date-posted-desc, date-taken-asc, date-taken-desc, interestingness-desc, and interestingness-asc.",
                "optional": "1",
                "name": "sort",
            },
            {
                "text": "Filter results by media type. Possible values are <code>all</code> (default), <code>photos</code> or <code>videos</code>",
                "optional": "1",
                "name": "media",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "description": "Returns a list of your geo-tagged photos.",
        "needslogin": True,
        "name": "flickr.photos.getWithGeoData",
    },
    "flickr.auth.getToken": {
        "errors": [
            {
                "text": "The specified frob does not exist or has already been used.",
                "message": "Invalid frob",
                "code": "108",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.auth.getToken",
        "explanation": '<p><code>perms</code> can have values of <code>none</code>, <code>read</code>, <code>write</code> or <code>delete</code>. For more information, see the <a href="/services/api/auth.spec.html">Auth API spec</a>.</p>',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {"text": "The frob to check.", "optional": "0", "name": "frob"},
        ],
        "needslogin": False,
        "response": '<auth>\r\n\t<token>976598454353455</token>\r\n\t<perms>write</perms>\r\n\t<user nsid="12037949754@N01" username="Bees" fullname="Cal H" />\r\n</auth>',
        "description": 'Returns the auth token for the given frob, if one has been attached. <b>This method call must be signed</b>, and is <b><a href="/services/api/auth.oauth.html">deprecated in favour of OAuth</a></b>.',
    },
    "flickr.photos.setMeta": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photo id passed was not the id of a photo belonging to the calling user. It might be an invalid id, or the photo might be owned by another user. ",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to set information for.",
                "optional": "0",
                "name": "photo_id",
            },
            {"text": "The title for the photo.", "optional": "0", "name": "title"},
            {
                "text": "The description for the photo.",
                "optional": "0",
                "name": "description",
            },
        ],
        "description": "Set the meta information for a photo.",
        "needslogin": True,
        "name": "flickr.photos.setMeta",
    },
    "flickr.stats.getPhotoDomains": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The photo id was either invalid or was for a photo not owned by the calling user.",
                "message": "Photo not found",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.stats.getPhotoDomains",
        "explanation": '<p>There is one <code>&lt;domain&gt;</code> element for each referring domain, with attributes for the domain name and the number of views.</p>\r\n\r\n<p>For details on the referrers coming from each domain listed you can call <a href="/services/api/flickr.stats.getPhotoReferrers.html">flickr.stats.getPhotoReferrers</a></p>',
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format.\r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.",
                "optional": "0",
                "name": "date",
            },
            {
                "text": "The id of the photo to get stats for. If not provided, stats for all photos will be returned.",
                "optional": "1",
                "name": "photo_id",
            },
            {
                "text": "Number of domains to return per page. If this argument is omitted, it defaults to 25. The maximum allowed value is 100.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<domains page="1" perpage="25" pages="1" total="3">\r\n\t<domain name="images.search.yahoo.com" views="127" />\r\n\t<domain name="flickr.com" views="122" />\r\n\t<domain name="images.google.com" views="70" />\r\n</domains>\r\n',
        "description": "Get a list of referring domains for a photo",
    },
    "flickr.groups.discuss.topics.add": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The group by that ID does not exist\r\n",
                "message": "Group not found",
                "code": "1",
            },
            {
                "text": "Either this account is not a member of the group, or discussion in this group is disabled.",
                "message": "Cannot post to group",
                "code": "2",
            },
            {
                "text": "The post message is too long.",
                "message": "Message is too long",
                "code": "3",
            },
            {
                "text": "Subject and message are required.",
                "message": "Missing required arguments",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the group to add a topic to.\r\n",
                "optional": "0",
                "name": "group_id",
            },
            {"text": "The topic subject.", "optional": "0", "name": "subject"},
            {"text": "The topic message.", "optional": "0", "name": "message"},
        ],
        "description": "Post a new discussion topic to a group.",
        "needslogin": True,
        "name": "flickr.groups.discuss.topics.add",
    },
    "flickr.galleries.editMeta": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "One or more required parameters was missing from your request.",
                "message": "Required parameter missing",
                "code": "1",
            },
            {
                "text": "The title or description arguments could not be validated.",
                "message": "Invalid title or description",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The gallery ID to update.",
                "optional": "0",
                "name": "gallery_id",
            },
            {
                "text": "The new title for the gallery.",
                "optional": "0",
                "name": "title",
            },
            {
                "text": "The new description for the gallery.",
                "optional": "1",
                "name": "description",
            },
        ],
        "description": "Modify the meta-data for a gallery.",
        "needslogin": True,
        "name": "flickr.galleries.editMeta",
    },
    "flickr.galleries.getListForPhoto": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return the list of galleries to which a photo has been added.  Galleries are returned sorted by date which the photo was added to the gallery.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the photo to fetch a list of galleries for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "Number of galleries to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": False,
        "response": '<galleries total="7" page="1" pages="1" per_page="100">\r\n    <gallery id="9634-72157621980433950" \r\n             url="http://www.flickr.com/photos/revdancatt/galleries/72157621980433950" \r\n             owner="35468159852@N01" date_create="1249748647" date_update="1260486168" \r\n\t     primary_photo_id="2080242123" primary_photo_server="2209" \r\n\t     primary_photo_farm="3" primary_photo_secret="55c9"\r\n             count_photos="18" count_videos="0">\r\n        <title>Vivitar Ultra Wide &amp; Slim Selection</title>\r\n        <description>The cheap and cheerful camera that isn\'t quite as cheap as it used to be.</description>\r\n    </gallery>\r\n   <gallery id="22342631-72157622254010831" \r\n             url="http://www.flickr.com/photos/22365685@N03/galleries/72157622254010831" \r\n             owner="22365685@N03" date_create="1253035020" date_update="1260431618" \r\n             primary_photo_id="3182914049" primary_photo_server="3319" \r\n             primary_photo_farm="4" primary_photo_secret="b94fb"\r\n             count_photos="13" count_videos="0">\r\n        <title>Awesome Pics</title>\r\n        <description />\r\n    </gallery>\r\n</galleries>',
        "name": "flickr.galleries.getListForPhoto",
    },
    "flickr.tags.getClusterPhotos": {
        "needssigning": False,
        "requiredperms": "none",
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The tag that this cluster belongs to.",
                "optional": "0",
                "name": "tag",
            },
            {
                "text": "The top three tags for the cluster, separated by dashes (just like the url).",
                "optional": "0",
                "name": "cluster_id",
            },
        ],
        "description": "Returns the first 24 photos for a given tag cluster",
        "needslogin": False,
        "name": "flickr.tags.getClusterPhotos",
    },
    "flickr.prefs.getGeoPerms": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": 'Returns the default privacy level for geographic information attached to the user\'s photos and whether or not the user has chosen to use geo-related EXIF information to automatically geotag their photos.\r\n\r\nPossible values, for viewing geotagged photos, are:\r\n\r\n<ul>\r\n<li>0 : <i>No default set</i></li>\r\n<li>1 : Public</li>\r\n<li>2 : Contacts only</li>\r\n<li>3 : Friends and Family only</li>\r\n<li>4 : Friends only</li>\r\n<li>5 : Family only</li>\r\n<li>6 : Private</li>\r\n</ul>\r\n\r\nUsers can edit this preference at <a href="http://www.flickr.com/account/geo/privacy/">http://www.flickr.com/account/geo/privacy/</a>.\r\n<br /><br />\r\nPossible values for whether or not geo-related EXIF information will be used to geotag a photo are:\r\n\r\n<ul>\r\n<li>0: Geo-related EXIF information will be ignored</li>\r\n<li>1: Geo-related EXIF information will be used to try and geotag photos on upload</li>\r\n</ul>\r\n\r\nUsers can edit this preference at <a href="http://www.flickr.com/account/geo/exif/?from=privacy">http://www.flickr.com/account/geo/exif/?from=privacy</a>',
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": True,
        "response": '<rsp stat="ok">\r\n<person nsid="12037949754@N01" geoperms="1" importgeoexif="0" />\r\n</rsp>',
        "name": "flickr.prefs.getGeoPerms",
    },
    "flickr.contacts.getPublicList": {
        "errors": [
            {
                "text": "The specified user NSID was not a valid user.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.contacts.getPublicList",
        "explanation": '<p>See <a href="/services/api/flickr.contacts.getList.html">flickr.contacts.getList</a> for an explanation of the response.</p>',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user to fetch the contact list for.",
                "optional": "0",
                "name": "user_id",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 1000. The maximum allowed value is 1000.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "Include additional information for each contact, such as realname, is_friend, is_family, path_alias and location.",
                "optional": "1",
                "name": "show_more",
            },
        ],
        "needslogin": False,
        "response": '<contacts page="1" pages="1" perpage="1000" total="3">\r\n\t<contact nsid="12037949629@N01" username="Eric" iconserver="1" ignored="1" /> \r\n\t<contact nsid="12037949631@N01" username="neb" iconserver="1" ignored="0" /> \r\n\t<contact nsid="41578656547@N01" username="cal_abc" iconserver="1" ignored="0" />\r\n</contacts>',
        "description": "Get the contact list for a user.",
    },
    "flickr.tags.getListUserRaw": {
        "errors": [
            {
                "text": "The calling user was not logged in.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get the raw versions of a given tag (or all tags) for the currently logged-in user.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The tag you want to retrieve all raw versions for.",
                "optional": "1",
                "name": "tag",
            },
        ],
        "needslogin": False,
        "response": '<who id="12037949754@N01">\r\n    <tags>\r\n        <tag clean="foo">\r\n            <raw>foo</raw>\r\n            <raw>Foo</raw>\r\n            <raw>f:oo</raw>\r\n        </tag>\r\n    </tags>\r\n</who>',
        "name": "flickr.tags.getListUserRaw",
    },
    "flickr.photos.getContactsPublicPhotos": {
        "errors": [
            {
                "text": "The user NSID passed was not a valid user NSID.",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Fetch a list of recent public photos from a users' contacts.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user to fetch photos for.",
                "optional": "0",
                "name": "user_id",
            },
            {
                "text": "Number of photos to return. Defaults to 10, maximum 50. This is only used if <code>single_photo</code> is not passed.",
                "optional": "1",
                "name": "count",
            },
            {
                "text": "set as 1 to only show photos from friends and family (excluding regular contacts).",
                "optional": "1",
                "name": "just_friends",
            },
            {
                "text": "Only fetch one photo (the latest) per contact, instead of all photos in chronological order.",
                "optional": "1",
                "name": "single_photo",
            },
            {
                "text": "Set to 1 to include photos from the user specified by user_id.",
                "optional": "1",
                "name": "include_self",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: license, date_upload, date_taken, owner_name, icon_server, original_format, last_update.",
                "optional": "1",
                "name": "extras",
            },
        ],
        "needslogin": False,
        "response": '<photos>\r\n\t<photo id="2801" owner="12037949629@N01"\r\n\t\tsecret="123456" server="1"\r\n\t\tusername="Eric is the best" title="grease" /> \r\n\t<photo id="2499" owner="33853651809@N01"\r\n\t\tsecret="123456" server="1"\r\n\t\tusername="cal18" title="36679_o" /> \r\n\t<photo id="2437" owner="12037951898@N01"\r\n\t\tsecret="123456" server="1"\r\n\t\tusername="georgie parker" title="phoenix9_stewart" /> \r\n</photos>',
        "name": "flickr.photos.getContactsPublicPhotos",
    },
    "flickr.photosets.getList": {
        "errors": [
            {
                "text": "The user NSID passed was not a valid user NSID and the calling user was not logged in.\r\n",
                "message": "User not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.photosets.getList",
        "explanation": "<p>Photosets are returned in the user's specified order, which may not mean the newest set is first. Applications displaying photosets should respect the user's ordering.</p>",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user to get a photoset list for. If none is specified, the calling user is assumed.",
                "optional": "1",
                "name": "user_id",
            },
            {
                "text": "The page of results to get. Currently, if this is not provided, all sets are returned, but this behaviour may change in future.",
                "optional": "1",
                "name": "page",
            },
            {
                "text": "The number of sets to get per page. If paging is enabled, the maximum number of sets per page is 500.",
                "optional": "1",
                "name": "per_page",
            },
        ],
        "needslogin": False,
        "response": '<photosets page="1" pages="1" perpage="30" total="2" cancreate="1">\r\n    <photoset id="72157626216528324" primary="5504567858" secret="017804c585" server="5174" farm="6" photos="22" videos="0" count_views="137" count_comments="0" can_comment="1" date_create="1299514498" date_update="1300335009">\r\n      <title>Avis Blanche</title>\r\n      <description>My Grandma\'s Recipe File.</description>\r\n    </photoset>\r\n    <photoset id="72157624618609504" primary="4847770787" secret="6abd09a292" server="4153" farm="5" photos="43" videos="12" count_views="523" count_comments="1" can_comment="1" date_create="1280530593" date_update="1308091378">\r\n      <title>Mah Kittehs</title>\r\n      <description>Sixty and Niner. Born on the 3rd of May, 2010, or thereabouts. Came to my place on Thursday, July 29, 2010.</description>\r\n    </photoset>\r\n</photosets>',
        "description": "Returns the photosets belonging to the specified user.",
    },
    "flickr.auth.getFullToken": {
        "errors": [
            {
                "text": "The passed mini-token was not valid.",
                "message": "Mini-token not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.auth.getFullToken",
        "explanation": '<p><code>perms</code> can have values of <code>none</code>, <code>read</code>, <code>write</code> or <code>delete</code>. For more information, see the <a href="/services/api/auth.spec.html">Auth API spec</a>.</p>',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The mini-token typed in by a user. It should be 9 digits long. It may optionally contain dashes.",
                "optional": "0",
                "name": "mini_token",
            },
        ],
        "needslogin": False,
        "response": '<auth>\r\n\t<token>976598454353455</token>\r\n\t<perms>write</perms>\r\n\t<user nsid="12037949754@N01" username="Bees" fullname="Cal H" />\r\n</auth>',
        "description": 'Get the full authentication token for a mini-token. <b>This method call must be signed</b>, and is <b><a href="/services/api/auth.oauth.html">deprecated in favour of OAuth</a></b>.',
    },
    "flickr.galleries.getPhotos": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.galleries.getPhotos",
        "explanation": 'Returns a <a href="http://code.flickr.com/blog/2008/08/19/standard-photos-response-apis-for-civilized-age/">standard photo response</a>.  Additionally if the gallery creator has included a comment with the photo this will be then the photo element will have the attribute has_comment="1" and the child element "comment" will be present.',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the gallery of photos to return",
                "optional": "0",
                "name": "gallery_id",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "needslogin": False,
        "response": '<photos page="1" pages="1" perpage="500" total="2">\r\n\t<photo id="2822546461" owner="78398753@N00" secret="2dbcdb589f" server="1" farm="1" title="FOO" \r\n     ispublic="1" isfriend="0" isfamily="0" is_primary="1" has_comment="1">\r\n\t\t<comment>best cat picture ever!</comment>\r\n\t</photo>\r\n\t<photo id="2822544806" owner="78398753@N00" secret="bd93cbe917" server="1" farm="1" title="OOK" \r\n     ispublic="1" isfriend="0" isfamily="0" is_primary="0" has_comment="0" />\r\n</photos>',
        "description": "Return the list of photos for a gallery",
    },
    "flickr.groups.discuss.replies.getInfo": {
        "errors": [
            {
                "text": "The topic_id is invalid",
                "message": "Topic not found",
                "code": "1",
            },
            {
                "text": "The reply_id is invalid",
                "message": "Reply not found",
                "code": "2",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get information on a group topic reply.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The ID of the topic the post is in.",
                "optional": "0",
                "name": "topic_id",
            },
            {
                "text": "The ID of the reply to fetch.",
                "optional": "0",
                "name": "reply_id",
            },
        ],
        "needslogin": False,
        "response": '<?xml version="1.0" encoding="utf-8" ?>\r\n<rsp stat="ok">\r\n  <reply id="72157607082559968" author="30134652@N05" authorname="JAMAL\'S ACCOUNT" is_pro="0" role="admin" iconserver="0" iconfarm="0" can_edit="1" can_delete="1" datecreate="1337975921" lastedit="0">\r\n    <message>...well, too bad.</message>\r\n  </reply>\r\n</rsp>',
        "name": "flickr.groups.discuss.replies.getInfo",
    },
    "flickr.photos.geo.getLocation": {
        "errors": [
            {
                "text": "The photo id was either invalid or was for a photo not viewable by the calling user.",
                "message": "Photo not found.",
                "code": "1",
            },
            {
                "text": "The photo requested has no location data or is not viewable by the calling user.",
                "message": "Photo has no location information.",
                "code": "2",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get the geo data (latitude and longitude and the accuracy level) for a photo.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo you want to retrieve location data for.",
                "optional": "0",
                "name": "photo_id",
            },
            {"text": "Extra flags.", "optional": "1", "name": "extras"},
        ],
        "needslogin": False,
        "response": '<photo id="123">\r\n        <location latitude="-17.685895" longitude="-63.36914" accuracy="6" />\r\n</photo>',
        "name": "flickr.photos.geo.getLocation",
    },
    "flickr.places.find": {
        "errors": [
            {
                "text": "One or more required parameters was not included with the API call.",
                "message": "Required parameter missing",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.places.find",
        "explanation": "Each place returned will contain its place ID, corresponding URL (underneath www.flickr.com/places) and place type for disambiguating different locations with the same name.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The query string to use for place ID lookups",
                "optional": "0",
                "name": "query",
            },
            {
                "text": "A bounding box for limiting the area to query.",
                "optional": "1",
                "name": "bbox",
            },
            {"text": "Secret sauce.", "optional": "1", "name": "extras"},
            {
                "text": "Do we want sexy time words in our venue results?",
                "optional": "1",
                "name": "safe",
            },
        ],
        "needslogin": False,
        "response": '<places query="Alabama" total="3">\r\n   <place place_id="VrrjuESbApjeFS4." woeid="2347559"\r\n               latitude="32.614" longitude="-86.680"\r\n               place_url="/United+States/Alabama"\r\n               place_type="region">Alabama, Alabama, United States</place>\r\n   <place place_id="cGHuc0mbApmzEHoP" woeid="2352520"\r\n               latitude="43.096" longitude="-78.389"\r\n               place_url="/United+States/New+York/Alabama"\r\n               place_type="locality">Alabama, New York, United States</place>\r\n   <place place_id="o4yVPEqYBJvFMP8Q" woeid="1579389"\r\n               latitude="-26.866" longitude="26.583"\r\n               place_url="/South+Africa/North+West/Alabama"\r\n               place_type="locality">Alabama, North West, South Africa</place>\r\n</places>',
        "description": "Return a list of place IDs for a query string.<br /><br />\r\nThe flickr.places.find method is <b>not</b> a geocoder. It will round <q>up</q> to the nearest place type to which place IDs apply. For example, if you pass it a street level address it will return the city that contains the address rather than the street, or building, itself.",
    },
    "flickr.photosets.comments.editComment": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The comment id passed was not a valid comment id.",
                "message": "Comment not found.",
                "code": "2",
            },
            {
                "text": "Comment text can't be blank.",
                "message": "Blank comment.",
                "code": "8",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the comment to edit.",
                "optional": "0",
                "name": "comment_id",
            },
            {
                "text": "Update the comment to this text.",
                "optional": "0",
                "name": "comment_text",
            },
        ],
        "description": "Edit the text of a comment as the currently authenticated user.",
        "needslogin": True,
        "name": "flickr.photosets.comments.editComment",
    },
    "flickr.auth.getFrob": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": 'Returns a frob to be used during authentication. <b>This method call must be signed</b>, and is <b><a href="/services/api/auth.oauth.html">deprecated in favour of OAuth</a></b>.',
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": False,
        "response": "<frob>746563215463214621</frob>",
        "name": "flickr.auth.getFrob",
    },
    "flickr.photos.comments.getRecentForContacts": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Limits the resultset to photos that have been commented on since this date. The date should be in the form of a Unix timestamp.<br /><br />\r\nThe default, and maximum, offset is (1) hour.\r\n\r\n\r\n",
                "optional": "1",
                "name": "date_lastcomment",
            },
            {
                "text": "A comma-separated list of contact NSIDs to limit the scope of the query to.",
                "optional": "1",
                "name": "contacts_filter",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "description": "Return the list of photos belonging to your contacts that have been commented on recently.",
        "needslogin": True,
        "name": "flickr.photos.comments.getRecentForContacts",
    },
    "flickr.photos.notes.add": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The calling user does not have permission to add a note to this photo",
                "message": "User cannot add notes",
                "code": "2",
            },
            {
                "text": "One or more of the required arguments were not supplied.",
                "message": "Missing required arguments",
                "code": "3",
            },
            {
                "text": "The maximum number of notes for the photo has been reached.",
                "message": "Maximum number of notes reached",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Add a note to a photo. Coordinates and sizes are in pixels, based on the 500px image size shown on individual photo pages.",
        "needssigning": True,
        "requiredperms": "write",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to add a note to",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The left coordinate of the note",
                "optional": "0",
                "name": "note_x",
            },
            {
                "text": "The top coordinate of the note",
                "optional": "0",
                "name": "note_y",
            },
            {"text": "The width of the note", "optional": "0", "name": "note_w"},
            {"text": "The height of the note", "optional": "0", "name": "note_h"},
            {
                "text": "The description of the note",
                "optional": "0",
                "name": "note_text",
            },
        ],
        "needslogin": True,
        "response": '<note id="1234" />',
        "name": "flickr.photos.notes.add",
    },
    "flickr.photos.suggestions.removeSuggestion": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The unique ID for the location suggestion to approve.",
                "optional": "0",
                "name": "suggestion_id",
            },
        ],
        "description": "Remove a suggestion, made by the calling user, from a photo.",
        "needslogin": True,
        "name": "flickr.photos.suggestions.removeSuggestion",
    },
    "flickr.photos.setPerms": {
        "errors": [
            {
                "text": "The photo id passed was not a valid photo id of a photo belonging to the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "Some or all of the required arguments were not supplied.",
                "message": "Required arguments missing",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Set permissions for a photo.",
        "needssigning": True,
        "requiredperms": "write",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to set permissions for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "1 to set the photo to public, 0 to set it to private.",
                "optional": "0",
                "name": "is_public",
            },
            {
                "text": "1 to make the photo visible to friends when private, 0 to not.",
                "optional": "0",
                "name": "is_friend",
            },
            {
                "text": "1 to make the photo visible to family when private, 0 to not.",
                "optional": "0",
                "name": "is_family",
            },
            {
                "text": "who can add comments to the photo and it's notes. one of:<br />\r\n<code>0</code>: nobody<br />\r\n<code>1</code>: friends &amp; family<br />\r\n<code>2</code>: contacts<br />\r\n<code>3</code>: everybody",
                "optional": "0",
                "name": "perm_comment",
            },
            {
                "text": "who can add notes and tags to the photo. one of:<br />\r\n<code>0</code>: nobody / just the owner<br />\r\n<code>1</code>: friends &amp; family<br />\r\n<code>2</code>: contacts<br />\r\n<code>3</code>: everybody\r\n",
                "optional": "0",
                "name": "perm_addmeta",
            },
        ],
        "needslogin": True,
        "response": '<photoid secret="abcdef" originalsecret="abcdef">1234</photoid>',
        "name": "flickr.photos.setPerms",
    },
    "flickr.photos.people.add": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The NSID passed was not a valid user id.",
                "message": "Person not found",
                "code": "1",
            },
            {
                "text": "The photo id passed was not a valid photo id.",
                "message": "Photo not found",
                "code": "2",
            },
            {
                "text": "The person being added to the photo does not allow the calling user to add them.",
                "message": "User cannot add this person to photos",
                "code": "3",
            },
            {
                "text": "The owner of the photo doesn't allow the calling user to add people to their photos.",
                "message": "User cannot add people to that photo",
                "code": "4",
            },
            {
                "text": "The person being added to the photo does not want to be identified in this photo.",
                "message": "Person can't be tagged in that photo",
                "code": "5",
            },
            {
                "text": "Not all of the co-ordinate parameters (person_x, person_y, person_w, person_h) were passed with valid values.",
                "message": "Some co-ordinate paramters were blank",
                "code": "6",
            },
            {
                "text": "You can only add yourself to another member's non-public photos.",
                "message": "Can't add that person to a non-public photo",
                "code": "7",
            },
            {
                "text": "The maximum number of people has already been added to the photo.",
                "message": "Too many people in that photo",
                "code": "8",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to add a person to.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The NSID of the user to add to the photo.",
                "optional": "0",
                "name": "user_id",
            },
            {
                "text": "The left-most pixel co-ordinate of the box around the person.",
                "optional": "1",
                "name": "person_x",
            },
            {
                "text": "The top-most pixel co-ordinate of the box around the person.",
                "optional": "1",
                "name": "person_y",
            },
            {
                "text": "The width (in pixels) of the box around the person.",
                "optional": "1",
                "name": "person_w",
            },
            {
                "text": "The height (in pixels) of the box around the person.",
                "optional": "1",
                "name": "person_h",
            },
        ],
        "description": "Add a person to a photo. Coordinates and sizes of boxes are optional; they are measured in pixels, based on the 500px image size shown on individual photo pages.",
        "needslogin": True,
        "name": "flickr.photos.people.add",
    },
    "flickr.photos.getExif": {
        "errors": [
            {
                "text": "The photo id was either invalid or was for a photo not viewable by the calling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The owner of the photo does not want to share EXIF data.",
                "message": "Permission denied",
                "code": "2",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "name": "flickr.photos.getExif",
        "explanation": "<p>The <code>&lt;clean&gt;</code> element contains a pretty-formatted version of the tag where availabale.</p>",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to fetch information for.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The secret for the photo. If the correct secret is passed then permissions checking is skipped. This enables the 'sharing' of individual photos by passing around the id and secret.",
                "optional": "1",
                "name": "secret",
            },
        ],
        "needslogin": False,
        "response": '<photo id="4424" secret="06b8e43bc7" server="2">\r\n\t<exif tagspace="TIFF" tagspaceid="1" tag="271" label="Manufacturer">\r\n\t\t<raw>Canon</raw>\r\n\t</exif>\r\n\t<exif tagspace="EXIF" tagspaceid="0" tag="33437" label="Aperture">\r\n\t\t<raw>90/10</raw>\r\n\t\t<clean>f/9</clean>\r\n\t</exif>\r\n\t<exif tagspace="GPS" tagspaceid="3" tag="4" label="Longitude">\r\n\t\t<raw>64/1, 42/1, 4414/100</raw>\r\n\t\t<clean>64\xb0 42\' 44.14"</clean>\r\n\t</exif>\r\n</photo>\r\n',
        "description": "Retrieves a list of EXIF/TIFF/GPS tags for a given photo. The calling user must have permission to view the photo.",
    },
    "flickr.photos.licenses.getInfo": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Fetches a list of available photo licenses for Flickr.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": False,
        "response": '<licenses>\r\n        <license id="0" name="All Rights Reserved" url="" />\r\n\t<license id="1" name="Attribution-NonCommercial-ShareAlike License"\r\n\t\turl="http://creativecommons.org/licenses/by-nc-sa/2.0/" /> \r\n\t<license id="2" name="Attribution-NonCommercial License"\r\n\t\turl="http://creativecommons.org/licenses/by-nc/2.0/" /> \r\n\t<license id="3" name="Attribution-NonCommercial-NoDerivs License"\r\n\t\turl="http://creativecommons.org/licenses/by-nc-nd/2.0/" /> \r\n\t<license id="4" name="Attribution License"\r\n\t\turl="http://creativecommons.org/licenses/by/2.0/" /> \r\n\t<license id="5" name="Attribution-ShareAlike License"\r\n\t\turl="http://creativecommons.org/licenses/by-sa/2.0/" /> \r\n\t<license id="6" name="Attribution-NoDerivs License"\r\n\t\turl="http://creativecommons.org/licenses/by-nd/2.0/" /> \r\n\t<license id="7" name="No known copyright restrictions"\r\n\t\turl="http://flickr.com/commons/usage/" />\r\n        <license id="8" name="United States Government Work"\r\n                url="http://www.usa.gov/copyright.shtml" />\r\n</licenses>',
        "name": "flickr.photos.licenses.getInfo",
    },
    "flickr.groups.pools.add": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photo id passed was not the id of a photo owned by the caling user.",
                "message": "Photo not found",
                "code": "1",
            },
            {
                "text": "The group id passed was not a valid id for a group the user is a member of.",
                "message": "Group not found",
                "code": "2",
            },
            {
                "text": "The specified photo is already in the pool for the specified group.",
                "message": "Photo already in pool",
                "code": "3",
            },
            {
                "text": "The photo has already been added to the maximum allowed number of pools.",
                "message": "Photo in maximum number of pools",
                "code": "4",
            },
            {
                "text": "The user has already added the maximum amount of allowed photos to the pool.",
                "message": "Photo limit reached",
                "code": "5",
            },
            {
                "text": "The pool is moderated, and the photo has been added to the Pending Queue. If it is approved by a group administrator, it will be added to the pool.",
                "message": "Your Photo has been added to the Pending Queue for this Pool",
                "code": "6",
            },
            {
                "text": "The pool is moderated, and the photo has already been added to the Pending Queue.",
                "message": "Your Photo has already been added to the Pending Queue for this Pool",
                "code": "7",
            },
            {
                "text": "The content has been disallowed from the pool by the group admin(s).",
                "message": "Content not allowed",
                "code": "8",
            },
            {
                "text": "A group pool has reached the upper limit for the number of photos allowed.",
                "message": "Maximum number of photos in Group Pool",
                "code": "10",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to add to the group pool. The photo must belong to the calling user.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The NSID of the group who's pool the photo is to be added to.",
                "optional": "0",
                "name": "group_id",
            },
        ],
        "description": "Add a photo to a group's pool.",
        "needslogin": True,
        "name": "flickr.groups.pools.add",
    },
    "flickr.machinetags.getValues": {
        "errors": [
            {
                "text": "Missing or invalid namespace argument.",
                "message": "Not a valid namespace",
                "code": "1",
            },
            {
                "text": "Missing or invalid predicate argument.",
                "message": "Not a valid predicate",
                "code": "2",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return a list of unique values for a namespace and predicate.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The namespace that all values should be restricted to.",
                "optional": "0",
                "name": "namespace",
            },
            {
                "text": "The predicate that all values should be restricted to.",
                "optional": "0",
                "name": "predicate",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
            {"text": "Minimum usage count.", "optional": "1", "name": "usage"},
        ],
        "needslogin": False,
        "response": '<values namespace="upcoming" predicate="event" page="1" pages="1" total="3" perpage="500">\r\n    <value usage="3">123</value>\r\n    <value usage="1">456</value>\r\n    <value usage="147">789</value>\r\n</values>',
        "name": "flickr.machinetags.getValues",
    },
    "flickr.photosets.delete": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photoset id passed was not a valid photoset id or did not belong to the calling user.",
                "message": "Photoset not found",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photoset to delete. It must be owned by the calling user.",
                "optional": "0",
                "name": "photoset_id",
            },
        ],
        "description": "Delete a photoset.",
        "needslogin": True,
        "name": "flickr.photosets.delete",
    },
    "flickr.push.unsubscribe": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {
                "text": "One of the required arguments for the method was not provided.",
                "message": "Required parameter missing",
                "code": "1",
            },
            {
                "text": "One of the arguments was specified with an illegal value.",
                "message": "Invalid parameter value",
                "code": "2",
            },
            {
                "text": "The verification callback failed, or failed to return the expected response to confirm the un-subscription.",
                "message": "Callback failed or invalid response",
                "code": "4",
            },
            {
                "text": "A subscription with those details exists already, but it is in a pending (non-verified) state. Please wait a bit for the verification callback to complete before attempting to update the subscription.",
                "message": "Subscription awaiting verification callback response - try again later",
                "code": "6",
            },
            {
                "text": "No subscription matching the provided details for this user could be found.",
                "message": "Subscription not found",
                "code": "7",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": 'The type of subscription. See <a href="http://www.flickr.com/services/api/flickr.push.getTopics.htm">flickr.push.getTopics</a>.',
                "optional": "0",
                "name": "topic",
            },
            {
                "text": "The url for the subscription endpoint (must be the same url as was used when creating the subscription).",
                "optional": "0",
                "name": "callback",
            },
            {
                "text": "The verification mode, either 'sync' or 'async'. See the <a href=\"http://pubsubhubbub.googlecode.com/svn/trunk/pubsubhubbub-core-0.3.html#subscribingl\">Google PubSubHubbub spec</a> for details.",
                "optional": "0",
                "name": "verify",
            },
            {
                "text": 'The verification token to be echoed back to the subscriber during the verification callback, as per the <a href="http://pubsubhubbub.googlecode.com/svn/trunk/pubsubhubbub-core-0.3.html#subscribing">Google PubSubHubbub spec</a>. Limited to 200 bytes.',
                "optional": "1",
                "name": "verify_token",
            },
        ],
        "description": "Why would you want to do this?\r\n<br><br>\r\n<i>(this method is experimental and may change)</i>",
        "needslogin": True,
        "name": "flickr.push.unsubscribe",
    },
    "flickr.stats.getCollectionStats": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The collection id was either invalid or was for a collection not owned by the calling user.",
                "message": "Collection not found",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get the number of views on a collection for a given date.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format.\r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.",
                "optional": "0",
                "name": "date",
            },
            {
                "text": "The id of the collection to get stats for.",
                "optional": "0",
                "name": "collection_id",
            },
        ],
        "needslogin": True,
        "response": '<stats views="24" />',
        "name": "flickr.stats.getCollectionStats",
    },
    "flickr.photos.suggestions.approveSuggestion": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The unique ID for the location suggestion to approve.",
                "optional": "0",
                "name": "suggestion_id",
            },
        ],
        "description": "Approve a suggestion for a photo.",
        "needslogin": True,
        "name": "flickr.photos.suggestions.approveSuggestion",
    },
    "flickr.places.getPlaceTypes": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Fetches a list of available place types for Flickr.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": False,
        "response": '<place_types>\r\n   <place_type place_type_id="22">neighbourhood</place_type>\r\n   <place_type place_type_id="7">locality</place_type>\r\n   <place_type place_type_id="9">county</place_type>\r\n   <place_type place_type_id="8">region</place_type>\r\n   <place_type place_type_id="12">country</place_type>\r\n   <place_type place_type_id="29">continent</place_type>\r\n</place_types>',
        "name": "flickr.places.getPlaceTypes",
    },
    "flickr.photos.removeTag": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The calling user doesn't have permission to delete the specified tag. This could mean it belongs to someone else, or doesn't exist.",
                "message": "Tag not found",
                "code": "1",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": 'The tag to remove from the photo. This parameter should contain a tag id, as returned by <a href="/services/api/flickr.photos.getInfo.html">flickr.photos.getInfo</a>.',
                "optional": "0",
                "name": "tag_id",
            },
        ],
        "description": "Remove a tag from a photo.",
        "needslogin": True,
        "name": "flickr.photos.removeTag",
    },
    "flickr.photos.getRecent": {
        "needssigning": False,
        "requiredperms": "none",
        "errors": [
            {
                "text": "",
                "message": "bad value for jump_to, must be valid photo id.",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {"text": "", "optional": "1", "name": "jump_to"},
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "description": "Returns a list of the latest public photos uploaded to flickr.",
        "needslogin": False,
        "name": "flickr.photos.getRecent",
    },
    "flickr.photosets.getPhotos": {
        "errors": [
            {
                "text": "The photoset id passed was not a valid photoset id.",
                "message": "Photoset not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get the list of photos in a set.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photoset to return the photos for.",
                "optional": "0",
                "name": "photoset_id",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: license, date_upload, date_taken, owner_name, icon_server, original_format, last_update, geo, tags, machine_tags, o_dims, views, media, path_alias, url_sq, url_t, url_s, url_m, url_o",
                "optional": "1",
                "name": "extras",
            },
            {
                "text": "Return photos only matching a certain privacy level. This only applies when making an authenticated call to view a photoset you own. Valid values are:\r\n<ul>\r\n<li>1 public photos</li>\r\n<li>2 private photos visible to friends</li>\r\n<li>3 private photos visible to family</li>\r\n<li>4 private photos visible to friends &amp; family</li>\r\n<li>5 completely private photos</li>\r\n</ul>\r\n",
                "optional": "1",
                "name": "privacy_filter",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 500. The maximum allowed value is 500.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
            {
                "text": "Filter results by media type. Possible values are <code>all</code> (default), <code>photos</code> or <code>videos</code>",
                "optional": "1",
                "name": "media",
            },
        ],
        "needslogin": False,
        "response": '<photoset id="4" primary="2483" page="1" perpage="500" pages="1" total="2">\r\n\t<photo id="2484" secret="123456" server="1"\r\n\t\ttitle="my photo" isprimary="0" /> \r\n\t<photo id="2483" secret="123456" server="1"\r\n\t\ttitle="flickr rocks" isprimary="1" /> \r\n</photoset>',
        "name": "flickr.photosets.getPhotos",
    },
    "flickr.people.getPhotos": {
        "needssigning": True,
        "requiredperms": "read",
        "errors": [
            {"text": "", "message": "Required arguments missing", "code": "1"},
            {
                "text": "A user_id was passed which did not match a valid flickr user.",
                "message": "Unknown user",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the user who's photos to return. A value of \"me\" will return the calling user's photos.",
                "optional": "0",
                "name": "user_id",
            },
            {
                "text": "Safe search setting:\r\n\r\n<ul>\r\n<li>1 for safe.</li>\r\n<li>2 for moderate.</li>\r\n<li>3 for restricted.</li>\r\n</ul>\r\n\r\n(Please note: Un-authed calls can only see Safe content.)",
                "optional": "1",
                "name": "safe_search",
            },
            {
                "text": "Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "min_upload_date",
            },
            {
                "text": "Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date should be in the form of a unix timestamp.",
                "optional": "1",
                "name": "max_upload_date",
            },
            {
                "text": "Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date should be in the form of a mysql datetime.",
                "optional": "1",
                "name": "min_taken_date",
            },
            {
                "text": "Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date should be in the form of a mysql datetime.",
                "optional": "1",
                "name": "max_taken_date",
            },
            {
                "text": "Content Type setting:\r\n<ul>\r\n<li>1 for photos only.</li>\r\n<li>2 for screenshots only.</li>\r\n<li>3 for 'other' only.</li>\r\n<li>4 for photos and screenshots.</li>\r\n<li>5 for screenshots and 'other'.</li>\r\n<li>6 for photos and 'other'.</li>\r\n<li>7 for photos, screenshots, and 'other' (all).</li>\r\n</ul>",
                "optional": "1",
                "name": "content_type",
            },
            {
                "text": "Return photos only matching a certain privacy level. This only applies when making an authenticated call to view photos you own. Valid values are:\r\n<ul>\r\n<li>1 public photos</li>\r\n<li>2 private photos visible to friends</li>\r\n<li>3 private photos visible to family</li>\r\n<li>4 private photos visible to friends & family</li>\r\n<li>5 completely private photos</li>\r\n</ul>",
                "optional": "1",
                "name": "privacy_filter",
            },
            {
                "text": "A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: <code>description</code>, <code>license</code>, <code>date_upload</code>, <code>date_taken</code>, <code>owner_name</code>, <code>icon_server</code>, <code>original_format</code>, <code>last_update</code>, <code>geo</code>, <code>tags</code>, <code>machine_tags</code>, <code>o_dims</code>, <code>views</code>, <code>media</code>, <code>path_alias</code>, <code>url_sq</code>, <code>url_t</code>, <code>url_s</code>, <code>url_q</code>, <code>url_m</code>, <code>url_n</code>, <code>url_z</code>, <code>url_c</code>, <code>url_l</code>, <code>url_o</code>",
                "optional": 1,
                "name": "extras",
            },
            {
                "text": "Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.",
                "optional": 1,
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": 1,
                "name": "page",
            },
        ],
        "description": 'Return photos from the given user\'s photostream. Only photos visible to the calling user will be returned. This method must be authenticated; to return public photos for a user, use <a href="/services/api/flickr.people.getPublicPhotos.html">flickr.people.getPublicPhotos</a>.',
        "needslogin": True,
        "name": "flickr.people.getPhotos",
    },
    "flickr.reflection.getMethods": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns a list of available flickr API methods.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": False,
        "response": "<methods>\r\n\t<method>flickr.blogs.getList</method>\r\n\t<method>flickr.blogs.postPhoto</method>\r\n\t<method>flickr.contacts.getList</method>\r\n\t<method>flickr.contacts.getPublicList</method>\r\n</methods>",
        "name": "flickr.reflection.getMethods",
    },
    "flickr.blogs.getServices": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return a list of Flickr supported blogging services",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": False,
        "response": '<services>\r\n<service id="beta.blogger.com">Blogger</service>\r\n<service id="Typepad">Typepad</service>\r\n<service id="MovableType">Movable Type</service>\r\n<service id="LiveJournal">LiveJournal</service>\r\n<service id="MetaWeblogAPI">Wordpress</service>\r\n<service id="MetaWeblogAPI">MetaWeblogAPI</service>\r\n<service id="Manila">Manila</service>\r\n<service id="AtomAPI">AtomAPI</service>\r\n<service id="BloggerAPI">BloggerAPI</service>\r\n<service id="Vox">Vox</service>\r\n<service id="Twitter">Twitter</service>\r\n</services>',
        "name": "flickr.blogs.getServices",
    },
    "flickr.test.login": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "A testing method which checks if the caller is logged in then returns their username.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": True,
        "response": '<user id="12037949754@N01">\r\n\t<username>Bees</username> \r\n</user>\r\n',
        "name": "flickr.test.login",
    },
    "flickr.places.placesForBoundingBox": {
        "errors": [
            {
                "text": "One or more required parameter is missing from the API call.",
                "message": "Required parameters missing",
                "code": "1",
            },
            {
                "text": "The bbox argument was incomplete or incorrectly formatted",
                "message": "Not a valid bbox",
                "code": "2",
            },
            {
                "text": "An invalid place type was included with your request.",
                "message": "Not a valid place type",
                "code": "3",
            },
            {
                "text": "The bounding box passed along with your request was too large for the request place type.",
                "message": "Bounding box exceeds maximum allowable size for place type",
                "code": "4",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Return all the locations of a matching place type for a bounding box.<br /><br />\r\n\r\nThe maximum allowable size of a bounding box (the distance between the SW and NE corners) is governed by the place type you are requesting. Allowable sizes are as follows:\r\n\r\n<ul>\r\n<li><strong>neighbourhood</strong>: 3km (1.8mi)</li>\r\n<li><strong>locality</strong>: 7km (4.3mi)</li>\r\n<li><strong>county</strong>: 50km (31mi)</li>\r\n<li><strong>region</strong>: 200km (124mi)</li>\r\n<li><strong>country</strong>: 500km (310mi)</li>\r\n<li><strong>continent</strong>: 1500km (932mi)</li>\r\n</ul>",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "A comma-delimited list of 4 values defining the Bounding Box of the area that will be searched. The 4 values represent the bottom-left corner of the box and the top-right corner, minimum_longitude, minimum_latitude, maximum_longitude, maximum_latitude.",
                "optional": "0",
                "name": "bbox",
            },
            {
                "text": 'The name of place type to using as the starting point to search for places in a bounding box. Valid placetypes are:\r\n\r\n<ul>\r\n<li>neighbourhood</li>\r\n<li>locality</li>\r\n<li>county</li>\r\n<li>region</li>\r\n<li>country</li>\r\n<li>continent</li>\r\n</ul>\r\n<br />\r\n<span style="font-style:italic;">The "place_type" argument has been deprecated in favor of the "place_type_id" argument. It won\'t go away but it will not be added to new methods. A complete list of place type IDs is available using the <a href="http://www.flickr.com/services/api/flickr.places.getPlaceTypes.html">flickr.places.getPlaceTypes</a> method. (While optional, you must pass either a valid place type or place type ID.)</span>',
                "optional": "1",
                "name": "place_type",
            },
            {
                "text": 'The numeric ID for a specific place type to cluster photos by. <br /><br />\r\n\r\nValid place type IDs are :\r\n\r\n<ul>\r\n<li><strong>22</strong>: neighbourhood</li>\r\n<li><strong>7</strong>: locality</li>\r\n<li><strong>8</strong>: region</li>\r\n<li><strong>12</strong>: country</li>\r\n<li><strong>29</strong>: continent</li>\r\n</ul>\r\n<br /><span style="font-style:italic;">(While optional, you must pass either a valid place type or place type ID.)</span>\r\n',
                "optional": "1",
                "name": "place_type_id",
            },
            {
                "text": "Perform a recursive place type search. For example, if you search for neighbourhoods in a given bounding box but there are no results the method will also query for localities and so on until one or more valid places are found.<br /<br /> \r\nRecursive searches do not change the bounding box size restrictions for the initial place type passed to the method.",
                "optional": "1",
                "name": "recursive",
            },
        ],
        "needslogin": False,
        "response": '<places place_type="neighbourhood" total="21"\r\n   pages="1" page="1" \r\n   bbox="-122.42307100000001,37.773779,-122.381071,37.815779">\r\n   <place place_id=".aaSwYSbApnq6seyGw" woeid="23512025"\r\n      latitude="37.788" longitude="-122.412" \r\n      place_url="/United+States/California/San+Francisco/Downtown"\r\n      place_type="neighbourhood">\r\n      Downtown, San Francisco, CA, US, United States\r\n   </place>\r\n   <place place_id="3KymK1GbCZ41eBVBxg" woeid="28288707"\r\n      latitude="37.776" longitude="-122.417" \r\n      place_url="/United+States/California/San+Francisco/Civic+Center"\r\n      place_type="neighbourhood">\r\n      Civic Center, San Francisco, CA, US, United States\r\n   </place>\r\n   <place place_id="9xdhxY.bAptvBjHo" woeid="2379855"   \r\n      latitude="37.796" longitude="-122.407" \r\n      place_url="/United+States/California/San+Francisco/Chinatown"\r\n      place_type="neighbourhood">\r\n      Chinatown, San Francisco, CA, US, United States\r\n   </place>\r\n   <!-- and so on -->\r\n</places>',
        "name": "flickr.places.placesForBoundingBox",
    },
    "flickr.groups.leave": {
        "needssigning": True,
        "requiredperms": "delete",
        "errors": [
            {
                "text": "The group_id doesn't exist",
                "message": "Required arguments missing",
                "code": "1",
            },
            {
                "text": "The group by that ID does not exist",
                "message": "Group does not exist",
                "code": "2",
            },
            {
                "text": "The user is not a member of the group that was specified",
                "message": "Account is not in that group",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the Group to leave",
                "optional": "0",
                "name": "group_id",
            },
            {
                "text": "Delete all photos by this user from the group",
                "optional": "1",
                "name": "delete_photos",
            },
        ],
        "description": "Leave a group.\r\n\r\n<br /><br />If the user is the only administrator left, and there are other members, the oldest member will be promoted to administrator.\r\n\r\n<br /><br />If the user is the last person in the group, the group will be deleted.",
        "needslogin": True,
        "name": "flickr.groups.leave",
    },
    "flickr.galleries.getInfo": {
        "errors": [
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The gallery ID you are requesting information for.",
                "optional": "0",
                "name": "gallery_id",
            },
        ],
        "needslogin": False,
        "response": '<gallery id="6065-72157617483228192" url="http://www.flickr.com/photos/straup/galleries/72157617483228192" \r\nowner="35034348999@N01" \r\n         primary_photo_id="292882708" date_create="1241028772" date_update="1270111667" count_photos="17"\r\n count_videos="0" primary_photo_server="112" primary_photo_farm="1" primary_photo_secret="7f29861bc4">\r\n\t<title>Cat Pictures I\'ve Sent To Kevin Collins</title>\r\n\t<description />\r\n</gallery>',
        "name": "flickr.galleries.getInfo",
    },
    "flickr.photosets.reorderPhotos": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The photoset id passed was not a valid photoset id or did not belong to the calling user.",
                "message": "Photoset not found",
                "code": "1",
            },
            {
                "text": "One or more of the photo ids passed was not a valid photo id or does not belong to the calling user.",
                "message": "Photo not found",
                "code": "2",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photoset to reorder. The photoset must belong to the calling user.",
                "optional": "0",
                "name": "photoset_id",
            },
            {
                "text": "Ordered, comma-delimited list of photo ids. Photos that are not in the list will keep their original order",
                "optional": "0",
                "name": "photo_ids",
            },
        ],
        "description": "",
        "needslogin": True,
        "name": "flickr.photosets.reorderPhotos",
    },
    "flickr.stats.getPhotoStats": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The photo id was either invalid or was for a photo not owned by the calling user.",
                "message": "Photo not found",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get the number of views, comments and favorites on a photo for a given date.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format.\r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.",
                "optional": "0",
                "name": "date",
            },
            {
                "text": "The id of the photo to get stats for.",
                "optional": "0",
                "name": "photo_id",
            },
        ],
        "needslogin": True,
        "response": '<stats views="24" comments="4" favorites="1"/>',
        "name": "flickr.stats.getPhotoStats",
    },
    "flickr.prefs.getHidden": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns the default hidden preference for the user.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            }
        ],
        "needslogin": True,
        "response": '<rsp stat="ok">\r\n<person nsid="12037949754@N01" hidden="1" />\r\n</rsp>',
        "name": "flickr.prefs.getHidden",
    },
    "flickr.activity.userComments": {
        "errors": [
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns a list of recent activity on photos commented on by the calling user. <b>Do not poll this method more than once an hour</b>.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Number of items to return per page. If this argument is omitted, it defaults to 10. The maximum allowed value is 50.",
                "optional": "1",
                "name": "per_page",
            },
            {
                "text": "The page of results to return. If this argument is omitted, it defaults to 1.",
                "optional": "1",
                "name": "page",
            },
        ],
        "needslogin": True,
        "response": '<items>\r\n\t<item type="photoset" id="395" owner="12037949754@N01" \r\n\t\tprimary="6521" secret="5a3cc65d72" server="2" \r\n\t\tcomments="1" views="33" photos="7" more="0">\r\n\t\t<title>A set of photos</title>\r\n\t\t<activity>\r\n\t\t\t<event type="comment"\r\n\t\t\tuser="12037949754@N01" username="Bees"\r\n\t\t\tdateadded="1144086424">yay</event>\r\n\t\t</activity>\r\n\t</item>\r\n\r\n\t<item type="photo" id="10289" owner="12037949754@N01"\r\n\t\tsecret="34da0d3891" server="2" comments="1"\r\n\t\tnotes="0" views="47" faves="0" more="0">\r\n\t\t<title>A photo</title>\r\n\t\t<activity>\r\n\t\t\t<event type="comment"\r\n\t\t\tuser="12037949754@N01" username="Bees"\r\n\t\t\tdateadded="1133806604">test</event>\r\n\t\t\t<event type="note"\r\n\t\t\tuser="12037949754@N01" username="Bees"\r\n\t\t\tdateadded="1118785229">nice</event>\r\n\t\t</activity>\r\n\t</item>\r\n</items>',
        "name": "flickr.activity.userComments",
    },
    "flickr.photos.people.editCoords": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The NSID passed was not a valid user id.",
                "message": "Person not found",
                "code": "1",
            },
            {
                "text": "The photo id passed was not a valid photo id.",
                "message": "Photo not found",
                "code": "2",
            },
            {
                "text": "The calling user did not originally add this person to the photo, and is not the person in question.",
                "message": "User cannot edit that person in that photo",
                "code": "3",
            },
            {
                "text": "Not all of the co-ordinate parameters (person_x, person_y, person_w, person_h) were passed with valid values.",
                "message": "Some co-ordinate paramters were blank",
                "code": "4",
            },
            {
                "text": "None of the co-ordinate parameters were valid.",
                "message": "No co-ordinates given",
                "code": "5",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the photo to edit a person in.",
                "optional": "0",
                "name": "photo_id",
            },
            {
                "text": "The NSID of the person to edit in a photo.",
                "optional": "0",
                "name": "user_id",
            },
            {
                "text": "The left-most pixel co-ordinate of the box around the person.",
                "optional": "0",
                "name": "person_x",
            },
            {
                "text": "The top-most pixel co-ordinate of the box around the person.",
                "optional": "0",
                "name": "person_y",
            },
            {
                "text": "The width (in pixels) of the box around the person.",
                "optional": "0",
                "name": "person_w",
            },
            {
                "text": "The height (in pixels) of the box around the person.",
                "optional": "0",
                "name": "person_h",
            },
            {
                "text": "An email address for an 'invited' person in a photo",
                "optional": "1",
                "name": "email",
            },
        ],
        "description": "Edit the bounding box of an existing person on a photo.",
        "needslogin": True,
        "name": "flickr.photos.people.editCoords",
    },
    "flickr.photos.comments.editComment": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The requested comment is against a photo which no longer exists.",
                "message": "Photo not found.",
                "code": "1",
            },
            {
                "text": "The comment id passed was not a valid comment id",
                "message": "Comment not found.",
                "code": "2",
            },
            {
                "text": "Comment text can not be blank",
                "message": "Blank comment.",
                "code": "8",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the comment to edit.",
                "optional": "0",
                "name": "comment_id",
            },
            {
                "text": "Update the comment to this text.",
                "optional": "0",
                "name": "comment_text",
            },
        ],
        "description": "Edit the text of a comment as the currently authenticated user.",
        "needslogin": True,
        "name": "flickr.photos.comments.editComment",
    },
    "flickr.urls.getGroup": {
        "errors": [
            {
                "text": "The NSID specified was not a valid group.",
                "message": "Group not found",
                "code": "1",
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Returns the url to a group's page.",
        "needssigning": False,
        "requiredperms": "none",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The NSID of the group to fetch the url for.",
                "optional": "0",
                "name": "group_id",
            },
        ],
        "needslogin": False,
        "response": '<group nsid="48508120860@N01" url="http://www.flickr.com/groups/test1/" /> ',
        "name": "flickr.urls.getGroup",
    },
    "flickr.stats.getPhotostreamStats": {
        "errors": [
            {
                "text": "The user you have requested stats has not enabled stats on their account.",
                "message": "User does not have stats",
                "code": "1",
            },
            {
                "text": "No stats are available for the date requested. Flickr only keeps stats data for the last 28 days.",
                "message": "No stats for that date",
                "code": "2",
            },
            {
                "text": "The date provided could not be parsed",
                "message": "Invalid date",
                "code": "3",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "description": "Get the number of views on a user's photostream for a given date.",
        "needssigning": True,
        "requiredperms": "read",
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "Stats will be returned for this date. This should be in either be in YYYY-MM-DD or unix timestamp format.\r\n\r\nA day according to Flickr Stats starts at midnight GMT for all users, and timestamps will automatically be rounded down to the start of the day.",
                "optional": "0",
                "name": "date",
            },
        ],
        "needslogin": True,
        "response": '<stats views="24" />',
        "name": "flickr.stats.getPhotostreamStats",
    },
    "flickr.blogs.postPhoto": {
        "needssigning": True,
        "requiredperms": "write",
        "errors": [
            {
                "text": "The blog id was not the id of a blog belonging to the calling user",
                "message": "Blog not found",
                "code": "1",
            },
            {
                "text": "The photo id was not the id of a public photo",
                "message": "Photo not found",
                "code": "2",
            },
            {
                "text": "A password is not stored for the blog and one was not passed with the request",
                "message": "Password needed",
                "code": "3",
            },
            {
                "text": "The blog posting failed (a blogging API failure of some sort)",
                "message": "Blog post failed",
                "code": "4",
            },
            {
                "text": "The passed signature was invalid.",
                "message": "Invalid signature",
                "code": 96,
            },
            {
                "text": "The call required signing but no signature was sent.",
                "message": "Missing signature",
                "code": 97,
            },
            {
                "text": "The login details or auth token passed were invalid.",
                "message": "Login failed / Invalid auth token",
                "code": 98,
            },
            {
                "text": "The method requires user authentication but the user was not logged in, or the authenticated method call did not have the required permissions.",
                "message": "User not logged in / Insufficient permissions",
                "code": 99,
            },
            {
                "text": "The API key passed was not valid or has expired.",
                "message": "Invalid API Key",
                "code": 100,
            },
            {
                "text": "The requested service is temporarily unavailable.",
                "message": "Service currently unavailable",
                "code": 105,
            },
            {
                "text": "The requested response format was not found.",
                "message": 'Format "xxx" not found',
                "code": 111,
            },
            {
                "text": "The requested method was not found.",
                "message": 'Method "xxx" not found',
                "code": 112,
            },
            {
                "text": "The SOAP envelope send in the request could not be parsed.",
                "message": "Invalid SOAP envelope",
                "code": 114,
            },
            {
                "text": "The XML-RPC request document could not be parsed.",
                "message": "Invalid XML-RPC Method Call",
                "code": 115,
            },
            {
                "text": "One or more arguments contained a URL that has been used for abuse on Flickr.",
                "message": "Bad URL found",
                "code": 116,
            },
        ],
        "arguments": [
            {
                "text": 'Your API application key. <a href="/services/api/misc.api_keys.html">See here</a> for more details.',
                "optional": 0,
                "name": "api_key",
            },
            {
                "text": "The id of the blog to post to.",
                "optional": "1",
                "name": "blog_id",
            },
            {
                "text": "The id of the photo to blog",
                "optional": "0",
                "name": "photo_id",
            },
            {"text": "The blog post title", "optional": "0", "name": "title"},
            {"text": "The blog post body", "optional": "0", "name": "description"},
            {
                "text": "The password for the blog (used when the blog does not have a stored password).",
                "optional": "1",
                "name": "blog_password",
            },
            {
                "text": "A Flickr supported blogging service.  Instead of passing a blog id you can pass a service id and we'll post to the first blog of that service we find.",
                "optional": "1",
                "name": "service",
            },
        ],
        "description": "",
        "needslogin": True,
        "name": "flickr.blogs.postPhoto",
    },
}
