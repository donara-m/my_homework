#Task 1
print("Task 1\n")
'''
1. Write a Python class which should contain
a constructor to create a dictionary from a string.
Sample string : ‘python’
Expected output: {‘p’: 1, ‘y’: 1, ‘t’: 2, ‘h’: 1, ‘o’: 1, ‘n’:1}
a method which returns a version of the dictionary without duplicate values.
a method which returns the highest 3 values in a dictionary
a method which presents the dictionary
'''
class DictionaryFromString:

	def __init__(self, input_string):
		self.input_string = input_string

	def new_dict(self):
		my_dict = dict()
		
		for i in list(self.input_string):
			import random
			my_dict.update({i:random.randint(1,len(self.input_string))})
		return my_dict

my_string = DictionaryFromString("python")
print(my_string.new_dict())


#Task 2
print("\nTask 2\n")
'''
2. Write a Python class named Circle constructed by a radius and two methods 
which will compute the area and the perimeter of a circle
'''
class Circle:

	def __init__(self, radius):
		self.radius = radius

	def perimeter(self):
		p = 2 * 3.14 * self.radius
		return F"Perimeter is {p}"

	def area(self):
		area = 3.14 * self.radius**2
		return F"Area is {area}"

my_circle = Circle(4)
print(my_circle.perimeter())
print(my_circle.area())


