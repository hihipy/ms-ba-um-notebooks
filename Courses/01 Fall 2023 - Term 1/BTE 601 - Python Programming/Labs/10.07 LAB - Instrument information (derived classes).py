'''
10.7 LAB: Instrument information (derived classes)
Given the base class Instrument, define a derived class StringInstrument for string instruments with a constructor that initializes the attributes of the Instrument class as well as new attributes of the following types

integer to store the number of strings
integer to store the number of frets
boolean to store whether the instrument is bowed

Ex. If the input is:

Drums
Zildjian
2015
2500
Guitar
Gibson
2002
1200
6
19
False

the output is:

Instrument Information: 
   Name: Drums
   Manufacturer: Zildjian
   Year built: 2015
   Cost: 2500
Instrument Information: 
   Name: Guitar
   Manufacturer: Gibson
   Year built: 2002
   Cost: 1200
   Number of strings: 6
   Number of frets: 19
   Is bowed: False
'''
class Instrument:
    def __init__(self, name, manufacturer, year_built, cost):
        self.name = name
        self.manufacturer = manufacturer
        self.year_built = year_built
        self.cost = cost
      
    def print_info(self):
        print(f'Instrument Information:')
        print(f'   Name: { self.name }')
        print(f'   Manufacturer: { self.manufacturer }')
        print(f'   Year built: { self.year_built }')
        print(f'   Cost: { self.cost }')

class StringInstrument(Instrument):
    def __init__(self, name, manufacturer, year_built, cost, num_strings, num_frets, is_bowed):
        super().__init__(name, manufacturer, year_built, cost)  # Calling the parent class's __init__ method
        self.num_strings = num_strings
        self.num_frets = num_frets
        self.is_bowed = is_bowed
        
    def print_info(self):  # Overriding the base class method to include string instrument-specific attributes
        super().print_info()  # Call the parent class's print_info method
        print(f'   Number of strings: { self.num_strings }')
        print(f'   Number of frets: { self.num_frets }')
        print(f'   Is bowed: { self.is_bowed }')

if __name__ == "__main__":
    instrument_name = input()
    manufacturer_name = input()
    year_built = int(input())
    cost = int(input())
    
    string_instrument_name = input()
    string_manufacturer = input()
    string_year_built = int(input())
    string_cost = int(input())
    num_strings = int(input())
    num_frets = int(input())
    is_bowed = input() == 'True'
    
    my_instrument = Instrument(instrument_name, manufacturer_name, year_built, cost)
    my_string_instrument = StringInstrument(string_instrument_name, string_manufacturer, string_year_built, string_cost, num_strings, num_frets, is_bowed)

    my_instrument.print_info()
    my_string_instrument.print_info()  # This will now print all the relevant details for the string instrument