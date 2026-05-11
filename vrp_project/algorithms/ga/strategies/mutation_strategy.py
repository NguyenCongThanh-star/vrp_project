from abc import ABC, abstractmethod
import random


class MutationStrategy(ABC):
    @abstractmethod
    def mutate(self, chromosome):
        pass


class SwapMutation(MutationStrategy):
    def mutate(self, chromosome):
        a, b = random.sample(range(len(chromosome.sequence)), 2)
        chromosome.sequence[a], chromosome.sequence[b] = \
            chromosome.sequence[b], chromosome.sequence[a]


class InversionMutation(MutationStrategy):
    def mutate(self, chromosome):
        a, b = sorted(random.sample(range(len(chromosome.sequence)), 2))
        chromosome.sequence[a:b] = reversed(chromosome.sequence[a:b])