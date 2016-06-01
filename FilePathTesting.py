import os

def getRelativePath(highest_directory):
    '''
    print highest_directory
    #Need to normalise paths before string splitting
    print os.path.normpath(highest_directory)
    #print os.path.abspath(highest_directory)
    drive, path_and_file = os.path.splitdrive(os.path.normpath(highest_directory))
    print drive
    print path_and_file
    path, file = os.path.split(path_and_file)
    print path
    print file
    '''

    path_list = os.path.normpath(highest_directory).split(os.sep)
    print path_list
    path_stuff_to_remove = path_list[:-1]
    run_id = path_list[-1]
    print path_stuff_to_remove

    key_part = []
    for i in path_list:
        if i not in path_stuff_to_remove:
            key_part.append(i)
    return key_part



folder_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160224_M02641_0082_000000000-ALPHF\\"
#folder_h = "C:\\Users\\Sara\\Documents\\Before\\160520_M00766_0034_000000000-ANJEU\\"

test_dir = "C:\\Users\\Sara\\Documents\\Before\\160520_M00766_0034_000000000-ANJEU\\Data\\Intensities\\"
print getRelativePath(folder_h)