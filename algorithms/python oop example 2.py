# Parent class (Person)
class Person:
    def __init__(self, name, age, gender):
        # Public data members
        self.name = name
        self.age = age
        
        # Protected data member
        self._gender = gender
        
        # Private data member
        self.__id = "1234"

    # Public method to access private data member
    def get_id(self):
        return self.__id
    
    # Public method to update private data member
    def set_id(self, new_id):
        self.__id = new_id
    
    # Public method to access protected data member
    def get_gender(self):
        return self._gender
    
    # Public method to update protected data member
    def set_gender(self, new_gender):
        self._gender = new_gender
    
    # Public method to display information
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self._gender}, ID: {self.__id}")

# Child class (Student) inheriting from Person
class Student(Person):
    def __init__(self, name, age, gender, roll_number, grade):
        # Call the constructor of the parent class
        super().__init__(name, age, gender)
        
        # Additional data members specific to Student class
        self.roll_number = roll_number
        self.grade = grade
        
    # Override the display_info method of the parent class
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self._gender}, ID: {self.get_id()}")
        print(f"Roll Number: {self.roll_number}, Grade: {self.grade}")

# Creating objects of the Student class
student1 = Student("Alice", 15, "Female", "S001", "A+")
student2 = Student("Bob", 16, "Male", "S002", "A")

# Polymorphism: Using the display_info method of the Student class
student1.display_info()
student2.display_info()
