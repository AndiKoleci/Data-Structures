class Graph:
    def __init__(self, type):
        self.type=type 
        #0 = undirected
        #1 = directed
        self.nodes = []
        self.edges = []
        
    def add_edge(self, tuple):
        node1 = tuple[0]
        node2 = tuple[1]
        if node1 not in self.nodes:
            self.nodes.append(node1)
        if node2 not in self.nodes:
            self.nodes.append(node2)    
        edge = (tuple[0], tuple[1], tuple[2])
            
        if edge not in self.edges:
            self.edges.append(edge)
                
        if self.type==0:
            edge = (tuple[1], tuple[0], tuple[2])
            if edge not in self.edges:
                self.edges.append(edge)
    
    def init_graph(self, list):
        for tuple in list:
            self.add_edge(tuple)
                
    def print_graph(self):
        for edge in self.edges:
            print(str(edge[0]) + " " + str(edge[1]) + " " + str(edge[2]))
                
    def print_nodes(self):
        for edge in self.edges:
            print(str(edge))
            
    
    
connections = [('A', 'B', 2), ('B', 'C', 3)]
graph = Graph(0)
graph.init_graph(connections)
graph.print_nodes()
