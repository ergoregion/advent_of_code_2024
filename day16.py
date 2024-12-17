import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation

with open('data/day16data', 'r') as file:
    txt = file.read()

arr = [list(x) for x in txt.splitlines()]
print(arr)


def is_a_block(c):
    return c == '#'

class Node:
    def __init__(self, p, orientation):
        self.p = np.array(p)
        self.orientation = orientation
        self.is_end = False
        self.edges =[]
class Edge:
    def __init__(self, node1, node2, cost):
        self.node1=node1
        self.node2=node2
        self.cost = cost

blocks = np.array([[is_a_block(y) for y in x] for x in arr])
nodes = []
nodes_indexed = {}

for i, l in enumerate(arr):
    for j, c in enumerate(l):
        if not blocks[i,j]:
            nodes.append(Node(np.array([i,j]),np.array([-1,0])))
            nodes.append(Node(np.array([i,j]),np.array([1,0])))
            nodes.append(Node(np.array([i,j]),np.array([0, -1])))
            nodes.append(Node(np.array([i,j]),np.array([0, 1])))

            if c == 'S':
                start_node = nodes[-1]
            if c == 'E':
                nodes[-1].is_end=True
                nodes[-2].is_end=True
                nodes[-3].is_end=True
                nodes[-4].is_end=True

            nodes[-1].edges.append(Edge(nodes[-1],nodes[-4], 1000))
            nodes[-1].edges.append(Edge(nodes[-1],nodes[-3], 1000))

            nodes[-2].edges.append(Edge(nodes[-2],nodes[-3], 1000))
            nodes[-2].edges.append(Edge(nodes[-2],nodes[-4], 1000))

            nodes[-3].edges.append(Edge(nodes[-3],nodes[-1], 1000))
            nodes[-3].edges.append(Edge(nodes[-3],nodes[-2], 1000))

            nodes[-4].edges.append(Edge(nodes[-4],nodes[-2], 1000))
            nodes[-4].edges.append(Edge(nodes[-4],nodes[-1], 1000))

            nodes_indexed[(i,j)] = nodes[-4:]


print(start_node.p)
print(len(nodes))

i=0
for n in nodes:
    if i%1000==0:
        print(i)
    i=i+1
    one_forward = (n.p + n.orientation)
    if not blocks[tuple(one_forward)]:
        node_candidates = (x for x in nodes_indexed[(one_forward[0],one_forward[1])] if (all(x.p == one_forward) and all(x.orientation==n.orientation)))
        n.edges.append(Edge(n, node_candidates.__next__(), 1))

node_best_scores = dict((n,np.inf) for n in nodes)
node_best_scores[start_node]=0
nodes_unsolved = set([start_node])
nodes_solved = set()


while not len(nodes_unsolved)==0:

    sorted_nodes = sorted(nodes_unsolved, key=lambda x: node_best_scores[x])
    best_node_unsolved = sorted_nodes[0]
    if (best_node_unsolved.is_end):
        print(f"score: {node_best_scores[best_node_unsolved]}")
        best_score = node_best_scores[best_node_unsolved]
        break
    score = node_best_scores[best_node_unsolved]
    for edge in best_node_unsolved.edges:
        if(edge.node2 not in nodes_solved):
            nodes_unsolved.add(edge.node2)
            new_score = score+edge.cost
            if (new_score < node_best_scores[edge.node2]):
                node_best_scores[edge.node2]= new_score
    nodes_unsolved.remove(best_node_unsolved)
    nodes_solved.add(best_node_unsolved)


for n in nodes:
    if n.is_end:
        print(node_best_scores[n])

node_best_scores = dict((n,np.inf) for n in nodes)
node_best_routes = dict((n,[]) for n in nodes)
node_best_scores[start_node]=0
nodes_unsolved = set([start_node])
nodes_solved = set()
nodes_involved_in_best_routes=set()

fig = plt.figure()
frames =[]
def printa(i, n):
    result = np.array([[(2 if is_a_block(y) else 0) for y in x] for x in arr])

    for b in nodes_solved:
        result[b.p[0], b.p[1]] = 4

    for b in nodes_unsolved:
        result[b.p[0], b.p[1]] = 10

    #for b in node_best_routes[n]:
       # result[b.p[0], b.p[1]] = 20

    frames.append([plt.imshow(result,animated=True)])


while not len(nodes_unsolved)==0:

    sorted_nodes = sorted(nodes_unsolved, key=lambda x: node_best_scores[x])
    best_node_unsolved = sorted_nodes[0]
    if (best_node_unsolved.is_end ):
        if(node_best_scores[best_node_unsolved] == best_score):
            for n in node_best_routes[best_node_unsolved]:
                nodes_involved_in_best_routes.add(n)
                nodes_involved_in_best_routes.add(best_node_unsolved)


    score = node_best_scores[best_node_unsolved]
    for edge in best_node_unsolved.edges:
        if(edge.node2 not in nodes_solved):
            nodes_unsolved.add(edge.node2)
            new_score = score+edge.cost
            if (new_score <= node_best_scores[edge.node2]):
                node_best_scores[edge.node2]= new_score
                node_best_routes[edge.node2].extend([x for x in node_best_routes[edge.node1]])
                node_best_routes[edge.node2].append(edge.node1)
    nodes_unsolved.remove(best_node_unsolved)
    nodes_solved.add(best_node_unsolved)
    if len(nodes_solved)%10000 ==0:
        printa(len(nodes_solved), best_node_unsolved)

print(len(nodes_involved_in_best_routes))


ani = animation.ArtistAnimation(fig, frames, interval=2, blit=True,
                                repeat_delay=100)

ani.save('c:/temp/images/maze_movie.mp4')

locations = [(n.p[0],n.p[1]) for n in nodes_involved_in_best_routes]
locations = set(locations)
print(len(locations))
