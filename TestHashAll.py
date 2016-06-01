import sys, os, hashlib

def fileList(highest_directory):
    file_list = []
    name_list = []
    path_list_base = os.path.normpath(highest_directory).split(os.sep)
    path_stuff_to_remove = path_list_base[:-1]
    for path, subdirs, files in os.walk(highest_directory):
        for name in files:
            file_list.append(os.path.join(path, name))
            name = [name]
            path_list = os.path.normpath(path).split(os.sep)
            key_part = []
            for i in path_list:
                if i not in path_stuff_to_remove:
                    key_part.append(i)
            key_whole = key_part + name
            key_id = tuple(key_whole)
            name_list.append(key_id)
    return (file_list,name_list)

def hashing(inp_file, hash_algo=hashlib.sha256(), blocks_to_load=65536):
    with open(inp_file, "rb") as fl:
        for chunk in iter(lambda: fl.read(blocks_to_load), b""):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

##Folder before transfer
#folder_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160224_M02641_0082_000000000-ALPHF\\"
folder_h = "C:\\Users\\Sara\Documents\\Before\\160520_M00766_0034_000000000-ANJEU\\"
names = fileList(folder_h)[1]

hashdict_before = {}
for i, file_name in enumerate(fileList(folder_h)[0]):
    hashdict_before.update({names[i]:hashing(file_name, hashlib.sha256())})
#print hashdict_before
print "Run before transfer hashed"

##Folder after transfer
#folder2_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160224_M02641_0082_000000000-ALPHF\\"
#folder2_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160224_M02641_0082_000000000-ALPHF - Copy\\" #Deleted a file in this one for testing
#folder2_h = "C:\\Users\\Sara\\Google Drive\\MScProjectExtras\\ExtraDataForDatabase\\160225_M00766_0013_000000000-AL5YL\\"
folder2_h = "C:\\Users\\Sara\\Documents\\After\\160520_M00766_0034_000000000-ANJEU\\"
names = fileList(folder2_h)[1]

hashdict_after = {}
for i, file_name in enumerate(fileList(folder2_h)[0]):
    hashdict_after.update({names[i]:hashing(file_name, hashlib.sha256())})
#print hashdict_after
print "Run after transfer hashed"

'''
if hashdict_before == hashdict_after:
    print "All OK"
else:
    raise Exception("Transfer error")
'''

#assert(hashdict_before==hashdict_after)

#where is the problem
for k, v in hashdict_before.iteritems():
    #print k
    #print v
    ##assert k in hashdict_after #if this fails, the file it triggers on is missing after transfer. This passes even if the hashes are different.
    assert v == hashdict_after.get(k, k) #Don't need above test as if there's no value this will return the key and fail, as it won't match the value
    #print hashdict_after.get(k, k)
print "Successful transfer"

