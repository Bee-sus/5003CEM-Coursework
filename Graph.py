class Graph:

    def __init__(self):
        # Dictionary to store adjacency list representation
        self.adj_list = {}

    def addVertex(self, vertex):
        # Add a new vertex to the graph
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def addEdge(self, from_vertex, to_vertex):
        # Connect one vertex with another vertex (directed edge)
        # Ensure both vertices exist in the graph
        if from_vertex not in self.adj_list:
            self.addVertex(from_vertex)
        if to_vertex not in self.adj_list:
            self.addVertex(to_vertex)

        # Add edge if it doesn't already exist
        if to_vertex not in self.adj_list[from_vertex]:
            self.adj_list[from_vertex].append(to_vertex)
            return True
        return False

    def getToAdjVertex(self, vertex):
        # List all vertices that have outgoing edges from the given vertex
        if vertex in self.adj_list:
            return self.adj_list[vertex].copy()
        return []

    def getFromAdjVertex(self, target_vertex):
        # Get all vertices that have edges pointing to the given vertex
        incoming = []
        for vertex in self.adj_list:
            if target_vertex in self.adj_list[vertex]:
                incoming.append(vertex)
        return incoming

