import numpy

all_powers_of_cubes = []

with open("puzzle-input.txt", "r") as file:
	for line in file.readlines():
		game_id = int(line.split(":")[0].split(" ")[1])
		lowest_number_of_cubes = [0, 0, 0]
		games_list = line.split(':')[1].split(";")
		for game in games_list:
			colors = game.split(",")
			for color in colors:
				here_color = color.split(" ")[2]
				number = int(color.split(" ")[1])
				if "red" in color:
					if lowest_number_of_cubes[0] < number:
						lowest_number_of_cubes[0] = number
				if "green" in color:
					if lowest_number_of_cubes[1] < number:
						lowest_number_of_cubes[1] = number
				if "blue" in color:
					if lowest_number_of_cubes[2] < number:
						lowest_number_of_cubes[2] = number
		all_powers_of_cubes.append(numpy.prod(lowest_number_of_cubes))

print(sum(all_powers_of_cubes))

				