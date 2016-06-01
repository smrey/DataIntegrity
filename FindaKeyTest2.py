import os

def fileList(highest_directory):
    file_list = []

    for path, subdirs, files in os.walk(highest_directory):
        #print path
        #print subdirs
        #print os.path.split(path)
        for name in files:
            #file_list.append(os.path.join(path, name))
            print path
            print os.path.split(path)
            print os.path.splitext(path)
            print name #Can this be used as a key for the dictionary (i.e. is it unique to each run?)- NO
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