import mdptoolbox
import numpy as np

# transition probabilities is a number of states by number of states matrix and there`s one for each action

# 2 actions, 2 states, 2 states
prob = np.zeros((2, 2, 2))
# action a0
prob[0] = [[0.5, 0.5],
           [0.4, 0.6]]
# action a1
prob[1] = [[0.8, 0.2],
           [0.7, 0.3]]

# and reward matrix is a number of states(5) by the number of actions(2)
rewards = np.zeros((2, 2))
rewards[0] = [6, 4]
rewards[1] = [-3, -5]

vi = mdptoolbox.mdp.FiniteHorizon(prob, rewards, 1, 10)
vi.run()

print(vi.V)
print(vi.policy)
