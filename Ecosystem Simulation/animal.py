class Animal:
    def __init__(self, x, y, health, speed, vision_range, reproduction_threshold):
        self.x = x
        self.y = y
        self.health = health
        self.speed = speed
        self.vision_range = vision_range
        self.reproduction_threshold = reproduction_threshold

        self.hunger = 100
        self.thirst = 100

    def update(self):
        self.health -= 0.1

        self.hunger -= 1
        self.thirst -= 1

        if self.hunger <= 0 or self.thirst <= 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

class Herbivore(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, health=80, speed=2, vision_range=5, reproduction_threshold=70)

class Carnivore(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, health=100, speed=4, vision_range=7, reproduction_threshold=60)

class Rabbit(Herbivore):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Rabbit"
        self.color = "White"

class Lion(Carnivore):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Lion"
        self.color = "Red"

class AnimalManager:
    def __init__(self, grid):
        self.grid = grid
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def update(self):
        for animal in self.animals:
            animal.update()
            self.animals = [a for a in self.animals if a.is_alive()]
