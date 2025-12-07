# a minimum spanning tree (MST) is a subset of the edges of connected, weighted and undirected graphs which:
# - connects all vertices together
# - no cycle
# - minimum total edge
# real life problem-:
# - connect five island with bridges
# - the cost of bridges between island varies based on different factors
# - which bridge should be constructed so that all island are accessible and the cost is minimum
# disjoint set -> it is a data structure that keep track of set of elements which are partitioned into a number of disjoints and non overlapping sets
# and each sets have representative which help in identifying that sets, it is of the following type-:
# - make set (N) -> used to create initial set
# eg., A  B  C  D  E
# - union set (x, y) -> merge two given sets
# eg., union(A,B) -> AB  C  D  E   and union(A,E) -> ABE  C  D
# - find set (x) -> returns the set name in which this element is there
# eg., find(B) -> (in) AB  C  D  E (it will return) -> A
# time complexity -> O(1) and space complexity -> O(1)
class Disjoint_Set:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
    def union(self,x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

ver = ["A","B","C","D","E"]
ds = Disjoint_Set(ver)
ds.union("A", "B")
print(ds.find("A"))
print(ds.find("B"))

