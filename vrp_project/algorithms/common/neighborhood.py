# algorithms/common/neighborhood.py

import random
from copy import deepcopy


def swap_move(solution):
    """
    Swap two random positions.

    Example:
    [1,2,3,4]
    ->
    [1,4,3,2]
    """

    if len(solution) < 2:
        return solution

    new_solution = deepcopy(solution)

    i, j = random.sample(range(len(new_solution)), 2)

    new_solution[i], new_solution[j] = (
        new_solution[j],
        new_solution[i],
    )

    return new_solution


def insert_move(solution):
    """
    Remove one element and insert it
    into another random position.

    Example:
    [1,2,3,4,5]
    ->
    [1,2,5,3,4]
    """

    if len(solution) < 2:
        return solution

    new_solution = deepcopy(solution)

    i, j = random.sample(range(len(new_solution)), 2)

    customer = new_solution.pop(i)
    new_solution.insert(j, customer)

    return new_solution


def reverse_segment_move(solution):
    """
    Reverse a random segment.

    Example:
    [1,2,3,4,5]
    ->
    [1,4,3,2,5]
    """

    if len(solution) < 2:
        return solution

    new_solution = deepcopy(solution)

    i, j = sorted(
        random.sample(range(len(new_solution)), 2)
    )

    new_solution[i:j] = reversed(
        new_solution[i:j]
    )

    return new_solution


def random_neighbor(solution):
    """
    Generate one random neighbor solution.
    """

    operators = [
        swap_move,
        insert_move,
        reverse_segment_move,
    ]

    operator = random.choice(operators)

    return operator(solution)


def generate_neighbors(solution, count=10):
    """
    Generate multiple neighbor solutions.

    Useful for:
    - Simulated Annealing
    - Best Neighbor Search
    - Hybrid Optimization
    """

    neighbors = []

    for _ in range(count):
        neighbors.append(
            random_neighbor(solution)
        )

    return neighbors