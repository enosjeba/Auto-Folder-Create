import os

project_name = str(input('Project Name :'))
number_of_folders = int(input('Enter Number of Folders you want :'))
folder_names = []

# def project_folder(project_name):
#     os.mkdir(f'./{project_name}/')
#     os.chdir(f'./{project_name}/')

#change working directory to project folder

# def create_folder(folder_name, number):
#     os.makedirs(f'./{folder_name}/')

if number_of_folders > 0:
    os.mkdir(f'./{project_name}/')
    os.chdir(f'./{project_name}')
    print(f'You are in {project_name} folder')
    while True:  
        a = len(folder_names)+1
        data = input(f'Enter Sub-Folder {a} Name ')
        folder_names.append(data)
        if len(folder_names) == number_of_folders:
            print("Number of Folders : ", len(folder_names))
            break
else:
    print("Check inputs")

for i in folder_names:
    os.mkdir(f'./{i}/')
    print(f'created folder {i}')