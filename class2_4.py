class Hotel:
	def __init__(self, name:str, place:str, rooms_mid:dict, mid_room_price:int, rooms_lux:dict, lux_room_price:int):
		self.hotel_name = name
		self.location = place
		self.mid_room = rooms_mid
		self.mid_room_price mid_room_price
		self.lux_room = rooms_lux
		self.lux_room_price = lux_room_price

	def hotel_present(self):
		return F"{self.hotel_name} is one of the most attractive places of interest that offers {self.location}\
We have two types of rooms: \nStandart rooms {self.mid_room_price} amd \n Luxe rooms {self.lux_room_price} amd."

	def booking_room(self, room, isLux):
		if isLux
		self.mid_room[room] = "busy"

	def available_room_check(self, sale_mid, sale_lux):
		self.mid_sale = sale_mid
		self.lux_sale = sale_lux
		if self.sale is None:
			pass
		else:
			discount_standart = 0.01 * (100 - self.mid_sale) * self.mid_room_price
			discount_lux = 0.01 * (100 - self.lux_sale) * self.lux_room_price
		return F"Standart room (discounted) {discount_standart} \nLuxe room (discounted) {discount_lux}"

class Taxi:
	def __init__(self, name, car_types:list, price_for_tour:int):
		self.taxi_name = name
		self.car_types = car_type
		self.taxi_price = price_for_tour

	def taxi_present(self):
		return F"{self.taxi_name} offers tours all over Armenia with comfortable {self.car_types} cars\
and you will pay for it {self.taxi_price} amd."

	def discount(self, sale:int):
		self.sale = sale
		if self.sale is None:
			pass
		else:
			self.taxi_price = 0.01 * (100 - self.sale) * self.taxi_price 

		return self.taxi_price

class Tour(Hotel, Taxi):
	def __init__(self, name, mid_room_price, lux_room_price, price_for_tour):
		Hotel.__init__(self, mid_room_price, lux_room_price)
		Taxi.__init__(self, price_for_tour)
		self.tour_name = name
		self.price_lux = self.lux_room_price + self.price_for_tour
		self.price_mid = self.mid_room_price + self.price_for_tour
		

	def tour_present(self):



