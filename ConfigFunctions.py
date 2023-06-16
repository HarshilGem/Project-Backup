import tkinter as tk
from tkinter.filedialog import askdirectory

config_location = "D:\\HarshilBackupProject\\project_backup.config"


def create_config():  # TODO: Add interval and selection adding
    tk.Tk().withdraw()  # prevents an empty tkinter window from appearing
    config_location = askdirectory(title="Select Folder for saving config file")
    config_location = config_location + "/project_backup.config"

    try:
        c = open(config_location, "x")
    except Exception:
        print(Exception)
        c = open(config_location, "w")
        c.write("")
    a = open(config_location, "a")

    a.write("src=" + askdirectory(title="Select Source Folder") + "\n")
    a.write("dst=" + askdirectory(title="Select Destination Folder") + "\n")

    a.write("int=" + "60" + "\n")
    a.write("sel=" + "Files" + "\n")


def read_config(field, return_line = False):  # Done
    config = open(config_location, "r")
    Lines = config.readlines()

    i = 0
    for line in Lines:
        # print("Checking: " + line)
        if (line.find(field) == 0):
            if return_line:
                return i
            else:
                return line[4:len(line)]

        i += 1
    return ""


def alter_config(field, data):  #Done
    try:
        lines = []  # Initialize an empty list to store lines

        with open(config_location, 'r') as file:
            for line in file:
                lines.append(line)
        print(lines)
        print(read_config(field, True))
        lines[read_config(field, True)] = field + "=" + data + "\n"


        cleaner = open(config_location, 'w')
        cleaner.write("") #cleaning file
        appender = open(config_location, 'a')
        for i in lines:
            appender.write(i)
        return True
    except:
        return False