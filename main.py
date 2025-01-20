import time
import pygame
import random
from generate_map.generate_map import generate_random_map
from draw_game.draw import draw_chessboard
from draw_game.draw import draw_game
from ai_algorithm.ai import get_all_possible_moves
from ai_algorithm.ai import select_random_move
from game_algorithm.game_algo import get_cell_value_and_coordinates
from game_algorithm.game_algo import print_map
from game_algorithm.game_algo import is_move_valid
from game_algorithm.game_algo import move

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

def main():
	map, snake_pos = generate_random_map()
	pygame.init()
	clock = pygame.time.Clock()
	width, height = 700, 700
	screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
	pygame.display.set_caption("Snake AI")

	direction = None
	running = True
	draw_chessboard(screen, width, height, 3)
	draw_game(screen, map)
	print_map(map)

	while running:
		for event in pygame.event.get():
			# Check for QUIT event
			if event.type == pygame.QUIT:
				running = False
				break
			# Check for KEYDOWN event
			if event.type == pygame.KEYDOWN:
				key = pygame.key.get_pressed()
				if key[pygame.K_ESCAPE] or key[pygame.K_q]:
					running = False
					break
				# Need to check if going backward
				elif key[pygame.K_w]:
					direction = "UP" 
				elif key[pygame.K_s]:
					direction = "DOWN" 
				elif key[pygame.K_a]:
					direction = "LEFT" 
				elif key[pygame.K_d]:
					direction = "RIGHT"
				elif key[pygame.K_SPACE]:
					possible_moves = get_all_possible_moves(map, snake_pos)
					random_move = select_random_move(possible_moves)
					direction = random_move['direction']
					# print(select_random_move(possible_moves))
					# Get list of possible moves
					# Select the best move or random move
					# direction = "AI"
					# continue

				target_cell = get_cell_value_and_coordinates(map, snake_pos, direction)
				move_validity = is_move_valid(snake_pos, target_cell)
				if move_validity == 0:
					pass
				elif move_validity == -1:
					running = False
					print(f"{RED}YOU ARE DEAD{RESET}")
				else:
					move(target_cell, map, snake_pos)
					draw_chessboard(screen, width, height, len(snake_pos))
					draw_game(screen, map)
					print_map(map)
					pass
	
		pygame.display.flip()
	pygame.quit()

if __name__ == "__main__":
	main()

# Action would be: UP, DOWN, LEFT, RIGHT
# State would be: DANGER_RIGHT, DANGER_LEFT, DANGER_UP, DANGER_DOWN, APPLE_RIGHT, APPLE_LEFT, APPLE_UP, APPLE_DOWN