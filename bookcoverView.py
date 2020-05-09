#'''this is the view nd creates a tkinter window.'''
#import bookcontroller as bc
#from tkinter import *
#from PIL import ImageTk, Image

#class Window:
#    '''This class deals with the view and entire running.'''
#    def __init__(self):
        # we create the window
#        self.root = Tk()
#        self.root.geometry('500x200')
#        self.root.title('Cover Books')
#        DEFAULT_FONT = ('Comicsans', 16)
#        # we create a label
#        self.label = Label(self.root, text = 'Please Input ISBN code.',
#                           font = DEFAULT_FONT)
#        self.label.pack()
#        self.e = Entry(self.root, width = 25, font = DEFAULT_FONT)
#        self.e.pack()
#        self.e.focus_set()
        #we create a button
#        b = Button(self.root,text='search',font = DEFAULT_FONT,
#                   command= self.printtext)
#        b.pack(side='bottom')
        

#    def printtext(self):
#        '''We get the string input.'''
#        global e
#        string = self.e.get()
#        self.getImage(string) 

#    def run(self):
#        '''This runs the code.'''
#        self.root.mainloop()

#    def getImage(self,text):
#        '''We get the image with this.'''
#        t = bc.Functioning()
#        im1 = ImageTk.PhotoImage(Image.open(t.searchImage(text)))
#        panel = Label(self.root, image = im1)
#        panel.pack()
        
        

#if __name__ == '__main__':
#    search = Window()
#    search.run()

'''The code could not process the image it was getting. I found that
the problem was with printing the book cover to the tkinter window.
After a little reading and attempts, it is now successful.'''


'''This is the view and creates a tkinter window.'''
from tkinter import *
from PIL import ImageTk, Image

class Window():
    '''This class deals with the view and entire running.'''
    def __init__(self):
        pass
        
    def quit1(self):
        '''This method helps with quitting the program.'''
        self.root.destroy()
        self.string = 'quit'

    def printtext(self):
        '''We get the string input.'''
        global e
        # We get the user input here.
        self.string = self.e.get()
        self.root.destroy()

    def run(self):
        '''This runs the code.'''
        # we create the window
        self.root = Tk()
        self.root.geometry('500x200')
        self.root.title('Cover Books')
        DEFAULT_FONT = ('Comicsans', 16)
        # we create a label
        self.label = Label(self.root, text = 'Please Input ISBN code.',
                           font = DEFAULT_FONT)
        self.label.pack()
        self.e = Entry(self.root, width = 25, font = DEFAULT_FONT)
        self.e.pack()
        self.e.focus_set()
        #we create a button
        bq = Button(self.root, text='Quit', font=DEFAULT_FONT,
                    command=self.quit1)
        bq.pack(side='bottom')
        b = Button(self.root,text='Search & Print',font = DEFAULT_FONT,
                   command= self.printtext)
        b.pack(side='bottom')
        self.root.mainloop()

    def getImage(self,text):
        '''We get the image with this.'''
        # We get the image here
        im1 = Image.open(text)
        return im1
    
    def imme(self):
        '''This is an intermediate function which happens after the
        book cover is printed.'''
        self.master.destroy()
        self.run()

    def book_cover(self):
        '''This method prints the book cover image to the GUI screen
         window.'''
        self.master = Tk()
        self.master.geometry("700x700")
        DEFAULT_FONT = ('Comicsans', 14)
        path = "image.jpg"
        # We open the image
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(self.master, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        # We also have a main menu button
        b = Button(self.master,text='Go to main menu',font = DEFAULT_FONT,
                   command= self.imme)
        b.pack(side='bottom')
        self.master.mainloop()

