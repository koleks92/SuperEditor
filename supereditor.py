'''SuperEditor is a text editor in Python made for CS50P Final Project'''

from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

# Create a SuperEditor window
se_window = Tk()

class Editor():
    def __init__(self, window):
        self.window = window

        # Window + Title
        window.geometry('1200x800')
        window.title('SuperEditor')
        # Scrool bar
        scrollbar = Scrollbar(window)
        scrollbar.pack(side=RIGHT,fill=Y)
        # Text area
        Editor = Text(window,width=400,height=450,yscrollcommand=scrollbar.set)
        Editor.pack(fill=BOTH)
        scrollbar.config(command = Editor.yview)

    def menu_bar(self):
        menubar = Menu(self.window)
        #File Menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command='donothing')
        filemenu.add_command(label="Open", command='donothing')
        filemenu.add_command(label="Save", command='donothing')
        filemenu.add_separator()
        filemenu.add_command(label="Exit", comman=self.window.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        # Edit menu
            # TODO
        # Format menu
            # TODO
        # View mnue
            # TODO
        # About menu
            # TODO
        
        # Add the menu bar
        self.window.config(menu=menubar)




  

def main():
    editor = Editor(se_window)
    editor.menu_bar()


    # Rune the SuperEditor
    se_window.mainloop()



if __name__ == "__main__":
    main()




