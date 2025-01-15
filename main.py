import time
import pygame
import random
from generate_map.generate_map import generate_random_map
from generate_map.generate_map import generate_random_apple
from draw_game.draw import draw_chessboard
from draw_game.draw import draw_game

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

def print_map(map):
	for row in map:
		for cell in row:
			if cell == "R":
				print(RED + cell + RESET, end=" ")
			elif cell == "G":
				print(GREEN + cell + RESET, end=" ")
			elif cell == "H" or cell == "S":
				print(YELLOW + cell + RESET, end=" ")
			elif cell == "W":
				print(CYAN + cell + RESET, end=" ")
			else:
				print(cell, end=" ")
		print()

def update_snake_pos(snake_pos, pos_to_go, target_cell):
	new_snake_pos = snake_pos.copy()

	if target_cell == "0":
		snake_pos.insert(0, pos_to_go)
		snake_pos.pop()
	elif target_cell == "G":
		snake_pos.insert(0, pos_to_go)
	elif target_cell == "R":
		snake_pos.insert(0, pos_to_go)
		snake_pos.pop()
		snake_pos.pop()
	return snake_pos

def erase_old_snake(map, snake_pos):
	for pos in snake_pos:
			map[pos[0]][pos[1]] = "0"

def update_map(map, snake_pos, target_cell):
	for pos in snake_pos:
		if pos == snake_pos[0]:
			map[pos[0]][pos[1]] = "H"
		else:
			map[pos[0]][pos[1]] = "S"
	
	if target_cell == "G":
		apple_pos = generate_random_apple(map, "G", 1)
	if target_cell == "R":
		apple_pos = generate_random_apple(map, "R", 1)

def move(direction, map, snake_pos):
	"""
	returns: "DEAD" or "ALIVE"
	"""
	head = snake_pos[0]

	if direction == "UP":
		pos_to_go = [head[0] - 1, head[1]]
	elif direction == "DOWN":
		pos_to_go = [head[0] + 1, head[1]]
	elif direction == "LEFT":
		pos_to_go = [head[0], head[1] - 1]
	elif direction == "RIGHT":
		pos_to_go = [head[0], head[1] + 1]
	else:
		return "PASS"

	target_cell = map[pos_to_go[0]][pos_to_go[1]]

	# ------ Check death ------ #
	if target_cell == "W":
		print(f"{RED}YOU HIT A WALL YOU ARE DEAD{RESET}")
		return "DEAD"
	elif target_cell == "S":
		if pos_to_go == snake_pos[1]:
			return "PASS"
		else:
			print(f"{RED}YOU ATE YOURSELF YOU ARE DEAD{RESET}")
			return "DEAD"
	elif target_cell == "R" and len(snake_pos) == 1:
		print(f"{RED}YOU ATE A RED APPLE YOU ARE DEAD{RESET}")
		return "DEAD"

	# ------ Debug ------ #
	# if target_cell == "0":
	# 	print("YOU ARE STILL ALIVE")
	# elif target_cell == "G":
	# 	print("YOU EAT GREEN APPLE")
	# elif target_cell == "R":
	# 	print("YOU EAT RED APPLE")

	# ------ Update elements ------ #
	erase_old_snake(map, snake_pos) # Can be optimized by only erasing the last cell of the snake
	snake_pos = update_snake_pos(snake_pos, pos_to_go, target_cell)
	update_map(map, snake_pos, target_cell)

	return "ALIVE"

def main():
	map, snake_pos = generate_random_map()
	# print_map(map)
	# print(snake_pos)

	# move("RIGHT", map, snake_pos)
	# print_map(map)
	# print(snake_pos)
	
	pygame.init()
	clock = pygame.time.Clock()
	width, height = 1000, 1000
	screen = pygame.display.set_mode((width, height))
	direction = None
	running = True
	last_move_time = 0
	draw_chessboard(screen, width // 10)
	draw_game(screen, map)
	print_map(map)

	while running:
		for event in pygame.event.get():
			# Check for QUIT event
			if event.type == pygame.QUIT:
				running = False
			# Check for KEYDOWN event
			if event.type == pygame.KEYDOWN:
				key = pygame.key.get_pressed()
				if key[pygame.K_ESCAPE] or key[pygame.K_q]:
					running = False
	
				# Need to check if going backward
				if key[pygame.K_w]:
					direction = "UP"
				elif key[pygame.K_s]:
					direction = "DOWN"
				elif key[pygame.K_a]:
					direction = "LEFT"
				elif key[pygame.K_d]:
					direction = "RIGHT"

		current_time = pygame.time.get_ticks()
		if current_time - last_move_time >= 200:
			player = move(direction, map, snake_pos)
			if player == "DEAD":
				running = False
			elif player == "ALIVE":
				draw_chessboard(screen, width // 10)
				draw_game(screen, map)
				print_map(map)
			last_move_time = current_time  #
	
		pygame.display.flip()
		clock.tick(20)

	pygame.quit()

if __name__ == "__main__":
	main()