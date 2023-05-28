import tkinter as tk
from  tkinter.filedialog import askdirectory

def create_config():
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

    src = askdirectory(title="Select Source Folder")
    dest = askdirectory(title="Select Destination Folder")
    a.write("src=" + src + "\n")
    print("src written")
    a.write("dest=" + dest + "\n")
    print("dest written")
    # a.write("interval=" + get_number_from_gui() + "\n")
    print("interval written")
    # a.write("selected=" + get_subdata_config(src) + "\n")

    return True
def read_config(field):
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

    label = tk.Label(window, text="Enter a number:")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

    window.mainloop()

create_config()