"""
For homework write decorator which  decorates a function with following feature:
the runtime of decorated function will be written in a file, every time the function is called
"""

from datetime import datetime

def my_function():
	print("Hello World")

def decorator(func):
	def decor():
		called_time = datetime.now()
		with open("call.txt", "w") as file:
			file.write(F"{func.__name__} was called at {called_time}")
		func()

	return decor

my_function = decorator(my_function)

my_function()