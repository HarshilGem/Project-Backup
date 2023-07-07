def create_config():
    print("Opening web page")

def read_config(field, config_location, return_line_number = False):  # Done
    config = open(config_location, "r")
    Lines = config.readlines()

    i = 0
    for line in Lines:
        # print("Checking: " + line)
        if (line.find(field) == 0):
            if return_line_number:
                # print("Returning")
                return i
            else:
                # print("Returning", line[4:len(line)])
                return line[4:len(line)]

        i += 1
    return "Data Not Found"