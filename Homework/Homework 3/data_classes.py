import json
# more information on how to store json files in Lecture 6

class Person():
    """A person in general."""
    def __init__(self,name,age,email):
        """Initialize personal details."""
        self.name = name
        self.age = age
        self.email = email

    def save_file(self):
        """Take the info from Person and make it a dictionary."""
        person_info = {
            "name": self.name,
            "age": self.age,
            "email": self.email
        }

        return person_info


    def display_file(self):
        #placeholder

   

class Student(Person):
    """A student."""
    def __init__(self, student_id):
        "Initializing student details."
        self.student_id = student_id
    
    


