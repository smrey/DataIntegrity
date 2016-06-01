# http://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
# http://stackoverflow.com/questions/24847602/how-to-create-a-checksum-of-a-file-in-python

#Import the hashlib library
import hashlib

#define the hashing as a function
#Because the file is likely to be too large to load in memory all at once, load it in chunks
def hashing(inp_file, hash_algo, blocks_to_load=65536):
    with open(inp_file, "rb") as fl:
        for chunk in iter(lambda: fl.read(blocks_to_load), b""):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

f_name = "C:\Users\Admin\Dropbox\gatkbestpractices.pdf"
print hashing(f_name, hashlib.sha256())




