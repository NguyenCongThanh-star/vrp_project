# algorithms/ga/fitness.py

from domain.cost import penalized_cost


class Fitness:
    """
    Genetic Algorithm Fitness Evaluator

    Multi-objective optimization:
    - minimize total distance
    - minimize number of vehicles
    - penalize capacity violations
    """

    def __init__(
        self,
        decoder,
        depot,
        capacity,
        vehicle_weight=100,
        capacity_penalty_weight=1000,
    ):

        self.decoder = decoder

        self.depot = depot
        self.capacity = capacity

        self.vehicle_weight = vehicle_weight
        self.capacity_penalty_weight = (
            capacity_penalty_weight
        )

    # -------------------------------------------------
    # FITNESS EVALUATION
    # -------------------------------------------------

    def evaluate(self, chromosome):
        """
        Evaluate chromosome fitness.

        Lower cost = better solution.
        """

        solution = self.decoder.decode(
            chromosome.genes
        )

        cost = penalized_cost(
            solution=solution,
            depot=self.depot,
            capacity=self.capacity,
            vehicle_weight=self.vehicle_weight,
            capacity_penalty_weight=(
                self.capacity_penalty_weight
            ),
        )

        return cost