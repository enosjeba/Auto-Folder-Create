import os

def ProjectName():
    project_name = str(input('Project Name :'))
    return project_name

def mainfolder(project_name):
    os.mkdir(f'./{project_name}/')
    os.chdir(f'./{project_name}')
    print(f'You are in {project_name} folder')

def subfolder(folder_list):
    for i in folder_list:
        os.mkdir(f'./{i}/')
        print(f'created folder {i}')

folders = ['hey', 'tHIS', 'wORKS']

proj = ProjectName()
rootdir = mainfolder(project_name=proj)
sub = subfolder(folders)