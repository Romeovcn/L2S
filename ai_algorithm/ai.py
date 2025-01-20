import random
from game_algorithm.game_algo import get_cell_value_and_coordinates
from game_algorithm.game_algo import is_move_valid

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