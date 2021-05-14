print("Task 1\n")
class Hotel:
	def __init__(self, name, place, rooms_mid_count, mid_room_price, rooms_lux_count, lux_room_price):
		self.hotel_name = name
		self.location = place
		self.mid_room = {}
		for i in range(1, rooms_mid_count+1):
			self.mid_room[F"room{i}"] = "free"
		self.mid_room_price = mid_room_price
		self.lux_room = {}
		for i in range(1, rooms_lux_count+1):
			self.lux_room[F"L_room{i}"] = "free"
		self.lux_room_price = lux_room_price

	def hotel_present(self):
		print(F"{self.hotel_name} is one of the most attractive places of interest that offers {self.location}. "\
			F"We have two types of rooms: \nStandart rooms {self.mid_room_price} amd \nLuxe rooms {self.lux_room_price} amd.")

	def booking_room(self, room, is_lux:bool):
		if is_lux:
			self.lux_room[room] = "busy"
		else:
			self.mid_room[room] = "busy"

	def available_room_check(self, room, is_lux):
		if is_lux:
			return self.lux_room[room]
		else:
			return self.mid_room[room]


	def discount(self, sale):
		self.sale = sale
		if self.sale is None:
			pass
		else:
			discount_standart = 0.01 * (100 - self.sale) * self.mid_room_price
			discount_lux = 0.01 * (100 - self.sale) * self.lux_room_price
			return F"Luxe room {int(discount_lux)} amd \nStandart room {int(discount_standart)} amd"

class Taxi:
	def __init__(self, name, car_types:list, price_for_tour:int):
		self.taxi_name = name
		self.car_types = car_types
		self.taxi_price = price_for_tour

	def taxi_present(self):
		return F"{self.taxi_name} offers tours all over Armenia with comfortable {self.car_types} cars "\
			F"and you will pay for it {self.taxi_price} amd."

	def discount(self, sale):
		self.sale = sale
		if self.sale is None:
			pass
		else:
			self.taxi_price = 0.01 * (100 - self.sale) * self.taxi_price 

		return int(self.taxi_price)

class Tour(Hotel, Taxi):
	def __init__(self, name, mid_room_price, lux_room_price, price_for_tour):
		Hotel.__init__(self, mid_room_price, lux_room_price)
		Taxi.__init__(self, price_for_tour)
		self.tour_name = name
		self.price_lux = Hotel.lux_room_price + Taxi.price_for_tour
		self.price_mid = Hotel.mid_room_price + Taxi.price_for_tour

	def tour_present(self):
		print(F"Hello we offer {self.tour_name} tour we have two options {self.price_lux} and {self.price_mid},"\
			F"which includes transport with {self.taxi_name} company which provides {self.car_types} cars and price for it is {self.taxi_price},"\
			F"we will stay at {self.hotel_name} which offers two types of rooms standart {self.mid_room_price} and luxe {self.lux_room_price}")

print("\nTask 2\n")
class Triangle:
	def __init__(self, a, b, c):
		self.side1 = a 
		self.side2 = b
		self.side3 = c 

	def to_sorted_list(self):
		return sorted([self.side1, self.side2, self.side3])

	def similar_triangles(self, other):
		if (self.to_sorted_list()[0] / other.to_sorted_list()[0]) == (self.to_sorted_list()[1] / other.to_sorted_list()[1]) and (self.to_sorted_list()[0] / other.to_sorted_list()[0]) == (self.to_sorted_list()[2] / other.to_sorted_list()[2]):
			return True
		else:
			return False

	def __gt__(self, other):
		if self.similar_triangles(other) and (self.to_sorted_list()[0] > other.to_sorted_list()[0]):
			return True
		else:
			return False

x = Triangle(4, 5, 3)
y = Triangle(3, 5, 4)
z = Triangle(6, 10, 8)

print(x.similar_triangles(y))
print(z > x)