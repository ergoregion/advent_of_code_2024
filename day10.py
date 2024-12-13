
with open('data/day10data', 'r') as file:
    txt = file.read()

arr = [list(x) for x in txt.splitlines()]
arr = [[int(i) for i in x] for x in txt.splitlines()]
print(arr)

reachable_sinks = [[None for i in x] for x in txt.splitlines()]
routes = [[None for i in x] for x in txt.splitlines()]
print(reachable_sinks)

class Location:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def value(self):
        return arr[self.x][self.y]

    def steps_up_one(self):
        result =[]
        v = arr[self.x][self.y]
        if(self.x-1>=0 and arr[self.x-1][self.y] == v+1):
            result.append(Location(self.x-1,self.y))
        if(self.y-1>=0 and arr[self.x][self.y-1] == v+1):
            result.append(Location(self.x,self.y-1))
        if(self.x+1<len(arr) and arr[self.x+1][self.y] == v+1):
            result.append(Location(self.x+1,self.y))
        if(self.y+1<len(arr[0]) and arr[self.x][self.y+1] == v+1):
            result.append(Location(self.x,self.y+1))
        return result

    def reachable_sinks(self):
        if arr[self.x][self.y]==9 :
            return set([tuple([self.x,self.y])])
        if reachable_sinks[self.x][self.y] is None:
            r = set()
            for l in self.steps_up_one():
                r= r.union(l.reachable_sinks())
            reachable_sinks[self.x][self.y] = r

        return reachable_sinks[self.x][self.y]


    def routes(self):
        if arr[self.x][self.y]==9 :
            return 1
        if routes[self.x][self.y] is None:
            r = 0
            for l in self.steps_up_one():
                r = r+l.routes()
            routes[self.x][self.y] = r

        return routes[self.x][self.y]

#print(arr[3][5])
#l = Location(3,5).steps_up_one()
#print(Location(3,5).reachable_sinks())

result =0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] ==0:
            l= Location(i,j)
            print(l.reachable_sinks())
            result =result+(len(l.reachable_sinks()))
print(result)


result =0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] ==0:
            l= Location(i,j)
            print(l.routes())
            result =result+l.routes()
print(result)


