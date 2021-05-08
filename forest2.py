import mdptoolbox

import numpy as np

# transition probabilities is a number of states by number of states matrix and there`s one for each action

# 2 actions, 5 states, 5 states
prob = np.zeros((1, 5, 5))
# 1 action
prob[0] = [[1, 0., 0., 0., 0.],
           [0., 1, 0., 0., 0.],
           [0., 0.0, 1, 0., 0.],
           [0., 0.0, 0., 1, 0.],
           [0., 0.0, 0., 0., 1]]

# and reward matrix is a number of states(5) by the number of actions(2)
rewards = np.zeros((5, 1))
rewards[0] = [0.]
rewards[1] = [0.]
rewards[2] = [0.]
rewards[3] = [0.]
rewards[4] = [0.3]

R = np.array([[0],
              [0],
              [0],
              [0],
              [0.3]])

# value iteration
vi = mdptoolbox.mdp.ValueIteration(prob, rewards, 1)
vi.run()

optimal_policy = vi.policy
expected_values = vi.V

print(optimal_policy)
# (0, 1, 1, 0, 1) wait cut cut wait cut
print(expected_values)
# (3.1021779262212235, 3.7152970594035533, 3.7152970594035533, 3.732177926221223, 4.715297059403554)

vi = mdptoolbox.mdp.FiniteHorizon(prob, R, 1, 5)
vi.run()

# print(optimal_policy)
print(vi.V)
