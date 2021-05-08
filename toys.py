import mdptoolbox

import numpy as np

# transition probabilities is a number of states by number of states matrix and there`s one for each action

# 2 actions, 5 states, 5 states
prob = np.zeros((3, 2, 2))
# 1 action a0
prob[0] = [[0.9, 0.1],
           [0.8, 0.2]]
# a1
prob[1] = [[0.4, 0.6],
           [0.45, 0.55]]
# a2
prob[2] = [[0.35, 0.65],
           [0.3, 0.7]]
# and reward matrix is a number of states(5) by the number of actions(2)
rewards = np.zeros((2, 3))
rewards[0] = [0.6, 0.1, 0.45]
rewards[1] = [0.7, 0.05, 0.5]


# value iteration
vi = mdptoolbox.mdp.ValueIteration(prob, rewards, 1)
vi.run()

optimal_policy = vi.policy
expected_values = vi.V

print(optimal_policy)
# (0, 1, 1, 0, 1) wait cut cut wait cut
print(expected_values)
# (3.1021779262212235, 3.7152970594035533, 3.7152970594035533, 3.732177926221223, 4.715297059403554)

vi = mdptoolbox.mdp.FiniteHorizon(prob, rewards, 1, 5)
vi.run()

print(vi.V)
print(vi.policy)
