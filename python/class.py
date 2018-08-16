#!/usr/bin/python

# Please be careful about coding standard while solving exercises

# Create a class to store information about a person
# Write a method to calculate his or her age

# Hint: use datetime module to calculate person's age

class Person:

    def __init__(self, name, surname, birthdate):
        # +++your code here+++
	"""Initializes the data."""
        self.name = name
	self.surname = surname
	self.birthdate = birthdate
        print("(Initializing {})".format(self.name))
        print("(Initializing {})".format(self.surname))
        print("(Initializing {})".format(self.birthdate))
        return
    
    def age(self):
        # +++your code here+++
        return 2018 - (self.birthdate)


if __name__ == '__main__':
    
    #We want to see person's age by using below code.

    person = Person("mehmet","karakose", 1923)
    print person.age()
    
