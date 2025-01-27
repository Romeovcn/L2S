def check_up(map, snake_pos):
	pass

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

	state = f"DU_{DANGER_UP} DD_{DANGER_DOWN} DL_{DANGER_LEFT} DR_{DANGER_RIGHT}, GU_{GREEN_UP} GD_{GREEN_DOWN} GL_{GREEN_LEFT} GR_{GREEN_RIGHT}, RU_{RED_UP} RD_{RED_DOWN} RL_{RED_LEFT} RR_{RED_RIGHT}"
	print(state)
	return state

# DU_{DANGER_UP} DD_{DANGER_DOWN} DL_{DANGER_LEFT} DR_{DANGER_RIGHT}, GU_{GREEN_UP} GD_{GREEN_DOWN} GL_{GREEN_LEFT} GR_{GREEN_RIGHT}, RU_{RED_UP} RD_{RED_DOWN} RL_{RED_LEFT} RR_{RED_RIGHT}