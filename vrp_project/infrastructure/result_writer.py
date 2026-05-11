import json
import os


def save_results(results, filename="results/logs/results.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

def save_solution(solution, filename="results/solution.json"):
    """
    Save VRP solution to JSON file.

    Output format:
    [
        {
            "route_id": 0,
            "customers": [1, 5, 3],
            "total_demand": 45,
            "distance": 120.5
        },
        ...
    ]
    """

    # tạo folder nếu chưa có
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    data = []

    for i, route in enumerate(solution.routes):
        route_data = {
            "route_id": i,
            "customers": [c.id for c in route.customers],
            "total_demand": route.total_demand(),
            "distance": route.distance(solution.routes[0].customers[0])  # ⚠️ sẽ fix bên dưới
        }

        data.append(route_data)

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)