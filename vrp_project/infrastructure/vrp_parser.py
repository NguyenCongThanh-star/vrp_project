from domain.entities.customer import Customer


def parse_vrp_file(path):
    customers = []
    depot = None
    capacity = 0

    with open(path, "r") as f:
        lines = f.readlines()

    reading_coords = False
    reading_demand = False

    coords = {}
    demands = {}

    for line in lines:
        line = line.strip()

        if line.startswith("CAPACITY"):
            capacity = int(line.split()[-1])

        elif line.startswith("NODE_COORD_SECTION"):
            reading_coords = True
            continue

        elif line.startswith("DEMAND_SECTION"):
            reading_coords = False
            reading_demand = True
            continue

        elif line.startswith("DEPOT_SECTION"):
            reading_demand = False
            continue

        elif reading_coords:
            parts = line.split()
            coords[int(parts[0])] = (float(parts[1]), float(parts[2]))

        elif reading_demand:
            parts = line.split()
            demands[int(parts[0])] = float(parts[1])

    for cid in coords:
        x, y = coords[cid]
        demand = demands.get(cid, 0)

        customer = Customer(cid, x, y, demand)

        if cid == 1:
            depot = customer
        else:
            customers.append(customer)

    return depot, customers, capacity