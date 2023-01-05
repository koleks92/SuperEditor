import tkinter as tk
import tkinter.filedialog as fd

filetypes = [("Text Files", "*.txt"), ('All Files', '*.*')]

'''File menu'''

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
    if len(text.get("1.0", "end-1c")) != 0:
        file_not_empty(window, text)
    
    text.delete(1.0, tk.END)

def open_file(window, text):
    '''Open file'''
    if len(text.get("1.0", "end-1c")) != 0:
        file_not_empty(window, text)
    try:
        filename = fd.askopenfilename(initialdir='/home/zbenik', filetypes=filetypes)
        text.delete(1.0, tk.END)
        with open(filename, "r") as input_file:
            read = input_file.read()
            text.insert(tk.END, read)
        window.title(f"SuperEditor - {filename}")
    except:
        pass

def exit(window, text):
    msg_box = tk.messagebox.askquestion('Save me!',
    'Do you want to save current file before you exit SuperEditor?',
    icon='warning')
    if msg_box == 'yes':
        save_file(window, text)        
    else:
        window.quit()
    

def file_not_empty(window, text):
    msg_box = tk.messagebox.askquestion('Save me!', 'Do you want to save current file before opening a new file?',
                                        icon='warning')
    if msg_box == 'yes':
        save_file(window, text)        
    else:
        pass

'''Edit Menu'''

def undo(text):
    pass

def cut(text):
    global data 
    if text.selection_get():
        data = text.selection_get()
        text.delete('sel.first','sel.last')

def copy(text):
    global data
    if text.selection_get():
        data = text.selection_get()

def paste(text):
    global data
    text.insert(tk.END, data)

def delete(text):
    if text.selection_get():
        text.delete('sel.first','sel.last')

def select_all(text):
    '''Select all text'''
    text.tag_add("sel", "1.0","end")
    text.tag_config("sel",background="gray",foreground="white")






        