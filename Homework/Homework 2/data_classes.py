class Person():
    """A person in general."""
    def __init__(self,name,age,email):
        """Initialize personal details."""
        self.name = name
        self.age = age
        self.email = email

class Student(Person):
    """A student."""
    def __init__(self,student_id):
        "Initializing student details."

