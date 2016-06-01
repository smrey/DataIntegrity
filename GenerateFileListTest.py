#Generate a list of all files in an NGS folder
import sys,os

folder_h = "C:\\Users\\Admin\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160224_M02641_0082_000000000-ALPHF\\"

def fileList(highest_directory):
    file_list = []
    for path, subdirs, files in os.walk(highest_directory):
        for name in files:
            file_list.append(os.path.join(path, name))
    return file_list

print fileList(folder_h)

