import random

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"


class Map:
    def __init__(self, size):
        self.size = size
        self.map = None
        self.snake_pos = None
        self.score = 0

    def generate_random_map(self):
        self.map = []

        for i in range(self.size + 2):
            if i == 0 or i == self.size + 1:
                self.map.append(["W"] * (self.size + 2))
            else:
                self.map.append(["W"] + ["0"] * self.size + ["W"])

        X = random.randint(1, self.size)
        Y = random.randint(1, self.size)
        snake_head_pos = [X, Y]
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

        first_body_pos = random.choice(possibilties)
        self.map[first_body_pos[0]][first_body_pos[1]] = "S"

        possibilties = []
        if self.map[first_body_pos[0] + 1][first_body_pos[1]] == "0":
            possibilties.append([first_body_pos[0] + 1, first_body_pos[1]])
        if self.map[first_body_pos[0] - 1][first_body_pos[1]] == "0":
            possibilties.append([first_body_pos[0] - 1, first_body_pos[1]])
        if self.map[first_body_pos[0]][first_body_pos[1] + 1] == "0":
            possibilties.append([first_body_pos[0], first_body_pos[1] + 1])
        if self.map[first_body_pos[0]][first_body_pos[1] - 1] == "0":
            possibilties.append([first_body_pos[0], first_body_pos[1] - 1])

        second_body_pos = random.choice(possibilties)
        self.map[second_body_pos[0]][second_body_pos[1]] = "S"

        self.generate_random_apple("G", 2)
        self.generate_random_apple("R", 1)

        self.snake_pos = [snake_head_pos, first_body_pos, second_body_pos]
        self.score = 3
        self.update_state()

    def print_snake_vision(self):
        snake_y = self.snake_pos[0][0]
        snake_x = self.snake_pos[0][1]
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if x == snake_x or y == snake_y:
                    print(cell, end='')
                else:
                    print(" ", end='')
            print()
        print()

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
        DU, RU, GU = self.__check_up()
        DD, RD, GD = self.__check_down()
        DL, RL, GL = self.__check_left()
        DR, RR, GR = self.__check_right()

        self.state = (
            f"DU_{DU} DD_{DD} DL_{DL} DR_{DR}, "
            f"GU_{GU} GD_{GD} GL_{GL} GR_{GR}, "
            f"RU_{RU} RD_{RD} RL_{RL} RR_{RR}"
        )

    def __check_up(self):
        snake_pos = self.snake_pos
        snake_head = snake_pos[0]
        map = self.map
        first_cell = map[snake_head[0] - 1][snake_head[1]]

        if len(snake_pos) > 1:
            first_body_pos = (snake_pos[1][0], snake_pos[1][1])
            first_cell_pos = (snake_head[0] - 1, snake_head[1])
            if first_body_pos == first_cell_pos:
                return (0, 0, 0)

        if first_cell == "W" or first_cell == "S":
            return (1, 0, 0)
        if first_cell == "G":
            return (0, 0, 1)

        i = snake_head[0] - 1
        while i > 0:
            if map[i][snake_head[1]] == "S":
                break
            if map[i][snake_head[1]] == "G":
                return (0, 0, 2)
            i -= 1
        return (0, 0, 0)

    def __check_down(self):
        snake_pos = self.snake_pos
        snake_head = snake_pos[0]
        map = self.map
        first_cell = map[snake_head[0] + 1][snake_head[1]]

        if len(snake_pos) > 1:
            first_body_pos = (snake_pos[1][0], snake_pos[1][1])
            first_cell_pos = (snake_head[0] + 1, snake_head[1])
            if first_body_pos == first_cell_pos:
                return (0, 0, 0)

        if first_cell == "W" or first_cell == "S":
            return (1, 0, 0)
        if first_cell == "G":
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
            if first_body_pos == first_cell_pos:
                return (0, 0, 0)

        if first_cell == "W" or first_cell == "S":
            return (1, 0, 0)
        if first_cell == "G":
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
            if first_body_pos == first_cell_pos:
                return (0, 0, 0)

        if first_cell == "W" or first_cell == "S":
            return (1, 0, 0)
        if first_cell == "G":
            return (0, 0, 1)

        i = snake_head[1] + 1
        while i < self.size + 1:
            if map[snake_head[0]][i] == "S":
                break
            if map[snake_head[0]][i] == "G":
                return (0, 0, 2)
            i += 1
        return (0, 0, 0)
