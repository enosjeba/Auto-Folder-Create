
number_of_folders.pack()

folder_names = []

def project_name():
    project_name = project_name_inp.get()
    return

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