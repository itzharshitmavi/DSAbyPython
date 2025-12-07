# Graph traversal-:
# it is a way of visiting all vertices in graph
# 1. breadth first search -> BFS is an algorithm for traversing graph data structure. it starts at some arbitrary node of a graph and
# explores the neighbor nodes(which are ar current level) first, before moving to the next level neighbours
# - BFS algorithm-:
# enqueue any starting vertex
# while queue is not empty
#   p = dequeue()
#   if p is unvisited
#       mark it visited
#       enqueue all adjacent
#       unvisited vertices of p
# time complexity -> O(V + E) and space complexity -> O(V + E)
# 2. depth first search -> DFS is an algorithm for traversing a graph data structure which starts selecting some arbitrary node
# and explores as far as possible along each edge before
# DFS algorithm-:
# push any staring vertex
# while stack is not empty
#   p = pop()
#   if p is unvisited
#       mark it visited
#       push all adjacent
#       unvisited vertices of p
# time complexity ->O(V + E) and space complexity -> O(V + E)
class Graph:
    def __init__(self, g_dict = None):
        if g_dict is None:
            g_dict = {}
        self.g_dict = g_dict
    def add_edge(self, vertex, edge):
        self.g_dict[vertex].append(edge)
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            de_vertex = queue.pop(0)
            print(de_vertex)
            for adjacent_vertex in self.g_dict[de_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    queue.append(adjacent_vertex)
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            pop_vertex = stack.pop()
            print(pop_vertex)
            for adjacent_vertex in self.g_dict[pop_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    stack.append(adjacent_vertex)

cust_dict = {"a" : ["b","c"],
             "b" : ["a","d","e"],
             "c" : ["a","e"],
             "d" : ["b","e","f"],
             "e" : ["d","f"],
             "f" : ["d","e"]}
graph = Graph(cust_dict)
graph.bfs("a")
graph.dfs("a")
