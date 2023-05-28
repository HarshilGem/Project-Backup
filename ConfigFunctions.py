import tkinter as tk
from  tkinter.filedialog import askdirectory

config_location = "D:\HarshilProject\Output\project_backup.config"

def create_config(): #TODO: Add interval and selection adding
    tk.Tk().withdraw()  # prevents an empty tkinter window from appearing
    config_location = askdirectory(title="Select Folder for saving config file")
    config_location = config_location + "/project_backup.config"

    try:
        c = open(config_location, "x")
    except(Exception):
        print(Exception)
        c = open(config_location, "w")
        c.write("")
    a = open(config_location, "a")

    a.write("src=" + askdirectory(title="Select Source Folder") + "\n")
    a.write("dst=" + askdirectory(title="Select Destination Folder") + "\n")

    # a.write("int=" + get_number_from_gui() + "\n")
    # a.write("sel=" + get_subdata_config(src) + "\n")

def read_config(field): #Done
    config = open(config_location, "r")
    Lines = config.readlines()

    for line in Lines:
        print("Checking: " + line)
        if(line.find(field) == 0):
            return line[4:len(line)]
    return ""

def alter_config():
    return True

def get_number_from_gui():
    def submit():
        number = entry.get()
        window.destroy()
        return int(number)

    window = tk.Tk()
    window.title("Number Input")

    label = tk.Label(window, text="Enter a number: ")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

    window.mainloop()

print("output: " + read_config("int"))