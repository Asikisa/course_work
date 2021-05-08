import mdptoolbox, mdptoolbox.example
import numpy as np
# P, R = mdptoolbox.example.forest()

# R = np.array([[6], [-3]])
#
# rewards = np.zeros((2, 2))
# rewards[0] = [9, 3]
# rewards[1] = [3, -7]

reward = np.array([[[9, 3],
               [3, -7]]])

# P = np.array([[[0.1, 0.9, 0.0], [0.1, 0.0, 0.9], [0.1, 0.0, 0.9]], [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 0.0, 0.0]]])
# P = np.array([[[0.5, 0.5], [0.8, 0.2]], [[0.4, 0.6], [0.7, 0.3]]])
P = np.array([[[0.5, 0.5],
               [0.4, 0.6]]])
# R = np.array([[0.0, 0.0], [0.0, 0.1], [4.0, 2.0]])
# R = np.array([[0.0, 0.0], [0.0, 0.1]])

fh = mdptoolbox.mdp.FiniteHorizon(P, reward, 1, 5)
fh.run()
print(fh.V)
print(fh.policy)
# vi = mdptoolbox.mdp.ValueIteration(P, R, 0.9)
# vi.run()
# print(vi.V)
# print(vi.policy)