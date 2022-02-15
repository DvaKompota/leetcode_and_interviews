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
