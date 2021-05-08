import numpy as np

# default matrix
R = np.array([[9, 3],
              [3, -7]])

# probability matrix
P = np.array([[0.5, 0.5],
              [0.4, 0.6]])

# coefficient matrix
Q = [0, 0]

MAX_IT = 10
STATE_NUMBER = len(R)

result_matrix = np.zeros((MAX_IT, STATE_NUMBER))
for i in range(MAX_IT):
    if i == 0:
        for j in range(STATE_NUMBER):
            a = P[j][0]*R[j][0]
            b = P[j][1]*R[j][1]
            result_matrix[i][j] = a + b
            Q[j] = a + b
    else:
        for j in range(STATE_NUMBER):
            a = P[j][0]*result_matrix[i-1][0]
            b = P[j][1]*result_matrix[i-1][1]
            result_matrix[i][j] = a + b + Q[j]

print(result_matrix)

