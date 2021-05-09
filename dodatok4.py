import numpy as np

# default matrix
R = np.array([[[9, 3], [4, 4]],
              [[3, -7], [1, -19]]])

# probability matrix
P = np.array([[[0.5, 0.5], [0.8, 0.2]],
              [[0.4, 0.6], [0.7, 0.3]]])

# example result
# result = [[[6, -3], [4, -5]],
#           [[7.5, - 2.4], [6.2, -3.7]]]
# Q example
# Q_ex = [[6, 4], [-3, -5]]

MAX_IT = 5
STATE_NUMBER = len(R)
ACTION_NUMBER = 2

# coefficient matrix
Q = np.zeros((STATE_NUMBER, ACTION_NUMBER))

result_matrix = np.zeros((MAX_IT, ACTION_NUMBER, STATE_NUMBER))
for i in range(MAX_IT):
    if i == 0:
        for j in range(STATE_NUMBER):
            x = [0, 0]
            for k in range(ACTION_NUMBER):
                summ = 0
                for s in range(STATE_NUMBER):
                    a = P[k][j][s] * R[k][j][s]
                    summ += a
                x[k] = summ
            result_matrix[i][j] = x
        Q = result_matrix[0]
    else:
        for j in range(STATE_NUMBER):
            x = [0, 0]
            for k in range(ACTION_NUMBER):
                summ = 0
                for s in range(STATE_NUMBER):
                    a = P[k][j][s] * result_matrix[i-1][j][s]
                    summ += a
                x[k] = summ + Q[j][k]
            result_matrix[i][j] = x

print(result_matrix)

