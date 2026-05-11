# algorithms/greedy/greedy_solver.py

from algorithms.base_solver import BaseSolver

from algorithms.common.local_search import (
    improve_solution
)

from domain.entities.route import Route
from domain.entities.solution import Solution


class GreedySolver(BaseSolver):
    """
    Greedy VRP Solver

    Strategy:
    - Nearest Neighbor
    - Capacity Constraint
    - Hybrid Local Search (2-opt)
    """

    def __init__(
        self,
        problem,
        use_local_search=True,
    ):
        super().__init__(problem)

        self.use_local_search = (
            use_local_search
        )

    # -------------------------------------------------
    # SOLVE
    # -------------------------------------------------

    def solve(self):

        depot = self.problem.depot

        customers = (
            self.problem.customers[:]
        )

        # Support both names
        capacity = getattr(
            self.problem,
            "vehicle_capacity",
            self.problem.capacity
        )

        unvisited = customers[:]

        routes = []

        # -------------------------------------------------
        # BUILD ROUTES
        # -------------------------------------------------

        while unvisited:

            route_customers = []

            current_load = 0

            current_node = depot

            while True:

                # -----------------------------------------
                # FEASIBLE CUSTOMERS
                # -----------------------------------------

                feasible_customers = [

                    c for c in unvisited

                    if (
                        current_load + c.demand
                        <= capacity
                    )
                ]

                if not feasible_customers:
                    break

                # -----------------------------------------
                # NEAREST NEIGHBOR
                # -----------------------------------------

                next_customer = min(
                    feasible_customers,
                    key=lambda c:
                    current_node.distance_to(c)
                )

                route_customers.append(
                    next_customer
                )

                current_load += (
                    next_customer.demand
                )

                unvisited.remove(
                    next_customer
                )

                current_node = next_customer

            routes.append(
                Route(route_customers)
            )

        # -------------------------------------------------
        # CREATE SOLUTION
        # -------------------------------------------------

        solution = Solution(routes)

        # -------------------------------------------------
        # LOCAL SEARCH IMPROVEMENT
        # -------------------------------------------------

        if self.use_local_search:

            solution = improve_solution(
                solution,
                depot
            )

        return solution