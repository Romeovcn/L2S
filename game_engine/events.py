from game_engine.game_algorithm import is_mv_legal
from q_learning.ai import calc_move


def check_key_events(pygame, map, q_table, settings, flags):
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
                if key[pygame.K_w] and is_mv_legal("UP", settings['dir']):
                    flags['need_update'] = True
                    settings['dir'] = "UP"
                elif key[pygame.K_s] and is_mv_legal("DOWN", settings['dir']):
                    flags['need_update'] = True
                    settings['dir'] = "DOWN"
                elif key[pygame.K_a] and is_mv_legal("LEFT", settings['dir']):
                    flags['need_update'] = True
                    settings['dir'] = "LEFT"
                elif key[pygame.K_d] and is_mv_legal("RIGHT", settings['dir']):
                    flags['need_update'] = True
                    settings['dir'] = "RIGHT"
                elif key[pygame.K_SPACE]:  # Play turn by turn
                    flags['need_update'] = True
                    settings['dir'] = calc_move(map, q_table, settings, flags)
                elif key[pygame.K_b]:  # Debug print
                    print(f"State: {map.state}")
                    print(f"Q_values: {q_table[map.state]}")
            elif key[pygame.K_UP]:
                if settings['speed'] - 20 < 0:
                    settings['speed'] = 0
                else:
                    settings['speed'] -= 20
                print(settings['speed'])
            elif key[pygame.K_DOWN]:
                if settings['speed'] + 20 > 500:
                    settings['speed'] = 500
                else:
                    settings['speed'] += 20
                print(settings['speed'])
