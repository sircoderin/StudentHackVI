'''
Log in to spotify.
Run this program with python.
A browser should open. Copy the URL in browser window and paste it in the
terminal window.
'''

import sys
import spotipy
import spotipy.util as util

if(len(sys.argv)==2):
    scope = sys.argv[1]
else:
    print("Usage: token_gen.py scope")
    sys.exit()

#set up login credentials
CODRIN_CLIENT_ID = '4616f84bd6c344d49c4d49712de27d1d'
CODRIN_CLIENT_SECRET = '78fd807f7f06423b9d51f1e1fb4b8df3'

token = util.prompt_for_user_token('',scope,client_id=CODRIN_CLIENT_ID,client_secret=CODRIN_CLIENT_SECRET,redirect_uri='http://localhost:8181/')






out_file = open("token.txt","w")
out_file.write(token)
print("Token outputed to file token.txt")
