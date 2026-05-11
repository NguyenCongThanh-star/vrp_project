# domain/cost.py


def total_distance(solution, depot):
    """
    Calculate total travel distance.

    Objective:
    Minimize total route distance.
    """

    return solution.total_cost(depot)


def vehicle_penalty(
    solution,
    vehicle_weight=100
):
    """
    Penalize using too many vehicles.

    Objective:
    Encourage fewer routes/vehicles.
    """

    return (
        solution.total_vehicles()
        * vehicle_weight
    )


def capacity_penalty(
    solution,
    capacity,
    penalty_weight=1000
):
    """
    Penalize capacity violations.

    If:
    total_demand > capacity

    Add penalty proportional
    to exceeded demand.
    """

    penalty = 0

    for route in solution.routes:

        overload = (
            route.total_demand() - capacity
        )

        if overload > 0:

            penalty += (
                overload * penalty_weight
            )

    return penalty


def penalized_cost(
    solution,
    depot,
    capacity,
    vehicle_weight=100,
    capacity_penalty_weight=1000,
):
    """
    Multi-objective VRP cost function.

    Cost =
        total distance
        + vehicle penalty
        + capacity penalty
    """

    distance_cost = total_distance(
        solution,
        depot
    )

    vehicles_cost = vehicle_penalty(
        solution,
        vehicle_weight
    )

    overload_cost = capacity_penalty(
        solution,
        capacity,
        capacity_penalty_weight
    )

    total_cost = (
        distance_cost
        + vehicles_cost
        + overload_cost
    )

    return total_cost