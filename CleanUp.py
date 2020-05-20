import os
import shutil
#cleaning up the files in the directory and file

def cleanup(path):
    if os.path.isdir(path):
        print('Cleaning up folder: {}'.format(path))
        shutil.rmtree(path)
    elif os.path.isfile(path):
        print('Cleaning up file: {}'.format(path))
        os.remove(path)
    else:
        print('Path not found. {}'.format(path))

if __name__ == '__main__':
    cleanup('D:/Pycharm Projects/Testing_Python/tmp')
