import os

def fileList(highest_directory):
    file_list = []
    print os.walk(highest_directory)
    #print os.stat(highest_directory)
    base_dir = os.path.dirname(highest_directory)
    print highest_directory
    print base_dir
    print os.path.relpath(highest_directory, test_dir)
    print os.path.normpath(highest_directory) # Doesn't seem to do anything useful- actually this is useful. Normalises the way of describing the delimiters removing edge cases
    print os.path.split(highest_directory)

    '''
    for path, subdirs, files in os.walk(highest_directory):
        print path
        print subdirs
    '''
    '''
        for name in files:
            #file_list.append(os.path.join(path, name))
            print path
            print name #Can this be used as a key for the dictionary (i.e. is it unique to each run?)- NO
    '''
    '''
            if name in file_list:
                print "Duplicate"
                break
    '''
            #file_list.append(name)

    #return file_list

folder_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160224_M02641_0082_000000000-ALPHF\\"
folder_h = "C:\\Users\\Sara\\Documents\\Before\\160520_M00766_0034_000000000-ANJEU\\"

test_dir = "C:\\Users\\Sara\\Documents\\Before\\160520_M00766_0034_000000000-ANJEU\\Data\\Intensities\\"
print fileList(folder_h)