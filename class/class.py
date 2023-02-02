class Student:
    def __init__(self, name, place, age):
        self.name = name
        self.place = place
        self.age = age
    
    def get_age(self):
        return self.age

    def set_age(self, age: int):
        self.age = age
    
    def display_student_details(self):
        print("Name: ", self.name)
        print("Place: ", self.place)
        print("Age: ", self.age)
