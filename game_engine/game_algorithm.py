RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"


def update_snake_pos(map, target_cell):
    if target_cell['value'] == "0":
        map.snake_pos.insert(0, target_cell['coordinates'])
        map.snake_pos.pop()
    elif target_cell['value'] == "G":
        map.snake_pos.insert(0, target_cell['coordinates'])
    elif target_cell['value'] == "R":
        map.snake_pos.insert(0, target_cell['coordinates'])
        map.snake_pos.pop()
        map.snake_pos.pop()


def erase_old_snake(map):
    for pos in map.snake_pos:
        map.map[pos[0]][pos[1]] = "0"


def update_map(map, target_cell):
    for pos in map.snake_pos:
        if pos == map.snake_pos[0]:
            map.map[pos[0]][pos[1]] = "H"
        else:
            map.map[pos[0]][pos[1]] = "S"

    if target_cell == "G":
        map.generate_random_apple("G", 1)
    if target_cell == "R":
        map.generate_random_apple("R", 1)


def move(map, target_cell):
    erase_old_snake(map)
    update_snake_pos(map, target_cell)
    update_map(map, target_cell['value'])


def get_target_cell(map, direction):
    """
    returns: {"value": char, "coordinates": [x, y]}
    """
    snake_pos = map.snake_pos
    snake_head_pos = snake_pos[0]

    if direction == "UP":
        pos_to_go = [snake_head_pos[0] - 1, snake_head_pos[1]]
    elif direction == "DOWN":
        pos_to_go = [snake_head_pos[0] + 1, snake_head_pos[1]]
    elif direction == "LEFT":
        pos_to_go = [snake_head_pos[0], snake_head_pos[1] - 1]
    elif direction == "RIGHT":
        pos_to_go = [snake_head_pos[0], snake_head_pos[1] + 1]
    else:
        return None

    target_cell = map.map[pos_to_go[0]][pos_to_go[1]]
    return {"value": target_cell, "coordinates": pos_to_go}


def is_mv_legal(new_direction, old_direction):
    if new_direction == "UP" and old_direction == "DOWN":
        return False
    if new_direction == "DOWN" and old_direction == "UP":
        return False
    if new_direction == "LEFT" and old_direction == "RIGHT":
        return False
    if new_direction == "RIGHT" and old_direction == "LEFT":
        return False
    return True


def is_move_valid(snake_pos, target_cell):
    """
    returns: 0 if move is not possible, -1 if player is dead
    """
    if target_cell['value'] == "0":  # On top because it's the most common case
        return 1
    if target_cell['value'] == "W":  # Hit a wall
        return -1
    if target_cell['value'] == "R" and len(snake_pos) == 1:
        return -1
    if target_cell['value'] == "S":
        return -1
    return 1  # If it's a green apple
