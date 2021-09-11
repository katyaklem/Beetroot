zoo = [
	['monkey', 'tiger', 'elephant'],
	['frog', 'snake'],
	['owl', 'pigeon'],
	['hamster', 'mouse', 'hedgehog']
]

for zoo_section in zoo:
	for animal in zoo_section:
		if ('a' in animal) == True:
			print(animal)
