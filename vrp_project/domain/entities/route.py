class Route:
    def __init__(self, customers=None):
        self.customers = customers if customers else []

    def add_customer(self, customer):
        self.customers.append(customer)

    def total_demand(self):
        return sum(c.demand for c in self.customers)

    def distance(self, depot):
        if not self.customers:
            return 0

        dist = 0

        # depot -> first
        dist += depot.distance_to(self.customers[0])

        # between customers
        for i in range(len(self.customers) - 1):
            dist += self.customers[i].distance_to(self.customers[i + 1])

        # last -> depot
        dist += self.customers[-1].distance_to(depot)

        return dist