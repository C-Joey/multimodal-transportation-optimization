import cvxpy as cp
import numpy as np
# Create two scalar optimization variables.
n = 5
# cvxpy使用cp.Variable(n,intger = True) 中的intger参数来规定x变量为整数
x = cp.Variable(n, integer=True)
# # Create two constraints.
A1 = np.ones((5, 5))
for i in range(A1.shape[0]):
    for j in range(A1.shape[1]):
        if i == j:
            pass
        else:
            A1[i, j] = A1[i, j] * 0
A2 = A1 * (-1)
A3 = np.array([[-1, 0, 0, 0, 0],
               [-0.9, -1, 0, 0, 0],
               [-0.8, -(40 / 48), -1, 0, 0],
               [-0.3, -(5 / 8), -0.8, -1, 0]
              ])
B = np.array([0, 0, 0, 0, 0, 25, 12, 12.5, 2, 0,
              10, 40, 90, 80, 0, 40, 2, -30, 32])
A = np.vstack((A2, A1, A1, A3))
constraints = [A @ x <= B]
objects = cp.Minimize(cp.sum(x))
# Define and solve the GUROBI problem.
prob = cp.Problem(objects, constraints)
# 调用GUROBI
prob.solve(solver=cp.CPLEX)
# Print result.
print("\nThe optimal value is", prob.value)
print("A solution x is")
print(x.value)
# print(help(prob))
# print (cp.installed_solvers())