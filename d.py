#input dictionary
inputDict = {"Month":[1,2,3,4], "Regular":[90,100,120,110], "Overtime":[50,60,80,70], "Demand":[100,190,210,160]}

#create 2d matrix
rows = len(inputDict["Regular"])*2
cols = len(inputDict["Demand"])

#initialise the variables
mat = [[0 for i in range(cols)] for j in range(rows)]
regular = inputDict["Regular"]
overtime = inputDict["Overtime"]
demand = inputDict["Demand"]

#fill regular demand
for inx in range(0,len(regular)):
  output = min(regular[inx], demand[inx])
  demand[inx] -= output
  regular[inx] -= output
  mat[inx*2][inx] = output

  if(demand[inx] > 0):
    for jnx in reversed(range(inx)):
      output = min(regular[jnx], demand[inx])
      if(output > 0):
        demand[inx]-= output
        regular[jnx] -= output
        mat[(jnx*2)][inx] = output

#fill overtime demand
for inx in range(0, len(overtime)):
  output = min(overtime[inx], demand[inx]);
  demand[inx] -= output
  overtime[inx] -= output
  mat[(inx*2) + 1][inx] = output

  if(demand[inx] > 0):
    for jnx in reversed(range(inx)):
      output = min(overtime[jnx], demand[inx])
      if(output > 0):
        demand[inx]-= output
        overtime[jnx] -= output
        mat[(jnx*2)+1][inx] = output

#find surplus
surplus = 0
for inx in range(len(regular)):
  surplus += regular[inx]
  surplus += overtime[inx]

print("The surplus:",surplus)
print("\nMatrix:\n", mat)

price = 0

#find the total cost
for i in range(rows):
  idx = 0
  for j in range(i//2, cols):
    #print(i, j, mat[i][j])
    if i % 2 == 0:
      price += mat[i][j] * (6 + (idx * 0.1))
    else:
      price += mat[i][j] * (9 + (idx * 0.1))
    idx += 1
    #print(i, j, mat[i][j],price)
print(price)