'''SuperEditor is a text editor in Python made for CS50P Final Project'''

from tkinter import *
import tkinter as tk
import functions


# Create a SuperEditor window
se_window = Tk()

class Editor():
    def __init__(self, window):
        # Window + Title
        window.geometry('1200x800')
        window.title('SuperEditor')
        # Scrool bar
        scrollbar = Scrollbar(window)
        scrollbar.pack(side=RIGHT,fill=Y)
        # Text area
        editor = Text(window,width=400,height=450,yscrollcommand=scrollbar.set)
        editor.pack(fill=BOTH)
        scrollbar.config(command = editor.yview)

        # Selfs
        self.window = window
        self.editor = editor


    def menu_bar(self):
        menubar = Menu(self.window)
        #File Menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=lambda: functions.new_file(self.window, self.editor))
        filemenu.add_command(label="Open", command=lambda: functions.open_file(self.window, self.editor))
        filemenu.add_command(label="Save", command=lambda: functions.save_file(self.window,self.editor))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda: functions.exit(self.window,self.editor))
        menubar.add_cascade(label="File", menu=filemenu)
        # Edit menu
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command='TODO')
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command='TODO')
        editmenu.add_command(label="Copy", command='TODO')
        editmenu.add_command(label="Paste", command='TODO')
        editmenu.add_command(label="Delete", command='TODO')
        editmenu.add_separator()
        editmenu.add_command(label="Select All", command='TODO')
        menubar.add_cascade(label="Edit", menu=editmenu)
        # Format menu
        formatmenu = Menu(menubar, tearoff=0)
        formatmenu.add_command(label="Font", command='TODO')
        menubar.add_cascade(label="Format", menu=formatmenu)
        # View menu
        viewmenu = Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Statusbar", command='TODO')
        menubar.add_cascade(label="View", menu=viewmenu)
                # About menu
        aboutmenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label="Help", command='TODO')
        aboutmenu.add_command(label="About", command='TODO')
        menubar.add_cascade(label="About", menu=aboutmenu)
        
        # Add the menu bar
        self.window.config(menu=menubar)



 

def main():
    editor = Editor(se_window)
    editor.menu_bar()


    # Rune the SuperEditor
    se_window.mainloop()

if __name__ == "__main__":
    main()




