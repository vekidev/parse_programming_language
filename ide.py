import tkinter as tk
from tkinter import *
import tkinter.filedialog
import TKlighter

def new_file():
    txt.delete('1.0',END)

def open_file():
    filepath = tkinter.filedialog.askopenfilename(filetypes= (("ParseScript Files","*.ps"),("All files","*.*")))
    file = open(filepath, 'r')
    txt.delete('1.0',END)
    txt.insert('1.0', file.read())
    file.close()

def save_file():
    file = tkinter.filedialog.asksaveasfile(defaultextension='.ps',
                                    filetypes=[
                                        ("Text file",".ps")
                                    ])
    if file is None:
        return
    filetext = str(txt.get(1.0,END))
    file.write(filetext)
    file.close()

root = tk.Tk()

menubar = Menu(root)
root.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New File            ", command = new_file)
fileMenu.add_command(label="Save as...          ", command = save_file)
fileMenu.add_command(label="Load                ", command = open_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit                ", command = exit)
txt = tk.Text(root, bg='black', insertbackground="white", fg="white",padx=10,pady=10,font=("Courier New",20))
txt.pack(fill=BOTH, expand=YES)

default_commands = ["print", "print_ret", "input", "input_int", "clear", "cls", "is_num", "is_str", "is_func", "str", "int", "float", "append", "pop", "extend", "sqrt", "cbrt", "fact", "random_int", "random_str", "degrees", "stop", "len"]
default_variables = ["true", "false", "pi", "null", "none"]
digits = '0123456789'

def light(event):
    for command in default_commands:
        TKlighter.custom_h(txt, command, '#cc20e3')
    for var in default_variables:
        TKlighter.custom_h(txt, var, '#20b2e3')
    for digit in digits:
        TKlighter.custom_chars_h(txt, digit, "#0f49a6")
    TKlighter.custom_h(txt, 'func', '#e3841e')
    TKlighter.custom_h(txt, 'run', '#e3841e')
    TKlighter.custom_h(txt, 'define', '#e3841e')
    TKlighter.custom_h(txt, 'while', '#e3841e')
    TKlighter.custom_h(txt, 'return', '#e3841e')
    TKlighter.custom_h(txt, 'continue', '#e3841e')
    TKlighter.custom_h(txt, 'break', '#e3841e')
    TKlighter.custom_h(txt, 'var', '#e3841e')
    TKlighter.custom_h(txt, 'if', '#e6241e')
    TKlighter.custom_h(txt, 'elif', '#e6241e')
    TKlighter.custom_h(txt, 'else', '#e6241e')
    TKlighter.custom_h(txt, 'for', '#e6241e')
    TKlighter.custom_h(txt, 'to', '#e6241e')
    TKlighter.custom_h(txt, 'step', '#e6241e')
    TKlighter.custom_h(txt, 'then', '#e6241e')
    TKlighter.custom_h(txt, 'end', '#e6241e')
    TKlighter.custom_regex_h(txt, r'"\w+"', "#16a82e")
    TKlighter.custom_regex_h(txt, r'"', "#16a82e")
    TKlighter.custom_regex_h(txt, r'#\w+', "gray")
    TKlighter.custom_regex_h(txt, r'#', "gray")
    TKlighter.custom_chars_h(txt, '"', "#16a82e")

txt.bind('<Key>', light)

root.geometry("720x480")
root.title("Parse IDE")

root.mainloop()
