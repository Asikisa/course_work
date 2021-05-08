import mdptoolbox.example
import numpy as np

reward = np.array([[[9, 3],
                  [3, -7]]])

P = np.array([[[0.5, 0.5],
               [0.4, 0.6]]])

fh = mdptoolbox.mdp.FiniteHorizon(P, reward, 1, 5)
fh.run()
print(fh.V)
print(fh.policy)
