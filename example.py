import mdptoolbox, mdptoolbox.example
import numpy as np

P, R = mdptoolbox.example.forest()
print(R)
print(P)

fh = mdptoolbox.mdp.FiniteHorizon(P, R, 1, 5)
fh.run()
print(fh.V)
# print(fh.policy)

vi = mdptoolbox.mdp.ValueIteration(P, R, 1)
vi.run()

print(vi.V)
# print(vi.policy)

prob = np.zeros((2, 5, 5))
# 1 action
prob[0] = [[0.3, 0.7, 0., 0., 0.],
           [0.3, 0.0, 0.7, 0., 0.],
           [0.3, 0.0, 0., 0.7, 0.],
           [0.3, 0.0, 0., 0., 0.7],
           [0.3, 0.0, 0., 0., 0.7]]