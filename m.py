import numpy as np
from scipy.optimize import minimize

K = [10,5,15]
D = [2,4,4]
h = [0.3,0.1,0.2]
a = [1,1,1]
A = 25

y_star = []
for i in range(len(K)):
  y_star.append((2*K[i]*D[i]/h[i])**0.5)

if(sum(y_star)>A):
  print("Violates!")

def objective(Y):
  val = 0
  for i in range(len(Y)):
    val+=(K[i]*D[i]/Y[i] + h[i]*Y[i]/2)
  return val

def constraint(Y):
  val = 0
  for i in range(len(Y)):
    val -= a[i]*Y[i]
  return val + A

Y = [2 for i in range(len(K))]
constr = {
    'type' : 'ineq',
    'fun' : constraint
}
bounds = ((0,float('inf')) for i in range(len(K)))
cons = [constr]
sol = minimize(objective,Y,method='SLSQP',constraints=cons)
print(sol)