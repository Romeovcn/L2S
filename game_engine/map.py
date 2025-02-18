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
		self.update_state()

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
	
	def update_state(self):
		# Check if there is a danger in the next cell in this direction. 0: No, 1: Yes
		DANGER_UP = 0
		DANGER_DOWN = 0
		DANGER_RIGHT = 0
		DANGER_LEFT = 0

		# Check if there is a green apple in this direction. 0: No, 1: Yes in the direct next cell, 2: Yes and no obstacles
		GREEN_UP = 0
		GREEN_DOWN = 0
		GREEN_RIGHT = 0
		GREEN_LEFT = 0

		# Check if there is a red apple in the next cell in this direction. 0: No, 1: Yes
		RED_UP = 0
		RED_DOWN = 0
		RED_RIGHT = 0
		RED_LEFT = 0

		snake_head = self.snake_pos[0]

		UP = self.map[snake_head[0] - 1][snake_head[1]]
		DOWN = self.map[snake_head[0] + 1][snake_head[1]]
		LEFT = self.map[snake_head[0]][snake_head[1] - 1]
		RIGHT = self.map[snake_head[0]][snake_head[1] + 1]

		DANGER_UP, RED_UP, GREEN_UP = self.__check_up()
		DANGER_DOWN, RED_DOWN, GREEN_DOWN = self.__check_down()
		DANGER_LEFT, RED_LEFT, GREEN_LEFT = self.__check_left()
		DANGER_RIGHT, RED_RIGHT, GREEN_RIGHT = self.__check_right()

		self.state = f"DU_{DANGER_UP} DD_{DANGER_DOWN} DL_{DANGER_LEFT} DR_{DANGER_RIGHT}, GU_{GREEN_UP} GD_{GREEN_DOWN} GL_{GREEN_LEFT} GR_{GREEN_RIGHT}, RU_{RED_UP} RD_{RED_DOWN} RL_{RED_LEFT} RR_{RED_RIGHT}"

	def __check_up(self):
		snake_pos = self.snake_pos
		snake_head = snake_pos[0]
		map = self.map

		first_cell = map[snake_head[0] - 1][snake_head[1]]
		if len(snake_pos) > 1: 
			first_body_pos = (snake_pos[1][0], snake_pos[1][1])
			first_cell_pos = (snake_head[0] - 1, snake_head[1])

			if first_body_pos == first_cell_pos: # Check if going backward
				return (0, 0, 0)
		if first_cell == "W" or first_cell == "S":
			return (1, 0, 0)
		if first_cell == "S":
			return (1, 0, 0)
		if first_cell == "G": # check if first cell is green apple returns (0, 1, 0)
			return (0, 0, 1)
		# if first_cell == "R": # check if first cell is red apple returns (0, 1, 0)
		# 	red_apple = 1
		# 	return (0, 1, 0)
		i = snake_head[0] - 1
		while i > 0:
			if map[i][snake_head[1]] == "S":
				break
			if map[i][snake_head[1]] == "G":
				return (0, 0, 2)
			i -= 1
		return (0, 0, 0) # IS_DANGER: Boolean, RED_APPLE: Boolean, GREEN_APPLE: 0: 0, 1: 1, 3: 1 in direction

	def __check_down(self):
		snake_pos = self.snake_pos
		snake_head = snake_pos[0]
		map = self.map
	
		first_cell = map[snake_head[0] + 1][snake_head[1]]
		if len(snake_pos) > 1: 
			first_body_pos = (snake_pos[1][0], snake_pos[1][1])
			first_cell_pos = (snake_head[0] + 1, snake_head[1])

			if first_body_pos == first_cell_pos: # Check if going backward
				return (0, 0, 0)
		if first_cell == "W" or first_cell == "S":
			return (1, 0, 0)
		# if first_cell == "R": # check if first cell is red apple returns (0, 1, 0)
		# 	return (0, 1, 0)
		if first_cell == "G": # check if first cell is green apple returns (0, 1, 0)
			return (0, 0, 1)
		i = snake_head[0] + 1
		while i < self.size + 1:
			if map[i][snake_head[1]] == "S":
				break
			if map[i][snake_head[1]] == "G":
				return (0, 0, 2)
			i += 1
		return (0, 0, 0)

	def __check_left(self):
		snake_pos = self.snake_pos
		snake_head = snake_pos[0]
		map = self.map

		first_cell = map[snake_head[0]][snake_head[1] - 1]
		if len(snake_pos) > 1: 
			first_body_pos = (snake_pos[1][0], snake_pos[1][1])
			first_cell_pos = (snake_head[0], snake_head[1] - 1)

			if first_body_pos == first_cell_pos: # Check if going backward
				return (0, 0, 0)
		if first_cell == "W" or first_cell == "S":
			return (1, 0, 0)
		# if first_cell == "R": # check if first cell is red apple returns (0, 1, 0)
		# 	return (0, 1, 0)
		if first_cell == "G": # check if first cell is green apple returns (0, 1, 0)
			return (0, 0, 1)
		i = snake_head[1] - 1
		while i > 0:
			if map[snake_head[0]][i] == "S":
				break
			if map[snake_head[0]][i] == "G":
				return (0, 0, 2)
			i -= 1
		return (0, 0, 0)

	def __check_right(self):
		snake_pos = self.snake_pos
		snake_head = snake_pos[0]
		map = self.map

		first_cell = map[snake_head[0]][snake_head[1] + 1]
		if len(snake_pos) > 1: 
			first_body_pos = (snake_pos[1][0], snake_pos[1][1])
			first_cell_pos = (snake_head[0], snake_head[1] + 1)

			if first_body_pos == first_cell_pos: # Check if going backward
				return (0, 0, 0)
		if first_cell == "W" or first_cell == "S":
			return (1, 0, 0)
		# if first_cell == "R": # check if first cell is red apple returns (0, 1, 0)
		# 	return (0, 1, 0)
		if first_cell == "G": # check if first cell is green apple returns (0, 1, 0)
			return (0, 0, 1)
		i = snake_head[1] + 1
		while i < self.size + 1:
			if map[snake_head[0]][i] == "S":
				break
			if map[snake_head[0]][i] == "G":
				return (0, 0, 2)
			i += 1
		return (0, 0, 0)