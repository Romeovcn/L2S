import random

def get_reward_up(state):
    reward = 0
    if state.find("DU_1") != -1:
        reward += -100
    elif state.find("GU_1") != -1:
        reward += 100
    elif state.find("GU_2") != -1:
        reward += 20
    elif state.find("GD_2") != -1 or state.find("GL_2") != -1 or state.find("GR_2") != -1:
        reward += -10
    return reward


def get_reward_down(state):
    reward = 0
    if state.find("DD_1") != -1:
        reward += -100
    elif state.find("GD_1") != -1:
        reward += 100
    elif state.find("GD_2") != -1:
        reward += 20
    elif state.find("GU_2") != -1 or state.find("GL_2") != -1 or state.find("GR_2") != -1:
        reward += -10
    return reward


def get_reward_left(state):
    reward = 0
    if state.find("DL_1") != -1:
        reward += -100
    elif state.find("GL_1") != -1:
        reward += 100
    elif state.find("GL_2") != -1:
        reward += 20
    elif state.find("GU_2") != -1 or state.find("GD_2") != -1 or state.find("GR_2") != -1:
        reward += -10
    return reward


def get_reward_right(state):
    reward = 0
    if state.find("DR_1") != -1:
        reward += -100
    elif state.find("GR_1") != -1:
        reward += 100
    elif state.find("GR_2") != -1:
        reward += 20
    elif state.find("GU_2") != -1 or state.find("GD_2") != -1 or state.find("GL_2") != -1:
        reward += -10
    return reward


def get_reward(state, action): # Negative reward if going in opposite direction of green apple
    reward = 0
    if action == "UP":
        reward = get_reward_up(state)
    if action == "DOWN":
        reward = get_reward_down(state)
    if action == "LEFT":
        reward = get_reward_left(state)
    if action == "RIGHT":
        reward = get_reward_right(state)
    return reward
