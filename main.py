import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    label = tk.Label(root, text="Select the source folder")
    label.pack()

    button = tk.Button(root, text="Ok")
    button.pack()
    root.wait_variable(tk.BooleanVar())
    # f.copyFolderData(src, dest)