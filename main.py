from config_file import read_config
from file_operations import start_copy
from time import sleep

config_file = "D:\\project_backup.config" #Location of config file

if __name__ == '__main__':
    print("Running")

    src = read_config("SRC", config_file, False)[:-1]
    dest = read_config("DST", config_file, False)[:-1]
    interval = read_config("INT", config_file, False)[:-1]
    selected_files = read_config("SEL", config_file, False).split("|")

    print("Src: ", src)
    print("Dest: ", dest)
    print("Interval: ", interval)
    print("Selected Files: ", selected_files)

    print("Completed")

   
    print("Loopinggggggggggggggggg")
    start_copy(src, dest, selected_files)
        # break
        #sleep(int(interval) * 10)
