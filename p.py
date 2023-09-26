from sympy import *
import math

D = 187.5
h = 0.02
K = 20
L = 2
C1 = 3
C2 = 2.5
q = 1000

ym = (2*K*D/h)**0.5
TCU1_y = C1*D + K*D/ym + h*ym/2

def fun_Q():
  var('Q')
  return max(solve(Q**2 + (2*(C2*D - TCU1_y))*Q/h + 2*K*D/h,Q))

Q = fun_Q()

y_star = (2*K*D/h)**0.5
t0 = y_star/D #cycle length

if(L>t0):
  n = math.floor(L/t0)
  le = L - n*t0
  print("Reorder point thus occurs when inventory model drops to : ",le*D)
else:
  print("Reorder point thus occurs when inventory model drops to : ",L*D)

if(q<ym or q>Q):
  print("y* = ",ym)
else:
  print('y* = ',q)