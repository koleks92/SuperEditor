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

    def text_area(self):

        # Create frame for format buttons/lists
        format_frame = Frame(self.window, height = 30)
        format_frame.pack( side = TOP )
                

        #Func to make text bold
        def bolder(event):
            current_tags = editor.tag_names("sel.first")

            if "bold" in current_tags:
                editor.tag_remove("bold", "sel.first", "sel.last")
            else:
                editor.tag_add("bold", "sel.first", "sel.last")
                bold_font = font.Font(editor, editor.cget("font"))
                bold_font.configure(weight="bold")
                editor.tag_configure("bold", font=bold_font)

        #Func to make text italic
        def italicer():
            current_tags = editor.tag_names("sel.first")

            if "italic" in current_tags:
                editor.tag_remove("italic", "sel.first", "sel.last")
            else:
                editor.tag_add("italic", "sel.first", "sel.last")
                italic_font = font.Font(editor, editor.cget("font"))
                italic_font.configure(slant="italic")
                editor.tag_configure("italic", font=italic_font)

        # Func to underline the text
        def underliner():
            current_tags = editor.tag_names("sel.first")

            if "underline" in current_tags:
                editor.tag_remove("underline", "sel.first", "sel.last")
            else:
                editor.tag_add("underline", "sel.first", "sel.last")
                under_font = font.Font(editor, editor.cget("font"))
                under_font.configure(underline=True)
                editor.tag_configure("underline", font=under_font)
         

        # Func to overstrike the text
        def overstriker():
            over_font = font.Font(editor, editor.cget("font"))
            over_font.configure(overstrike=True)

            editor.tag_configure("overstrike", font=over_font)

            current_tags = editor.tag_names("sel.first")

            if "overstrike" in current_tags:
                editor.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                editor.tag_add("overstrike", "sel.first", "sel.last")
       

        #Bold func
        bold_button = Button(format_frame, text="Bold", command = bolder)
        bold_button.pack(side="left")

        #Italic func
        italic_button = Button(format_frame, text="Italic", command = italicer)
        italic_button.pack(side="left")

        #Underline_func
        under_button = Button(format_frame, text="Underline", command = underliner)
        under_button.pack(side="left")

        #Overstrike_func
        over_button = Button(format_frame, text="Overstrike", command= overstriker)
        over_button.pack(side="left")


        # TEXT AREA
        user_font = font.Font()
        editor = Text(self.window, width=200, height= 200,yscrollcommand=self.scrollbar.set, undo = True,
        font=user_font)
        editor.pack(fill=BOTH)
        self.scrollbar.config(command = editor.yview) 

        # Self assigment
        self.editor = editor
        self.user_font = user_font
        
        # BInds
        editor.bind_all("<Control-a>",lambda event: functions.select_all(editor, event=event))


    def menu_bar(self):
        menubar = Menu(self.window)
        
        #Font family subemnu
        font_menu = Menu(menubar, tearoff=0)
        font_list = ["Roman", "Courier", "MS Serif", "MS Sans Serif", "Modern",
        "Terminal", "Arial", "Arial Baltic", "Courier New", "MS Gothic", "Times New Roman",
        "Tahoma", "Calibri", "Comic Sans MS", "Verdana"]
        for font in font_list:
            font_menu.add_command(label=font, command = lambda font=font: self.user_font.config(family=font))
        
        #Font size submenu
        size_menu = Menu(menubar, tearoff=0)
        for size in range(1,33):
            size_menu.add_command(label=str(size), command = lambda size=size: self.user_font.config(size=size))
        
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
        editmenu.add_command(label="Undo", command=self.editor.edit_undo, accelerator="Ctrl+Z")
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
        formatmenu.add_cascade(label="Font", menu=font_menu)
        formatmenu.add_cascade(label="Size", menu=size_menu)
        formatmenu.add_command(label="Background color", command=lambda: functions.self.bg_color(self.editor))
        formatmenu.add_command(label="Font color", command= lambda: functions.text_color(self.editor))
        menubar.add_cascade(label="Format", menu=formatmenu)
        # View menu
        viewmenu = Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Fullscreen", command = lambda: functions.fullscreen(self.window))
        menubar.add_cascade(label="View", menu=viewmenu)
        # About menu
        aboutmenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label="Help", command=lambda: functions.help(self.window))
        aboutmenu.add_command(label="About", command=lambda: functions.about(self.window))
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




