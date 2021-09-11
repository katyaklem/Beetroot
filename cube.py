experiments = [2, 11, 3, 5, 3, None, 1, 9, 9, 8, 12, 7, 4, None, 6, 2, 1, 3, 8, 3, 12, 4, 6, None, 11, 2, 5, 7, 3, 9]

yellow = list(range(1,7))
blue = list(range(1,13))
red = list(range(1,21))

yellow_mistake = 0
blue_mistake = 0
red_mistake = 0

count_of_experiment = []
probability_blue = []
probability_red = []

for experiment in experiments:

	if experiment == None:
		continue

	if yellow_mistake < 6:
		for variant in yellow:
			if experiment == variant:
				yellow_mistake = 0
				continue
			elif experiment > variant:
				yellow_mistake +=1 
				if yellow_mistake == 6:
					print('In is NO yellow')

	if blue_mistake < 12:
		for variant in blue:
			if experiment == variant:
				blue_mistake = 0
				continue
			elif experiment > variant:
				blue_mistake +=1 
				if blue_mistake == 12:
					print('In is NO blue')

if blue_mistake < 12:
	print('Maybe is it blue, see it in the future.')


for experiment in experiments:
	
	if experiment == None:
		continue
	else:
		count_of_experiment.append(experiments.count(experiment))

print(count_of_experiment)
	
for experiment in count_of_experiment:
	probability_blue.append(experiment/len(blue))
	probability_red.append(experiment/len(red))

print(probability_blue)
print(probability_red)

average_probability_blue = sum(probability_blue) / len(probability_blue)
average_probability_red = sum(probability_red) / len(probability_red)

print(average_probability_blue)
print(average_probability_red)

if probability_red > probability_blue:
	print('it is red cube')
else:
	print('it is blue cube')
		
