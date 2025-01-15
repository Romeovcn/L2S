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