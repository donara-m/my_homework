import os
import random

quantity = 0
for i in range(20):
	i =  random.randint(1, 100)
	print(i)
	if i % 2 == 1:
		with open("odd_num.txt", "a") as file:
			file.write(F"{str(i)}\n")
			quantity += 1
	else:
		pass
print(F"Quantity is {quantity}")

amount = 0

with open("odd_num.txt") as file:
	for _ in range(quantity):
		num = file.readline()
		amount += int(num)
		print(num)
		
	print(F"The sum is {amount}")
