# topological sort -> sorts given action in such a way that if there is a dependency of one action on another, then the dependent action always comes later than its parent action
# eg.,              exercise            buy breakfast fruits
#                     ⬇️                 ⬇️
#                    bath         prepare breakfast
#                      ⬇️        /      ⬇️
#                    breakfast /      wash dishes
#                      ⬇️
#                     work
# (eg., for having breakfast we have to prepare it and to prepare it we have to buy some breakfast fruits/vegetables)
# topological sort algorithm-:
# if a vertex depends on current vertex:
#   go to that vertex and
#   then come back to current vertex
# else
#   push current vector to stack
# time complexity ->O(V + E) and space complexity -> O(V + E)
from collections import defaultdict
class Graph:
    def __init__(self, number_of_vertices):
        self.graph = defaultdict(list)
        self.number_of_vertices = number_of_vertices
    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
    def topological_sort_util(self, v, visited, stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topological_sort_util(i, visited, stack)
        stack.insert(0, v)
    def topological_sort(self):
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited:
                self.topological_sort_util(k, visited, stack)
        print(stack)

cust = Graph(8)
cust.add_edge("A", "C")
cust.add_edge("C", "E")
cust.add_edge("E", "H")
cust.add_edge("E", "F")
cust.add_edge("F", "G")
cust.add_edge("B", "D")
cust.add_edge("B", "C")
cust.add_edge("D", "F")
cust.topological_sort()
