import time
import pygame
import random
from game_algorithm.game_algo import get_cell_value_and_coordinates, print_map, is_move_valid, move, is_move_valid
from ai_algorithm.ai import perform_AI_move
from generate_map.generate_map import generate_random_map
from draw_game.draw import draw_chessboard, draw_game

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

def main():
	pygame.init()
	width, height = 700, 700
	screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
	pygame.display.set_caption("Snake AI")

	running = True
	epsilon = 1.0         # Exploration rate
	min_epsilon = 0.01    # Minimum exploration rate
	epsilon_decay = 0.995 # Decay factor for epsilon
	q_table = {}          # Q-table

	for episode in range(1000):
		print(f"Episode: {episode}")
		map, snake_pos = generate_random_map()
		direction = None
		draw_chessboard(screen, width, height, 3)
		draw_game(screen, map)
		pygame.display.flip()
		print_map(map)

		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: # Check for QUIT event
					running = False
					break
				if event.type == pygame.KEYDOWN: # Check for KEYDOWN event
					key = pygame.key.get_pressed()
					if key[pygame.K_ESCAPE] or key[pygame.K_q]:
						running = False
						break
					elif key[pygame.K_w]:
						direction = "UP" 
					elif key[pygame.K_s]:
						direction = "DOWN" 
					elif key[pygame.K_a]:
						direction = "LEFT" 
					elif key[pygame.K_d]:
						direction = "RIGHT"
					elif key[pygame.K_SPACE]:
						direction = perform_AI_move(map, snake_pos, epsilon, q_table)

			if direction:
				target_cell = get_cell_value_and_coordinates(map, snake_pos, direction)
				move_validity = is_move_valid(snake_pos, target_cell)
				if move_validity == 0:
					pass
				elif move_validity == -1:
					print(f"{RED}YOU ARE DEAD{RESET}")
					break
				else:
					move(target_cell, map, snake_pos)
					draw_chessboard(screen, width, height, len(snake_pos))
					draw_game(screen, map)
					pygame.display.flip()
					print_map(map)
					epsilon = max(min_epsilon, epsilon * epsilon_decay) # Decay epsilon
					pass
				direction = None

		if not running:
			break
	
	pygame.quit()

if __name__ == "__main__":
	main()

# The Q-Learning Algorithm

# The Q-value (or action-value) represents the quality of a particular action A taken in a specific state S.
# Specifically, it estimates the expected cumulative reward the agent can achieve if it starts in state S,
# takes action A, and then follows the optimal policy thereafter.

# Exploration / Exploitation

# This phase is not part of the q-learning algorithm, but it is a common strategy used in reinforcement learning.
# Common Strategies for Exploration/Exploitation:
# - Epsilon-Greedy Strategy:
# - Boltzmann Exploration:

# State and Action

# State are the features that describe the environment. (We must define them)
# Action would be: UP, DOWN, LEFT, RIGHT
# State would be: DANGER_RIGHT, DANGER_LEFT, DANGER_UP, DANGER_DOWN, APPLE_RIGHT, APPLE_LEFT, APPLE_UP, APPLE_DOWN