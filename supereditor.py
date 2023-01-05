'''SuperEditor is a text editor in Python made for CS50P Final Project'''

from tkinter import *
import tkinter as tk
import functions
from tkinter import font




class Editor():

    def __init__(self, window):
        # Window + Title
        window.geometry('1200x800')
        window.title('SuperEditor')

        # Scrool bar
        scrollbar = Scrollbar(window)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        # Selfs
        self.window = window
        self.scrollbar = scrollbar




    def format_bar(self):
        
        

        # Create font list
        font_list = []
        for f in font.families():
            font_list.append(f)
        value_font = tk.StringVar(self.window)
        value_font.set(font_list[5])
        font_menu = tk.OptionMenu(self.window, value_font, *font_list)
        font_menu.pack()

        self.value_font = value_font
    

        
    def text_area(self):
        
        #Func to change size
        def size_choice(e):
            user_font.config(size=e)
        #Func to change font
        def font_choice(e):
            user_font.config(family=e)

        # Create the sizes list
        size_list = ["2", "4", "8", "10", "12", "14", "16",
        "18", "20", "22", "24", "26", "28", "30", "32", "36"
        ,"40", "44", "48", "56", "64"]
        value_size = tk.StringVar(self.window)
        value_size.set(size_list[5])
        size_menu = tk.OptionMenu(self.window, value_size, *size_list,
        command = size_choice)
        size_menu.pack()

        # Create font list
        font_list = ["Roman", "Courier", "MS Serif", "MS Sans Serif", "Modern",
        "Terminal", "Arial", "Arial Baltic", "Courier New", "MS Gothic", "Times New Roman",
        "Tahoma", "Calibri", "Comic Sans MS", "Verdana"]
 
        value_font = tk.StringVar(self.window)
        value_font.set(font_list[0])
        font_menu = tk.OptionMenu(self.window, value_font, *font_list, command=font_choice)
        font_menu.pack()

        # TEXT AREA
        user_font = font.Font()
        editor = Text(self.window, width=200, height= 200,yscrollcommand=self.scrollbar.set, undo = True,
        font=user_font)
        editor.pack(fill=BOTH)
        self.scrollbar.config(command = editor.yview) 

        # Self assigment
        self.editor = editor
        
        # Ctrl+A
        editor.bind("<Control-A>",lambda event: functions.select_all(editor, event=event))


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
        formatmenu.add_command(label="Font...", command='TODO')
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
    # Text area with basic format
    editor.text_area()
    # Create menubar
    editor.menu_bar()
    # Rune the SuperEditor
    se_window.mainloop()



if __name__ == "__main__":
    main()




