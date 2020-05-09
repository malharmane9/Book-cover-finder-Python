#import urllib.request
#import urllib.parse
#import json
#base url
#BASEurl = 'http://covers.openlibrary.org/b/isbn/'
#class Books:
    
#    def __init__(self):
#        pass

#    def imageSearch(self,text):
#        #we search the image
#        url = BASEurl + text + '-M.jpg'
#        x = urllib.request.urlopen(url)
#        return url
'''The code could not process the image it was getting. I found that
the problem was with printing the book cover to the tkinter window.
After a little reading and attempts, it is now successful.'''

'''This is the model for the bookcover API.'''
import urllib.request
import urllib.parse
from io import BytesIO
import requests
#base url
BASEurl = 'http://covers.openlibrary.org/b/isbn/'
class Books:
    '''This class deals like the backbone of the program. It deal with the
    processing data.'''
    def __init__(self):
        pass

    def imageSearch(self,text):
        # We search the image
        url = BASEurl + text + '-L.jpg'
        # we open the image in the same folder as the code
        with open('image.jpg', 'wb') as handle:
            resp = requests.get(url, stream=True)
            if not resp.ok:
                print(resp)

            for block in resp.iter_content(1024):
                if not block:
                    break
                handle.write(block)
        x = urllib.request.urlopen(url)
        myimage = x.read()
        # We decode the code
        myimage = BytesIO(myimage)
        # We return the image data
        return myimage
