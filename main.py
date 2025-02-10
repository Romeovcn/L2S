import cProfile
import pygame
import time
import argparse
import json

from game_engine.game_algorithm import get_cell_value_and_coordinates, is_move_valid, move
from game_engine.generate_map import Map
from game_engine.draw import display_game
from game_engine.events import check_key_events
from q_learning.ai import calculate_next_move

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

def perform_move(map, direction, game_data):
	snake_pos = map.snake_pos

	target_cell = get_cell_value_and_coordinates(map, direction)
	move_validity = is_move_valid(snake_pos, target_cell)
	if move_validity == -1:
		# print(f"{RED}YOU ARE DEAD{RESET}")
		if len(snake_pos) > game_data["best_score"]:
			game_data["best_score"] = len(snake_pos)
		game_data["total_score"] += len(snake_pos)
		game_data["nb_game"] += 1
		return -1
	else:
		move(map, target_cell)
		# map.print()
		return 1

def main():
	parser = argparse.ArgumentParser(description="Q-Learning Snake AI")
	parser.add_argument("--hide-display", dest="hide_display", action="store_true", help="Hide the display of the game", default=False)
	parser.add_argument("--size", type=int, help="Size of the board", required=False, default=10) # Set max size around 50 and min
	parser.add_argument("--verbose", action="store_true", help="Enable verbose mode", required=False, default=False)
	parser.add_argument("--save", action="store_true", help="Save q_values in file", required=False, default=False)
	# parser.add_argument("--learn", action="store_true", help="Enable learning mode", required=False, default=False)
	# parser.add_argument("--sessions", action="store_true", help="Enable learning mode", required=False, default=False)
	# parser.add_argument("--load", action="store_true", help="Enable learning mode", required=False, default=False)
	args = parser.parse_args()
	map = Map(args.size)

	if not args.hide_display:
		pygame.init()
		screen = pygame.display.set_mode((1300, 900), pygame.NOFRAME)
		pygame.display.set_caption("Snake AI")
	else:
		screen = None

	game_data = {"epoch": 0, "nb_game": 0, "total_score": 0, "best_score": 0, "total_nb_moves": 0}
	speed = 0.5
	running = True
	pause = False
	epsilon = 0.8
	min_epsilon = 0.01
	epsilon_decay = 0.995
	q_table = {}

	for episode in range(1000):
		# print(f"Episode: {episode}")
		map.generate_random_map()
		direction = None
		display_game(map, screen, game_data)
		# map.print()

		while running:
			# current_time = pygame.time.get_ticks()
			# for event in pygame.event.get():
			if not args.hide_display:
				running, direction, pause = check_key_events(pygame, running, direction, pause, map)

			if not pause:
				direction = calculate_next_move(map, epsilon, q_table)
				epsilon = max(min_epsilon, epsilon * epsilon_decay) # Decay epsilon
		
			if direction:
				move_validity = perform_move(map, direction, game_data)
				if move_validity == -1:
					break
				display_game(map, screen, game_data)
				game_data["total_nb_moves"] += 1
				direction = None

			# clock.tick(20)
			pass

		if not running:
			break
	
	if not args.hide_display:
		pygame.quit()

	# Round all values
	print(f"Best Score: {game_data['best_score']}")
	print(f"Number of Games: {game_data['nb_game']}")
	print(f"Average Score: {game_data['total_score'] / game_data['nb_game']}")
	print(f"Average moves: {game_data['total_nb_moves'] / game_data['nb_game']}")

	if args.save:
		with open("q_values.txt", "w") as file:
			json.dump(q_table, file)

	# with open("q_values.txt", "r") as file:
	# 	loaded_dict = json.load(file)

if __name__ == "__main__":
	# cProfile.run('main()')
	main()