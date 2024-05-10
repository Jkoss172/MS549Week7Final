import matplotlib.pyplot as plt
import networkx as nx

# helper functions to use three of the networkx algorithms
def dijkstra(graph,start,end):
    path = nx.dijkstra_path(graph,start,end)
    print(f'Dijkstra shortest path from {start} -> {end}: {path}')
def astar(graph,start,end):
    path = nx.astar_path(graph,start,end)
    print(f'A* shortest path from {start} -> {end}: {path}')
def bfs(graph,start):
    bfs_edges = nx.bfs_edges(graph,start)
    print(f'Breadth-first search from {start}: {list(bfs_edges)}')

edges = [['A','B'], ['A','D'], ['A','E'],['A','F'], ['A','G'],
         ['B','H'], ['B','I'], ['B','J'], ['B','C'],
         ['C','K'], ['C','L'],['C','M'], ['C','D'],
         ['D','N'], ['D','E'],
         ['E','O'], ['E','P'], ['E','F'],
         ['F','Q'],
         ['G','S'], ['G','T'],
         ['T','U']]

custom_edges = [
        ('A','B',4) ,
        ('A','D',2) ,
        ('A','E',4),
        ('A','F',8),
        ('A','G',3),
        ('B', 'H',2),
        ('B', 'I',2),
        ('B','J',1),
        ('B', 'C',3),
        ('C','K',1),
        ('C','L',2),
        ('C','M',2),
        ('C','D',2),
        ('D','N',1),
        ('D','E',4),
        ('E','O',1),
        ('E','P',1),
        ('E', 'F',5),
        ('F', 'Q',2),
        ('G', 'S',1),
        ('G', 'T',3),
        ('T', 'U',2)
]

G = nx.Graph()    
G.add_edges_from(edges)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(
    G, pos, edge_color='black', width=1, linewidths=1,
    node_size=500, node_color='green', alpha=0.9,
    labels={node: node for node in G.nodes()}
)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=
    {
        ('A','B'):4 ,
        ('A','D'):2 ,
        ('A','E'):4,
        ('A','F'):8,
        ('A','G'):3,
        ('B','H'):2,
        ('B','I'):2,
        ('B','J'):1,
        ('B','C'):3,
        ('C','K'):1,
        ('C','L'):2,
        ('C','M'):2,
        ('C','D'):8,
        ('D','N'):1,
        ('D','E'):4,
        ('E','O'):1,
        ('E','P'):1,
        ('E','F'):5,
        ('F','Q'):2,
        ('G','S'):1,
        ('G','T'):3,
        ('T','U'):2
        
    },
    font_color='red'
)
plt.axis('off')
plt.show()


# create nodes and graph based on board game edges with weights
G.add_weighted_edges_from(custom_edges)
# shortest path using dijkstra's algorithm
dijkstra(G,'A','H')
dijkstra(G,'D','G')
# shortest path using a* algorithm
astar(G,'C','S')
astar(G,'Q','T')
# breadth-first sorting, list of possible paths from a starting node
bfs(G,'C')
bfs(G,'G')