import math

print("Task 1\n")
'''
create class Shape which has
attrs: name
methods: present_shape
class Triangle which is child of class Shape
attrs: side1, side2, base, height
methods: present, area, perimeter
class Square child of class Shape
attrs: side1, side2
methods: present, area, perimeter, get_bias (անկյունագիծ)
and try
'''
class Shape:
	def __init__(self, name):
		self.shape_name = name

	def present_shape(self):
		return(F"{self.shape_name} is a geometrical body")

class Triangle(Shape):
	def __init__(self, name:str, side1:float, side2:float, base:float, height:float):
		self.triangle_side1 = side1
		self.triangle_side2 = side2
		self.triangle_side3 = base
		self.triangle_height = height
		super().__init__(name)

	def triangle_present(self):
		return (F"{self.present_shape()} in type of triangle.\nTriangle is a polygon with three sides.\
			\nAB = {self.triangle_side1}cm \nBC = {self.triangle_side2}cm \nCA = {self.triangle_side3}cm\
			\nBH = {self.triangle_height}cm (height). \n{self.triangle_perimeter()}cm \n{self.triangle_area()}cm2")
	
	def triangle_area(self):
		triangle_area = self.triangle_side3 * self.triangle_height / 2
		return ("The area of {} triangle is {}".format(self.shape_name, triangle_area))

	def triangle_perimeter(self):
		triangle_perimeter = self.triangle_side1 + self.triangle_side2 + self.triangle_side3
		return (F"The perimeter of {self.shape_name} triangle is {triangle_perimeter}")

class Square(Shape):
	def __init__(self, name:str, side1:float, side2:float):
		self.square_side1 = side1
		self.square_side2 = side2
		Shape.__init__(self, name)

	def square_present(self):
		return (F"{self.present_shape()}. Square is four-sided mathematical shape.The opposite sides have the same lengths.\
			\nAB = {self.square_side1}cm \nBC = {self.square_side2}cm \n{self.square_get_bias()}cm\
			\n{self.square_parimeter()}cm \n{self.square_area()}cm2")
	
	def square_area(self):
		a = self.square_side1 * self.square_side2
		return (F"The area of {self.shape_name} is {a}" )
	
	def square_parimeter(self):
		p = (self.square_side1 + self.square_side2) * 2
		return (F"The parimeter of {self.shape_name} is {p}")
	
	def square_get_bias(self):
		get_bias = math.sqrt(self.square_side1**2 + self.square_side2**2)
		return (F"The diaganal of {self.shape_name} is {get_bias}")

shape_1 = Triangle("ABC", 6, 8, 10, 4.8)
print(shape_1.triangle_present())

shape_2 = Square("ABCD", 3, 7)
print(shape_2.square_present())

print("\nTask 2\n")
'''
Create 3 classes (Country, Brand, Season)
class Country should have
	name
	continent
	and a method which RETURNS name and continent in text
class Brand should have
	brand name
	business start date
	and a method which RETURNS the presentation
class Season should have
	season name
	and average temperature
	and a method which RETURNS the presentation
After this create Product class which inherits from (Country, Brand, Season) classes
it should have
	product name
	product type
	product price
	product quantity
	and a method which will present the product
	a method which will discount product price with given percent
	a method which will increase the quantity
	and a method which decrease the quantity
'''

class Country:
	def __init__(self, c_name, continent):
		self.country_name = c_name
		self.country_continent = continent

	def country_present(self):
		return (F"{self.country_name} is located in {self.country_continent}.")


class Brand:
	def __init__(self, b_name, date):
		self.brand_name = b_name
		self.start_date = date

	def brand_present(self):
		return (F"{self.brand_name} is founded in {self.start_date}.")

class Season:
	def __init__(self, s_name, temperature):
		self.season_name = s_name
		self.season_average_temperature = temperature

	def season_present(self):
		return (F"The average temperature in {self.season_name} is {self.season_average_temperature}C.")

class Product(Country, Brand, Season):
	def __init__(self, p_name, p_type, p_price:int, p_quantity:int, b_name, date, s_name, temperature, c_name, continent):
		self.product_name = p_name
		self.product_type = p_type
		self.product_price = p_price
		self.product_quantity = p_quantity
		Brand.__init__(self, b_name, date)
		Season.__init__(self, s_name, temperature)
		Country.__init__(self, c_name, continent)

	def product_present(self):
		print(F"We are presenting {self.product_type} {self.product_name} from {self.brand_name}. {self.brand_present()} in {self.country_name}.\
			\n{self.country_present()} You can wear {self.product_name} in {self.season_name}. {self.season_present()}\
			\nThe price of {self.product_name} is {self.product_price}.", sep=" ")

	def sale(self, persent):
		self.persent = persent
		if self.persent is None:
			pass
		else:
			discounted_price = self.product_price * (100 - self.persent) / 100

		return discounted_price

	def quantity_increase(self, increased_quantity):
		self.product_quantity += increased_quantity
		
	def quantity_decrease(self, decreased_quantity):
		self.product_quantity -= decreased_quantity

my_product = Product("Superstar", "Shoes", 85, 5, "Adidas","1949","Spring","20", "Germany","Europe")

my_product.product_present()

print(F"Discounted price is {my_product.sale(40)}$")

my_product.quantity_increase(10)
print(F"After increase {my_product.product_quantity}")

my_product.quantity_decrease(3)
print(F"After decrease {my_product.product_quantity}")