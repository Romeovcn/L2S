# Example file showing a circle moving on screen
import pygame

def move(key, snake_pos):
	if key[pygame.K_w]:
		snake_pos[1] -= 1
	if key[pygame.K_s]:
		snake_pos[1] += 1
	if key[pygame.K_a]:
		snake_pos[0] -= 1
	if key[pygame.K_d]:
		snake_pos[0] += 1

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

def check_map(map):
	if len(map) != 10:
		raise Exception("Map must have 10 rows")
	if len(map[0]) != 10:
		raise Exception("Map must have 10 columns")
	for row in map:
		for cell in row:
			if cell != "W" and cell != "0" and cell != "G" and cell != "R":
				raise Exception("Map must contain only 'W' (wall) '0' (empty) 'G' (green apple) 'R' (red apple) or ")

def main():
	map =	[["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "0", "0", "0", "0", "0", "0", "0", "0", "W"],
			["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]]

	try:
		check_map(map)
	except Exception as e:
		print(e)
	# snake_pos = [0,	0]
	# pygame.init()
	# width, height = 1000, 1000
	# screen = pygame.display.set_mode((width, height))
	# running = True

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
	# 				move(keys, snake_pos)

	# 	# fill the screen with a color to wipe away anything from last frame
	# 	draw_chessboard(screen, width // 10)
	# 	draw_snake(screen, snake_pos)

	
	# 	# flip() the display to put your work on screen
	# 	pygame.display.flip()

	# pygame.quit()

if __name__ == "__main__":
	main()