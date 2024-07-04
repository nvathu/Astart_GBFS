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
        
    def A_star_1(self,s,g,heuristic):
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
                return hh
            else:
                for v, _ in self.graph[cur_node]:
                    if v not in visited:
                        frontiers.push(heuristic[v] + hh, v)
    
      
    def A_star(self, s, g):
        Frontier = PriorityQueue()
        expanded = []
        Frontier.push(s,0)
        temp = 0
        while not Frontier.isEmpty():
            cost_old, node = Frontier.pop() 
            if node in expanded:
                continue
            else:
                expanded.append(node)
            if node == g:
                return cost_old, expanded
            if self.graph.get(node) is not None:
                for nodee in self.graph.get(node):
                    if nodee[0] not in expanded: 
                        Frontier.push(nodee[0], nodee[1] + cost_old)




   
        
                

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

print("Ham a* co heristic input", g.A_star_1(start, goal, heuristic))

print("Ham a* khong co heristic input nhung ra ket qua output nhu yeu cau \n1: tong do dai duong di",g.A_star(start,goal)[0], "\n2: duong di tim duoc\n",g.A_star(start,goal)[1])

f = open("output.txt", "w")
f.write(str(g.A_star(start,goal)[0]))
