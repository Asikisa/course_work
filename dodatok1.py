import random
import numpy as np
# states matrix
S = ['s0', 's1']
# probability matrix
P = {'s0s0': 0.5, 's1s0': 0.4}
# number of steps
total = 100000
set_of_states = []

# current state [s0 = 0 or s1 = 1]
cur_state = 0
# cur_state = 1
while total > 0:
    # imitation of real situation with random probability
    probability = random.random()
    if cur_state == 0:
        if probability > P['s0s0']:
            prev_state = cur_state
            cur_state = 0
            set_of_states.append(cur_state)
        else:
            prev_state = cur_state
            cur_state = 1
            set_of_states.append(cur_state)
    else:
        if probability >= P['s1s0']:
            prev_state = cur_state
            cur_state = 1
            set_of_states.append(cur_state)
        else:
            prev_state = cur_state
            cur_state = 0
            set_of_states.append(cur_state)
    total -= 1

print("ймовірність потрапити в 1 стан", 1 - np.sum(set_of_states)/len(set_of_states))
print("ймовірність потрапити в 2 стан", np.sum(set_of_states)/len(set_of_states))

