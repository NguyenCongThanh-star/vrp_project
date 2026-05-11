# algorithms/sa/sa_solver.py

import random
import math

from algorithms.base_solver import BaseSolver

from algorithms.common.decoder import Decoder

from algorithms.common.neighborhood import (
    random_neighbor
)

from algorithms.common.local_search import (
    improve_solution
)


class SimulatedAnnealingSolver(BaseSolver):
    """
    Simulated Annealing Solver for VRP

    Features:
    - Random Neighborhood Search
    - Probabilistic Acceptance
    - Cooling Schedule
    - Hybrid 2-opt Local Search
    - Convergence History
    """

    def __init__(
        self,
        problem,
        initial_temp=1000,
        cooling_rate=0.995,
        iterations=500,
        use_local_search=True,
    ):
        super().__init__(problem)

        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.iterations = iterations

        self.use_local_search = (
            use_local_search
        )

        self.decoder = Decoder(problem)

        # convergence history
        self.history = []

    # -------------------------------------------------
    # INITIAL SOLUTION
    # -------------------------------------------------

    def initial_solution(self):
        """
        Generate random permutation.
        """

        customer_ids = [
            c.id
            for c in self.problem.customers
        ]

        random.shuffle(customer_ids)

        return customer_ids

    # -------------------------------------------------
    # COST FUNCTION
    # -------------------------------------------------

    def cost(self, chromosome):

        solution = self.decoder.decode(
            chromosome
        )

        return self.problem.cost(solution)

    # -------------------------------------------------
    # SOLVE
    # -------------------------------------------------

    def solve(self):

        # ---------------------------------------------
        # INITIALIZATION
        # ---------------------------------------------

        current = self.initial_solution()

        current_cost = self.cost(current)

        best = current[:]
        best_cost = current_cost

        temperature = self.initial_temp

        # ---------------------------------------------
        # MAIN LOOP
        # ---------------------------------------------

        for iteration in range(self.iterations):

            # -----------------------------------------
            # GENERATE NEIGHBOR
            # -----------------------------------------

            new_solution = random_neighbor(
                current
            )

            new_cost = self.cost(
                new_solution
            )

            # -----------------------------------------
            # DELTA
            # -----------------------------------------

            delta = (
                new_cost - current_cost
            )

            # -----------------------------------------
            # ACCEPTANCE RULE
            # -----------------------------------------

            if (
                delta < 0
                or random.random()
                < math.exp(-delta / temperature)
            ):

                current = new_solution
                current_cost = new_cost

                # update best
                if current_cost < best_cost:

                    best = current[:]
                    best_cost = current_cost

            # -----------------------------------------
            # COOLING
            # -----------------------------------------

            temperature *= (
                self.cooling_rate
            )

            # -----------------------------------------
            # SAVE HISTORY
            # -----------------------------------------

            self.history.append(best_cost)

            # -----------------------------------------
            # LOG
            # -----------------------------------------

            print(
                f"[SA] Iteration "
                f"{iteration + 1}/{self.iterations} "
                f"| Best Cost = {best_cost:.2f} "
                f"| Temp = {temperature:.2f}"
            )

        # ---------------------------------------------
        # FINAL DECODE
        # ---------------------------------------------

        final_solution = self.decoder.decode(
            best
        )

        # ---------------------------------------------
        # APPLY LOCAL SEARCH (2-opt)
        # ---------------------------------------------

        if self.use_local_search:

            final_solution = improve_solution(
                final_solution,
                self.problem.depot
            )

        return final_solution