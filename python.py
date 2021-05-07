#Task 1
print("Task 1\n")
'''
Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
'''

sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40], [40]]
print(F"Sample list {sample_list}")

copy_list = sample_list.copy()
for element in copy_list:
	if sample_list.count(element) != 1:
		sample_list.remove(element)

print(F"Sample list without duplicate {sample_list}")

#Task 2
print("\nTask 2\n")
'''
Write a Python program to flatten a given nested list structure.
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
'''

mixed_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]] 

flatten_list = []
for item in mixed_list:
	if type(item) is not list:
		flatten_list.append(item)
	else:
		flatten_list.extend(item)

print(F"Mixed list {mixed_list}")
print(F"Flatten list {flatten_list}")


#Task 3
print("\nTask 3\n")
'''
Write a Python function to split a given list into two parts where the length of the first part of the list is given. 
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
suppose the length of the first part of the list: 3
([1, 1, 2], [3, 4, 4, 5, 1])
'''

original_list = [1, 1, 2,"Kate", 3, 4, 4, "hi", 5, 1]

def split_list(my_list: list) -> list:
	
	first_length = int(input("The length of the first part of the list with 10 elements is : "))

	new_list = [original_list[:first_length], original_list[first_length:]]

	return new_list

print(split_list.__annotations__)

print(F"\nThe original list is {original_list}")
print(F"\nThe new list is {split_list(original_list)}")

#Task 4
print("Task 4\n")
'''
Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
 dict1={1:10, 2:20}
 dict2={3:30, 4:40}
 dict3={5:50,6:60}
 dict4={6:50,7:60}
list_dict = [dict1, dict2, dict3, dict4]
 Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
Try for as second version
'''

dict_1={1:10, 2:20}
dict_2={3:30, 4:40}
dict_3={5:50, 6:60}
dict_4={6:50, 7:60}

dict_1.update(dict_2)
dict_1.update(dict_3)
dict_1.update(dict_4)

print(F"Connected dictionary is {dict_1}")

#Task 5
print("\nTask 5\n")
'''
Write a Python program to drop empty Items from a given Dictionary.
 Original Dictionary:
 {'c1': 'Red', 'c2': 'Green', 'c3': None}
 New Dictionary after dropping empty items:
 {'c1': 'Red', 'c2': 'Green'}
'''

sample_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': 'Blue', 'c5': None}
print(F"Dictionary: {sample_dict}")

copy_dict = sample_dict.copy()
for key in copy_dict.keys():
	if sample_dict[key] == None:
		sample_dict.pop(key)

print(F"Dictionary after dropping empty items is {sample_dict}")


# comment