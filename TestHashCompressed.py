'''
This will not work unless it is the same archive.
The hash of the archived file, whether a .tar, .zip etc. appears to be context dependent,
as  well as time dependent, so if created first in the script it is repeatable but if created
later on in the script gives a different hash *shrugs
'''

import os,shutil,hashlib, zipfile
import time

oupt_file = "C:\\Users\\Sara\\Documents\\test"
#"bztar", extension=".tar.bz2"

''' commented out in case it was shutil causing the issues, but same issues seen with zipfile
def archiveFolder(inp_folder, archive_format="zip", extension=".zip"):
    inp_folder = os.path.normpath(inp_folder)
    #with zipfile.ZipFile(inp_folder, 'r') as archive_file:
        #archive_file.write(oupt_file)
    ##might want to put a check file exists in here (shutil module?)
    shutil.make_archive(oupt_file, format=archive_format, root_dir=inp_folder)
    return (oupt_file + extension)
'''
def archiveFolder(inp_folder, archive_format="zip", extension=".zip"):
    inp_folder = os.path.normpath(inp_folder)
    with zipfile.ZipFile(oupt_file+extension, 'w') as archive_file:
        archive_file.write(inp_folder)
    return (oupt_file + extension)

def hashing(inp_file, hash_algo=hashlib.sha256(), blocks_to_load=65536):
    with open(inp_file, "rb") as fl:
        for chunk in iter(lambda: fl.read(blocks_to_load), b""):
            hash_algo.update(chunk)
    return hash_algo #.hexdigest()

## Folder before transfer
folder_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160224_M02641_0082_000000000-ALPHF\\"
#folder_h = "C:\\Users\Sara\\Documents\Before\\160520_M00766_0034_000000000-ANJEU\\"

## Folder after transfer
#folder2_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160224_M02641_0082_000000000-ALPHF\\"
#folder2_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160224_M02641_0082_000000000-ALPHF - Copy\\" #Deleted a file in this one for testing
#folder2_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160224_M02641_0082_000000000-ALPHF - Copy (2)\\"
folder2_h = "C:\\Users\\Sara\\Documents\\160224_M02641_0082_000000000-ALPHF\\"
#folder2_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160225_M00766_0013_000000000-AL5YL\\"

'''
result_before = archiveFolder(folder_h)
hash_before = hashing(result_before)
hash_before_2 = hashing(result_before)
#os.remove(oupt_file + ".tar.bz2")
print hash_before
print hash_before_2

print hash_before.hexdigest()
print hash_before_2.hexdigest()

os.remove(oupt_file + ".zip")
'''

result_before_3 = archiveFolder(folder_h)
hash_before_3 = hashing(result_before_3)
print hash_before_3
print hash_before_3.hexdigest()

os.remove(oupt_file + ".zip")


result_after = archiveFolder(folder2_h)
hash_after = hashing(result_after)
print hash_after
print hash_after.hexdigest()

os.remove(oupt_file + ".zip")

