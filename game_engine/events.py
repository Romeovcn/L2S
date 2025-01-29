from q_learning.get_state import get_state

def check_key_events(pygame, event, running, direction, pause, map, snake_pos):
	"""
	Returns: running(True|False), direction(direction|None), pause(True|False)
	"""
	if event.type == pygame.QUIT: # Check for QUIT event
		return False, False, None, False

	if event.type == pygame.KEYDOWN: # Check for KEYDOWN event
		key = pygame.key.get_pressed()
		if key[pygame.K_ESCAPE] or key[pygame.K_q]:
			running = False
		elif key[pygame.K_w] and pause: #  and pause:
			print("UP")
			direction = "UP"
		elif key[pygame.K_s] and pause: #  and pause:
			print("DOWN")
			direction = "DOWN" 
		elif key[pygame.K_a] and pause: #  and pause:
			print("LEFT")
			direction = "LEFT" 
		elif key[pygame.K_d] and pause: #  and pause:
			print("RIGHT")
			direction = "RIGHT"
		elif key[pygame.K_p]: # Pause the game
			print("AI is paused")
			pause = True if not pause else False
		# elif key[pygame.K_SPACE]: # Play turn by turn
			# if pause:
				# direction = perform_AI_move(map, snake_pos, epsilon, q_table)
		# elif key[pygame.K_UP]: # Augment speed
		# 	speed = speed - 0.1 if speed - 0.1 > 0 else 0
		# 	print(f"{GREEN}Speed: {speed}{RESET}")
		# elif key[pygame.K_DOWN]: # Decrease speed
		elif key[pygame.K_b]: # Debug print
			get_state(map, snake_pos)
	# print(running, need_update, direction, pause)
	return running, direction, pause