import flickr_api as f
import sys

try :
    username = sys.argv[1]
    try :
        access_token = sys.argv[2]
        f.set_auth_handler(access_token)
    except IndexError : pass
    
    u = f.Person.findByUserName(username)
    ps = u.getPhotosets()
    
    for i,p in enumerate(ps) :
        print i,p.title
except IndexError :
    print "usage: python show_albums.py username [access_token_file]"
    print "Displays the list of photosets belonging to a user"
