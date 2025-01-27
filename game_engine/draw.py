import pygame

def draw_chessboard(screen, width, height, snake_len, game_data):
	BG_COLOR = (35, 39, 55)
	SQUARE_COLOR = (24, 24, 36)
	GREEN_APPLE_COLOR = (255, 0, 0)
	RED_APPLE_COLOR = (0, 255, 0)
	WALL_COLOR = (255, 255, 255)

	GAME_SIZE = min(width, height)
	SQUARE_SIZE = 48
	ROWS = 12
	COLS = 12
	best_score = game_data["best_score"]
	nb_game = game_data["nb_game"]
	total_score = game_data["total_score"]
	average_score = total_score / nb_game if nb_game > 0 else 0
	average_score = round(average_score, 2)

	screen.fill((0, 0, 0)) # Fill the screen with black
	pygame.draw.rect(screen, BG_COLOR, (100, 100, 598, 598)) # Fill the board
	font = pygame.font.Font(None, 36)
	score_text = font.render(f"Score: {snake_len}", True, (255, 255, 255))
	best_score_text = font.render(f"Best Score: {best_score}", True, (255, 255, 255))
	av_score_text = font.render(f"Average Score: {average_score}", True, (255, 255, 255))
	screen.blit(score_text, (10, 10))
	screen.blit(best_score_text, (200, 10))
	screen.blit(av_score_text, (400, 10))

	for row in range(ROWS):
		for col in range(COLS):
			pygame.draw.rect(screen, SQUARE_COLOR, (col * 50 + 100, row * 50 + 100, 48, 48))

def draw_snake(screen, snake_pos):
	pixel_pos = pygame.Vector2(snake_pos[0] * 100 + 50, snake_pos[1] * 100 + 50)
	pygame.draw.circle(screen, "red", pixel_pos, 50)

def draw_game(screen, map):
	GREEN_APPLE_COLOR = (0, 255, 0)
	RED_APPLE_COLOR = (255, 0, 0)
	WALL_COLOR = (0, 0, 0)
	SNAKE_COLOR = (255, 255, 255)
	HEAD_COLOR = (200, 200, 200)

	FULL_SQUARE_SIZE = 50
	SQUARE_SIZE = 48
	GAME_START_OFFSET = 100

	for y in range(12):
		for x in range(12):
			cell = map[y][x]
			x_offset = x * FULL_SQUARE_SIZE + GAME_START_OFFSET
			y_offset = y * FULL_SQUARE_SIZE + GAME_START_OFFSET
			if cell == "G":
				color = GREEN_APPLE_COLOR
			elif cell == "R":
				color = RED_APPLE_COLOR
			elif cell == "W":
				color = WALL_COLOR
			elif cell == "H":
				color = HEAD_COLOR
			elif cell == "S":
				color = SNAKE_COLOR
				# SNAKE_COLOR = tuple(max(0, c - 20) for c in SNAKE_COLOR)
			
			if cell != "0":
				pygame.draw.rect(screen, color, (x_offset, y_offset, SQUARE_SIZE, SQUARE_SIZE))