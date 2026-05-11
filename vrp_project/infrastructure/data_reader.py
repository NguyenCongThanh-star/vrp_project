import csv
from domain.entities.customer import Customer


def read_customers_from_csv(path):
    customers = []

    with open(path, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            customer = Customer(
                id=int(row["id"]),
                x=float(row["x"]),
                y=float(row["y"]),
                demand=float(row["demand"])
            )
            customers.append(customer)

    return customers