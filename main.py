# My Classmates
from pyscript import display, document # pyright: ignore[reportMissingImports]


class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    # Introduce Method
    def introduce(self):
        return(f"Hello! I am {self.name} from {self.section}. I like {self.favorite_subject}.") # Default Message

# Objects of Class: Classmate
c1 = Classmate("Sean", "Topaz", "PE")
c2 = Classmate("Allen", "Topaz", "ICT")
c3 = Classmate("Ramon", "Topaz", "TLE")
c4 = Classmate("Jalainie", "Topaz", "Math")
c5 = Classmate("Calvin", "Topaz", "English")

# List of Classmates
classmates = [c1, c2, c3, c4, c5]

# Show List of Classmates
def show_list(e):
    document.getElementById('output').innerHTML = "" # Clear Output

    # Looping Introductions for each Object
    for i in classmates:
        display(i.introduce(), target="output") 

# Add Classmate towards the List
def add_classmate(e):
    document.getElementById('output').innerHTML = "" # Clear Output

    # Input values
    name = document.getElementById('name').value
    section = document.getElementById('section').value
    favorite_subject = document.getElementById('subject').value

    # Create new classmate
    new_member = Classmate(name, section, favorite_subject)
    classmates.append(new_member)

    # Update list
    show_list
