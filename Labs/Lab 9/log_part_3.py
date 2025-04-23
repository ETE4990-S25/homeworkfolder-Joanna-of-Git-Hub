import json
import matplotlib

def jsonMonitor(file):
    with open(file, "r") as f:
        count_dict = f.load()

    count_i, count_e, count_w, count_c = 0
    # critical_list = []
    for key in count_dict:
        if key == "INFO":
            count_i += 1
        elif key == "WARNING":
            count_w += 1
        elif key == "ERROR":
            count_e += 1
        else:
            count_c += 1
            for value in key:
                print(count_dict[key][value])

def graphErrors(input):
    a =1