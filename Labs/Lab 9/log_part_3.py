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

def graphErrors(file):
    """Takes in a json or txt file that has already parsed the amount and type of errors."""
    
    with open(file, "r") as f:
        count_dict = f.load()

    #taken from Mr. Powers's notes
    categories = list("INFO","ERROR","WARNING","CRITICAL")
    
    count_i, count_e, count_w, count_c = 0
    count_list = []
    for key in count_dict:
        if key == "INFO":
            count_i += 1
        elif key == "ERROR":
            count_w += 1
        elif key == "WARNING":
            count_e += 1
        else:
            count_c += 1

    count_list.append(count_i)
    count_list.append(count_e)
    count_list.append(count_w)
    count_list.append(count_c)

    matplotlib.bar(categories, count_list)
    matplotlib.title('Logged Information')
    matplotlib.xlabel('Categories')
    matplotlib.ylabel('Amount')

    matplotlib.show()
