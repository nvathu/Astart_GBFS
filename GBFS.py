from collections import defaultdict
import heapq
from PriorityQueue import PriorityQueue

# define graph
class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v, l):
        self.graph[u].append((v, l))

    # function to be implemented
    def GBFS(self, s, g):
        frontiers = PriorityQueue()
        visited = []
        
        
        frontiers.push(heuristic[s], s)
        frontiers.check()

        while not frontiers.isEmpty():
            cur_node, hh = frontiers.pop()
            if cur_node in visited:
                continue
            else:
                visited.append(cur_node)
            if cur_node == g:
                print('done')
                print(hh[2]) 
                return hh
            else:
                for v, _ in self.graph[cur_node]:
                    if v not in visited:
                        frontiers.push(heuristic[v] + hh, v)
                        frontiers.check()




   
        
                

        
    

# Driver code
# Create a graph given in the above diagram
g = Graph()
heuristic = []

with open('input.txt', 'r') as f:
    n, m = [int(x) for x in next(f).split()]
    for i in range(m):
        u, v, l = [int(x) for x in next(f).split()]
        g.addEdge(u, v, l)
    for i in range(n):
        h = [int(x) for x in next(f).split()]
        heuristic.append(h)
    start, goal = [int(x) for x in next(f).split()]

f = open("output.txt", "w")
f.write(str(g.GBFS(start,goal)[0]))