# Import needed libraries
from os import makedirs
from os import listdir
from os.path import isfile, join

# Get a list of files from a directory
folder_path = r'C:\hysplit4\working'
file_list = [files for files in listdir(folder_path) if isfile(join(folder_path, files))]

# Create .txt file
fdump_file = open(r'C:\Users\mxmmc\Desktop\fdump_files.txt', 'w+')
                   
# Output .txt file of desired files from a directory
for files in file_list:
    if 'fdump' in files:
        fdump_file.write(folder_path + '\\' + files + '\n')
fdump_file.close()
        
