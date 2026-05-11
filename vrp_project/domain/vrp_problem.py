# domain/vrp_problem.py

from domain.cost import penalized_cost


class VRPProblem:

    def __init__(
        self,
        depot,
        customers,
        vehicle_capacity
    ):

        self.depot = depot

        self.customers = customers

        # old naming
        self.vehicle_capacity = (
            vehicle_capacity
        )

        # new naming (IMPORTANT)
        self.capacity = vehicle_capacity

    # -------------------------------------------------
    # GET CUSTOMER
    # -------------------------------------------------

    def get_customer(self, customer_id):

        for customer in self.customers:

            if customer.id == customer_id:
                return customer

        return None

    # -------------------------------------------------
    # COST FUNCTION
    # -------------------------------------------------

    def cost(self, solution):

        return penalized_cost(
            solution=solution,
            depot=self.depot,
            capacity=self.capacity
        )