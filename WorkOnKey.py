import sys, os, hashlib

def fileList(highest_directory):
    file_list = []
    for path, subdirs, files in os.walk(highest_directory):
        for name in files:
            file_list.append(os.path.join(path, name))
    return file_list

def nameList(highest_directory):
    name_list = []
    for path, subdirs, files in os.walk(highest_directory):
        for name in files:
            name_list.append(name)
            #print name  # Can this be used as a key for the dictionary (i.e. is it unique to each run?)
    return name_list


def hashing(inp_file, hash_algo, blocks_to_load=65536):
    with open(inp_file, "rb") as fl:
        for chunk in iter(lambda: fl.read(blocks_to_load), b""):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()


folder_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160224_M02641_0082_000000000-ALPHF\\"

hashdict = {}
names = nameList(folder_h)
for i, file_name in enumerate(fileList(folder_h)):
    hashdict.update({names[i]:hashing(file_name, hashlib.sha256())})
print hashdict
