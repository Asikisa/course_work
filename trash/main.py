import random

import numpy as np
import matplotlib.pyplot as plt

S = ['s0', 's1']
A = ['a0', 'a1']


P = {'a0s0s1': 0.5, 'a0s0s0': 0.5, 'a1s0s1': 0.2, 'a1s0s0': 0.8, 'a0s1s0': 0.4, 'a0s1s1': 0.6, 'a1s1s0': 0.7,
     'a1s1s1': 0.3}
R = {'a0s0s1': 3, 'a0s0s0': 9, 'a1s0s1': 4, 'a1s0s0': 4, 'a0s1s0': 3, 'a0s1s1': -7, 'a1s1s0': 1,
     'a1s1s1': -19}

# print(random.random())
# print(P['a0s0s1'])
total = 10000
set_of_states = []
set_of_states1 = []

cur_state = 0
cur_state1 = 0
prev_state = 1
strategy = 3
while total > 0:
    probability = random.random()
    if cur_state == 0:
        # без реклами a0
        if strategy < 3:
            # 'a0s0s1': 0.5
            if probability < P['a0s0s1']:
                print('s1')
                prev_state = cur_state
                cur_state = 1
                set_of_states.append(R['a0s0s1'])
            else:
                print('s0')
                prev_state = cur_state
                cur_state = 0
                set_of_states.append(R['a0s0s0'])
        # з рекламою а1
        else:
            # 'a1s0s1': 0.2
            if probability < P['a1s0s1']:
                print('s1')
                prev_state = cur_state
                cur_state = 1
                set_of_states.append(R['a1s0s1'])
            else:
                print('s0')
                prev_state = cur_state
                cur_state = 0
                set_of_states.append(R['a1s0s0'])
    else:
        # без покращень а0
        if strategy % 2 == 0:
            # 'a0s1s0': 0.4
            if probability < P['a0s1s0']:
                print('s0')
                prev_state = cur_state
                cur_state = 0
                set_of_states.append(R['a0s1s0'])
            else:
                print('s1')
                prev_state = cur_state
                cur_state = 1
                set_of_states.append(R['a0s1s1'])
        else:
            # 'a0s1s0': 0.4
            if probability < P['a1s1s0']:
                print('s0')
                prev_state = cur_state
                cur_state = 0
                set_of_states.append(R['a1s1s0'])
            else:
                print('s1')
                prev_state = cur_state
                cur_state = 1
                set_of_states.append(R['a1s1s1'])

    probability1 = random.random()
    if cur_state1 == 0:
        # без реклами a0
        if strategy < 3:
            # 'a0s0s1': 0.5
            if probability1 < P['a0s0s1']:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a0s0s1'])
            else:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a0s0s0'])
        # з рекламою а1
        else:
            # 'a1s0s1': 0.2
            if probability1 < P['a1s0s1']:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a1s0s1'])
            else:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a1s0s0'])
    else:
        # без покращень а0
        if strategy % 2 == 0:
            # 'a0s1s0': 0.4
            if probability1 < P['a0s1s0']:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a0s1s0'])
            else:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a0s1s1'])
        else:
            # 'a0s1s0': 0.4
            if probability1 < P['a1s1s0']:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a1s1s0'])
            else:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a1s1s1'])
    total -= 1
print(set_of_states)
print(set_of_states1)
print(np.sum(set_of_states))
print(np.sum(set_of_states1))
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
