#!/usr/bin/env python
# coding: utf-8






"""
Ques 1. Hill Climb algorithm to optimize the objective function f(x) = x^2[-5,5]
"""




import numpy as np
from matplotlib import pyplot



def objective_function(x):
    return x[0]**2.0



def hill_climb(bound,n_iterations,step_size):
    sol = bound[:,0]+np.random.rand(len(bound))*(bound[:,1]- bound[:,0])
    sol_eval = objective_function(sol)
    solutions = []
    solutions.append(sol)
    for i in range(n_iterations):
        candidate = sol + np.random.randn(len(bound))*step_size
        candidate_eval = objective_function(candidate)
        if candidate_eval <= sol_eval:
            sol,sol_eval = candidate,candidate_eval
            solutions.append(sol)
            print('>%d f(%s) = %.5f' % (i,sol,sol_eval))
    return [sol,sol_eval,solutions]


np.random.seed(18)
bound = np.asarray([[-5.0,5.0]])
n_iterations = 1000
step_size = 0.1
best,score,solutions = hill_climb(bound,n_iterations,step_size)
print("Done !")
print('f(%s) = %f' % (best,score))
ip = np.arange(bound[0,0],bound[0,1],0.1)
pyplot.plot(ip, [objective_function([x]) for x in ip], '--')
pyplot.axvline(x=[0.0], ls='--', color='blue')
pyplot.plot(solutions, [objective_function(x) for x in solutions], 'o', color='red')
pyplot.show()


pyplot.plot(solutions, '.-')
pyplot.xlabel('Improvement Number')
pyplot.ylabel('Evaluation f(x)')
pyplot.show()


"""
End of Ques 1.
"""




"""
Ques 2. Water Jug Problem using BFS.

"""




from collections import deque




def bfs(a, b, target):
   m = {}
   isSolvable = False
   path = []
   q = deque()
   q.append((0, 0))

   while (len(q) > 0):
       u = q.popleft()
       if ((u[0], u[1]) in m):
           continue
       if ((u[0] > a or u[1] > b or
            u[0] < 0 or u[1] < 0)):
           continue
       path.append([u[0], u[1]])
       m[(u[0], u[1])] = 1
       if (u[0] == target or u[1] == target):
           isSolvable = True
            
           if (u[0] == target):
               if (u[1] != 0):
                   path.append([u[0], 0])
           else:
               if (u[0] != 0):
                   path.append([0, u[1]])
           sz = len(path)
           for i in range(sz):
               print("(", path[i][0], ",",
                          path[i][1], ")")
           break
       q.append([u[0], b])
       q.append([a, u[1]]) 

       for ap in range(max(a, b) + 1):
           c = u[0] + ap
           d = u[1] - ap
           if (c == a or (d == 0 and d >= 0)):
               q.append([c, d])
           c = u[0] - ap
           d = u[1] + ap
           if ((c == 0 and c >= 0) or d == b):
               q.append([c, d])
       q.append([a, 0])
       q.append([0, b])
   if (not isSolvable):
       print ("No solution")

       
jug1,jug2,target = 4,3,2
print("Path from initial state to goal state:")
bfs(jug1,jug2,target)






