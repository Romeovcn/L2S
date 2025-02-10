from q_learning.get_state import get_state
from q_learning.reward import get_reward
from q_learning.get_state import get_state
from game_engine.game_algorithm import get_cell_value_and_coordinates
from game_engine.game_algorithm import is_move_legal

def check_key_events(pygame, running, direction, pause, map):
	"""
	Returns: running(True|False), direction(direction|None), pause(True|False)
	"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Check for QUIT event
			return False, None, True

		if event.type == pygame.KEYDOWN: # Check for KEYDOWN event
			key = pygame.key.get_pressed()
			if key[pygame.K_ESCAPE] or key[pygame.K_q]:
				return False, None, True
			elif key[pygame.K_w] and pause and is_move_legal(map, "UP"): # and check_move_validty: #  and pause:
				direction = "UP"
			elif key[pygame.K_s] and pause and is_move_legal(map, "DOWN"): #  and pause:
				direction = "DOWN" 
			elif key[pygame.K_a] and pause and is_move_legal(map, "LEFT"): #  and pause:
				direction = "LEFT" 
			elif key[pygame.K_d] and pause and is_move_legal(map, "RIGHT"): #  and pause:
				direction = "RIGHT"
			elif key[pygame.K_p]: # Pause the game
				print("AI is paused")
				pause = True if not pause else False
		# 	# elif key[pygame.K_SPACE]: # Play turn by turn
		# 		# if pause:
		# 			# direction = perform_AI_move(map, snake_pos, epsilon, q_table)
		# 	# elif key[pygame.K_UP]: # Augment speed
		# 	# 	speed = speed - 0.1 if speed - 0.1 > 0 else 0
		# 	# 	print(f"{GREEN}Speed: {speed}{RESET}")
		# 	# elif key[pygame.K_DOWN]: # Decrease speed
			# elif key[pygame.K_b]: # Debug print
			# 	state = get_state(map, snake_pos)
			# 	print(f"State: {state}")
				# for action in ["UP", "DOWN", "LEFT", "RIGHT"]:
				# 	print(f"{action}: {get_reward(state, action)}")
	return running, direction, pause