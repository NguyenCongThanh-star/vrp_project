class Solution:
    def __init__(self, routes=None):
        self.routes = routes if routes else []

    def add_route(self, route):
        self.routes.append(route)

    def total_cost(self, depot):
        return sum(route.distance(depot) for route in self.routes)

    def total_vehicles(self):
        return len(self.routes)