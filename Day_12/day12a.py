with open("input.txt") as input_file:
    data = input_file.read().split()

edges = []

for i in data:
    edges.append(i.split("-"))


class Cave:
    """
    This creates a Cave class
    """
    def __init__(self, name):
        self.name = name
        self.available = True
        if self.name.isupper():
            self.big = True
        else:
            self.big = False
        self.neighbors = []

    def add_neighbor(self, neighbor):
        for elem in caves:
            if elem.name == neighbor:
                self.neighbors.append(elem)

    def find_route(self, route):
        """This searches for a route to the exit"""
        if self.name == "end":
            routes.add(route)
            return
        if self.available:
            if not self.big:
                self.available = False
            route += self.name
            for c in self.neighbors:
                c.find_route(route)
            self.available = True
        return


cave_list = []

for i in range(len(edges)):
    for j in range(2):
        if edges[i][j] not in cave_list:
            cave_list.append(edges[i][j])

caves = []

for i in cave_list:
    caves.append(Cave(i))

for i in edges:
    for j in caves:
        if j.name == i[0]:
            j.add_neighbor(i[1])

for i in edges:
    for j in caves:
        if j.name == i[1]:
            j.add_neighbor(i[0])

routes = set()

for i in caves:
    if i.name == "start":
        i.find_route("")

print("Part 1: ", len(routes))
