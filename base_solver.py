# algorithms/base_solver.py

from abc import ABC, abstractmethod


class BaseSolver(ABC):
    """
    Abstract Base Class for all VRP solvers.

    Every solver must implement:
    - solve()

    Shared features:
    - history
    - best_cost
    - best_solution
    """

    def __init__(self, problem):

        self.problem = problem

        # convergence history
        self.history = []

        # best result
        self.best_solution = None
        self.best_cost = float("inf")

    # -------------------------------------------------
    # MAIN SOLVE METHOD
    # -------------------------------------------------

    @abstractmethod
    def solve(self):
        """
        Run optimization algorithm.

        Must return:
        Solution object
        """
        pass

    # -------------------------------------------------
    # SAVE BEST SOLUTION
    # -------------------------------------------------

    def update_best(
        self,
        solution,
        cost
    ):
        """
        Update global best solution.
        """

        if cost < self.best_cost:

            self.best_cost = cost
            self.best_solution = solution

    # -------------------------------------------------
    # ADD HISTORY
    # -------------------------------------------------

    def add_history(self, value):
        """
        Save convergence value.
        """

        self.history.append(value)

    # -------------------------------------------------
    # RESET SOLVER
    # -------------------------------------------------

    def reset(self):
        """
        Reset solver state.
        """

        self.history = []

        self.best_solution = None

        self.best_cost = float("inf")