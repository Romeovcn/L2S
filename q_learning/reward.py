def get_reward_up(state):
	if state.find("DU_1") != -1:
		return -100
	if state.find("RU_1") != -1:
		return -20
	if state.find("GU_1") != -1:
		return 100
	if state.find("GU_2") != -1:
		return 50
	return 0

def get_reward_down(state):
	if state.find("DD_1") != -1:
		return -100
	if state.find("RD_1") != -1:
		return -20
	if state.find("GD_1") != -1:
		return 100
	if state.find("GD_2") != -1:
		return 50
	return 0

def get_reward_left(state):
	if state.find("DL_1") != -1:
		return -100
	if state.find("RL_1") != -1:
		return -20
	if state.find("GL_1") != -1:
		return 100
	if state.find("GL_2") != -1:
		return 50
	return 0

def get_reward_right(state):
	if state.find("DR_1") != -1:
		return -100
	if state.find("RR_1") != -1:
		return -20
	if state.find("GR_1") != -1:
		return 100
	if state.find("GR_2") != -1:
		return 50
	return 0

def get_reward(state, action): # Can be optimized
	if action == "UP":
		return get_reward_up(state)
	if action == "DOWN":
		return get_reward_down(state)
	if action == "LEFT":
		return get_reward_left(state)
	if action == "RIGHT":
		return get_reward_right(state)
	return 0