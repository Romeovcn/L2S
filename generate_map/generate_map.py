import random

def get_available_pos(map):
	available_pos = set()

	for row_index, row in enumerate(map):
		for col_index, cell in enumerate(row):
			if cell == "0":
				available_pos.add((row_index, col_index))
	
	return available_pos
	# print(available_pos)

def generate_random_apple(map, value, count):
	available_pos = get_available_pos(map)
	for i in range(count):
		if len(available_pos) == 0:
			print(f"Error: No available position to generate {value} apple")
			return map
		random_position = random.choice(list(available_pos))
		x, y = random_position
		map[x][y] = value
	return map

def generate_random_map():
	map =	[["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]]
	
	snake_head_pos = [random.randint(1, 8), random.randint(1, 8)]
	map[snake_head_pos[0]][snake_head_pos[1]] = "H"

	possibilties = []
	if map[snake_head_pos[0] + 1][snake_head_pos[1]] == "0":
		possibilties.append([snake_head_pos[0] + 1, snake_head_pos[1]])
	if map[snake_head_pos[0] - 1][snake_head_pos[1]] == "0":
		possibilties.append([snake_head_pos[0] - 1, snake_head_pos[1]])
	if map[snake_head_pos[0]][snake_head_pos[1] + 1] == "0":
		possibilties.append([snake_head_pos[0], snake_head_pos[1] + 1])
	if map[snake_head_pos[0]][snake_head_pos[1] - 1] == "0":
		possibilties.append([snake_head_pos[0], snake_head_pos[1] - 1])
	
	snake_first_body_pos = random.choice(possibilties)
	map[snake_first_body_pos[0]][snake_first_body_pos[1]] = "S"

	possibilties = []
	if map[snake_first_body_pos[0] + 1][snake_first_body_pos[1]] == "0":
		possibilties.append([snake_first_body_pos[0] + 1, snake_first_body_pos[1]])
	if map[snake_first_body_pos[0] - 1][snake_first_body_pos[1]] == "0":
		possibilties.append([snake_first_body_pos[0] - 1, snake_first_body_pos[1]])
	if map[snake_first_body_pos[0]][snake_first_body_pos[1] + 1] == "0":
		possibilties.append([snake_first_body_pos[0], snake_first_body_pos[1] + 1])
	if map[snake_first_body_pos[0]][snake_first_body_pos[1] - 1] == "0":
		possibilties.append([snake_first_body_pos[0], snake_first_body_pos[1] - 1])
	
	snake_second_body_pos = random.choice(possibilties)
	map[snake_second_body_pos[0]][snake_second_body_pos[1]] = "S"

	generate_random_apple(map, "G", 2)
	generate_random_apple(map, "R", 1)

	snake_pos = [snake_head_pos, snake_first_body_pos, snake_second_body_pos]

	return map, snake_pos