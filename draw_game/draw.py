import pygame
from enum import Enum

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