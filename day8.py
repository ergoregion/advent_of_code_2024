

with open('data/day8data', 'r') as file:
    txt = file.read()

arr = [list(x) for x in txt.splitlines()]
print(arr)

width = len(arr[0])
height = len(arr)

anteni = []

for i in range(width):
    for j in range(height):
        if arr[i][j] != '.':
            anteni.append([arr[i][j], i,j ])

print(anteni)
nodes = set()
for a in anteni:
    for b in anteni:
        if a==b:
            pass
        elif a[0]!=b[0]:
            pass
        else:
            a_x=a[1]
            a_y=a[2]
            b_x=b[1]
            b_y=b[2]


            node_x = a_x
            node_y = a_y
            i=0
            while(node_x>=0 and node_y>=0 and node_x<width and node_y<height):
                nodes.add((node_x, node_y))
                i=i+1
                node_x = a_x +i*(a_x- b_x)
                node_y =  a_y+i*(a_y - b_y)

print(nodes)

print(len(nodes))