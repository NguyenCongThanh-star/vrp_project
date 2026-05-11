from abc import ABC, abstractmethod
import random


class SelectionStrategy(ABC):
    @abstractmethod
    def select(self, population):
        pass


class TournamentSelection(SelectionStrategy):
    def __init__(self, k=3):
        self.k = k

    def select(self, population):
        return max(
            random.sample(population, self.k),
            key=lambda c: c.fitness
        )


class RouletteWheelSelection(SelectionStrategy):
    """
    Fitness proportionate selection
    """

    def select(self, population):
        total_fitness = sum(c.fitness for c in population)

        pick = random.uniform(0, total_fitness)
        current = 0

        for c in population:
            current += c.fitness
            if current > pick:
                return c

        return population[-1]