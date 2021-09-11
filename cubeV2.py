experiments = [2, 11, 3, 5, 3, None, 1, 9, 9, 8, 12, 7, 4, None, 6, 2, 1, 3, 8, 3, 12, 4, 6, None, 11, 2, 5, 7, 3, 9]

yellow = list(range(1,7))
blue = list(range(1,13))
red = list(range(1,21))

count_of_experiment = []
probability_yellow = []
probability_blue = []
probability_red = []

for experiment in experiments:
	
	if experiment == None:
		continue
	else:
		count_of_experiment.append(experiments.count(experiment))

print(count_of_experiment)
	
for experiment in count_of_experiment:
	probability_yellow.append(experiment/len(yellow))
	probability_blue.append(experiment/len(blue))
	probability_red.append(experiment/len(red))

print(probability_yellow)
print(probability_blue)
print(probability_red)

average_probability_yellow = sum(probability_yellow) / len(probability_yellow)
average_probability_blue = sum(probability_blue) / len(probability_blue)
average_probability_red = sum(probability_red) / len(probability_red)

print(average_probability_yellow)
print(average_probability_blue)
print(average_probability_red)

if probability_yellow > probability_blue and probability_yellow > probability_red:
	print('it is yellow cube')
elif probability_blue > probability_yellow and probability_blue > probability_red:
	print('it is blue cube')
else:
	print('it is red cube')