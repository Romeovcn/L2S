def check_key_events(pygame, event, running, direction, pause):
	if event.type == pygame.QUIT: # Check for QUIT event
		return False, None, False
	if event.type == pygame.KEYDOWN: # Check for KEYDOWN event
		key = pygame.key.get_pressed()
		if key[pygame.K_ESCAPE] or key[pygame.K_q]:
			running = False
		elif key[pygame.K_w]:
			direction = "UP" 
		elif key[pygame.K_s]:
			direction = "DOWN" 
		elif key[pygame.K_a]:
			direction = "LEFT" 
		elif key[pygame.K_d]:
			direction = "RIGHT"
		elif key[pygame.K_p]: # Pause the game
			pause = True if not pause else False
		# elif key[pygame.K_SPACE]: # Play turn by turn
			# if pause:
				# direction = perform_AI_move(map, snake_pos, epsilon, q_table)
		# elif key[pygame.K_UP]: # Augment speed
		# 	speed = speed - 0.1 if speed - 0.1 > 0 else 0
		# 	print(f"{GREEN}Speed: {speed}{RESET}")
		# elif key[pygame.K_DOWN]: # Decrease speed
		# elif key[pygame.K_b]: # Debug print
	return running, direction, pause