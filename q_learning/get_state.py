def check_up(map, snake_pos):
	snake_head = snake_pos[0]
	first_cell = map[snake_head[0] - 1][snake_head[1]]
	
	if len(snake_pos) > 1: 
		first_body_pos = (snake_pos[1][0], snake_pos[1][1])
		first_cell_pos = (snake_head[0] - 1, snake_head[1])

		if first_body_pos == first_cell_pos: # Check if going backward
			return (False, False, False)
	if first_cell == "W" or first_cell == "S":
		return (True, False, False)
	if first_cell == "S":
		return (True, False, False)
	if first_cell == "R": # check if first cell is red apple returns (False, True, False)
		return (False, True, False)
	if first_cell == "G": # check if first cell is green apple returns (False, True, False)
		return (False, False, 1)
	# print(f"snake_head: {snake_head}")
	i = snake_head[0] - 1
	while i > 0:
		# print(f"checking: ({i}, {snake_head[1]})")
		if map[i][snake_head[1]] == "G":
			return (False, False, 2)
		i -= 1
	return (False, False, False) # IS_DANGER: Boolean, RED_APPLE: Boolean, GREEN_APPLE: 0: False, 1: True, 3: True in direction

def check_down(map, snake_pos):
	snake_head = snake_pos[0]
	first_cell = map[snake_head[0] + 1][snake_head[1]]

	if len(snake_pos) > 1: 
		first_body_pos = (snake_pos[1][0], snake_pos[1][1])
		first_cell_pos = (snake_head[0] + 1, snake_head[1])

		if first_body_pos == first_cell_pos: # Check if going backward
			return (False, False, False)
	if first_cell == "W" or first_cell == "S":
		return (True, False, False)
	if first_cell == "R": # check if first cell is red apple returns (False, True, False)
		return (False, True, False)
	if first_cell == "G": # check if first cell is green apple returns (False, True, False)
		return (False, False, 1)
	# print(f"snake_head: {snake_head}")
	i = snake_head[0] + 1
	while i < 11:
		# print(f"checking: ({i}, {snake_head[1]})")
		if map[i][snake_head[1]] == "G":
			return (False, False, 2)
		i += 1
	return (False, False, False)

def check_left(map, snake_pos):
	snake_head = snake_pos[0]
	first_cell = map[snake_head[0]][snake_head[1] - 1]

	if len(snake_pos) > 1: 
		first_body_pos = (snake_pos[1][0], snake_pos[1][1])
		first_cell_pos = (snake_head[0], snake_head[1] - 1)

		if first_body_pos == first_cell_pos: # Check if going backward
			return (False, False, False)
	if first_cell == "W" or first_cell == "S":
		return (True, False, False)
	if first_cell == "R": # check if first cell is red apple returns (False, True, False)
		return (False, True, False)
	if first_cell == "G": # check if first cell is green apple returns (False, True, False)
		return (False, False, 1)
	# print(f"snake_head: {snake_head}")
	i = snake_head[1] - 1
	while i > 0:
		# print(f"checking: ({i}, {snake_head[1]})")
		if map[snake_head[0]][i] == "G":
			return (False, False, 2)
		i -= 1
	return (False, False, False)

def check_right(map, snake_pos):
	snake_head = snake_pos[0]
	first_cell = map[snake_head[0]][snake_head[1] + 1]
	
	if len(snake_pos) > 1: 
		first_body_pos = (snake_pos[1][0], snake_pos[1][1])
		first_cell_pos = (snake_head[0], snake_head[1] + 1)

		if first_body_pos == first_cell_pos: # Check if going backward
			return (False, False, False)
	if first_cell == "W" or first_cell == "S":
		return (True, False, False)
	if first_cell == "R": # check if first cell is red apple returns (False, True, False)
		return (False, True, False)
	if first_cell == "G": # check if first cell is green apple returns (False, True, False)
		return (False, False, 1)
	# print(f"snake_head: {snake_head}")
	i = snake_head[1] + 1
	while i < 11:
		# print(f"checking: ({i}, {snake_head[1]})")
		if map[snake_head[0]][i] == "G":
			return (False, False, 2)
		i += 1
	return (False, False, False)

def get_state(map, snake_pos):
	# Check if there is a danger in the next cell in this direction. 0: No, 1: Yes
	DANGER_UP = 0
	DANGER_DOWN = 0
	DANGER_RIGHT = 0
	DANGER_LEFT = 0

	# Check if there is a green apple in this direction. 0: No, 1: Yes and no obstacles, 2: Yes in the direct next cell
	GREEN_UP = 0
	GREEN_DOWN = 0
	GREEN_RIGHT = 0
	GREEN_LEFT = 0

	# Check if there is a red apple in the next cell in this direction. 0: No, 1: Yes
	RED_UP = 0
	RED_DOWN = 0
	RED_RIGHT = 0
	RED_LEFT = 0

	snake_head = snake_pos[0]

	UP = map[snake_head[0] - 1][snake_head[1]]
	DOWN = map[snake_head[0] + 1][snake_head[1]]
	LEFT = map[snake_head[0]][snake_head[1] - 1]
	RIGHT = map[snake_head[0]][snake_head[1] + 1]

	if UP == "W" or UP == "S":
		DANGER_UP = 1
	elif UP == "G":
		GREEN_UP = 1
	elif UP == "R":
		RED_UP = 1

	if DOWN == "W" or DOWN == "S":
		DANGER_DOWN = 1
	elif DOWN == "G":
		GREEN_DOWN = 1
	elif DOWN == "R":
		RED_DOWN = 1

	if LEFT == "W" or LEFT == "S":
		DANGER_LEFT = 1
	elif LEFT == "G":
		GREEN_LEFT = 1
	elif LEFT == "R":
		RED_LEFT = 1

	if RIGHT == "W" or RIGHT == "S":
		DANGER_RIGHT = 1
	elif RIGHT == "G":
		GREEN_RIGHT = 1
	elif RIGHT == "R":
		RED_RIGHT = 1

	DANGER_UP, RED_UP, GREEN_UP = check_up(map, snake_pos)
	DANGER_DOWN, RED_DOWN, GREEN_DOWN = check_down(map, snake_pos)
	DANGER_LEFT, RED_LEFT, GREEN_LEFT = check_left(map, snake_pos)
	DANGER_RIGHT, RED_RIGHT, GREEN_RIGHT = check_right(map, snake_pos)
	# down = check_down(map, snake_pos)
	# left = check_left(map, snake_pos)
	# right = check_right(map, snake_pos)
	# print(f"up:{up}")
	# print(f"down:{down}")
	# print(f"left:{left}")
	# print(f"right:{right}")

	state = f"DU_{DANGER_UP} DD_{DANGER_DOWN} DL_{DANGER_LEFT} DR_{DANGER_RIGHT}, GU_{GREEN_UP} GD_{GREEN_DOWN} GL_{GREEN_LEFT} GR_{GREEN_RIGHT}, RU_{RED_UP} RD_{RED_DOWN} RL_{RED_LEFT} RR_{RED_RIGHT}"
	print(state)
	return state

# DU_{DANGER_UP} DD_{DANGER_DOWN} DL_{DANGER_LEFT} DR_{DANGER_RIGHT}, GU_{GREEN_UP} GD_{GREEN_DOWN} GL_{GREEN_LEFT} GR_{GREEN_RIGHT}, RU_{RED_UP} RD_{RED_DOWN} RL_{RED_LEFT} RR_{RED_RIGHT}