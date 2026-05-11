from abc import ABC, abstractmethod
import random
from algorithms.ga.chromosome import Chromosome


class CrossoverStrategy(ABC):
    @abstractmethod
    def crossover(self, parent1: Chromosome, parent2: Chromosome) -> Chromosome:
        pass


class OrderCrossover(CrossoverStrategy):
    """
    OX - Order Crossover (chuẩn cho VRP/TSP)
    """

    def crossover(self, parent1, parent2):
        size = len(parent1.sequence)

        start, end = sorted(random.sample(range(size), 2))

        child_seq = [None] * size

        # copy đoạn từ parent1
        child_seq[start:end] = parent1.sequence[start:end]

        # fill từ parent2
        p2_seq = [x for x in parent2.sequence if x not in child_seq]

        idx = 0
        for i in range(size):
            if child_seq[i] is None:
                child_seq[i] = p2_seq[idx]
                idx += 1

        return Chromosome(child_seq)