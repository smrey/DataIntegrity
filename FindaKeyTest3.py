import os
'''
This function proves that there are no duplicate keys when using this method for generating keys
'''

def fileList(highest_directory):
    file_list = []
    path_list = os.path.normpath(highest_directory).split(os.sep)
    ##print path_list
    path_stuff_to_remove = path_list[:-1]
    #run_id = path_list[-1]
    ##print path_stuff_to_remove

    for path, subdirs, files in os.walk(highest_directory):
        for name in files:
            name = [name]
            #print type(name)
            path_list = os.path.normpath(path).split(os.sep)
            #print path_list
            key_part = []
            for i in path_list:
                if i not in path_stuff_to_remove:
                    key_part.append(i)
            #print key_part
            #print type(key_part)
            key_whole = key_part + name
            #print os.path.join(key_part)
            #print os.path.join(key_part, name)
            #print key_whole
            key_id = tuple(key_whole)

            if key_id in file_list:
                print "Duplicate"
                raise Exception("Duplicate Entry")

            file_list.append(key_id)

    return file_list


folder_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160224_M02641_0082_000000000-ALPHF\\"
folder_h = "C:\\Users\\Sara\\Documents\\Before\\160520_M00766_0034_000000000-ANJEU\\"

print fileList(folder_h)