#import bookcover as b

#class Functioning:

#    def __init__(self):
#        pass

#    def searchImage(self, txt):
#        '''We perform model search from here.'''
#        u = b.Books()
#        return u.imageSearch(txt)

'''The code could not process the image it was getting. I found that
the problem was with printing the book cover to the tkinter window.
After a little reading and attempts, it is now successful.'''

# needs PIL and requests to run
'''This is the controller file. it is and intermediary between the model
and the view.'''
import bookcovermodel as b
import bookcoverView as bv


class Functioning:
    '''This class deals with connection with model and view.'''
    def __init__(self):
        # We initiate the class
        self.x = bv.Window()

    def searchImage(self, txt):
        '''We perform model search from here.'''
        u = b.Books()
        # We call the model
        return u.imageSearch(txt)

    def run(self):
        '''We handle running the code frorm here.'''
        h = self.x.run()
        string = self.x.string
        # We search when the user click on search on the GUI
        while string != 'quit':
            t = self.searchImage(string)
            # We get the image
            self.x.getImage(t)
            # We print out the image on the GUI screen
            self.x.book_cover()
            string = self.x.string


if __name__ == '__main__':
    r = Functioning()
    # Function runs
    r.run()
                         

