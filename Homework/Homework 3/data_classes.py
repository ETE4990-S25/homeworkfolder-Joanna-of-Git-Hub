#Joanna Escobar
import json
class Person(object):
    """A person in general."""
    
    person_info={} #outside the definitions because I want it to be used throughout both classes
    person_file = 'personfile.json'
    
    def __init__(self, name, age, email): #initializes basic info
        """Initialize personal details."""
        self.name = name
        self.age = age
        self.email = email

        self.person_info = { #stores all of the gathered data into a simple dictionary
            "name": self.name,
            "age": self.age,
            "email": self.email
        }
    
    def save_file(self):
        """Take info from Person and put in json file."""     
        
        with open(self.person_file, 'w') as f: #using 'a' appends data instead of overwriting existing data
            json.dump(self.person_info, f)

    def show_file(self):
        self.person_file = 'personfile.json'
        with open(self.person_file) as f:
            person_json = json.load(f)

        print(person_json)

class Student(Person):
    """A student."""
    def __init__(self, name, age, email):
        """Initializing student details."""
        super().__init__(name, age, email)

        self.student_id = input("Input your ID number: ")
        self.person_info.update({"student id":self.student_id}) # I want to append student_id to the file
        
        #with open(self.student_id, 'w') as g:
            #json.dump(self.student_id, g)