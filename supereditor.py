'''SuperEditor is a text editor in Python made for CS50P Final Project'''

from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename



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
        filemenu.add_command(label="New", command='donothing')
        filemenu.add_command(label="Open", command='donothing')
        filemenu.add_command(label="Save", command=lambda: save_file(self.window,self.editor))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.window.quit)
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

def save_file(window, text):
    filename = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ('All Files', '*.*')])
    if not filename:
        return
    else:
        with open(filename, "w") as output_file:
            text = text.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"SuperEditor - {filename}")

        





if __name__ == "__main__":
    main()




