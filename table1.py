import random
import numpy as np
import matplotlib.pyplot as plt

S = ['s0', 's1']

P = {'s0s0': 0.5, 's1s0': 0.4}
R = {'s0s1': 3, 's0s0': 9, 's1s0': 3, 's1s1': -7}


total = 1000
total_1 = total
set_of_states = []
set_of_rewards = []

cur_state = 1
# set_of_states.append(cur_state)
# prev_state = 0
while total > 0:
    probability = random.random()
    if cur_state == 0:
        if probability > P['s0s0']:
            # print('s0')
            prev_state = cur_state
            cur_state = 0
            set_of_rewards.append(R['s0s0'])
            set_of_states.append(cur_state)
        else:
            # print('s1')
            prev_state = cur_state
            cur_state = 1
            set_of_rewards.append(R['s0s1'])
            set_of_states.append(cur_state)
    else:
        if probability >= P['s1s0']:
            # print('s0')
            prev_state = cur_state
            cur_state = 1
            set_of_rewards.append(R['s1s1'])
            set_of_states.append(cur_state)
        else:
            # print('s1')
            prev_state = cur_state
            cur_state = 0
            set_of_rewards.append(R['s1s0'])
            set_of_states.append(cur_state)
    total -= 1

print(set_of_states)
print(set_of_rewards)
# print(np.sum(set_of_states))
# print(len(set_of_states))
print("ймовірність потрапити в 2 стан", np.sum(set_of_states)/len(set_of_states))
print("ймовірність потрапити в 1 стан", 1 - np.sum(set_of_states)/len(set_of_states))
print("дохід", np.sum(set_of_rewards)/total_1)

# print(np.sum(set_of_rewards))
#
# x = np.arange(0, 10000)
# y = set_of_states
#
# fig, ax = plt.subplots()
#
# ax.bar(x, y)
#
# ax.set_facecolor('seashell')
# fig.set_facecolor('floralwhite')
# fig.set_figwidth(12)  # ширина Figure
# fig.set_figheight(6)  # высота Figure
#
# plt.show()
