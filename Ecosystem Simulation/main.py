import numpy as np
import matplotlib.pyplot as plt
from animal import AnimalManager, Rabbit, Lion

CONFIG = {"biome": "savannah",
          "tick_speed": 0.1,
          "plant_density": 0.3,
          "water_density": 0.1,
          "map_width": 100,
          "map_height": 100,
          }

class Biome:
    def __init__(self, name, base_color, plant_density, water_density):
        self.name = name
        self.base_color = base_color
        self.plant_density = plant_density
        self.water_density = water_density

    def generate_terrain(self, grid):
        probabilities = [1 - self.plant_density - self.water_density, self.plant_density, self.water_density]
        grid.cells = np.random.choice([0, 1, 2], size=grid.cells.shape, p=probabilities)


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.cells = np.zeros((height, width), dtype=int)


class Renderer:
    def __init__(self, grid, biome, manager):
        self.grid = grid
        self.biome = biome
        self.manager = manager

        self.fig, self.ax = plt.subplots()
        self.cmap = plt.matplotlib.colors.ListedColormap(["#C2B280", "#4a7c59", "#4a90d9"])
        self.im = self.ax.imshow(self.grid.cells, cmap=self.cmap, vmin=0, vmax=2)

    def update(self):
        self.im.set_data(self.grid.cells)

        self.ax.clear()
        self.ax.imshow(self.grid.cells, cmap=self.cmap, vmin=0, vmax=2)
        for animal in self.manager.animals:
            self.ax.plot(animal.x, animal.y, 'o', color=animal.color, markersize=1.25)

        plt.pause(1)

if __name__ == "__main__":
    grid = Grid(CONFIG["map_width"], CONFIG["map_height"])
    biome = Biome("savannah", "yellow", CONFIG["plant_density"], CONFIG["water_density"])
    biome.generate_terrain(grid)

    manager = AnimalManager(grid)
    manager.add_animal(Rabbit(10, 10))
    manager.add_animal(Rabbit(20, 15))
    manager.add_animal(Lion(30, 30))

    renderer = Renderer(grid, biome, manager)

    while True:
        renderer.update()
        manager.update()
