# # tkinter module of the library
# # GUI (graphical user interface) module of the library
# import tkinter as tk

# from tkinter import filedialog,messagebox # submodule of the library
# # main window code
# root =tk.Tk()
# root.title("Simple Text Editor")
# root.geometry("800x600")

# #create text area # tk.wrap is used to wrap the text as full ediotor

# text= tk.Text(
#     root,
#     wrap=tk.WORD,
#     font=("Arial", 12)

# ) 

# text.pack(expand=True,fill=tk.BOTH)

# #Main logic starts now

# #funcation 1 to create a new file
# def new_file():
#     text.delete(1.0,tk.END)
# #functaion 2 to open a new file

# def open_file():
#     file_path = filedialog.askopenfilename(
#     defaultextension=".txt",
#     filetypes=[("Text files","*.txt")]
#     )

#     if file_path:
#         #open file
#         with open(file_path,"r")as file:
#             #clear the old text
#             text.delete(1.0,tk.END)
#             text.insert(tk.End,file.read())
# #function 3 to save the file

# def save_file():
#     file_path= filedialog.asksaveasfilename(
#     defaultextension=".txt",
#     filetypes=[("Text files","*.txt")]
#     )
#     if file_path:
#         with open(file_path,"w") as file:
#             file.write(text.get(1.0,tk.END))

#     messagebox .showinfo("info","your file saved sucessfully!")

# #Menu bar code starts here    
# menu = tk.Menu(root)
# root.config(menu=menu)

# file_menu=tk.Menu(menu)

# #new ,openfile ,save text

# # add file meu to menu bar
# menu.add_command(label="File",menu=file_menu)
# file_menu.add_command(label="New",command=new_file)
# file_menu.add_command(label="open",command=open_file)
# file_menu.add_command(label="Save",command=save_file)
# file_menu.add_separator()
# file_menu.add_command(label="Exit",command=root.exit)








# it starts  the keep the window ediotor running

# root.mainloop()
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Tech-Ardpi32 private notepad")
root.geometry("800x600")

text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Arial", 12)
)

text.pack(expand=True, fill=tk.BOTH)

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )

    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

        messagebox.showinfo("Info", "Your file saved successfully!")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)

menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

file_menu.add_separator()

file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
