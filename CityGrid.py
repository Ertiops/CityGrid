import numpy as np
import matplotlib.pyplot as plt
from itertools import product

class CityGrid:
    def __init__(self, N, M, obstruction_rate=0.3):
        self.N = N
        self.M = M
        self.grid = np.zeros((N, M))
        self.place_obstructions(obstruction_rate)
    
    def place_obstructions(self, rate):
        num_obstructions = int(rate * self.N * self.M)
        indices = list(product(range(self.N), range(self.M)))
        np.random.shuffle(indices)
        obstructions = indices[:num_obstructions]
        for i, j in obstructions:
            self.grid[i, j] = 1
    
    def place_tower(self, i, j, R):
        coverage = np.zeros_like(self.grid)
        for x in range(max(0, i - R), min(self.N, i + R + 1)):
            for y in range(max(0, j - R), min(self.M, j + R + 1)):
                coverage[x, y] = 1
        return coverage
    
    def display_tower_coverage(self, i, j, R):
        coverage = self.place_tower(i, j, R)
        plt.imshow(coverage, cmap='viridis', origin='upper')
        plt.title(f'Tower Coverage at ({i}, {j})')
        plt.show()
    
    def optimize_tower_placement(self, R):
        towers = []
        for i in range(self.N):
            for j in range(self.M):
                if self.grid[i, j] == 0:
                    towers.append((i, j))
        return towers
    
    def display_tower_placement(self, R):
        towers = self.optimize_tower_placement(R)
        for tower in towers:
            plt.plot(tower[1], tower[0], 'ro')  # Plot towers as red dots
        plt.imshow(self.grid, cmap='binary', origin='upper', alpha=0.3)
        plt.title('Optimized Tower Placement')
        plt.show()

    def find_reliable_path(self, start, end, towers):
        # Simulating a reliable path finding algorithm
        # In this example, simply connecting towers with fewer hops
        path = [start]
        current = start
        while current != end:
            next_tower = min(towers, key=lambda x: self.distance(current, x))
            path.append(next_tower)
            current = next_tower
        return path
    
    def distance(self, tower1, tower2):
        return abs(tower1[0] - tower2[0]) + abs(tower1[1] - tower2[1])

    def visualize_city(self):
        plt.imshow(self.grid, cmap='binary', origin='upper', alpha=0.7)
        plt.title('City Grid')
        plt.show()

# Example Usage


city = CityGrid(N=20, M=20, obstruction_rate=0.3)


city.visualize_city()

city.display_tower_coverage(i=10, j=10, R=3)

city.display_tower_placement(R=3)

start_tower = (2, 3)
end_tower = (15, 18)
towers_list = city.optimize_tower_placement(R=3)
reliable_path = city.find_reliable_path(start_tower, end_tower, towers_list)
print("Reliable Path:", reliable_path)

exit()