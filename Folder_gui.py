from tkinter import *
import os

root = Tk()

title = Label(root, text="Folder Bag")
title.pack()

#Entry
project_name_inp = Entry(root)
project_name_inp.insert(0,"Enter Project Name")
project_name_inp.pack()

#Entry 
number_of_folders = Entry(root)
number_of_folders.insert(0,"Enter your ")
number_of_folders.pack()

folder_names = []

def project_name():
    project_name = project_name_inp.get()
    return

else:
    print("Check inputs")

for i in folder_names:
    os.mkdir(f'./{i}/')
    print(f'created folder {i}')

root.mainloop()