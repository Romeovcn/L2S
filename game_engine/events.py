from game_engine.game_algorithm import is_mv_legal
from q_learning.ai import calc_move


def check_key_events(pygame, map, q_table, settings, flags):
    YELLOW = "\033[33m"
    RST = "\033[0m"

    while True:
        event = pygame.event.poll()
        if event.type == pygame.NOEVENT:
            break

        if event.type == pygame.QUIT:
            flags["running"] = False

        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE] or key[pygame.K_q]:
                flags["running"] = False
            elif key[pygame.K_p]:
                if flags['pause']:
                    print(f"{YELLOW}[i] AI is unpaused{RST}")
                else:
                    print(f"{YELLOW}[i] AI is paused{RST}")
                flags['pause'] = not flags['pause']
            elif key[pygame.K_UP]:
                if settings['speed'] - 20 < 0:
                    settings['speed'] = 0
                else:
                    settings['speed'] -= 20
                print(f"{YELLOW}[i] Speed increase: {settings['speed']}{RST}")
            elif key[pygame.K_DOWN]:
                if settings['speed'] + 20 > 500:
                    settings['speed'] = 500
                else:
                    settings['speed'] += 20
                print(f"{YELLOW}[i] Speed decrease: {settings['speed']}{RST}")
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
                elif key[pygame.K_SPACE]:
                    flags['need_update'] = True
                    settings['dir'] = calc_move(map, q_table, settings, flags)
                elif key[pygame.K_b]:
                    print(f"State: {map.state}")
                    print(f"Q_values: {q_table[map.state]}")
