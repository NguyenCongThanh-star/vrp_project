# infrastructure/visualization.py

import matplotlib.pyplot as plt


# =====================================================
# PLOT VRP SOLUTION
# =====================================================

def plot_solution(solution, depot):
    """
    Plot VRP routes with different colors.
    """

    plt.figure(figsize=(10, 8))

    # -------------------------------------------------
    # DEPOT
    # -------------------------------------------------

    plt.scatter(
        depot.x,
        depot.y,
        marker="s",
        s=200,
        label="Depot"
    )

    # -------------------------------------------------
    # ROUTES
    # -------------------------------------------------

    colors = [
        "blue",
        "green",
        "red",
        "orange",
        "purple",
        "brown",
        "pink",
        "gray",
        "olive",
        "cyan",
    ]

    for i, route in enumerate(solution.routes):

        x = [depot.x]
        y = [depot.y]

        for customer in route.customers:

            x.append(customer.x)
            y.append(customer.y)

            # customer label
            plt.text(
                customer.x,
                customer.y,
                str(customer.id),
                fontsize=8
            )

        x.append(depot.x)
        y.append(depot.y)

        color = colors[i % len(colors)]

        plt.plot(
            x,
            y,
            marker="o",
            color=color,
            label=f"Route {i + 1}"
        )

    # -------------------------------------------------
    # TITLE
    # -------------------------------------------------

    plt.title("Vehicle Routing Problem Solution")

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")

    plt.legend()
    plt.grid(True)

    plt.show()


# =====================================================
# PLOT BENCHMARK COMPARISON
# =====================================================

def plot_benchmark(results):
    """
    Plot average cost comparison.
    """

    names = [
        r["solver"]
        for r in results
    ]

    costs = [
        r["avg_cost"]
        for r in results
    ]

    plt.figure(figsize=(8, 6))

    plt.bar(names, costs)

    plt.title("Algorithm Benchmark Comparison")

    plt.xlabel("Algorithm")
    plt.ylabel("Average Cost")

    plt.grid(axis="y")

    plt.show()


# =====================================================
# PLOT CONVERGENCE HISTORY
# =====================================================

def plot_convergence(history, title="Convergence History"):
    """
    Plot optimization progress over iterations.

    history:
    [1000, 900, 850, 800, ...]
    """

    plt.figure(figsize=(10, 6))

    generations = list(
        range(1, len(history) + 1)
    )

    plt.plot(
        generations,
        history,
        marker="o"
    )

    plt.title(title)

    plt.xlabel("Generation / Iteration")
    plt.ylabel("Best Cost")

    plt.grid(True)

    plt.show()


# =====================================================
# PLOT MULTIPLE CONVERGENCE CURVES
# =====================================================

def plot_multiple_convergence(histories):
    """
    Plot convergence of multiple algorithms.

    Example:
    histories = {
        "GA": [...],
        "SA": [...],
    }
    """

    plt.figure(figsize=(10, 6))

    for name, history in histories.items():

        generations = list(
            range(1, len(history) + 1)
        )

        plt.plot(
            generations,
            history,
            label=name
        )

    plt.title("Algorithm Convergence Comparison")

    plt.xlabel("Generation / Iteration")
    plt.ylabel("Best Cost")

    plt.legend()

    plt.grid(True)

    plt.show()