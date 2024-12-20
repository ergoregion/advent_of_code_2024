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
    def __init__(self, node1, node2, cost):
        self.node1=node1
        self.node2=node2
        self.cost = cost

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




def solve(from_node):
    node_best_scores = dict((n,np.inf) for n in nodes.values())
    node_best_scores[from_node]=0
    nodes_unsolved = set([from_node])
    nodes_solved = set()

    while not len(nodes_unsolved) == 0:

        sorted_nodes = sorted(nodes_unsolved, key=lambda x: node_best_scores[x])
        best_node_unsolved = sorted_nodes[0]

        score = node_best_scores[best_node_unsolved]
        for edge in best_node_unsolved.edges:
            if (edge.node2 not in nodes_solved):
                nodes_unsolved.add(edge.node2)
                new_score = score + 1
                if (new_score <= node_best_scores[edge.node2]):
                    node_best_scores[edge.node2] = new_score

        nodes_unsolved.remove(best_node_unsolved)
        nodes_solved.add(best_node_unsolved)
    return node_best_scores

node_best_scores_from_start = solve(start_node)
node_best_scores_to_end = solve(end_node)

baseline = node_best_scores_from_start[end_node]
print(baseline)

cheats = []

for n in nodes.values():
    for i in range(-2,3):
        for j in range(-2,3):
            cost = abs(i)+abs(j)
            if cost <=2:
                destination = n.p + np.array([i,j])
                if tuple(destination) in nodes:
                    m=nodes[tuple(destination)]
                    cheats.append(Cheat(n, m, 2))


print(len(cheats))

cheating_scores = {}

for i, c in enumerate(cheats):
    #print(f" {i} of {len(cheats)}")
    cheating_scores[c] = max(baseline-(node_best_scores_from_start[c.node1]+c.cost+ node_best_scores_to_end[c.node2]), 0)


v = cheating_scores.values()
result = sum(1 for x in v if x>=100)
print(result)



options= set(v)
counts = dict((o, sum(1 for x in v if x ==o)) for o in options)
print(counts)


# Part 2 add more cheats

cheats = []

for n in nodes.values():
    for i in range(-20,21):
        for j in range(-20,21):
            cost =  abs(i)+abs(j)
            if(cost<=20):
                destination = n.p + np.array([i, j])
                if tuple(destination) in nodes:
                    cheats.append(Cheat(n, nodes[tuple(destination)], cost))


cheating_scores = {}

for i, c in enumerate(cheats):
    #print(f" {i} of {len(cheats)}")
    cheating_scores[c] = max(baseline-(node_best_scores_from_start[c.node1]+c.cost+ node_best_scores_to_end[c.node2]), 0)


v = cheating_scores.values()
result = sum(1 for x in v if x>=100)

print(result)


