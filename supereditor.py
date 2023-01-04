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




