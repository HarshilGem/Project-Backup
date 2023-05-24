import os
import shutil

def copyFolderData(src, dest):
    if not os.path.exists(src) or not os.path.isdir(src):
        print(f"Source folder '{src}' does not exist.")
        return

    if not os.path.exists(dest) or not os.path.isdir(dest):
        print(f"Destination folder '{dest}' does not exist.")
        return
    else:
        print("Else called")
        cleanDir(dest)


    shutil.copytree(src, dest)

def cleanDir(dir):
    print("Cleaning folder")
    try:
        os.remove(dir)
    except Exception as error:
        try:
            shutil.rmtree(dir)
        except:
            print("Error Deleting")
        finally:
            try:
                os.mkdir(dir)
            except Exception as error:
                print("Folder couldn't be deleted")