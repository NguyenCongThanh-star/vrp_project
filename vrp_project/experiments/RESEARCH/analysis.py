# experiments/RESEARCH/analysis.py

import statistics
from collections import defaultdict


# =====================================================
# CALCULATE AVERAGE
# =====================================================

def calculate_average(values):

    if not values:
        return 0

    return sum(values) / len(values)


# =====================================================
# COMPARE ALGORITHMS
# =====================================================

def compare_algorithms(results):
    """
    Convert raw benchmark results
    into grouped statistics.

    Input:
    [
        {
            "solver": "GeneticSolver",
            "cost": 500
        },
        ...
    ]
    """

    grouped = defaultdict(list)

    # group by solver
    for result in results:

        solver = result["solver"]

        grouped[solver].append(result)

    comparison = {}

    # statistics
    for solver, data in grouped.items():

        costs = [
            d["cost"]
            for d in data
        ]

        times = [
            d["time"]
            for d in data
        ]

        comparison[solver] = {

            "best_cost": min(costs),

            "avg_cost": statistics.mean(
                costs
            ),

            "worst_cost": max(costs),

            "avg_time": statistics.mean(
                times
            ),

            "runs": len(data)
        }

    return comparison


# =====================================================
# GENERATE REPORT
# =====================================================

def generate_summary_report(results):

    comparison = compare_algorithms(
        results
    )

    report = []

    report.append("=" * 60)

    report.append("VRP BENCHMARK REPORT")

    report.append("=" * 60)

    report.append("")

    for (
        solver,
        stats
    ) in comparison.items():

        report.append(
            f"Algorithm: {solver}"
        )

        report.append(
            f"Runs: {stats['runs']}"
        )

        report.append(
            f"Best Cost: "
            f"{stats['best_cost']:.2f}"
        )

        report.append(
            f"Average Cost: "
            f"{stats['avg_cost']:.2f}"
        )

        report.append(
            f"Worst Cost: "
            f"{stats['worst_cost']:.2f}"
        )

        report.append(
            f"Average Time: "
            f"{stats['avg_time']:.4f}s"
        )

        report.append("-" * 60)

    return "\n".join(report)