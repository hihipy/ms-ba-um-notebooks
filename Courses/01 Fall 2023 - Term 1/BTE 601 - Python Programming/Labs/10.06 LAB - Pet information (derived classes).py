'''
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
'''
class Pet:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
    
    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: {self.name}')
        print(f'   Age: {self.age}')

class Cat(Pet):
    def __init__(self, name='', age=0, breed=''):
        super().__init__(name, age)  # Using super() to call the parent class's __init__ method
        self.breed = breed
    
    # Overriding the print_info method for the Cat class
    def print_info(self):
        super().print_info()  # Calling the parent class's print_info method
        if self.breed:  # Only print breed if it's defined
            print(f'   Breed: {self.breed}')

# Input and object creation remain unchanged
pet_name = input()
pet_age = int(input())
cat_name = input()
cat_age = int(input())
cat_breed = input()

# Create generic pet (using pet_name, pet_age) and then call print_info()
my_pet = Pet(pet_name, pet_age)
my_pet.print_info()

# Create cat pet (using cat_name, cat_age, cat_breed) and then call print_info()
my_cat = Cat(cat_name, cat_age, cat_breed)
my_cat.print_info()