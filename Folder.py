import os

project_name = str(input('Project Name :'))
number_of_folders = int(input('Enter Number of Folders you want :'))
folder_names = []

# def project_folder(project_name):
#     os.mkdir(f'./{project_name}/')
#     os.chdir(f'./{project_name}/')

#change working director
else:
    print("Check inputs")

for i in folder_names:
    os.mkdir(f'./{i}/')
    print(f'created folder {i}')