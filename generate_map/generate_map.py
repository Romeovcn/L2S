import random

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

	green_apple_count = 0
	while green_apple_count != 2:
		green_apple_pos = (random.randint(1, 8), random.randint(1, 8))
		if map[green_apple_pos[0]][green_apple_pos[1]] == "0":
			map[green_apple_pos[0]][green_apple_pos[1]] = "G"
			green_apple_count += 1

	while True:
		red_apple_pos = (random.randint(1, 8), random.randint(1, 8))
		if map[red_apple_pos[0]][red_apple_pos[1]] == "0":
			map[red_apple_pos[0]][red_apple_pos[1]] = "R"
			break
	snake_pos = [snake_head_pos, snake_first_body_pos, snake_second_body_pos]
	return map, snake_pos