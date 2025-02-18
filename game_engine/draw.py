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
    GREEN_APPLE_COLOR = (255, 0, 0)
    RED_APPLE_COLOR = (0, 255, 0)
    WALL_COLOR = (255, 255, 255)

    GAME_SIZE = 800 # height minus the top score bar
    BOARD_SIZE = map.size + 2
    SQUARE_SIZE = GAME_SIZE // BOARD_SIZE

    best_score = game_data["best_score"]
    nb_game = game_data["nb_game"]
    total_score = game_data["total_score"]
    average_score = total_score / nb_game if nb_game > 0 else 0
    average_score = round(average_score, 2)

    screen.fill((0, 0, 0)) # Fill the screen with black
    pygame.draw.rect(screen, BG_COLOR, (99, 99, (SQUARE_SIZE) * BOARD_SIZE + 1, (SQUARE_SIZE) * BOARD_SIZE + 1)) # Fill the board

    font = pygame.font.Font(None, 36)
    p_key = font.render(f"[P] To pause the game", True, (255, 255, 255))
    space_key = font.render(f"[SPACE] To get next agent move", True, (255, 255, 255))
    escape_key = font.render(f"[ESC] or [Q] Exit the game", True, (255, 255, 255))
    score_text = font.render(f"[UP] To increase speed", True, (255, 255, 255))
    score_text = font.render(f"[DOWN] To decrease speed", True, (255, 255, 255))
    screen.blit(p_key, (100, 10))
    screen.blit(space_key, (100, 40))
    screen.blit(escape_key, (100, 70))
    # score_text = font.render(f"[A] To decrease", True, (255, 255, 255))

    score_text = font.render(f"Score: {len(map.snake_pos)}", True, (255, 255, 255))
    best_score_text = font.render(f"Best Score: {best_score}", True, (255, 255, 255))
    av_score_text = font.render(f"Average Score: {average_score}", True, (255, 255, 255))
    session_nb__text = font.render(f"Session: {nb_game}", True, (255, 255, 255))
    screen.blit(score_text, (950, 100))
    screen.blit(best_score_text, (950, 130))
    screen.blit(av_score_text, (950, 160))
    screen.blit(session_nb__text, (950, 190))

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            pygame.draw.rect(screen, SQUARE_COLOR, (col * SQUARE_SIZE + 100, row * SQUARE_SIZE + 100, SQUARE_SIZE-1, SQUARE_SIZE-1))


def draw_snake(screen, snake_pos):
    pixel_pos = pygame.Vector2(snake_pos[0] * 100 + 50, snake_pos[1] * 100 + 50)
    pygame.draw.circle(screen, "red", pixel_pos, 50)


def draw_game(map, screen):
    GREEN_APPLE_COLOR = (0, 255, 0)
    RED_APPLE_COLOR = (255, 0, 0)
    WALL_COLOR = (0, 0, 0)
    SNAKE_COLOR = (255, 255, 255)
    HEAD_COLOR = (200, 200, 200)

    GAME_SIZE = 800 # height minus the top score bar
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
                # SNAKE_COLOR = tuple(max(0, c - 20) for c in SNAKE_COLOR)

            if cell != "0":
                pygame.draw.rect(screen, color, (x_offset, y_offset, SQUARE_SIZE, SQUARE_SIZE))