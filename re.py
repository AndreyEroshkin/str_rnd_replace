import random
from tempfile import mkstemp
from shutil import move, copymode
import os

def replace(file_path, tgt_fld: str, a=1000, b=10_000):
    is_changed = False
    #Create temp file
    fh, abs_path = mkstemp()
    with os.fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if line.startswith(tgt_fld):
                    line = tgt_fld + str(random.randint(a, b)) + '\n'
                    is_changed = True
                new_file.write(line)
    if is_changed:
        print(f'Field {tgt_fld} in {file_path} changed.')
    else:
        print(f'Field "{tgt_fld}" in {file_path} not found.')
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    os.remove(file_path)
    #Move new file
    move(abs_path, file_path)

def get_files_paths (basepath: str):
    for fname in os.listdir(PATH_DIR):
        path = os.path.join(basepath, fname)
        if os.path.isdir(path):
            # skip directories
            continue
        yield path


if __name__ == '__main__':
    # Path to edited files. In all files in directory field will be replaced
    PATH_DIR = './data/'
    # Target field name with = sign.
    FIELD_FOR_REPLACE = "FLD('S')="

    for file in get_files_paths(PATH_DIR):
        try:
            replace(file_path=file, tgt_fld=FIELD_FOR_REPLACE)
        except Exception as e:
            print(f'Error while processing file {file}.')
            print(e)


