"""
Project: Text Editor
Author: Hongjun Hu
Date: 2026-05-10
Description: A lightweight text editor built with Python and Tkinter 
             focusing on simplicity and ease of use.
"""

import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from tkinter import filedialog
import os
import sys

#code for pyinstaller
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

img_path = resource_path("logo.png")

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

#start building the window
root=ctk.CTk()
root.title("Text Editor")
root.geometry("800x600")
root.wm_iconbitmap(img_path)

#font type and size
FONTS = ["Arial", "Courier New", "Verdana", "Times New Roman", "Consolas"]
SIZES = ["10", "12", "14", "16", "20", "24", "32"]

#functions

def new_file():
    #delete the content in the text area, after asking the user whether to save them
    if messagebox.askyesno("confirm", "Are you sure you want to start a new file? The unsaved content will be deleted!!"):
        text_area.delete("1.0", tk.END)

    root.title("Text Editor")

def open_file():
    #let user choose file
    file_path = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    #delete the content in the text area and show the content in the file
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", content)
            root.title(f"{file_path} - Python Text Editor")

        #show the error
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}!!")


def save_file():
    #get the content in the text area
    content = text_area.get("1.0", tk.END)

    #let user enter the name of the file
    file_path = filedialog.asksaveasfilename(
        initialfile='Untitled.txt',
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
    )

    #save the file
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        root.title(f"{file_path} - text editor")

def change_font(*args):
    font = font_var.get()
    size = size_var.get()

    text_area.configure(font=(font, int(size)))

#show cut, copy and paste
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

def do_cut():
    text_area._textbox.event_generate("<<Cut>>")

def do_copy():
    text_area._textbox.event_generate("<<Copy>>")

def do_paste():
    text_area._textbox.event_generate("<<Paste>>")

#interface

#frame for menu
toolbar = ctk.CTkFrame(root, fg_color="#eeeeee") 
toolbar.pack(side="top", fill="x")

btn_new = ctk.CTkButton(toolbar, text="New File", width=100, command=new_file)
btn_new.pack(side="left", padx=2, pady=5)

btn_open = ctk.CTkButton(toolbar, text="Open File", width=100, command=open_file)
btn_open.pack(side="left", padx=2, pady=5)

btn_save = ctk.CTkButton(toolbar, text="Save", width=100, command=save_file)
btn_save.pack(side="left", padx=2, pady=5)

#font type and size settings
font_var = ctk.StringVar(root)
font_var.set("Arial")
font_dropdown = ctk.CTkOptionMenu(toolbar, values=FONTS, command=change_font, variable=font_var)
font_dropdown.pack(side="left", padx=5)

size_var = ctk.StringVar(root)
size_var.set("12")
size_dropdown = ctk.CTkOptionMenu(toolbar, values=SIZES, command=change_font, variable=size_var)
size_dropdown.pack(side="left", padx=5)

#text area
text_area = ctk.CTkTextbox(root, font=("Arial", 12))
text_area.pack(fill='both', expand=True)

#menu for right click
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Cut", command=do_cut)
context_menu.add_command(label="Copy", command=do_copy)
context_menu.add_command(label="Paste", command=do_paste)
context_menu.add_separator()
context_menu.add_command(label="Select All", command=lambda: text_area.tag_add("sel", "1.0", "end"))

text_area.bind("<Button-3>", show_context_menu)

root.mainloop()