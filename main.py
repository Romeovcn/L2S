import pygame
import argparse
import json

from game_engine.game_algorithm import get_cell_value_and_coordinates, is_move_valid, move
from game_engine.map import Map
from game_engine.draw import display_game
from game_engine.events import check_key_events, check_key_events_test
from q_learning.ai import calculate_next_move

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"


def is_dead(map, target_cell, game_data):
    snake_pos = map.snake_pos
    move_validity = is_move_valid(snake_pos, target_cell)

    if move_validity == -1:
        if len(snake_pos) > game_data["best_score"]:
            game_data["best_score"] = len(snake_pos)
        game_data["total_score"] += len(snake_pos)
        game_data["nb_game"] += 1
        return True
    return False


def check_death_and_move(screen, map, game_settings, game_data, flags):
    target_cell = get_cell_value_and_coordinates(map, game_settings['direction'])
    game_data["total_nb_moves"] += 1
    flags['need_update'] = False

    if is_dead(map, target_cell, game_data):
        return True

    move(map, target_cell)
    map.update_state()
    display_game(map, screen, game_data)

    if game_settings['verbose']:
        print(game_settings['direction'])
        map.print()
    return False


def get_and_parse_args():
    parser = argparse.ArgumentParser(description="Q-Learning Snake AI")
    parser.add_argument("--hide-display", dest="hide_display", action="store_true", help="Hide the display of the game", default=False)
    parser.add_argument("--size", type=int, help="Size of the board", required=False, default=10)
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode", required=False, default=False)
    parser.add_argument("--save", action="store_true", help="Save q_values in file", required=False, default=False)
    parser.add_argument("--learn", action="store_true", help="Enable learning mode", required=False, default=False)
    parser.add_argument("--sessions", type=int, help="Number of sessions", required=False, default=100)
    parser.add_argument("--load", type=str, help="Path to the file of the model", required=False, default=None)
    args = parser.parse_args()

    if args.size and (args.size < 5 or args.size > 50):
        print(f"{RED}Size must be between 5 and 50 included{RESET}")
        exit()
    return args


def get_pygame_screen(hide_display):
    if not hide_display:
        pygame.init()
        screen = pygame.display.set_mode((1300, 900))
        pygame.display.set_caption("Snake AI")
    else:
        screen = None
    return screen


def get_q_table(load):
    try:
        if load:
            with open(load, "r") as file:
                q_table = json.load(file)
            return q_table
        else:
            q_table = {}
            return q_table
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except FileNotFoundError:
        print("Error: File not found.")
    except OSError as e:
        print(f"Error opening file: {e}")


def print_results(game_data):
    print(f"Best Score: {game_data['best_score']}")
    print(f"Number of Games: {game_data['nb_game']}")
    if game_data['total_score'] > 0: print(f"Average Score: {game_data['total_score'] / game_data['nb_game']}")
    if game_data['total_nb_moves'] > 0: print(f"Average moves: {game_data['total_nb_moves'] / game_data['nb_game']}")


def get_default_direction(map):
    snake_pos = map.snake_pos
    snake_head_pos = snake_pos[0]
    snake_body_pos = snake_pos[1]

    if snake_head_pos[0] == snake_body_pos[0]:
        if snake_head_pos[1] < snake_body_pos[1]:
            return "LEFT"
        else:
            return "RIGHT"
    else:
        if snake_head_pos[0] < snake_body_pos[0]:
            return "UP"
        else:
            return "DOWN"


def main():
    # --------------- Define variables --------------- #
    args = get_and_parse_args()
    map = Map(args.size)
    screen = get_pygame_screen(args.hide_display)
    q_table = get_q_table(args.load)
    last_action_time = 0

    game_data = {"nb_game": 0, "total_score": 0, "best_score": 0, "total_nb_moves": 0}
    game_settings = {"speed": 0, "epsilon": 0.8, "direction": None, "learn": args.learn, "verbose": args.verbose}	
    flags = {"running": True, "pause": False, "need_update": False}

    # --------------- Game and agent training loop --------------- #
    for _ in range(args.sessions):
        map.generate_random_map()
        display_game(map, screen, game_data)
        game_settings['direction'] = get_default_direction(map)

        while flags["running"]:
            if not args.hide_display:
                check_key_events_test(pygame, map, q_table, game_settings, flags)

            if not flags["pause"] and not flags['need_update']:
                game_settings['direction'] = calculate_next_move(map, q_table, game_settings, flags)

            current_time = pygame.time.get_ticks()
            if flags['need_update'] and current_time - last_action_time >= game_settings['speed']:
                last_action_time = current_time
                if check_death_and_move(screen, map, game_settings, game_data, flags):
                    break

        if not flags["running"]:
            break

    # --------------- Exit and print results --------------- #
    if not args.hide_display:
        pygame.quit()

    print_results(game_data)

    if args.save:
        with open("q_values.txt", "w") as file:
            json.dump(q_table, file)


if __name__ == "__main__":
    main()