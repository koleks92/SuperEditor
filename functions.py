from tkinter.filedialog import asksaveasfilename

def save_file(window, text):
    '''Save file'''
    filename = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ('All Files', '*.*')])
    if not filename:
        return
    else:
        with open(filename, "w") as output_file:
            text = text.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"SuperEditor - {filename}")

        