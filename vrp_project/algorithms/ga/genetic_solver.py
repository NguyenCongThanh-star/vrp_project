# algorithms/ga/genetic_solver.py

import random

from algorithms.base_solver import BaseSolver

from algorithms.common.decoder import Decoder
from algorithms.common.local_search import improve_solution

from algorithms.ga.chromosome import Chromosome
from algorithms.ga.fitness import Fitness

from algorithms.ga.crossover import ordered_crossover
from algorithms.ga.mutation import swap_mutation


class GeneticSolver(BaseSolver):
    """
    Genetic Algorithm Solver for VRP

    Features:
    - Tournament Selection
    - Ordered Crossover (OX)
    - Swap Mutation
    - 2-opt Local Search
    - Convergence History
    - Hybrid Optimization
    """

    def __init__(
        self,
        problem,
        population_size=50,
        generations=100,
        mutation_rate=0.1,
        use_local_search=True,
    ):
        super().__init__(problem)

        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

        self.use_local_search = use_local_search

        # -------------------------------------------------
        # Decoder
        # -------------------------------------------------

        self.decoder = Decoder(problem)

        # -------------------------------------------------
        # Fitness
        # -------------------------------------------------

        self.fitness = Fitness(
            decoder=self.decoder,
            depot=problem.depot,
            capacity=problem.capacity,
        )

        # -------------------------------------------------
        # History
        # -------------------------------------------------

        self.history = []

    # -------------------------------------------------
    # INITIALIZE POPULATION
    # -------------------------------------------------

    def initialize_population(self):

        return [
            Chromosome.random(self.problem)
            for _ in range(self.population_size)
        ]

    # -------------------------------------------------
    # EVALUATE POPULATION
    # -------------------------------------------------

    def evaluate(self, population):

        for chromosome in population:

            chromosome.fitness = (
                self.fitness.evaluate(chromosome)
            )

    # -------------------------------------------------
    # TOURNAMENT SELECTION
    # -------------------------------------------------

    def select(self, population):

        tournament = random.sample(population, 3)

        return min(
            tournament,
            key=lambda c: c.fitness
        )

    # -------------------------------------------------
    # CREATE CHILD
    # -------------------------------------------------

    def create_child(
        self,
        parent1,
        parent2
    ):

        child_genes = ordered_crossover(
            parent1,
            parent2
        )

        if random.random() < self.mutation_rate:

            child_genes = swap_mutation(
                child_genes
            )

        return Chromosome(child_genes)

    # -------------------------------------------------
    # LOCAL SEARCH
    # -------------------------------------------------

    def apply_local_search(self, chromosome):

        solution = self.decoder.decode(
            chromosome.genes
        )

        improved_solution = improve_solution(
            solution,
            self.problem.depot
        )

        return improved_solution

    # -------------------------------------------------
    # SOLVE
    # -------------------------------------------------

    def solve(self):

        population = self.initialize_population()

        self.evaluate(population)

        best_solution = None
        best_cost = float("inf")

        for generation in range(self.generations):

            new_population = []

            # -------------------------------------------------
            # ELITISM
            # -------------------------------------------------

            elite = min(
                population,
                key=lambda c: c.fitness
            )

            new_population.append(elite)

            # -------------------------------------------------
            # GENERATE NEW POPULATION
            # -------------------------------------------------

            while len(new_population) < self.population_size:

                parent1 = self.select(population)
                parent2 = self.select(population)

                child = self.create_child(
                    parent1,
                    parent2
                )

                new_population.append(child)

            # -------------------------------------------------
            # EVALUATE
            # -------------------------------------------------

            self.evaluate(new_population)

            population = new_population

            # -------------------------------------------------
            # BEST CHROMOSOME
            # -------------------------------------------------

            best_chromosome = min(
                population,
                key=lambda c: c.fitness
            )

            current_solution = self.decoder.decode(
                best_chromosome.genes
            )

            # -------------------------------------------------
            # HYBRID LOCAL SEARCH
            # -------------------------------------------------

            if self.use_local_search:

                current_solution = improve_solution(
                    current_solution,
                    self.problem.depot
                )

            current_cost = self.problem.cost(
                current_solution
            )

            # -------------------------------------------------
            # SAVE HISTORY
            # -------------------------------------------------

            self.history.append(current_cost)

            # -------------------------------------------------
            # UPDATE GLOBAL BEST
            # -------------------------------------------------

            if current_cost < best_cost:

                best_cost = current_cost
                best_solution = current_solution

            # -------------------------------------------------
            # LOG
            # -------------------------------------------------

            print(
                f"[GA] Generation "
                f"{generation + 1}/{self.generations} "
                f"| Best Cost = {current_cost:.2f}"
            )

        return best_solution