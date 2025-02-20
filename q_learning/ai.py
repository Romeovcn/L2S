import random

from game_engine.game_algorithm import is_move_legal
from q_learning.reward import get_reward


def calculate_next_move(map, q_table, game_settings, flags):
    possible_moves = get_all_possible_moves(game_settings['direction'])
    state = map.state
    action = choose_action(game_settings, possible_moves, q_table, state)
    if game_settings['learn']:
        q_table[state] = update_q_value(q_table, state, action)
    flags['need_update'] = True

    return action


def choose_action(game_settings, possible_moves, q_table, state):
    if game_settings['learn'] and random.uniform(0, 1) < game_settings['epsilon']:  # Explore: choose a random action
        action = select_random_move(possible_moves)
    else:  # Exploit: choose the best known action in q_table
        action = get_best_move(q_table, state, possible_moves)

    if game_settings['learn']:
        game_settings['epsilon'] = update_epsilon(game_settings['epsilon'])
    return action


def update_epsilon(epsilon):
    min_epsilon = 0.01
    epsilon_decay = 0.995
    return max(min_epsilon, epsilon * epsilon_decay)


def get_best_move(q_table, state, possible_moves):
    Q_values = q_table.get(state, None)
    if Q_values is None:
        return select_random_move(possible_moves)
    action = max(possible_moves, key=Q_values.get)
    return action


def get_all_possible_moves(direction): # Can be optimized
    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    possible_moves = []

    for new_direction in directions:
        if is_move_legal(new_direction, direction):
            possible_moves.append(new_direction)
    return possible_moves


def select_random_move(possible_moves):
    return random.choice(possible_moves)


def update_q_value(q_table, state, action):
    Q_values = q_table.get(state, {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0})
    Q = Q_values[action]
    max_Q = max(Q_values[action] for action in ["UP", "DOWN", "LEFT", "RIGHT"])
    r = get_reward(state, action)
    gamma = 0.9

    Q_values[action] = Q + 0.1 * (r + gamma * max_Q - Q)
    return Q_values