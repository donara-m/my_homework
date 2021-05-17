import os

print(os.getcwd())
os.chdir("..")
print(os.getcwd())

if "new_dir" in os.listdir():
	os.chdir("new_dir")
	def make_in_dir1():
		os.chdir("Dir_1")
		list_dir1 = os.listdir()
		tup_dir1 = ("Dir_3", "Dir_2")
		for i in tup_dir1:
			if not i in list_dir1:
				os.mkdir(i)
				if not "Dir_4" in os.listdir("Dir_3"):
					os.mkdir("Dir_3/Dir_4")
				else:
					print("Directions already existed")
			else:
				print(F"{i} already exists")
				if not "Dir_4" in os.listdir("Dir_3"):
					os.mkdir("Dir_3/Dir_4")
		os.chdir("..")
		print("Well done!!!")
	if not "Dir_1" in os.listdir():
		os.mkdir("Dir_1")
		make_in_dir1()
	else:
		make_in_dir1()
	os.chdir("..")
else:
	os.makedirs("new_dir/Dir_1/Dir_2")
	os.makedirs("new_dir/Dir_1/Dir_3/Dir_4")
	print("Done")
			
answer = input("Do you want to delete 'new_dir'? \nyes / no\n")

if answer.lower() == "yes":
	row = os.listdir("new_dir")
	for f in row:
		os.chdir("new_dir")
		if f == "my_file.txt":
			os.remove("new_dir/my_file.txt")
			print(F"{f} is removed")
		elif not os.listdir(f):
			os.rmdir(f)
			print(F"{f} is removed")
		else:
			r1 = os.listdir(f)
			os.chdir(f)
			for i in r1:
				if not os.listdir(i):
					os.rmdir(i)
					print(F"{i} is removed")
				else:
					r2 = os.listdir(i)
					os.rmdir(F"{i}/{r2[0]}")
					print(F"{r2[0]} is removed")
					os.rmdir(i)
					print(F"{i} is removed")
		os.chdir("..")
		os.rmdir(f)
		print(F"{f} is removed")
	os.chdir("..")
	os.rmdir("new_dir")
	print("'new_dir' is removed")
else:
	print(F"'new_dir' direction is {os.getcwd()}")
				