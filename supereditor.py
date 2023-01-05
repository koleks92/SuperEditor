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

        format_frame = Frame(self.window, height = 30)
        format_frame.pack( side = TOP )
        
        #Func to change size
        def size_choice(e):
            new_size = font.Font(size=e)
            editor.tag_configure("size", font=new_size)
            current_tags = editor.tag_names("sel.first")
            editor.tag_add("size", "sel.first", "sel.last")            
        #Func to change font
        def font_choice(e):
            user_font.config(family=e)

        #Func to make text bold
        def bolder():
            bold_font = font.Font(editor, editor.cget("font"))
            bold_font.configure(weight="bold")

            editor.tag_configure("bold", font=bold_font)

            current_tags = editor.tag_names("sel.first")

            if "bold" in current_tags:
                editor.tag_remove("bold", "sel.first", "sel.last")
            else:
                editor.tag_add("bold", "sel.first", "sel.last")

        #Func to make text italic
        def italicer():
            italic_font = font.Font(editor, editor.cget("font"))
            italic_font.configure(slant="italic")

            editor.tag_configure("italic", font=italic_font)

            current_tags = editor.tag_names("sel.first")

            if "italic" in current_tags:
                editor.tag_remove("italic", "sel.first", "sel.last")
            else:
                editor.tag_add("italic", "sel.first", "sel.last")


        # Create the sizes list
        size_list = ["2", "4", "8", "10", "12", "14", "16",
        "18", "20", "22", "24", "26", "28", "30", "32", "36"
        ,"40", "44", "48", "56", "64"]
        value_size = tk.StringVar(format_frame)
        value_size.set(size_list[5])
        size_menu = tk.OptionMenu(format_frame, value_size, *size_list,
        command = size_choice)
        size_menu.pack(side="left")

        # Create font list
        font_list = ["Roman", "Courier", "MS Serif", "MS Sans Serif", "Modern",
        "Terminal", "Arial", "Arial Baltic", "Courier New", "MS Gothic", "Times New Roman",
        "Tahoma", "Calibri", "Comic Sans MS", "Verdana"]
 
        value_font = tk.StringVar(format_frame)
        value_font.set(font_list[0])
        font_menu = tk.OptionMenu(format_frame, value_font, *font_list, command=font_choice)
        font_menu.pack(side = "left")

        #Bold func
        bold_button = Button(format_frame, text="Bold", command = bolder)
        bold_button.pack(side="left")

        #Italic func
        italic_button = Button(format_frame, text="Italic", command = italicer)
        italic_button.pack(side="left")


        # TEXT AREA
        user_font = font.Font()
        editor = Text(self.window, width=200, height= 200,yscrollcommand=self.scrollbar.set, undo = True,
        font=user_font)
        editor.pack(fill=BOTH)
        self.scrollbar.config(command = editor.yview) 

        # Self assigment
        self.editor = editor
        
        # Ctrl+A
        editor.bind("<Control-a>",lambda event: functions.select_all(editor, event=event))
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




