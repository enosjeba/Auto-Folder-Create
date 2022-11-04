from tkinter import *

root = Tk()

# fg="color name"
# bg="color name"

title = Label(root, text="Folder Bag")
title.pack()

sub_title = Label(root, text="Start Your project")
sub_title.pack()

#Entry
project_name_inp = Entry(root)
project_name_inp.insert(0,"Enter Project Name")
project_name_inp.pack()

#Input Data
def inputs():
    project_name = project_name_inp.get()
    project_name_prnt = Label(root, text=project_name+ " created")
    project_name_prnt.pack()

#Button
# Additional Options
# command=function
btn_create = Button(root, text="Create Project", command=inputs)
btn_create.pack()


root.mainloop()