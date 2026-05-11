from abc import ABC, abstractmethod

class DistanceStrategy(ABC):
    @abstractmethod
    def compute(self, a, b):
        pass


class EuclideanDistance(DistanceStrategy):
    def compute(self, a, b):
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


class ManhattanDistance(DistanceStrategy):
    def compute(self, a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)