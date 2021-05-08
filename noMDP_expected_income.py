import numpy as np

# default matrix
# R = np.array([[9, 3, 1],
#               [3, -7, 1],
#               [3, -7, 1]])
R = np.array([[9, 3],
              [3, -7]])

# probability matrix
# P = np.array([[0.4, 0.4, 0.2],
#               [0.4, 0.5, 0.1],
#               [0.5, 0.3, 0.2]])
P = np.array([[0.5, 0.5],
              [0.4, 0.6]])

MAX_IT = 10
STATE_NUMBER = len(R)

# coefficient matrix
Q = np.zeros(STATE_NUMBER)

result_matrix = np.zeros((MAX_IT, STATE_NUMBER))
for i in range(MAX_IT):
    if i == 0:
        for j in range(STATE_NUMBER):
            summ = 0
            for k in range(STATE_NUMBER):
                a = P[j][k]*R[j][k]
                summ += a
            result_matrix[i][j] = summ
            Q[j] = summ
    else:
        for j in range(STATE_NUMBER):
            summ = 0  # ????????
            for k in range(STATE_NUMBER):
                a = P[j][k]*result_matrix[i-1][k]
                summ += a
            result_matrix[i][j] = summ + Q[j]

print(result_matrix)

