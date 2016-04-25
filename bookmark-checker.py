import json #import json librrary
from pprint import pprint #import pprint (cool tool for dump) form pprint linbrary
import requests
#import signal
import sys
import os.path

#def signal_handler(signum, frame):
#    raise Exception("Timed out!")

def getArg():
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            return sys.argv[1];
        else:
            return False

directories = {}

# with open('chrome_bookmarks.json') as bookmarks_file:
jsonFile = getArg()
# signal.signal(signal.SIGALRM, signal_handler)
#signal.alarm(5) #5s timeout
with open(jsonFile if jsonFile else 'chrome_bookmarks.json') as bookmarks_file:
        bookmarks = json.load(bookmarks_file)

        for bookmark in bookmarks :
                if not bookmark.has_key('url'):
                    directories[bookmark['id']] = bookmark['title']

        for bookmark in bookmarks :
            if bookmark.has_key('url'):
                try:
                    r = requests.get(bookmark['url'], verify=False, timeout=10)
                    if r.status_code == 404 or r.status_code == 500:
                        print('[NOPE] ' + directories[bookmark['parentId']] + ' : '  + bookmark['title'] + ' : ' + bookmark['url'])
                except Exception, msg:
                    print "--Timeout--"
                    print(bookmark['url'])
