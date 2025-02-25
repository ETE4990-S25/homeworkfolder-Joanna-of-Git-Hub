#Joanna Escobar
import json
class Person(object):
    """A person in general."""
    
    person_info={}
    person_file = 'personfile.json'
    
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
        
        with open(self.person_file, 'a') as f:
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

        self.student_id = input("Input your ID number: ")
        self.person_info.update({"student id":self.student_id})
        
        #with open(self.student_id, 'w') as g:
            #json.dump(self.student_id, g)