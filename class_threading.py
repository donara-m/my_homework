import threading
import json

def downdoad_image(name, link):
	import requests
	
	image_response = requests.get(link)

	with open(F"{name}.png", "wb") as file:
		file.write(image_response.content)


with open("animal.json", "r") as json_file:
	animals = json.load(json_file)
	print(animals)

thread_list = []
for animal in animals:
    thread_ = threading.Thread(target=downdoad_image, args=(animal,))
    thread_list.append(thread_)
    thread_.start()
​
for t in thread_list:
    t.join()
