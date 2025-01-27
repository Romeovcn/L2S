import random

from game_engine.game_algorithm import get_cell_value_and_coordinates
from game_engine.game_algorithm import is_move_valid
from q_learning.get_state import get_state

def calculate_next_move(map, snake_pos, epsilon, q_table):
	possible_moves = get_all_possible_moves(map, snake_pos) # Get list of possible moves
	state = get_state(map, snake_pos) # Get the current state of the game
	action = choose_action(epsilon, possible_moves, q_table, state) # Choose between Explore or Exploit
	q_table[state] = update_q_value(map, snake_pos, q_table, state, action) # Update the q value of the chosen action
	return action

def choose_action(epsilon, possible_moves, q_table, state):
	if random.uniform(0, 1) < epsilon: # Explore: choose a random action
		print("Exploring...")
		action = select_random_move(possible_moves)
	else: # Exploit: choose the best known action in q_table
		print("Exploiting...")
		action = get_best_move(q_table, state, possible_moves)
		print(f"ICICICI=>{action}")
	return action

def get_best_move(q_table, state, possible_moves):
	Q_values = q_table.get(state, None)
	if Q_values is None:
		return select_random_move(possible_moves)
	action = max(possible_moves, key=Q_values.get)
	return action

def get_all_possible_moves(map, snake_pos): # Can be optimized
	directions = ["UP", "DOWN", "LEFT", "RIGHT"]
	possible_moves = []

	for direction in directions:
		target_cell = get_cell_value_and_coordinates(map, snake_pos, direction)
		move_validity = is_move_valid(snake_pos, target_cell)
		if move_validity != 0:
			possible_moves.append(direction)
	return possible_moves

def select_random_move(possible_moves):
	return random.choice(possible_moves)

def get_reward(map, snake_pos, action): # Can be optimized
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
		return 10
	if target_cell['value'] == "R":
		return -10
	if target_cell['value'] == "W" or target_cell['value'] == "S":
		return -100
	return 0

def update_q_value(map, snake_pos, q_table, state, action):
	Q_values = q_table.get(state, {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0})
	Q = Q_values[action]
	max_Q = max(Q_values[action] for action in ["UP", "DOWN", "LEFT", "RIGHT"])
	r = get_reward(map, snake_pos, action)
	gamma = 0.9

	Q_values[action] = Q + 0.1 * (r + gamma * max_Q - Q)
	return Q_values