import pygame


def display_game(map, screen, game_data):
    if not screen:
        return
    draw_chessboard(map, screen, game_data)
    draw_game(map, screen)
    pygame.display.flip()


def draw_chessboard(map, screen, game_data):
    BG_COLOR = (35, 39, 55)
    SQUARE_COLOR = (24, 24, 36)
    TXT_COLOR = (255, 255, 255)

    GAME_SIZE = 800
    BOARD_SIZE = map.size + 2
    SQUARE_SIZE = GAME_SIZE // BOARD_SIZE

    best_score = game_data["best_score"]
    nb_game = game_data["nb_game"]
    total_score = game_data["total_score"]
    average_score = total_score / nb_game if nb_game > 0 else 0
    average_score = round(average_score, 2)

    screen.fill((0, 0, 0))  # Fill the window with black
    BOARD_PX_SIZE = SQUARE_SIZE * BOARD_SIZE + 1
    rect = (99, 99, BOARD_PX_SIZE, BOARD_PX_SIZE)
    pygame.draw.rect(screen, BG_COLOR, rect)  # Fill the board

    font = pygame.font.Font(None, 36)
    p_key = font.render("[P] To pause the game", True, TXT_COLOR)
    space_key = font.render("[SPACE] To get next agent move", True, TXT_COLOR)
    escape_key = font.render("[ESC] or [Q] Exit the game", True, TXT_COLOR)
    up_key = font.render("[UP] To increase speed", True, TXT_COLOR)
    down_key = font.render("[DOWN] To decrease speed", True, TXT_COLOR)
    move_key = font.render("[W,A,S,D] To move the snake", True, TXT_COLOR)

    score_txt = font.render(f"Score: {len(map.snake_pos)}", True, TXT_COLOR)
    best_score_txt = font.render(f"Best Score: {best_score}", True, TXT_COLOR)
    av_sc_txt = font.render(f"Average Score: {average_score}", True, TXT_COLOR)
    session_nb__txt = font.render(f"Session: {nb_game}", True, TXT_COLOR)

    screen.blit(p_key, (100, 10))
    screen.blit(space_key, (100, 40))
    screen.blit(escape_key, (100, 70))
    screen.blit(up_key, (500, 10))
    screen.blit(down_key, (500, 40))
    screen.blit(move_key, (500, 70))

    screen.blit(score_txt, (950, 100))
    screen.blit(best_score_txt, (950, 130))
    screen.blit(av_sc_txt, (950, 160))
    screen.blit(session_nb__txt, (950, 190))

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = col * SQUARE_SIZE + 100
            y = row * SQUARE_SIZE + 100
            rect = (x, y, SQUARE_SIZE - 1, SQUARE_SIZE - 1)
            pygame.draw.rect(screen, SQUARE_COLOR, rect)


def draw_game(map, screen):
    GREEN_APPLE_COLOR = (0, 255, 0)
    RED_APPLE_COLOR = (255, 0, 0)
    WALL_COLOR = (0, 0, 0)
    SNAKE_COLOR = (255, 255, 255)
    HEAD_COLOR = (200, 200, 200)

    GAME_SIZE = 800
    BOARD_SIZE = map.size + 2
    FULL_SQUARE_SIZE = GAME_SIZE // BOARD_SIZE
    SQUARE_SIZE = FULL_SQUARE_SIZE - 1

    GAME_START_OFFSET = 100

    for y in range(map.size + 2):
        for x in range(map.size + 2):
            cell = map.map[y][x]
            x_offset = x * FULL_SQUARE_SIZE + GAME_START_OFFSET
            y_offset = y * FULL_SQUARE_SIZE + GAME_START_OFFSET
            if cell == "G":
                color = GREEN_APPLE_COLOR
            elif cell == "R":
                color = RED_APPLE_COLOR
            elif cell == "W":
                color = WALL_COLOR
            elif cell == "H":
                color = HEAD_COLOR
            elif cell == "S":
                color = SNAKE_COLOR

            if cell != "0":
                rect = (x_offset, y_offset, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, color, rect)
