import numpy as np
import re

grid_size= (71,71)
#grid_size = (7,7)

bytes_to_fall = 1024
#bytes_to_fall = 12

blocks = []
with (open('data/day18data', 'r') as file):
    lines = file.readlines()
    for i,l in enumerate(lines):
        a_values = re.findall(r"[-+]?[0-9]+", lines[i])
        blocks.append((int(a_values[0]),int(a_values[1])))
print(blocks)


class Node:
    def __init__(self, p):
        self.p = np.array(p)
        self.edges =[]
class Edge:
    def __init__(self, node1, node2,):
        self.node1=node1
        self.node2=node2

nodes = [[] for i in range(grid_size[0])]
for i in range(grid_size[0]):
    for j in range(grid_size[1]):
        nodes[i].append((Node([i,j])))

def node (i,j,r):
    if (i in range(grid_size[0]) and j in range(grid_size[0])):
        if (i,j) not in blocks[:r] :
            return nodes[i][j]
        else:
            return None
    else:
        return None

def setup_edges(r):

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            n= node(i,j,r)
            if n is not None:
                n.edges = []
                m= node(i-1,j,r)
                if m is not None:
                    n.edges.append(Edge(n,m))
                m= node(i+1,j,r)
                if m is not None:
                    n.edges.append(Edge(n,m))
                m= node(i,j-1,r)
                if m is not None:
                    n.edges.append(Edge(n,m))
                m= node(i,j+1,r)
                if m is not None:
                    n.edges.append(Edge(n,m))


start_node = nodes[0][0]
last_node = nodes[-1][-1]

node_list = [item for sublist in nodes for item in sublist]

def run(r):
    setup_edges(r)
    node_best_scores = dict((n,np.inf) for n in node_list)
    node_best_scores[start_node]=0
    nodes_unsolved = set([start_node])
    nodes_solved = set()


    while not len(nodes_unsolved)==0:

        sorted_nodes = sorted(nodes_unsolved, key=lambda x: node_best_scores[x])
        best_node_unsolved = sorted_nodes[0]
        if (best_node_unsolved == last_node):
            break
        score = node_best_scores[best_node_unsolved]
        for edge in best_node_unsolved.edges:
            if(edge.node2 not in nodes_solved):
                nodes_unsolved.add(edge.node2)
                new_score = score+1
                if (new_score < node_best_scores[edge.node2]):
                    node_best_scores[edge.node2]= new_score
        nodes_unsolved.remove(best_node_unsolved)
        nodes_solved.add(best_node_unsolved)
    return node_best_scores[last_node]



print(run(bytes_to_fall))
assert(run(2870) != np.inf)

for i in range(len(blocks))[2870:]:
    print(i)

    r = run(i)
    if r == np.inf:
        print(f"First failure at {i}  Block at location:  {','.join(str(b) for b in blocks[0:i][-1])}")
        break




