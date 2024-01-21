"""
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
"""

# This program defines a base class for musical instruments and a derived class for string instruments.
# The derived class includes additional attributes specific to string instruments.

# Parent class for musical instruments


class Instrument:
    """
    Represents a musical instrument with basic attributes.
    """

    def __init__(self, name, manufacturer, year_built, cost):
        self.name = name
        self.manufacturer = manufacturer
        self.year_built = year_built
        self.cost = cost

    def print_info(self):
        """
        Prints basic information about the instrument.
        """
        print('Instrument Information:')
        print(f' Name: {self.name}')
        print(f' Manufacturer: {self.manufacturer}')
        print(f' Year built: {self.year_built}')
        print(f' Cost: {self.cost}')


class StringInstrument(Instrument):
    """
    Represents a string instrument, derived from the Instrument class.
    Includes additional attributes specific to string instruments.
    """

    def __init__(self, name, manufacturer, year_built, cost, num_strings, num_frets, is_bowed):
        super().__init__(name, manufacturer, year_built, cost)
        self.num_strings = num_strings
        self.num_frets = num_frets
        self.is_bowed = is_bowed

    def print_info(self):
        """
        Overrides the print_info method to include information specific to string instruments.
        """
        super().print_info()
        print(f' Number of strings: {self.num_strings}')
        print(f' Number of frets: {self.num_frets}')
        print(f' Is bowed: {self.is_bowed}')


if __name__ == "__main__":
    # Input for a generic instrument
    instrument_name = input("Enter instrument name: ")
    manufacturer_name = input("Enter manufacturer name: ")
    year_built = int(input("Enter year built: "))
    cost = int(input("Enter cost: "))

    # Input for a string instrument
    string_instrument_name = input("Enter string instrument name: ")
    string_manufacturer = input("Enter string manufacturer: ")
    string_year_built = int(input("Enter string year built: "))
    string_cost = int(input("Enter string cost: "))
    num_strings = int(input("Enter number of strings: "))
    num_frets = int(input("Enter number of frets: "))
    is_bowed = input("Is the instrument bowed (True/False): ") == 'True'

    # Create and print information for both the generic and string instruments
    my_instrument = Instrument(instrument_name, manufacturer_name, year_built, cost)
    my_string_instrument = StringInstrument(string_instrument_name, string_manufacturer, string_year_built, string_cost,
                                            num_strings, num_frets, is_bowed)

    my_instrument.print_info()
    my_string_instrument.print_info()
