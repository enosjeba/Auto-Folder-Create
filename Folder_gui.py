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

if number_of_folders.get() > 0:
    os.mkdir(f'./{project_name_inp.get()}/')
    os.chdir(f'./{project_name_inp.get()}')
    print(f'You are in {project_name_inp} folder')
    while True:
        a = len(folder_names)+1
        data = input(f'Enter Sub-Folder {a} Name ')
        folder_names.append(data)
        if len(folder_names) == number_of_folders:
            print("Number of Folders : ", len(folder_names))
            print(folder_names)
            break
else:
    print("Check inputs")

for i in folder_names:
    os.mkdir(f'./{i}/')
    print(f'created folder {i}')

root.mainloop()