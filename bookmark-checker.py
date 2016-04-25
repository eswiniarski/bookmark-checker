import json
import requests
import sys
import os.path
#from pprint import pprint

def getInputFile():
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            return sys.argv[1];
        else:
            return False

directories = {}
jsonFile = getInputFile()

with open(jsonFile if jsonFile else 'chrome_bookmarks.json') as bookmarks_file:
        bookmarks = json.load(bookmarks_file)

        #build dictionary of directory names
        for bookmark in bookmarks :
                if not bookmark.has_key('url'):
                    directories[bookmark['id']] = bookmark['title']

        #check bookmarks
        for bookmark in bookmarks :
            if bookmark.has_key('url'):
                try:
                    response = requests.get(bookmark['url'], verify=False, timeout=10)
                    if response.status_code == 404 or response.status_code == 500:
                        print('[FAIL] %s : %s : %s' % (directories[bookmark['parentId']], bookmark['title'], bookmark['url']))
                except Exception, msg:
                    print('--Timeout-- %s' % bookmark['url'])
