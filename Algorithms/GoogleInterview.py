class GoogleInterview:

	"""
	Write a function, that converts a given string of values separated by commas into a dictionary
	Values in the string can be put in double quotes - then commas inside of those quotes should not act like separators

	Input:
		"Go,ogle",GOO21W,"Pixel 5, 5G, Google-assistance",629.10

	Output:
		Company : Go,ogle
		SKU : GOO21W
		Description : Pixel 5, 5G, Google-assistance
		Price : 629.10
	"""
	def process_string(self, input_string: str) -> dict:
		words = []
		quotes_open = False
		word_start = 0
		for i, letter in enumerate(input_string):
			if letter == '"' and not quotes_open:
				quotes_open = True
				word_start = i + 1
			elif letter == '"' and quotes_open:
				words.append(input_string[word_start:i])
				quotes_open = False
			elif letter == ',' and not quotes_open:
				words.append(input_string[word_start:i]) if input_string[i - 1] != '"' else None
				word_start = i + 1
			elif i == len(input_string) - 1:
				words.append(input_string[word_start:i + 1])
		words.append("") if len(words) != 4 else None
		output = {"Company": words[0], "SKU": words[1], "Description": words[2], "Price": words[3], }
		return output

	"""
	Write a function, that counts the shortest distance between 2 nodes of the graph
	Distance between each pair of connected nodes is 1
	
	Input:
		start: "A"
		finish: "B"
		connections : [("A", "C"), ("B", "C"), ]
	
	Output:
		2
	"""
	def count_distance(self, start: str, finish: str, connections: [(), ]) -> int:
		pass

	"""
	Write a function, that simulates the actions of luggage handling for a large aircraft, assuming:
	Luggage is loaded into containers in the order the luggage arrives
	When a container is full, or there is no more luggage, the container is loaded into the aircraft
	The weight capacity of each container is 40 weight units
	At the destination, containers are unloaded from the plane in LIFO order the last one in being the first out
	Container contents are unloaded in FIFO order the last in being the last out
	
	Input: [10, 20, 15, 40, 25]
	Output: [25, 40, 15, 10, 20]
	"""
	def luggage_handling(self, luggage_to_load: [int]) -> [int]:
		if not luggage_to_load:
			raise ValueError("Nothing to transport")
		plane = [[], ]
		unloaded_luggage = []
		current_container_wieght = 0
		container = 0
		# loading
		for item in luggage_to_load:
			if item > 40:
				raise ValueError("This is too big")
			if current_container_wieght + item <= 40:
				plane[container].append(item)
				current_container_wieght += item
			else:
				container += 1
				plane.append([item])
				current_container_wieght = item
		# unloading
		for container in plane[-1::-1]:
			unloaded_luggage.extend(container)
		return unloaded_luggage
