'''SuperEditor is a text editor in Python made for CS50P Final Project'''

from tkinter import *
import tkinter as tk
import functions


class Editor():
    def __init__(self, window):
        # Window + Title
        window.geometry('1200x800')
        window.title('SuperEditor')
        # Scrool bar
        scrollbar = Scrollbar(window)
        scrollbar.pack(side=RIGHT,fill=Y)
        # Text area
        editor = Text(window,width=400,height=450,yscrollcommand=scrollbar.set, undo = True)
        editor.pack(fill=BOTH)
        scrollbar.config(command = editor.yview)

        # Selfs
        self.window = window
        self.editor = editor

        editor.bind("<Control-A>", functions.select_all(editor))



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
        editmenu.add_command(label="Undo", command=self.editor.edit_undo)
        editmenu.add_command(label="Redo", command=self.editor.edit_redo)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=lambda: functions.cut(self.editor), accelerator='Ctrl-X')
        editmenu.add_command(label="Copy", command=lambda: functions.copy(self.editor), accelerator='Ctrl-C')
        editmenu.add_command(label="Paste", command=lambda: functions.paste(self.editor), accelerator='Ctrl-V')
        editmenu.add_command(label="Delete", command=lambda: functions.delete(self.editor))
        editmenu.add_separator()
        editmenu.add_command(label="Select All", command=lambda: functions.select_all(self.editor), accelerator='Ctrl-A')
        menubar.add_cascade(label="Edit", menu=editmenu)
        # Format menu
        formatmenu = Menu(menubar, tearoff=0)
        formatmenu.add_command(label="Font", command=lambda: functions.font_size(self.editor))
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
    # Create a SuperEditor window
    se_window = Tk()
    # Create a text editor
    editor = Editor(se_window)
    # Create menubar
    editor.menu_bar()
    # Rune the SuperEditor
    se_window.mainloop()


if __name__ == "__main__":
    main()




