# algorithms/common/local_search.py

from copy import deepcopy


def route_distance(route, depot):
    """
    Calculate total distance of a route.

    depot -> customers -> depot
    """

    if not route.customers:
        return 0

    total = 0

    # depot -> first
    total += depot.distance_to(route.customers[0])

    # between customers
    for i in range(len(route.customers) - 1):
        total += route.customers[i].distance_to(
            route.customers[i + 1]
        )

    # last -> depot
    total += route.customers[-1].distance_to(depot)

    return total


def two_opt(route, depot):
    """
    Apply 2-opt optimization on a single route.

    Improve customer visiting order
    to reduce total travel distance.
    """

    best_route = deepcopy(route)
    best_distance = route_distance(best_route, depot)

    improved = True

    while improved:
        improved = False

        customers = best_route.customers

        for i in range(len(customers) - 1):
            for j in range(i + 1, len(customers)):

                if j - i == 1:
                    continue

                new_customers = (
                    customers[:i]
                    + customers[i:j][::-1]
                    + customers[j:]
                )

                new_route = deepcopy(best_route)
                new_route.customers = new_customers

                new_distance = route_distance(
                    new_route,
                    depot
                )

                if new_distance < best_distance:
                    best_route = new_route
                    best_distance = new_distance
                    improved = True

    return best_route


def improve_route(route, depot):
    """
    Improve a single route using local search.
    """

    return two_opt(route, depot)


def improve_solution(solution, depot):
    """
    Improve all routes inside a solution.
    """

    improved_solution = deepcopy(solution)

    improved_routes = []

    for route in improved_solution.routes:
        improved_route = improve_route(route, depot)
        improved_routes.append(improved_route)

    improved_solution.routes = improved_routes

    return improved_solution