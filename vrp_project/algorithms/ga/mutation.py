import random

def swap_mutation(genes, rate=0.1):
    for i in range(len(genes)):
        if random.random() < rate:
            j = random.randint(0, len(genes) - 1)
            genes[i], genes[j] = genes[j], genes[i]
    return genes