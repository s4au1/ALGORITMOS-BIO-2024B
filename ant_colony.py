import random
import math

class AntColony:
    def __init__(self, num_cities, num_ants, alpha, beta, rho, Q):
        self.num_cities = num_cities
        self.num_ants = num_ants
        self.alpha = alpha  # pheromone importance
        self.beta = beta  # heuristic importance
        self.rho = rho  # evaporation rate
        self.Q = Q  # pheromone update strength
        self.cities = [(random.random(), random.random()) for _ in range(num_cities)]
        self.distances = self.calculate_distances()
        self.pheromone_trails = [[1.0 for _ in range(num_cities)] for _ in range(num_cities)]

    def calculate_distances(self):
        distances = [[0.0 for _ in range(self.num_cities)] for _ in range(self.num_cities)]
        for i in range(self.num_cities):
            for j in range(i+1, self.num_cities):
                distances[i][j] = distances[j][i] = math.sqrt((self.cities[i][0] - self.cities[j][0])**2 + (self.cities[i][1] - self.cities[j][1])**2)
        return distances

    def construct_solution(self, ant):
        solution = [random.randint(0, self.num_cities-1)]
        for _ in range(self.num_cities-1):
            current_city = solution[-1]
            next_city = self.select_next_city(current_city, solution)
            solution.append(next_city)
        return solution

    def select_next_city(self, current_city, solution):
        probabilities = []
        for i in range(self.num_cities):
            if i not in solution:
                pheromone_trail = self.pheromone_trails[current_city][i]
                distance = self.distances[current_city][i]
                probability = (pheromone_trail**self.alpha) * (1.0 / distance**self.beta)
                probabilities.append(probability)
            else:
                probabilities.append(0.0)
        probabilities = [p / sum(probabilities) for p in probabilities]
        return random.choices(range(self.num_cities), weights=probabilities)[0]

    def update_pheromone_trails(self, solutions):
        for i in range(self.num_cities):
            for j in range(i+1, self.num_cities):
                self.pheromone_trails[i][j] = self.pheromone_trails[j][i] = (1.0 - self.rho) * self.pheromone_trails[i][j]
                for solution in solutions:
                    if i in solution and j in solution:
                        self.pheromone_trails[i][j] += self.Q / len(solution)

    def run(self, max_iterations):
        for _ in range(max_iterations):
            solutions = [self.construct_solution(i) for i in range(self.num_ants)]
            self.update_pheromone_trails(solutions)
        return solutions

# Example usage
ac = AntColony(num_cities=10, num_ants=10, alpha=1.0, beta=2.0, rho=0.5, Q=10.0)
solutions = ac.run(max_iterations=100)
print("Best solution:", min(solutions, key=lambda x: sum(ac.distances[x[i-1]][x[i]] for i in range(len(x)))))