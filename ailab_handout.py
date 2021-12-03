#Lab Assignment 1

# Write programs for introduction to Python.
#%%
#factorial
def factorial(n):
    if n==1:
        return n
    return n*factorial(n-1)

#prime check
def isPrime(n):
    for i in range(2,(int)(n**0.5)+1):
        if(n%i==0):
            return False
    return True


# Wrtie a program to implement BFS in Python
#%%
graph = {
        
         'a':['b','c'],
         'b':['d'],
         'c':['d'],
         'd':[]
        
        
        }


def bfs(source):
    queue =[]
    visited = []
    visited.append(source)
    queue.append(source)
    while queue:
        node = queue.pop(0)
        print(node,end=" ")
        for next in graph[node]:
            if next not in visited:
                queue.append(next)  
                visited.append(next)
                

#%%
#Write a program to implement DFS
graph2 = {
        
         'a':['b','c'],
         'b':['d'],
         'c':['d'],
         'd':[]
        
        
        }

def dfs(source,visited):
    print(source,end=" ")
    visited.append(source)
    for next in graph2[source]:
        if next not in visited:
            dfs(next,visited)
            


