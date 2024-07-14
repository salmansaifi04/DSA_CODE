class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_matrix = [[0]*vno for i in range(vno)]

    def add_edge(self, u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print('Invalid vertex')

    def remove_graph(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print('Invalid vertex')

    def has_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            print('Invalid vertex')

    def print_adj_matrix(self):
        for i in self.adj_matrix:
            print(" ".join(map(str, i)))


g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(3,4)

g.print_adj_matrix()
g.remove_graph(3,4)
print("after remove")
g.print_adj_matrix()

print(g.has_edge(0,1))
            