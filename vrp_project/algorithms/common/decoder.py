# algorithms/common/decoder.py

from domain.entities.route import Route
from domain.entities.solution import Solution


class Decoder:
    """
    Decode chromosome into VRP solution.

    Chromosome:
    [3, 5, 1, 2, 4]

    ->
    Solution(routes)
    """

    def __init__(self, problem):

        self.problem = problem

        # support both naming styles
        self.capacity = getattr(
            problem,
            "vehicle_capacity",
            problem.capacity
        )

    # =================================================
    # MAIN DECODE
    # =================================================

    def decode(self, chromosome):

        routes = []

        current_route = []

        current_load = 0

        for customer_id in chromosome:

            customer = self.problem.get_customer(
                customer_id
            )

            # -----------------------------------------
            # CAPACITY CHECK
            # -----------------------------------------

            if (
                current_load + customer.demand
                > self.capacity
            ):

                routes.append(
                    Route(current_route)
                )

                current_route = []

                current_load = 0

            # -----------------------------------------
            # ADD CUSTOMER
            # -----------------------------------------

            current_route.append(customer)

            current_load += customer.demand

        # ---------------------------------------------
        # FINAL ROUTE
        # ---------------------------------------------

        if current_route:

            routes.append(
                Route(current_route)
            )

        return Solution(routes)

    # =================================================
    # VALIDATION
    # =================================================

    def validate(self, solution):
        """
        Check if all routes satisfy capacity.
        """

        for route in solution.routes:

            if (
                route.total_demand()
                > self.capacity
            ):

                return False

        return True

    # =================================================
    # ROUTE LOADS
    # =================================================

    def route_loads(self, solution):
        """
        Return load of each route.
        """

        return [
            route.total_demand()
            for route in solution.routes
        ]

    # =================================================
    # NUMBER OF VEHICLES
    # =================================================

    def vehicle_count(self, solution):

        return len(solution.routes)