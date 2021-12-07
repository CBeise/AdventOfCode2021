import re


class Fish:
    """
    This creates a Fish object with a spawn timer and a population of fish with that spawn timer
    """
    def __init__(self, spawn, population=None):
        self.spawn = spawn
        self.population = 0

        if population:
            self.population = population


class School:
    """
    This creates a School object which contains a group of Fish objects
    """
    def __init__(self):
        self.fish = []

    def add_fish(self, spawn, population=1):
        i = 0
        while i <= len(self.fish):
            if i == len(self.fish):
                self.fish.append(Fish(spawn, population))
                i += 1
            elif self.fish[i].spawn == spawn:
                self.fish[i].population += population
                i = len(self.fish)
            i += 1


with open("input.txt") as coordinate_file:
    numbers = list(map(int, re.findall('\d+', coordinate_file.read())))

fish = School()

for i in range(len(numbers)):
    fish.add_fish(numbers[i])

print(fish)

for i in range(256):
    for j in range(len(fish.fish)):
        fish.fish[j].spawn -= 1
    j = 0
    while j < len(fish.fish):
        if fish.fish[j].spawn == -1:
            fish.add_fish(8, fish.fish[j].population)
            fish.add_fish(6, fish.fish[j].population)
            del fish.fish[j]
        else:
            j += 1

total = 0

for i in range(len(fish.fish)):
    total += fish.fish[i].population

print(total)
