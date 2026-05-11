import random

def ordered_crossover(parent1, parent2):
    size = len(parent1.genes)
    start, end = sorted(random.sample(range(size), 2))

    child = [None] * size
    child[start:end] = parent1.genes[start:end]

    pointer = 0
    for gene in parent2.genes:
        if gene not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = gene

    return child