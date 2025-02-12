from q_learning.get_state import get_state
from q_learning.get_state import get_state
from game_engine.game_algorithm import is_move_legal
from q_learning.ai import calculate_next_move

def check_key_events(pygame, running, direction, pause, map, q_table, epsilon, learn, need_update=False):
	"""
	Returns: running(True|False), direction(direction|None), pause(True|False)
	"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Check for QUIT event
			return False, None, True, False

		if event.type == pygame.KEYDOWN: # Check for KEYDOWN event
			key = pygame.key.get_pressed()
			if key[pygame.K_ESCAPE] or key[pygame.K_q]:
				return False, None, True, False
			elif key[pygame.K_w] and pause and is_move_legal("UP", direction): # and check_move_validty: #  and pause:
				need_update = True
				direction = "UP"
			elif key[pygame.K_s] and pause and is_move_legal("DOWN", direction): #  and pause:
				need_update = True
				direction = "DOWN" 
			elif key[pygame.K_a] and pause and is_move_legal("LEFT", direction): #  and pause:
				need_update = True
				direction = "LEFT" 
			elif key[pygame.K_d] and pause and is_move_legal("RIGHT", direction): #  and pause:
				need_update = True
				direction = "RIGHT"
			elif key[pygame.K_p]: # Pause the game
				print("AI is paused")
				pause = True if not pause else False
			elif key[pygame.K_SPACE] and pause: # Play turn by turn
				direction = calculate_next_move(map, epsilon, q_table, learn, direction)
				need_update = True
			elif key[pygame.K_b]: # Debug print
				state = get_state(map)
				print(f"State: {state}")
				print(f"Q_values: {q_table[state]}")
				# for action in ["UP", "DOWN", "LEFT", "RIGHT"]:
				# 	print(f"{action}: {get_reward(state, action)}")
		# 	# elif key[pygame.K_UP]: # Augment speed
		# 	# 	speed = speed - 0.1 if speed - 0.1 > 0 else 0
		# 	# 	print(f"{GREEN}Speed: {speed}{RESET}")
		# 	# elif key[pygame.K_DOWN]: # Decrease speed
	return running, direction, pause, need_update