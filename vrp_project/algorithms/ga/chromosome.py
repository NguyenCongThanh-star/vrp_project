import random

class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = None

    @staticmethod
    def random(problem):
        customer_ids = [c.id for c in problem.customers]
        random.shuffle(customer_ids)
        return Chromosome(customer_ids)