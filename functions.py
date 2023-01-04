import tkinter as tk
import tkinter.filedialog as fd

filetypes = [("Text Files", "*.txt"), ('All Files', '*.*')]

def save_file(window, text):
    '''Save file'''
    filename = fd.asksaveasfilename(defaultextension=".txt", filetypes=filetypes)
    if not filename:
        return
    else:
        with open(filename, "w") as output_file:
            text = text.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"SuperEditor - {filename}")

def new_file(window, text):
    '''New file'''
    if text.get(1.0, tk.END) != '':
        pass
    else:
        text.delete(1.0, tk.END)

def open_file(window, text):
    '''Open file'''
    filename = fd.askopenfilename(initialdir='/home/zbenik', filetypes=filetypes)
    with open(filename, "r") as input_file:
        read = input_file.read()
        text.insert(tk.END, read)
    window.title(f"SuperEditor - {filename}")
    text_file.close()

def file_not_empty(window, text):
    pass




        