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
# Parent Pet class
class Pet:

  def __init__(self, name='', age=0):
    self.name = name
    self.age = age

  def print_info(self):
    print('Pet Information:')
    print(f' Name: {self.name}') 
    print(f' Age: {self.age}')

# Child Cat class  
class Cat(Pet):

  def __init__(self, name='', age=0, breed=''):
    super().__init__(name, age) # Call parent __init__

    self.breed = breed
  
  # Override print_info
  def print_info(self):
    super().print_info() # Call parent print_info

    if self.breed: # Only print breed if defined
      print(f' Breed: {self.breed}')

# Take input  
pet_name = input()
pet_age = int(input())

cat_name = input()  
cat_age = int(input())
cat_breed = input()

# Create Pet object
my_pet = Pet(pet_name, pet_age)
my_pet.print_info()

# Create Cat object 
my_cat = Cat(cat_name, cat_age, cat_breed)
my_cat.print_info() # Prints breed too