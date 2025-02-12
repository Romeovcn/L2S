import random

from game_engine.game_algorithm import is_move_legal, perform_move
from q_learning.reward import get_reward
from game_engine.draw import display_game

def calculate_next_move(map, epsilon, q_table, learn, direction, screen, game_data):
	Q = 0
	r = 0

	possible_moves = get_all_possible_moves(direction) # Get list of possible moves
	state = map.state
	action = choose_action(epsilon, possible_moves, q_table, map.state, learn) # Choose between Explore or Exploit
	if learn:
		update_q_value(q_table, map.state, action)
	move_validity = perform_move(map, action, game_data)
	if move_validity == -1:
		return False, action
	display_game(map, screen, game_data)
	game_data["total_nb_moves"] += 1
	return True, action

def choose_action(epsilon, possible_moves, q_table, state, learn):
	if learn and random.uniform(0, 1) < epsilon: # Explore: choose a random action
		# print("Exploring...")
		action = select_random_move(possible_moves)
	else: # Exploit: choose the best known action in q_table
		# print("Exploiting...")
		action = get_best_move(q_table, state, possible_moves)
	return action

def get_best_move(q_table, state, possible_moves):
	Q_values = q_table.get(state, None)
	if Q_values is None:
		return select_random_move(possible_moves)

	# best_moves = []
	# best_value = None

	# for move in possible_moves:
	# 	if len(best_moves) == 0:
	# 		best_moves.append(move)
	# 		best_value = Q_values[move]
	# 	elif Q_values[move] == best_value:
	# 		best_moves.append(move)
	# 	elif Q_values[move] > best_value:
	# 		best_moves.clear()
	# 		best_moves.append(move)
	# 		best_value = Q_values[move]

	# if len(best_moves) > 1:
	# 	return select_random_move(best_moves)
	# return best_moves[0]
	action = max(possible_moves, key=Q_values.get)
	return action

def get_all_possible_moves(direction): # Can be optimized
	directions = ["UP", "DOWN", "LEFT", "RIGHT"]
	possible_moves = []

	for new_direction in directions:
		if is_move_legal(new_direction, direction):
			possible_moves.append(new_direction)
	return possible_moves

def select_random_move(possible_moves):
	return random.choice(possible_moves)

def update_q_value(q_table, state, action):
	Q_values = q_table.get(state, {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0})
	Q = Q_values[action]
	max_Q = max(Q_values[action] for action in ["UP", "DOWN", "LEFT", "RIGHT"])
	r = get_reward(state, action)
	gamma = 0.9

	Q_values[action] = Q + 0.1 * (r + gamma * max_Q - Q)
	return Q_values

# def update_q_value(q_table, reward, previous_Q, state, action):
# 	Q_values = q_table.get(state, {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0})
# 	Q = Q_values[action]
# 	max_Q = max(Q_values[action] for action in ["UP", "DOWN", "LEFT", "RIGHT"])
# 	r = get_reward(state, action)
# 	gamma = 0.9

# 	Q_values[action] = previous_Q + 0.1 * (r + gamma * max_Q - previous_Q)
# 	return Q_values

# def get_q_value(q_table, state, action):
# 	Q_values = q_table.get(state, {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0})
# 	Q = Q_values[action]

# 	return Q