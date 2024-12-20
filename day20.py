import numpy as np

with open('data/day20data', 'r') as file:
    txt = file.read()

arr = [list(x) for x in txt.splitlines()]
print(arr)


def is_a_block(c):
    return c == '#'

blocks = np.array([[is_a_block(y) for y in x] for x in arr])



class Node:
    def __init__(self, p):
        self.p = np.array(p)
        self.edges =[]
class Edge:
    def __init__(self, node1, node2):
        self.node1=node1
        self.node2=node2

class Cheat:
    def __init__(self, node1, node2):
        self.node1=node1
        self.node2=node2

nodes = {}

for i, l in enumerate(arr):
    for j, c in enumerate(l):
        if not blocks[i,j]:
            node = Node(np.array([i,j]))
            nodes[(i,j)] = node

            if c == 'S':
                start_node = node
            if c == 'E':
                end_node = node

cheats = []

for n in nodes.values():
    right = n.p +np.array([1,0])
    if tuple(right) in nodes:
        n.edges.append(Edge(n, nodes[tuple(right)]))

    left = n.p +np.array([-1,0])
    if tuple(left) in nodes:
        n.edges.append(Edge(n, nodes[tuple(left)]))

    up = n.p +np.array([0,1])
    if tuple(up) in nodes:
        n.edges.append(Edge(n, nodes[tuple(up)]))

    down = n.p +np.array([0,-1])
    if tuple(down) in nodes:
        n.edges.append(Edge(n, nodes[tuple(down)]))

    right2 = n.p + np.array([2, 0])
    if tuple(right2) in nodes:
        cheats.append(Cheat(n, nodes[tuple(right2)]))

    left2 = n.p + np.array([-2, 0])
    if tuple(left2) in nodes:
        cheats.append(Cheat(n, nodes[tuple(left2)]))

    up2 = n.p + np.array([0, 2])
    if tuple(up2) in nodes:
        cheats.append(Cheat(n, nodes[tuple(up2)]))

    down2 = n.p + np.array([0, -2])
    if tuple(down2) in nodes:
        cheats.append(Cheat(n, nodes[tuple(down2)]))



def solve(cheat = None):
    node_best_scores = dict((n,np.inf) for n in nodes.values())
    node_best_scores[start_node]=0
    nodes_unsolved = set([start_node])
    nodes_solved = set()

    while not len(nodes_unsolved) == 0:

        sorted_nodes = sorted(nodes_unsolved, key=lambda x: node_best_scores[x])
        best_node_unsolved = sorted_nodes[0]
        if (best_node_unsolved== end_node):
            best_score = node_best_scores[best_node_unsolved]
            return best_score

        score = node_best_scores[best_node_unsolved]
        for edge in best_node_unsolved.edges:
            if (edge.node2 not in nodes_solved):
                nodes_unsolved.add(edge.node2)
                new_score = score + 1
                if (new_score <= node_best_scores[edge.node2]):
                    node_best_scores[edge.node2] = new_score
        if cheat and cheat.node1 == best_node_unsolved:
            if (cheat.node2 not in nodes_solved):
                nodes_unsolved.add(cheat.node2)
                new_score = score + 2
                if (new_score <= node_best_scores[cheat.node2]):
                    node_best_scores[cheat.node2] = new_score

        nodes_unsolved.remove(best_node_unsolved)
        nodes_solved.add(best_node_unsolved)
    return np.inf

baseline = solve()
print(baseline)








#cheating_scores = {}

#for i, c in enumerate(cheats):
#    print(f" {i} of {len(cheats)}")
#    cheating_scores[c] = baseline-solve(c)


#v = cheating_scores.values()
#options= set(v)
#counts = dict((o, sum(1 for x in v if x ==o)) for o in options)
#print(counts)

result = sum(counts[x] for x in counts if x>=100)
print(result)