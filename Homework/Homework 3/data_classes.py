import json
class Person(object):
    """A person in general."""
    
    def __init__(self, name, age, email):
        """Initialize personal details."""
        self.name = name
        self.age = age
        self.email = email
    
    def save_file(self):
        """Take info from Person and put in json file."""
        person_info = {
            "name": self.name,
            "age": self.age,
            "email": self.email
        }
        person_file = 'personfile.json'
        with open(person_file, 'w') as f:
            json.dump(person_info, f)

    def show_file(self):
        filename = 'personfile.json'
        with open(filename) as f:
            person_json = json.load(f)

        print(person_json)

class Student(Person):
    """A student."""
    def __init__(self, name, age, email):
        """Initializing student details."""
        super().__init__(name, age, email)

        self.student_id = 000000
        