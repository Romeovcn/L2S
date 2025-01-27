from game_engine.generate_map import generate_random_apple

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

def print_map(map):
	for row in map:
		for cell in row:
			if cell == "R":
				print(RED + cell + RESET, end=" ")
			elif cell == "G":
				print(GREEN + cell + RESET, end=" ")
			elif cell == "H" or cell == "S":
				print(YELLOW + cell + RESET, end=" ")
			elif cell == "W":
				print(CYAN + cell + RESET, end=" ")
			else:
				print(cell, end=" ")
		print()
	print()

def update_snake_pos(snake_pos, pos_to_go, target_cell):
	if target_cell == "0":
		snake_pos.insert(0, pos_to_go)
		snake_pos.pop()
	elif target_cell == "G":
		snake_pos.insert(0, pos_to_go)
	elif target_cell == "R":
		snake_pos.insert(0, pos_to_go)
		snake_pos.pop()
		snake_pos.pop()
	return snake_pos

def erase_old_snake(map, snake_pos):
	for pos in snake_pos:
			map[pos[0]][pos[1]] = "0"

def update_map(map, snake_pos, target_cell):
	for pos in snake_pos:
		if pos == snake_pos[0]:
			map[pos[0]][pos[1]] = "H"
		else:
			map[pos[0]][pos[1]] = "S"
	
	if target_cell == "G":
		apple_pos = generate_random_apple(map, "G", 1)
	if target_cell == "R":
		apple_pos = generate_random_apple(map, "R", 1)

def move(target_cell, map, snake_pos):
	erase_old_snake(map, snake_pos) # Can be optimized by only erasing the last cell of the snake
	snake_pos = update_snake_pos(snake_pos, target_cell['coordinates'], target_cell['value'])
	update_map(map, snake_pos, target_cell['value'])

def get_cell_value_and_coordinates(map, snake_pos, direction):
	snake_head_pos = snake_pos[0]

	if direction == "UP":
		pos_to_go = [snake_head_pos[0] - 1, snake_head_pos[1]]
	elif direction == "DOWN":
		pos_to_go = [snake_head_pos[0] + 1, snake_head_pos[1]]
	elif direction == "LEFT":
		pos_to_go = [snake_head_pos[0], snake_head_pos[1] - 1]
	elif direction == "RIGHT":
		pos_to_go = [snake_head_pos[0], snake_head_pos[1] + 1]
	else:
		return None

	target_cell = map[pos_to_go[0]][pos_to_go[1]]
	return {"value": target_cell, "coordinates": pos_to_go}

def is_move_valid(snake_pos, target_cell):
	"""
	returns: 0 if move is not possible, -1 if player is dead, 1 if move is valid
	"""
	if target_cell['value'] == "0": # On top because it's the most common case
		return 1
	if target_cell['value'] == "W": # Hit a wall
		return -1
	if target_cell['value'] == "R" and len(snake_pos) == 1: # Hit size 0 with red apple
		return -1
	if target_cell['value'] == "S":
		if target_cell['coordinates'] == snake_pos[1]: # Check if going backward
			# print("Going backward")
			return 0
		return -1 # Else means ate itself
	return 1 # If it's a green apple