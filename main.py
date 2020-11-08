import random
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
from glob import glob




def replace(file_path, tgt_fld: str, a=1000, b=10_000):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if line.startswith(tgt_fld):
                    line = tgt_fld + str(random.randint(a, b)) + '\n'
                new_file.write(line)
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)





if __name__ == '__main__':
    # Path to edited files. In all files in directory field will be replaced
    PATH_DIR = './data/'
    # Target field
    FIELD_FOR_REPLACE = "FLD('S')="

    file_list = glob(pathname=PATH_DIR+'*', recursive=False)
    for file in file_list:
        replace(file_path=file, tgt_fld=FIELD_FOR_REPLACE)


