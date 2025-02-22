# Testing

# SK weather function
def weather(condition):
    if condition == "windy":
        print ("It's windy")
    elif condition == "cloudy":
        print ("It's cloudy")
    elif condition == "rainy":
        print ("It's raining")
    else:
        print ("Sun is out")

    print ("Condition")

#SK luxury function
def luxury(name, list):
    """Checks if the brand is in the list."""
    if name in list:
        print(name + " brand is in the list.")
    else:
        print(name + " brand is NOT in the list.")

