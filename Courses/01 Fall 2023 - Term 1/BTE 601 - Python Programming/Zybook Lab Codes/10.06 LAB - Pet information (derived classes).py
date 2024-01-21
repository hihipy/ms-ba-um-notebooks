"""
10.6 LAB: Pet information (derived classes)
The base class Pet has attributes name and age. The derived class Cat inherits attributes from the base class (Pet) and includes a breed attribute. Complete the program to:

Create a generic pet, and print the pet's information using print_info().
Create a Cat pet, use print_info() to print the cat's information, and add a statement to print the cat's breed attribute.
Ex:

If the input is:

Dobby
2
Kreacher
3
Scottish Fold

the output is:

Pet Information: 
   Name: Dobby
   Age: 2
Pet Information: 
   Name: Kreacher
   Age: 3
   Breed: Scottish Fold
"""
# The program defines a base class Pet and a derived class Cat.
# Pet has attributes name and age, and Cat inherits these attributes and adds a breed attribute.

# Parent Pet class definition


class Pet:
    def __init__(self, name='', age=0):
        # Initialize Pet instance with name and age.
        self.name = name
        self.age = age

    def print_info(self):
        # Print the information of the Pet.
        print('Pet Information:')
        print(f' Name: {self.name}')
        print(f' Age: {self.age}')


# Child Cat class definition
class Cat(Pet):
    def __init__(self, name='', age=0, breed=''):
        # Initialize Cat instance using Pet's __init__ method and add breed.
        super().__init__(name, age)
        self.breed = breed

    # Override the print_info method to include breed information.
    def print_info(self):
        # First, call the parent's print_info method.
        super().print_info()

        # Print the breed of the Cat, if it is defined.
        if self.breed:
            print(f' Breed: {self.breed}')


# Main section of the program
if __name__ == '__main__':
    # Input for generic pet
    pet_name = input("Enter pet's name: ")
    pet_age = int(input("Enter pet's age: "))

    # Create and print information of a generic pet
    my_pet = Pet(pet_name, pet_age)
    my_pet.print_info()

    # Input for cat
    cat_name = input("Enter cat's name: ")
    cat_age = int(input("Enter cat's age: "))
    cat_breed = input("Enter cat's breed: ")

    # Create and print information of a cat, including breed
    my_cat = Cat(cat_name, cat_age, cat_breed)
    my_cat.print_info()
