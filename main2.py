import random

import numpy as np
import matplotlib.pyplot as plt

S = ['s0', 's1']
A = ['a0', 'a1', 'a2']


P = {'a0s0s1': 0.5, 'a0s0s0': 0.5, 'a1s0s1': 0.2, 'a1s0s0': 0.8, 'a0s1s0': 0.4, 'a0s1s1': 0.6, 'a1s1s0': 0.7,
     'a1s1s1': 0.3, 'a2s0s0': 0.5, 'a2s0s1': 0.5, 'a2s1s0': 0.45, 'a2s1s1': 0.65}
R = {'a0s0s1': 3, 'a0s0s0': 9, 'a1s0s1': 4, 'a1s0s0': 4, 'a0s1s0': 3, 'a0s1s1': -7, 'a1s1s0': 1,
     'a1s1s1': -19, 'a2s0s0': 2, 'a2s0s1': 5, 'a2s1s0': 2, 'a2s1s1': -2}

# print(random.random())
# print(P['a0s0s1'])
total = 10000
set_of_states = []
set_of_states1 = []

cur_state = 1
cur_state1 = 1
prev_state = 1
strategy = 5
sum = 0
sum1 = 0

while total > 0:
    if cur_state == 0:
        # a0(first)a2(second)
        if strategy == 5:
            sum += P['a0s0s1']*R['a0s0s1']+R['a0s0s0']*P['a0s0s0']
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
        elif strategy == 6:
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
        elif strategy == 7:
            if probability < P['a2s0s1']:
                print('s1')
                prev_state = cur_state
                cur_state = 1
                set_of_states.append(R['a2s0s1'])
            else:
                print('s0')
                prev_state = cur_state
                cur_state = 0
                set_of_states.append(R['a2s0s0'])
        elif strategy == 8:
            if probability < P['a2s0s1']:
                print('s1')
                prev_state = cur_state
                cur_state = 1
                set_of_states.append(R['a2s0s1'])
            else:
                print('s0')
                prev_state = cur_state
                cur_state = 0
                set_of_states.append(R['a2s0s0'])
        elif strategy == 9:
            if probability < P['a2s0s1']:
                print('s1')
                prev_state = cur_state
                cur_state = 1
                set_of_states.append(R['a2s0s1'])
            else:
                print('s0')
                prev_state = cur_state
                cur_state = 0
                set_of_states.append(R['a2s0s0'])
        # без реклами a0
        elif strategy < 3:
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
        if strategy == 5:
            if probability < P['a0s1s1']:
                print('s1')
                prev_state = cur_state
                cur_state = 1
                set_of_states.append(R['a0s1s1'])
            else:
                print('s0')
                prev_state = cur_state
                cur_state = 0
                set_of_states.append(R['a0s1s0'])
        elif strategy == 6:
            if probability < P['a1s1s1']:
                print('s1')
                prev_state = cur_state
                cur_state = 1
                set_of_states.append(R['a1s1s1'])
            else:
                print('s0')
                prev_state = cur_state
                cur_state = 0
                set_of_states.append(R['a1s1s0'])
        elif strategy == 7:
            if probability < P['a2s1s1']:
                print('s1')
                prev_state = cur_state
                cur_state = 1
                set_of_states.append(R['a2s1s1'])
            else:
                print('s0')
                prev_state = cur_state
                cur_state = 0
                set_of_states.append(R['a2s1s0'])
        elif strategy == 8:
            if probability < P['a2s1s1']:
                print('s1')
                prev_state = cur_state
                cur_state = 1
                set_of_states.append(R['a2s1s1'])
            else:
                print('s0')
                prev_state = cur_state
                cur_state = 0
                set_of_states.append(R['a2s1s0'])
        elif strategy == 9:
            if probability < P['a2s1s1']:
                print('s1')
                prev_state = cur_state
                cur_state = 1
                set_of_states.append(R['a2s1s1'])
            else:
                print('s0')
                prev_state = cur_state
                cur_state = 0
                set_of_states.append(R['a2s1s0'])
        # без покращень а0
        elif strategy % 2 == 0:
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
    # покупка a2
    if cur_state1 == 0:
        if strategy == 5:
            if probability1 < P['a2s0s1']:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a2s0s1'])
            else:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a2s0s0'])
        elif strategy == 6:
            if probability1 < P['a2s0s1']:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a2s0s1'])
            else:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a2s0s0'])
        elif strategy == 7:
            if probability1 < P['a0s0s1']:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a0s0s1'])
            else:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a0s0s0'])
        elif strategy == 8:
            if probability1 < P['a1s0s1']:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a1s0s1'])
            else:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a1s0s0'])
        elif strategy == 9:
            if probability1 < P['a2s0s1']:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a2s0s1'])
            else:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a2s0s0'])
        # без реклами a0
        elif strategy < 3:
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
        if strategy == 5:
            if probability1 < P['a2s1s1']:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a2s1s1'])
            else:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a2s1s0'])
        elif strategy == 6:
            if probability1 < P['a2s1s1']:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a2s1s1'])
            else:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a2s1s0'])
        elif strategy == 7:
            if probability1 < P['a0s1s1']:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a0s1s1'])
            else:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a0s1s0'])
        elif strategy == 8:
            if probability1 < P['a1s1s1']:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a1s1s1'])
            else:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a1s1s0'])
        elif strategy == 9:
            if probability1 < P['a2s1s1']:
                print('s1')
                cur_state1 = 1
                set_of_states1.append(R['a2s1s1'])
            else:
                print('s0')
                cur_state1 = 0
                set_of_states1.append(R['a2s1s0'])
        # без покращень а0
        elif strategy % 2 == 0:
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
