from game_engine.game_algorithm import is_move_legal
from q_learning.ai import calculate_next_move



def check_key_events_test(pygame, map, q_table, game_settings, flags):
    """
    Returns: running(True|False), direction(direction|None), pause(True|False)
    """

    while True:
        event = pygame.event.poll()  # Non-blocking event check
        if event.type == pygame.NOEVENT:
            break  # No more events in the queue
        if event.type == pygame.QUIT:  # Check for QUIT event
            flags["running"] = False
        if event.type == pygame.KEYDOWN:  # Check for KEYDOWN event
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE] or key[pygame.K_q]:
                flags["running"] = False
            elif key[pygame.K_p]:  # Pause the game
                print("AI is paused")
                flags['pause'] = True if not flags['pause'] else False
            elif flags['pause']:
                if key[pygame.K_w] and is_move_legal("UP", game_settings['direction']):
                    flags['need_update'] = True
                    game_settings['direction'] = "UP"
                elif key[pygame.K_s] and is_move_legal("DOWN", game_settings['direction']):
                    flags['need_update'] = True
                    game_settings['direction'] = "DOWN"
                elif key[pygame.K_a] and is_move_legal("LEFT", game_settings['direction']):
                    flags['need_update'] = True
                    game_settings['direction'] = "LEFT"
                elif key[pygame.K_d] and is_move_legal("RIGHT", game_settings['direction']):
                    flags['need_update'] = True
                    game_settings['direction'] = "RIGHT"
                elif key[pygame.K_SPACE]:  # Play turn by turn
                    flags['need_update'] = True
                    game_settings['direction'] = calculate_next_move(map, q_table, game_settings, flags)
                elif key[pygame.K_b]:  # Debug print
                    print(f"State: {map.state}")
                    print(f"Q_values: {q_table[map.state]}")
            elif key[pygame.K_UP]:
                if game_settings['speed'] - 20 < 0:
                    game_settings['speed'] = 0
                else:
                    game_settings['speed'] -= 20
                print(game_settings['speed'])
            elif key[pygame.K_DOWN]:
                if game_settings['speed'] + 20 > 500:
                    game_settings['speed'] = 500
                else:
                    game_settings['speed'] += 20
                print(game_settings['speed'])


def check_key_events(pygame, map, q_table, game_settings, flags):
    """
    Returns: running(True|False), direction(direction|None), pause(True|False)
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check for QUIT event
            flags["running"] = False

        if event.type == pygame.KEYDOWN:  # Check for KEYDOWN event
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE] or key[pygame.K_q]:
                flags["running"] = False
            elif key[pygame.K_p]:  # Pause the game
                print("AI is paused")
                flags['pause'] = True if not flags['pause'] else False
            elif flags['pause']:
                if key[pygame.K_w] and is_move_legal("UP", game_settings['direction']):
                    flags['need_update'] = True
                    game_settings['direction'] = "UP"
                elif key[pygame.K_s] and is_move_legal("DOWN", game_settings['direction']):
                    flags['need_update'] = True
                    game_settings['direction'] = "DOWN"
                elif key[pygame.K_a] and is_move_legal("LEFT", game_settings['direction']):
                    flags['need_update'] = True
                    game_settings['direction'] = "LEFT"
                elif key[pygame.K_d] and is_move_legal("RIGHT", game_settings['direction']):
                    flags['need_update'] = True
                    game_settings['direction'] = "RIGHT"
                elif key[pygame.K_SPACE]:  # Play turn by turn
                    flags['need_update'] = True
                    game_settings['direction'] = calculate_next_move(map, q_table, game_settings, flags)
                elif key[pygame.K_b]:  # Debug print
                    print(f"State: {map.state}")
                    print(f"Q_values: {q_table[map.state]}")
            elif key[pygame.K_UP]:
                print("KEY UP")