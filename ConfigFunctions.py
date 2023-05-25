import os
import tkinter as tk
from tkinter import ttk

def create_config_file(src):
    print_directory_contents(src)
    create_checkbox_gui(print_directory_contents(src))

def create_checkbox_gui(arr):
    root = tk.Tk()
    root.state("zoomed") #Open page maximised

    # Create a canvas with scrollbar
    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame inside the canvas
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Create a list to store the checkbox values
    checkbox_values = []

    # Create checkboxes for each element in the array
    for item in arr:
        var = tk.BooleanVar()
        checkbox_values.append(var)
        checkbox = ttk.Checkbutton(frame, text=item, variable=var)
        checkbox.pack(anchor=tk.W)

    # Create an OK button to retrieve the selected checkbox values
    def get_selected_items():
        selected_items = [item for i, item in enumerate(arr) if checkbox_values[i].get()]
        print(selected_items)  # Replace with your desired action

    ok_button = ttk.Button(frame, text="OK", command=get_selected_items)
    ok_button.pack()

    # Configure the canvas scrolling
    canvas.configure(scrollregion=canvas.bbox("all"))

    root.mainloop()

def print_directory_contents(directory):
    i = 0
    output = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print('Directory:', item_path)
            output.append("DIR " + item_path)
        else:
            print('File:', item_path)
            output.append("FIL " + item_path)
    return output


# directory_path = 'D:\\HarshilProject\\src'
# print_directory_contents(directory_path)
# print(print_directory_contents(directory_path))
# create_checkbox_gui(print_directory_contents(directory_path))