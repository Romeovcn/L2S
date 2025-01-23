import random
from game_algorithm.game_algo import get_cell_value_and_coordinates
from game_algorithm.game_algo import is_move_valid

def perform_AI_move(map, snake_pos, epsilon, q_table):
	possible_moves = get_all_possible_moves(map, snake_pos)# Get list of possible moves
	state = get_state(map, snake_pos)
	action = choose_action(epsilon, possible_moves, q_table, state) # Choose between Explore or Exploit
	q_table[state] = update_q_value(map, snake_pos, q_table, state, action)
	return action # CHANGE THIS

def get_state(map, snake_pos):
	DANGER_UP = 0
	DANGER_DOWN = 0
	DANGER_RIGHT = 0
	DANGER_LEFT = 0

	GREEN_UP = 0
	GREEN_DOWN = 0
	GREEN_RIGHT = 0
	GREEN_LEFT = 0

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
	return state

def choose_action(epsilon, possible_moves, q_table, state):
	if random.uniform(0, 1) < epsilon:
		# Explore: choose a random action
		print("Exploring...")
		action = select_random_move(possible_moves)
	else:
		# Exploit: choose the best known action in q_table
		print("Exploiting...")
		action = get_best_move(q_table, state, possible_moves)
		print(f"ICICICI=>{action}")
	return action

def get_best_move(q_table, state, possible_moves):
	best_move = None
	Q_values = q_table.get(state, None)
	if Q_values is None:
		return select_random_move(possible_moves)
	action = max(possible_moves, key=Q_values.get)
	print(possible_moves)
	print(action)
	print(Q_values)
	return action

def get_all_possible_moves(map, snake_pos):
	directions = ["UP", "DOWN", "LEFT", "RIGHT"]
	possible_moves = []

	for direction in directions:
		target_cell = get_cell_value_and_coordinates(map, snake_pos, direction)
		move_validity = is_move_valid(snake_pos, target_cell)
		if move_validity != 0: # Check if move is not illegal
			# move = {"direction": direction, "target_cell": target_cell}
			possible_moves.append(direction)
	return possible_moves

def select_random_move(possible_moves):
	return random.choice(possible_moves)

def get_reward(map, snake_pos, action):
	# Eats green apple				+10
	# Eats red apple				−20
	# Hits a wall or itself			−100
	# Moves closer to green apple	+1
	# Moves closer to red apple		−1
	# Moves away from both			0
	# Survives one step (optional)	−0.1
	target_cell = get_cell_value_and_coordinates(map, snake_pos, action)
	if target_cell['value'] == "0":
		return -1
	if target_cell['value'] == "G":
		return 100
	if target_cell['value'] == "R":
		return -50
	if target_cell['value'] == "W" or target_cell['value'] == "S":
		return -100
	return 0

# def get_max_q_value(q_values, state, valid_actions): # protect valid actions
# 	"""
# 	returns: {"action": "UP | DOWN | LEFT | RIGHT", "value": 123}
# 	"""
# 	for q_value in q_values:
# 		if q_value["state"] == state:
# 			q_values = q_value["Q_SCORE"]
# 	return max(q_values[action] for action in valid_actions)

# def get_q_value(q_table, state, action):
# 	if action != "UP" and action != "DOWN" and action != "LEFT" and action != "RIGHT":
# 		raise ValueError("get_q_value(): Invalid input: action arg must be 'UP', 'DOWN', 'LEFT', or 'RIGHT'")
# 	values = q_table.get(state, None)
# 	if values is None:
# 		return 0
# 	return values[action]

def update_q_value(map, snake_pos, q_table, state, action): # TO FIX: need to check if q_values exists before updating
	Q_values = q_table.get(state, {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0})
	Q = Q_values[action]
	max_Q = max(Q_values[action] for action in ["UP", "DOWN", "LEFT", "RIGHT"])
	r = get_reward(map, snake_pos, action)
	gamma = 0.9

	Q_values[action] = Q + 0.1 * (r + gamma * max_Q - Q)
	print(Q_values)
	return Q_values