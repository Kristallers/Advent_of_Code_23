
all_valid_ids = []

with open("puzzle-input.txt", "r") as file:
	for line in file.readlines():
		game_id = int(line.split(":")[0].split(" ")[1])
		all_valid_ids.append(game_id)
		games_list = line.split(':')[1].split(";")
		for game in games_list:
			colors = game.split(",")
			for color in colors:
				if "red" in color.split(" ")[2] and int(color.split(" ")[1]) > 12:
					if game_id in all_valid_ids:
						all_valid_ids.remove(game_id)
				elif "green" in color.split(" ")[2] and int(color.split(" ")[1]) > 13:
					if game_id in all_valid_ids:
						all_valid_ids.remove(game_id)
				elif "blue" in color.split(" ")[2] and int(color.split(" ")[1]) > 14:
					if game_id in all_valid_ids:
						all_valid_ids.remove(game_id)
				# else:
				# 	print("both should be true",color.split(" ")[2] == "red" , int(color.split(" ")[1]) > 12)
			
print(sum(all_valid_ids))