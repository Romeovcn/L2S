import random
from game_algorithm.game_algo import get_cell_value_and_coordinates
from game_algorithm.game_algo import is_move_valid

def perform_AI_move(map, snake_pos):
	# Get list of possible moves
	# Choose between Explore or Exploit
	# If Explore, choose a random move and update the q-table
	# If exploit get q-value for each move, choose the best and update the q-table
	pass

def get_all_possible_moves(map, snake_pos):
	directions = ["UP", "DOWN", "LEFT", "RIGHT"]
	possible_moves = []

	for direction in directions:
		target_cell = get_cell_value_and_coordinates(map, snake_pos, direction)
		move_validity = is_move_valid(snake_pos, target_cell)
		if move_validity != 0: # Check if move is not illegal
			move = {"direction": direction, "target_cell": target_cell}
			possible_moves.append(move)
	return possible_moves

def select_random_move(possible_moves):
	return random.choice(possible_moves)

def get_reward(target_cell):
	# Eats green apple				+10
	# Eats red apple				−20
	# Hits a wall or itself			−100
	# Moves closer to green apple	+1
	# Moves closer to red apple		−1
	# Moves away from both			0
	# Survives one step (optional)	−0.1
	if target_cell == "0":
		return -1
	if target_cell == "G":
		return 10
	if target_cell == "R":
		return -5
	if target_cell == "W" or target_cell == "S":
		return -10
	return 0

def get_max_q_value(q_values, state, valid_actions): # protect valid actions
	for q_value in q_values:
		if q_value["state"] == state:
			q_values = q_value["Q_SCORE"]
	return max(q_values[action] for action in valid_actions)

def get_q_value(q_values, state, action):
	if action != "UP" and action != "DOWN" and action != "LEFT" and action != "RIGHT":
		raise ValueError("get_q_value(): Invalid input: action arg must be 'UP', 'DOWN', 'LEFT', or 'RIGHT'")

	# q_values = [
	# 	{	"state":	{"DANGER_RIGHT": 0, "DANGER_LEFT": 0, "DANGER_UP": 0, "DANGER_DOWN": 0,
   	# 					"APPLE_RIGHT": 0, "APPLE_LEFT": 0, "APPLE_UP": 0, "APPLE_DOWN": 0},
	# 		"Q_SCORE":	{'UP': 0, 'DOWN': 0, 'LEFT': 0, 'RIGHT': 0}},
	# ]
	for q_value in q_values:
		if q_value["state"] == state:
			return q_value["Q_SCORE"][action]
	return 0

# def choose_action(state):
    # if random.uniform(0, 1) < epsilon:
        # Explore: choose a random action
    # else:
        # Exploit: choose the best known action

# Q = get_q_value()
# r = get_reward("G")
# gamma = 0.9

# Q = Q + 0.1 * (r + gamma * get_max_q_value(Q, "S") - Q)