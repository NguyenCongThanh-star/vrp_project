# algorithms/hybrid/hybrid_solver.py

import random

from algorithms.base_solver import BaseSolver

from algorithms.common.decoder import Decoder
from algorithms.common.local_search import (
    improve_solution
)

from algorithms.ga.chromosome import (
    Chromosome
)

from algorithms.ga.crossover import (
    ordered_crossover
)

from algorithms.ga.mutation import (
    swap_mutation
)


class HybridSolver(BaseSolver):
    """
    Hybrid VRP Solver

    Combination:
    - Genetic Algorithm
    - Local Search (2-opt)

    Workflow:
    Population
        ↓
    GA Evolution
        ↓
    Decode
        ↓
    2-opt Improvement
        ↓
    Improved Solution
    """

    def __init__(
        self,
        problem,
        population_size=50,
        generations=100,
        mutation_rate=0.1,
    ):

        super().__init__(problem)

        self.population_size = (
            population_size
        )

        self.generations = generations

        self.mutation_rate = mutation_rate

        # IMPORTANT
        self.decoder = Decoder(problem)

        self.history = []

    # =================================================
    # INITIAL POPULATION
    # =================================================

    def initialize_population(self):

        population = []

        customer_ids = [
            c.id
            for c in self.problem.customers
        ]

        for _ in range(self.population_size):

            genes = customer_ids[:]

            random.shuffle(genes)

            chromosome = Chromosome(
                genes
            )

            population.append(
                chromosome
            )

        return population

    # =================================================
    # EVALUATE POPULATION
    # =================================================

    def evaluate_population(
        self,
        population
    ):

        scored_population = []

        for chromosome in population:

            # -----------------------------------------
            # DECODE
            # -----------------------------------------

            solution = self.decoder.decode(
                chromosome.genes
            )

            # -----------------------------------------
            # LOCAL SEARCH
            # -----------------------------------------

            improved_solution = (
                improve_solution(
                    solution,
                    self.problem.depot
                )
            )

            # -----------------------------------------
            # COST
            # -----------------------------------------

            score = self.problem.cost(
                improved_solution
            )

            scored_population.append(
                (
                    chromosome,
                    score,
                    improved_solution
                )
            )

        scored_population.sort(
            key=lambda x: x[1]
        )

        return scored_population

    # =================================================
    # TOURNAMENT SELECTION
    # =================================================

    def select_parent(
        self,
        scored_population
    ):

        tournament = random.sample(
            scored_population,
            3
        )

        tournament.sort(
            key=lambda x: x[1]
        )

        return tournament[0][0]

    # =================================================
    # CREATE NEXT GENERATION
    # =================================================

    def next_generation(
        self,
        scored_population
    ):

        new_population = []

        # ---------------------------------------------
        # ELITISM
        # ---------------------------------------------

        elite = scored_population[0][0]

        new_population.append(elite)

        # ---------------------------------------------
        # CREATE CHILDREN
        # ---------------------------------------------

        while (
            len(new_population)
            < self.population_size
        ):

            parent1 = self.select_parent(
                scored_population
            )

            parent2 = self.select_parent(
                scored_population
            )
            child_genes = ordered_crossover(
                parent1,
                parent2
            )

            # mutation
            if (
                random.random()
                < self.mutation_rate
            ):

                child_genes = swap_mutation(
                    child_genes
                )

            child = Chromosome(
                child_genes
            )

            new_population.append(
                child
            )

        return new_population

    # =================================================
    # SOLVE
    # =================================================

    def solve(self):

        population = (
            self.initialize_population()
        )

        best_solution = None

        best_cost = float("inf")

        for generation in range(
            self.generations
        ):

            # -----------------------------------------
            # EVALUATE
            # -----------------------------------------

            scored_population = (
                self.evaluate_population(
                    population
                )
            )

            (
                best_chromosome,
                score,
                solution
            ) = scored_population[0]

            # -----------------------------------------
            # SAVE HISTORY
            # -----------------------------------------

            self.history.append(score)

            # -----------------------------------------
            # UPDATE BEST
            # -----------------------------------------

            if score < best_cost:

                best_cost = score

                best_solution = solution

            # -----------------------------------------
            # LOG
            # -----------------------------------------

            print(
                f"[Hybrid GA + 2-opt] "
                f"Generation "
                f"{generation + 1}/"
                f"{self.generations} "
                f"| Best Cost = "
                f"{score:.2f}"
            )

            # -----------------------------------------
            # NEXT GENERATION
            # -----------------------------------------

            population = self.next_generation(
                scored_population
            )

        return best_solution