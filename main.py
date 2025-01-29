import cProfile
import pygame
import random
import time

from game_engine.game_algorithm import get_cell_value_and_coordinates, print_map, is_move_valid, move
from game_engine.generate_map import generate_random_map
from game_engine.draw import draw_chessboard, draw_game
from game_engine.events import check_key_events
from q_learning.ai import calculate_next_move

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

def perform_move(map, snake_pos, direction, game_data, screen, width, height):
	target_cell = get_cell_value_and_coordinates(map, snake_pos, direction)
	move_validity = is_move_valid(snake_pos, target_cell)
	if move_validity == 0:
		pass
	elif move_validity == -1:
		print(f"{RED}YOU ARE DEAD{RESET}")
		if len(snake_pos) > game_data["best_score"]:
			game_data["best_score"] = len(snake_pos)
		game_data["total_score"] += len(snake_pos)
		game_data["nb_game"] += 1
		return -1
	else:
		move(target_cell, map, snake_pos)
		draw_chessboard(screen, width, height, len(snake_pos), game_data)
		draw_game(screen, map)
		pygame.display.flip()
		print_map(map)
		pass

# def get_direction(snake_pos):

def main():
	pygame.init()
	width, height = 700, 700
	screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
	pygame.display.set_caption("Snake AI")
	clock = pygame.time.Clock()

	game_data = {"epoch": 0, "nb_game": 0, "total_score": 0, "best_score": 0}
	speed = 0.5
	running = True
	pause = False
	epsilon = 0.8
	min_epsilon = 0.01
	epsilon_decay = 0.995
	q_table = {}

	for episode in range(1000):
		print(f"Episode: {episode}")
		map, snake_pos = generate_random_map()
		direction = None
		draw_chessboard(screen, width, height, 3, game_data)
		draw_game(screen, map)
		pygame.display.flip()
		print_map(map)

		while running:
			# current_time = pygame.time.get_ticks()
			for event in pygame.event.get():
					running, direction, pause = check_key_events(pygame, event, running, direction, pause, map, snake_pos)

			if not pause:
				direction = calculate_next_move(map, snake_pos, epsilon, q_table)
				epsilon = max(min_epsilon, epsilon * epsilon_decay) # Decay epsilon

			if direction:
				print(f"Direction: {direction}")	
				if perform_move(map, snake_pos, direction, game_data, screen, width, height) == -1:
					break
				direction = None

			# clock.tick(20)

		if not running:
			break
	
	pygame.quit()

if __name__ == "__main__":
	# cProfile.run('main()')
	main()