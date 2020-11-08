import random
import tempfile
import shutil
import os

def replace(file_path, tgt_fld, a=1000, b=10000):
    """
    Replace number in target field on random integer
    from a to b.
    """
    is_changed = False
    #Create temp file
    fh, abs_path = tempfile.mkstemp()
    with os.fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if line.startswith(tgt_fld):
                    line = tgt_fld + str(random.randint(a, b)) + '\n'
                    is_changed = True
                new_file.write(line)
    if is_changed:
        print('Field {} in {} changed.'.format(tgt_fld, file_path))
    else:
        print('Field "{}" in {} not found.'.format(tgt_fld, file_path))
    #Copy the file permissions from the old file to the new file
    shutil.copymode(file_path, abs_path)
    #Remove original file
    os.remove(file_path)
    #Move new file
    shutil.move(abs_path, file_path)

def get_files_paths (basepath):
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
            print('Error while processing file {}.'.format(file))
            print(e)
