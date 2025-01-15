import pygame
from enum import Enum
import random
from generate_map.generate_map import generate_random_map

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

def draw_chessboard(screen, SQUARE_SIZE=100):
	ROWS = 10
	COLS = 10
	PAIR = (34, 129, 34)
	IMPAIR = (34, 120, 34)
	GREEN_APPLE = (255, 0, 0)
	RED_APPLE = (0, 255, 0)
	WALL = (255, 255, 255)

	for row in range(ROWS):
		for col in range(COLS):
			color = PAIR if (row + col) % 2 == 0 else IMPAIR
			pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_snake(screen, snake_pos):
	pixel_pos = pygame.Vector2(snake_pos[0] * 100 + 50, snake_pos[1] * 100 + 50)
	pygame.draw.circle(screen, "red", pixel_pos, 50)

def draw_game(screen, map):
	class Colors(Enum):
		SNAKE_HEAD = (255, 255, 0)
		SNAKE_BODY = (255, 255, 0)
		GREEN_APPLE = (0, 255, 0)
		RED_APPLE = (255, 0, 0)
		WALL = (0, 0, 0)

	for y in range(10):
		for x in range(10):
			cell = map[y][x]
			if cell == "G":
				pygame.draw.circle(screen, (0, 255, 0), (x * 100 + 50, y * 100 + 50), 50)
			elif cell == "R":
				pygame.draw.circle(screen, (255, 0, 0), (x * 100 + 50, y * 100 + 50), 50)
			elif cell == "W":
				pygame.draw.rect(screen, (0, 100, 0), (x * 100, y * 100, 100, 100))
			elif cell == "H":
				pygame.draw.circle(screen, (0, 0, 100), (x * 100 + 50, y * 100 + 50), 50)
			elif cell == "S":
				pygame.draw.circle(screen, (0, 0, 255), (x * 100 + 50, y * 100 + 50), 50)

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

def get_all_possible_moves(snake_pos):
	possible_moves = []
	head = snake_pos[0]
	if (head[0] + 1, head[1]) != snake_pos[1]:
		possible_moves.append((head[0] + 1, head[1]))
	if (head[0] - 1, head[1]) != snake_pos[1]:
		possible_moves.append((head[0] - 1, head[1]))
	if (head[0], head[1] + 1) != snake_pos[1]:
		possible_moves.append((head[0], head[1] + 1))
	if (head[0], head[1] - 1) != snake_pos[1]:
		possible_moves.append((head[0], head[1] - 1))
	return possible_moves

def move(key, map, snake_pos):
	head = snake_pos[0]
	map[head[0]][head[1]] = "S"

	if key == "UP":#key[pygame.K_w]:
		pos_to_go = [head[0] + 1, head[1]]
	if key == "DOWN":#key[pygame.K_s]:
		pos_to_go = [head[0] - 1, head[1]]
	if key == "LEFT":#key[pygame.K_a]:
		pos_to_go = [head[0], head[1] - 1]
	if key == "RIGHT":#key[pygame.K_d]:
		pos_to_go = [head[0], head[1] + 1]
	
	target_cell = map[pos_to_go[0]][pos_to_go[1]]
	print(target_cell)

	if target_cell == "0":
		print("YOU ARE STILL ALIVE")
	elif target_cell == "G":
		print("YOU EAT GREEN APPLE")
	elif target_cell == "R":
		print("YOU EAT RED APPLE")
	elif target_cell == "W":
		print("YOU HIT A WALL")
	elif target_cell == "S":
		previous_cell = snake_pos[1]
		if previous_cell == pos_to_go:
			print("YOU CAN'T GO BACK")
		else:
			print("YOU ATE YOURSELF")
	# print("YOU ARE STILL ALIVE")
	# tail = snake_pos.pop()
	# map[tail[0]][tail[1]] = "0"
	# map[head[0]][head[1]] = "H"
	# print(tail)

def main():
	# q_table = {"W": 0, "0": 0, "G": 0, "R": 0, "S": 0}
	map, snake_pos = generate_random_map()
	print_map(map)
	print(snake_pos)

	move("RIGHT", map, snake_pos)
	# print_map(map)
	# print(snake_pos)
	
	# print(get_all_possible_moves(snake_pos))


	# pygame.init()
	# width, height = 1000, 1000
	# screen = pygame.display.set_mode((width, height))
	# running = True

	# draw_chessboard(screen, width // 10)
	# draw_game(screen, map)
	# while running:
	# 	for event in pygame.event.get():
	# 		# Check for QUIT event
	# 		if event.type == pygame.QUIT:
	# 			running = False
	# 		# Check for KEYDOWN event
	# 		if event.type == pygame.KEYDOWN:
	# 			keys = pygame.key.get_pressed()
	# 			if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
	# 				running = False
	# 			if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
	# 				# move(keys, map)
	# 				draw_chessboard(screen, width // 10)
	# 				# draw_game(screen, map)
	# 	pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()