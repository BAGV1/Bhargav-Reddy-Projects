import numpy as np
import matplotlib.pyplot as plt

CONFIG = {"biome": "savannah",
          "tick_speed": 0.1,
          "plant_density": 0.3,
          "water_density": 0.1,
          "map_width": 50,
          "map_height": 50,
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
    def __init__(self, grid, biome):
        self.grid = grid
        self.biome = biome

        self.fig, self.ax = plt.subplots()
        self.im = self.ax.imshow(self.grid.cells, cmap='YlGn')

    def update(self):
        self.im.set_data(self.grid.cells)
        plt.pause(0.1)


if __name__ == "__main__":
    grid = Grid(CONFIG["map_width"], CONFIG["map_height"])
    biome = Biome("savannah", "yellow", CONFIG["plant_density"], CONFIG["water_density"])
    biome.generate_terrain(grid)
    renderer = Renderer(grid, biome)

    while True:
        renderer.update()
