# single source sortest path problem -> a single source problem is about finding a path between a given vertex (called source) to all other vertices in a graph such that the total distance between them (source and destination) is minimum.
# the problem:
# - five offices in different cities
# - travel cost between cities are known
# - find the cheapest way head office to branches in different cities
#--BFS for SSSP--
# enqueue any starting vertex
# while queue is not empty
#   p = dequeue()
#   if p is unvisited
#       mark it visited
#       enqueue all adjacent unvisited vertices of p
#       update parent of adjacent vertices to cur_vertex
# time complexity -> O(E) and space complexity -> O(E)
# why BFS does not work with weighted graph?
# graph type                        BFS
# unweighted-undirected             OK
# unweighted-directed               OK
# positive-weighted-undirected      ❌
# positive-weighted-directed        ❌
# negative-weighted-undirected      ❌
# negative-weighted-directed        ❌
# hence BFS not work with weighted graph because it does not give us best solution in the case
# why does DFS not work with SSSP?
# DFS has the tendency to go as far as possible form the source, hence it can never find sortest path
#--Dijkstra's algorithm for SSSP--
class Graph:
    def __init__(self, g_dict = None):
        if g_dict is None:
            g_dict = {}
        self.g_dict = g_dict
    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.g_dict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

custom_dict = {"a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]}
g = Graph(custom_dict)
print(g.bfs("a", "f"))

#--dijkstra implementation--

import heapq
class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex
class Nodes:
    def __init__(self, name):
        self.name = name
        self.visited = False
        # previous node that we come to this node
        self.predecessor = None
        self.neighbour = []
        self.min_distance = float("inf")
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbour.append(edge)
class Dijkstra:
    def __init__(self):
        self.heap = []
    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            # pop element with the lowest distance
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # consider the neighbours
            for edge in actual_vertex.neighbour:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    # update the heap
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True
    def get_shortest_path(self, vertex):
        print(f"the shortest path to the vertex is : {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.predecessor

# step 1 - create node
nodeA = Nodes("A")
nodeB = Nodes("B")
nodeC = Nodes("C")
nodeD = Nodes("D")
nodeE = Nodes("E")
nodeF = Nodes("F")
nodeG = Nodes("G")
nodeH = Nodes("H")
# step 2 - create edge
nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)
nodeB.add_edge(5,nodeD)
nodeB.add_edge(16, nodeE)
nodeB.add_edge(13, nodeF)
nodeC.add_edge(6,nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)
nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)
nodeE.add_edge(10, nodeG)
nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)
nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)
algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeG)
# dijkstra's algorithm with negative cycle
# a path is called negative cycle if:
# - there is a cycle
# - total weight of cycle is a negative number
# it doesn't work with dijkstra algorithm as, we cannot find the minimum distance in negative cycle
# we cannot find a negative cycle in graph

#--bellman ford algorithm--
#  type                             BFS     dijkstra    bellman ford
# unweighted-undirected             OK          OK          OK
# unweighted-directed               OK          OK          OK
# positive-weighted-undirected      ❌          OK          OK
# positive-weighted-directed        ❌          OK          OK
# negative-weighted-undirected      ❌          OK          OK
# negative-weighted-directed        ❌          OK          OK
# negative cycle                    ❌          ❌          OK
# bellman ford algorithm is used to find single source path. if there is a negative cycle it catches it and report its existence
# algorithm-:
# if the distance of destination vertex > (distance of source vertex + weight between source and destination vertex):
#   update distance of destination vertex to (distance of source vertex + weight between source and destination vertex)
# why bellman ford runs V - 1 times?
# if any node is achieved better distance in previous iteration, then better distance is used to improve distance of other vertices
# identify worst case graph that can be give to us
# time complexity -> O(EV) and space complexity -> O(V)
class Graph2:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
    def add_node(self, value):
        self.nodes.append(value)
    def print_solution(self, dist):
        print('vertex distance from source')
        for key, value in dist.items():
            print(' ' + key, ' :  ', value)
    def bellman_ford(self, src):
        dist = { i : float('inf') for i in self.nodes}
        dist[src] = 0
        for _ in range(self.V-1):
            for s, d, w in self.graph:
                if dist[s] != float('inf') and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        for s, d, w in self.graph:
            if dist[s] != float('inf') and dist[s] + w < dist[d]:
                print("graph contains negative cycle")
                return
        self.print_solution(dist)

g = Graph2(5)
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellman_ford("E")
#_______________________________________________________________________________________________________________|
#  means of define |                BFS            |     dijkstra                | bellman ford                 |
#---------------------------------------------------------------------------------------------------------------|
# time complexity  |                O(V^2)         |      O(V^2)                 |    O(VE)                     |
#---------------------------------------------------------------------------------------------------------------|
# space complexity |                O(E)           |       O(V)                  |    O(V)                      |
#---------------------------------------------------------------------------------------------------------------|
# implementation   |                easy           |       moderate              |   moderate                   |
#---------------------------------------------------------------------------------------------------------------|
# limitation       |   not work for weighted graph | not work for negative cycle |     N/A                      |
#---------------------------------------------------------------------------------------------------------------|
# unweighted graph |                 ok            |         ok                  |    ok                        |
#                  |--------------------------------------------------------------------------------------------|
#                 | use this as time complexity is | not use as implementation is | not use as time             |
#                  |  good and easy to implement   |      not easy               | complexity is bad            |
#---------------------------------------------------------------------------------------------------------------|
# weighted graph   |                 ❌            |         OK                  |     OK                       |
#                  |--------------------------------------------------------------------------------------------|
#                  |     not supported             | use as time complexity is   |   not use as time            |
#                  |                               | better than bellman ford    |   complexity is bad          |
#---------------------------------------------------------------------------------------------------------------|
# negative cycle   |                 ❌            |         ❌                 |      OK                      |
#                  |--------------------------------------------------------------------------------------------|
#                  |        not supported         |     not supported           | use this as other not support |
#---------------------------------------------------------------------------------------------------------------|

# Floyd warshall-:
#       8
#  A--------->B                      given
#  |  ↖ 4 ↗ 2 |  1                A  B  C  D
# 1 ⬇ /   \   ⬇                A  0  8  ♾️ 1
#  D--------->C                B ♾️️ 0   1  ♾️
#        9                     C 4 ♾️   0  ♾️
#                              D ♾️️ 2   9   0
# method of floyd warshall algorithm is:-
# if D[u][v] > D[u][viaX] + D[viaX][v]:
#   D[u][v] = D[u][viaX] + D[viaX][v]
# the only three possible ways to find distance between vertices and edges-:
# - the vertices is not reachable
# - two vertices are directly connected
#       this is the best solution
#       it can be improved via other vertex
# - two vertices are connected via other vertex
# floyd warshall does not work for negative cycle-:
# - to go through cycle we need to go via negative participating vertex at least twice
# - FW never runs loop twice via same vertex
# - hence, FW can never detect a negative cycle
# time complexity -> O(V^3) and space complexity -> O(V^2)
INF = 9999
def print_solution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF" , end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")
def floyd_warshall(nV, G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    print_solution(nV, distance)

G = [[0,8,INF,1],
     [INF, 0,1,INF],
     [4,INF,0,INF],
     [INF,2,9,1]]
floyd_warshall(4, G)
#  type                             BFS     dijkstra    bellman ford    floyd warshall
# unweighted-undirected             OK          OK          OK                 OK
# unweighted-directed               OK          OK          OK                 OK
# positive-weighted-undirected      ❌          OK          OK                 OK
# positive-weighted-directed        ❌          OK          OK                 OK
# negative-weighted-undirected      ❌          OK          OK                 OK
# negative-weighted-directed        ❌          OK          OK                 OK
# negative cycle                    ❌          ❌          OK                 ❌

#_______________________________________________________________________________________________________________|_____________________________|
#  means of define |                BFS            |     dijkstra                | bellman ford                 |     floyd warshall          |
#---------------------------------------------------------------------------------------------------------------|-----------------------------|
# time complexity  |                O(V^2)         |      O(V^2)                 |    O(VE)                     |          O(V^3)             |
#---------------------------------------------------------------------------------------------------------------|-----------------------------|
# space complexity |                O(E)           |       O(V)                  |    O(V)                      |           O(V^2)            |
#---------------------------------------------------------------------------------------------------------------|-----------------------------|
# implementation   |                easy           |       moderate              |   moderate                   |       moderate              |
#---------------------------------------------------------------------------------------------------------------|-----------------------------|
# limitation       |   not work for weighted graph | not work for negative cycle |     N/A                      | not work for negative cycle |
#---------------------------------------------------------------------------------------------------------------|-----------------------------|
# unweighted graph |                 ok            |         ok                  |    ok                        |       OK                    |
#                  |--------------------------------------------------------------------------------------------|-----------------------------|
#                 | use this as time complexity is | not use as implementation is | not use as time             |  can be used                |
#                  |  good and easy to implement   |      not easy               | complexity is bad            |                             |
#---------------------------------------------------------------------------------------------------------------|-----------------------------|
# weighted graph   |                 ❌            |         OK                  |     OK                       |            ok               |
#                  |--------------------------------------------------------------------------------------------|-----------------------------|
#                  |     not supported             | use as time complexity is   |   not use as time            | can be preferred as         |
#                  |                               | better than bellman ford    |   complexity is bad          |implementation is easy       |
#---------------------------------------------------------------------------------------------------------------|-----------------------------|
# negative cycle   |                 ❌            |         ❌                 |      OK                      |          ❌                 |
#                  |--------------------------------------------------------------------------------------------|-----------------------------|
#                  |        not supported         |     not supported           | use this as other not support |   not supported             |
#---------------------------------------------------------------------------------------------------------------|-----------------------------|
