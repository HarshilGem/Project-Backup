from config_file import read_config

config_file = "D:\\HarshilBackupProject\\project_backup.config"

if __name__ == '__main__':
    print("Running")

    src = read_config("SRC", config_file, False)
    dest = read_config("DST", config_file, False)
    interval = read_config("INT", config_file, False)
    selected_files = read_config("SEL", config_file, False).split("|")

    print("Src: ", src)
    print("Dest: ", dest)
    print("Interval: ", interval)
    print("Selected Files: ", selected_files)

    print("Completed")