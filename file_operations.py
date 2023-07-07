from os import mkdir
from shutil import copytree
from shutil import copy2
import shutil


def start_copy(src, dest, choosen_files_and_folders):
    cleanup_dest_folder(dest)

    for item in choosen_files_and_folders:
        print("---------- trying ", src + "\\" + item, dest + "\\" + item)
        copy_file(src + "\\" + item, dest + "\\" + item)

def cleanup_dest_folder(dest):
    mkdir(dest + "\\temp_cleanup_dest\\")
    copy_file(dest, dest + "\\temp_cleanup_dest\\", True)

def copy_file(src, dest, move = False):
    try:
        if move:
            shutil.move(src, dest)
        else:
            copytree(src, dest)
        print("Success")
    except NotADirectoryError:
        copy2(src, dest)
        print("Success")
    except FileNotFoundError:
        print("Source 404")
    except FileExistsError:
        print("Destination already exists")
    except Exception as e:
        print("Error: ", str(e))