def nameInList(name, list):
    """Input a name and a list to seach through. 
    Returns if name was found"""

    for items in list:
        if name in list[items]:
            print(name + "was in the list.")
        else:
            print(name + "was not in the list.")