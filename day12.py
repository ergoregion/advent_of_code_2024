
with open('data/day12data', 'r') as file:
    txt = file.read()

arr = [list(x) for x in txt.splitlines()]
print(arr)

region_flags= [[None for a in b] for b in arr]
region_count =0
region_data={}

class Region:
    def __init__(self, flag, value):
        self.flag = flag
        self.value = value
        self.area = 0
        self.locations=[]

    def add_location(self, location):
        self.locations.append(location)

    def calculate(self):
        self.area = len(self.locations)
        self.perimeter_tops =[]
        self.perimeter_lefts =[]
        self.perimeter_rights =[]
        self.perimeter_bottoms =[]
        for item in self.locations:
            if self.locations.count((item[0]-1, item[1])) ==0:
                self.perimeter_tops.append(item)
            if self.locations.count((item[0], item[1]-1)) ==0:
                self.perimeter_lefts.append(item)
            if self.locations.count((item[0]+1, item[1])) ==0:
                self.perimeter_bottoms.append(item)
            if self.locations.count((item[0], item[1]+1)) ==0:
                self.perimeter_rights.append(item)

        self.perimeter = len(self.perimeter_tops) +len(self.perimeter_lefts)+len(self.perimeter_rights)+len(self.perimeter_bottoms)
        self.sides = 0
        for item in self.perimeter_tops:
            if self.perimeter_tops.count((item[0], item[1]-1)) ==0:
                self.sides =self.sides +1
        for item in self.perimeter_lefts:
            if self.perimeter_lefts.count((item[0]-1, item[1])) ==0:
                self.sides =self.sides +1
        for item in self.perimeter_bottoms:
            if self.perimeter_bottoms.count((item[0], item[1]+1)) ==0:
                self.sides =self.sides +1
        for item in self.perimeter_rights:
            if self.perimeter_rights.count((item[0]+1, item[1])) ==0:
                self.sides =self.sides +1

def extend_region(i,j, region_no, value):
    if( not value == arr[i][j]):
        return
    if(not region_flags[i][j]==None):
        return
    region_flags[i][j] = region_no
    region_data[region_no].add_location((i,j))
    if (i > 0):
        extend_region(i-1,j, region_no, value)
    if (j > 0):
        extend_region(i,j-1, region_no, value)
    if (i < len(arr)-1):
        extend_region(i+1,j, region_no, value)
    if (j < len(arr[0])-1):
        extend_region(i,j+1, region_no, value)


for i in range(len(arr)):
    for j in range(len(arr[0])):
        if (region_flags[i][j] == None):
            region_flag = region_count
            region_data[region_flag] = Region(region_flag, arr[i][j])
            extend_region(i,j,region_flag, arr[i][j])
            region_count = region_count+1
print(region_count)

result =0

for a in region_data.values():
    a.calculate()
    result += a.area * a.perimeter
print(result)

result =0
for a in region_data.values():
    a.calculate()
    result += a.area * a.sides
print(result)

