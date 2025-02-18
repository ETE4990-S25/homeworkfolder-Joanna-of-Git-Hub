import json

class Person():
    """A person in general."""
    def __init__(self,name,age,email):
        """Initialize personal details."""
        self.name = name
        self.age = age
        self.email = email

    def json_save_person():
        #placeholder

    def json_screen_person():
        #placeholder


class Student(Person):
    """A student."""
    def __init__(self, student_id):
        "Initializing student details."
        self.student_id = student_id
    
    def json_save_student():
        #placeholder

    def json_screen_student():
        #placeholder