#JoannaLibraryTwo

def rolldice():
    """A function that rolls a six-sided dice and returns the value."""
    
    import random
    roll = random.randint(1,6)
    print(roll)
    return(roll)

def personalizedGreeting():
    """A function that displays a personalized greeting."""
    
    Name = input("Hi! What's your name?")
    print("Hi there " + Name)

rolldice()
personalizedGreeting()