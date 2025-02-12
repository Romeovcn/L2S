import random

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

class Map:
	def __init__(self, size):
		self.size = size  # Instance variable
		self.map = None
		self.snake_pos = None
		self.score = 0

	def generate_random_map(self):
		self.map =	[]
		
		for i in range(self.size + 2):
			if i == 0 or i == self.size + 1:
				self.map.append(["W"] * (self.size + 2))
			else:
				self.map.append(["W"] + ["0"] * self.size + ["W"])
	
		snake_head_pos = [random.randint(1, self.size), random.randint(1, self.size)]
		self.map[snake_head_pos[0]][snake_head_pos[1]] = "H"

		possibilties = []
		if self.map[snake_head_pos[0] + 1][snake_head_pos[1]] == "0":
			possibilties.append([snake_head_pos[0] + 1, snake_head_pos[1]])
		if self.map[snake_head_pos[0] - 1][snake_head_pos[1]] == "0":
			possibilties.append([snake_head_pos[0] - 1, snake_head_pos[1]])
		if self.map[snake_head_pos[0]][snake_head_pos[1] + 1] == "0":
			possibilties.append([snake_head_pos[0], snake_head_pos[1] + 1])
		if self.map[snake_head_pos[0]][snake_head_pos[1] - 1] == "0":
			possibilties.append([snake_head_pos[0], snake_head_pos[1] - 1])
		
		snake_first_body_pos = random.choice(possibilties)
		self.map[snake_first_body_pos[0]][snake_first_body_pos[1]] = "S"

		possibilties = []
		if self.map[snake_first_body_pos[0] + 1][snake_first_body_pos[1]] == "0":
			possibilties.append([snake_first_body_pos[0] + 1, snake_first_body_pos[1]])
		if self.map[snake_first_body_pos[0] - 1][snake_first_body_pos[1]] == "0":
			possibilties.append([snake_first_body_pos[0] - 1, snake_first_body_pos[1]])
		if self.map[snake_first_body_pos[0]][snake_first_body_pos[1] + 1] == "0":
			possibilties.append([snake_first_body_pos[0], snake_first_body_pos[1] + 1])
		if self.map[snake_first_body_pos[0]][snake_first_body_pos[1] - 1] == "0":
			possibilties.append([snake_first_body_pos[0], snake_first_body_pos[1] - 1])
		
		snake_second_body_pos = random.choice(possibilties)
		self.map[snake_second_body_pos[0]][snake_second_body_pos[1]] = "S"

		self.generate_random_apple("G", 2)
		self.generate_random_apple("R", 1)

		self.snake_pos = [snake_head_pos, snake_first_body_pos, snake_second_body_pos]
		self.score = 3

	def print(self):
		for row in self.map:
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
		print()

	def generate_random_apple(self, value, count):
		available_pos = self.get_available_pos()
		for _ in range(count):
			if len(available_pos) == 0:
				# print(f"Error: No available position to generate {value} apple")
				return
			random_position = random.choice(list(available_pos))
			x, y = random_position
			self.map[x][y] = value

	def get_available_pos(self):
		available_pos = set()

		for row_index, row in enumerate(self.map):
			for col_index, cell in enumerate(row):
				if cell == "0":
					available_pos.add((row_index, col_index))
		
		return available_pos