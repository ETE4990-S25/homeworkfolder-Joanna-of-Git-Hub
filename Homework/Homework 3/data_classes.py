import json
# more information on how to store json files in Lecture 6

class Person():
    """A person in general."""
    def __init__(self,name,age,email):
        """Initialize personal details."""
        self.name = name
        self.age = age
        self.email = email

   

class Student(Person):
    """A student."""
    def __init__(self, student_id):
        "Initializing student details."
        self.student_id = student_id
    
    
def save_file():
    #placeholder

def display_file():
    #placeholder