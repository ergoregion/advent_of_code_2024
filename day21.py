import numpy as np
import itertools
import re
import functools

with (open('data/day21data', 'r') as file):
    lines = file.readlines()


codes = [s.strip('\n') for s in lines]

print(codes)

class Graph:
    def __init__(self):
        self.nodes =[]
        self.edges =[]


numeric_graph = Graph()
numeric_graph.nodes = ['A','0','1','2','3','4','5','6','7','8','9']
numeric_graph.edges =[
    ('0','A','>'),
    ('A','3','^'),
    ('0','2','^'),
    ('1','2','>'),
    ('1','4','^'),
    ('2','3','>'),
    ('2','5','^'),
    ('3','6','^'),
    ('4','5','>'),
    ('4','7','^'),
    ('5','6','>'),
    ('5','8','^'),
    ('6','9','^'),
    ('7','8','>'),
    ('8','9','>'),
]

def reverse_direction(char):
    if char =='^':
        return 'V'
    elif char=='>':
        return'<'
    else:
        raise Exception

reverse_edges = []
for a in numeric_graph.edges:
    reverse_edges.append((a[1],a[0], reverse_direction(a[2])))
numeric_graph.edges.extend(reverse_edges)

print(len(numeric_graph.edges))


directional_graph = Graph()
directional_graph.nodes = ['A','<','>','^','V']
directional_graph.edges =[
    ('<','V','>'),
    ('V','>','>'),
    ('V','^','^'),
    ('>','A','^'),
    ('^','A','>'),
]
reverse_edges = []
for a in directional_graph.edges:
    reverse_edges.append((a[1],a[0], reverse_direction(a[2])))
directional_graph.edges.extend(reverse_edges)

print(len(directional_graph.edges))

def solve(graph, start_node, end_node):
    node_best_scores = dict((n, np.inf) for n in graph.nodes)
    node_best_routes = dict((n, set([''])) for n in graph.nodes)
    node_best_scores[start_node] = 0
    nodes_unsolved = set([start_node])
    nodes_solved = set()
    while not len(nodes_unsolved) == 0:

        sorted_nodes = sorted(nodes_unsolved, key=lambda x: node_best_scores[x])
        best_node_unsolved = sorted_nodes[0]
        score = node_best_scores[best_node_unsolved]
        routes = node_best_routes[best_node_unsolved]
        for edge in graph.edges:
            if (edge[0]==best_node_unsolved and edge[1] not in nodes_solved):
                nodes_unsolved.add(edge[1])
                new_score = score + 1
                new_routes = set([r +edge[2] for r in routes])
                if (new_score < node_best_scores[edge[1]]):
                    node_best_scores[edge[1]] = new_score
                    node_best_routes[edge[1]] = new_routes
                if (new_score == node_best_scores[edge[1]]):
                    node_best_scores[edge[1]] = new_score
                    node_best_routes[edge[1]] = node_best_routes[edge[1]].union(new_routes)
        nodes_unsolved.remove(best_node_unsolved)
        nodes_solved.add(best_node_unsolved)

    return node_best_scores[end_node], node_best_routes[end_node]

example = solve(numeric_graph, 'A','0')
print(example)


example = solve(directional_graph, 'A','<')
print(example)


def solve_sequence(graph, string):
    score,routes = solve(graph,'A', string[0])
    score = score+1
    routes = set(r+'A' for r in routes)
    for i in range(len(string)-1):
        new_score, new_routes = solve(graph,string[i], string[i+1])
        score+= new_score+1
        routes = set(r[0] + r[1]+ 'A' for r in itertools.product(routes, new_routes))
    return score, routes

print(solve_sequence(numeric_graph,"029A"))

print(solve_sequence(directional_graph,"^<"))
@functools.cache
def solve_directional_graph(start_node, end_node):
    return solve(directional_graph, start_node, end_node)

@functools.cache
def best_ways_to_press(string, start = 'A'):
    if len(string)==0:
        return 0,set([''])
    first = solve_directional_graph(start,string[0])
    end = best_ways_to_press(string[1:], string[0])
    return first[0]+1+end[0], set(r[0]+ 'A' + r[1] for r in itertools.product(first[1], end[1]))

print(best_ways_to_press("^<"))

def solve_nested_sequence(string):
    score, routes = solve_sequence(numeric_graph, string)

    for i in range(2):
        #print(len(routes))
        a = [best_ways_to_press(r) for r in routes]
        best_score = min(x[0] for x in a)
        routes = list(itertools.chain.from_iterable(x[1] for x in a if x[0]==best_score))
        smallest_route = min(routes, key=len)
        routes = list(r for r in routes if len(r)==len(smallest_route))
        #print(best_score)

    return best_score, set(routes)


result = 0
for r in codes:
    length, _ =solve_nested_sequence(r)
    numeric = int(re.findall(r"[-+]?[0-9]+", r)[0])
    print(length, numeric)
    result += length*numeric
print(result)

