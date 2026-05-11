# main.py

from config import *

# =====================================================
# INFRASTRUCTURE
# =====================================================

from infrastructure.data_reader import (
    read_customers_from_csv
)

from infrastructure.vrp_parser import (
    parse_vrp_file
)

from infrastructure.visualization import (
    plot_solution,
    plot_benchmark,
    plot_convergence,
)

from infrastructure.result_writer import (
    save_results,
    save_solution,
)

# =====================================================
# DOMAIN
# =====================================================

from domain.vrp_problem import VRPProblem

# =====================================================
# ALGORITHMS
# =====================================================

from algorithms.ga.genetic_solver import (
    GeneticSolver
)

from algorithms.greedy.greedy_solver import (
    GreedySolver
)

from algorithms.sa.sa_solver import (
    SimulatedAnnealingSolver
)

from algorithms.hybrid.hybrid_solver import (
    HybridSolver
)

# =====================================================
# EXPERIMENTS
# =====================================================

from experiments.RESEARCH.benchmark import (
    Benchmark
)

from experiments.RESEARCH.analysis import (
    generate_summary_report
)

# =====================================================
# LOAD PROBLEM
# =====================================================

def load_problem(data_path=None):

    if USE_BENCHMARK_FILE:

        depot, customers, capacity = (
            parse_vrp_file(BENCHMARK_PATH)
        )

    else:

        path = data_path or DATA_PATH

        customers = read_customers_from_csv(
            path
        )

        depot = customers[0]

        customers = customers[1:]

        capacity = VEHICLE_CAPACITY

    return VRPProblem(
        depot,
        customers,
        capacity
    )

# =====================================================
# RUN SINGLE SOLVER
# =====================================================

def run_single(problem):

    print("=== RUN SINGLE SOLVER ===")

    # ---------------------------------------------
    # SELECT SOLVER
    # ---------------------------------------------

    solver = HybridSolver(
        problem,
        **HYBRID_CONFIG
    )

    # ---------------------------------------------
    # SOLVE
    # ---------------------------------------------

    solution = solver.solve()

    cost = problem.cost(solution)

    print(f"\nFinal Cost: {cost:.2f}")

    print(
        f"Vehicles Used: "
        f"{solution.total_vehicles()}"
    )

    # ---------------------------------------------
    # PLOT SOLUTION
    # ---------------------------------------------

    if PLOT_SOLUTION:

        plot_solution(
            solution,
            problem.depot
        )

    # ---------------------------------------------
    # PLOT CONVERGENCE
    # ---------------------------------------------

    if hasattr(solver, "history"):

        plot_convergence(
            solver.history,
            title="Solver Convergence"
        )

    # ---------------------------------------------
    # SAVE SOLUTION
    # ---------------------------------------------

    if SAVE_RESULTS:

        save_solution(
            solution,
            problem.depot,
            SOLUTION_PATH
        )

    return solution

# =====================================================
# RUN BENCHMARK
# =====================================================

def run_benchmark(problem):

    print("=== RUN BENCHMARK ===")

    benchmark = Benchmark(
        problem,
        runs=BENCHMARK_RUNS
    )

    # ---------------------------------------------
    # ADD EXPERIMENTS
    # ---------------------------------------------

    benchmark.add_experiment(
        GeneticSolver,
        GA_CONFIG
    )

    benchmark.add_experiment(
        GreedySolver
    )

    benchmark.add_experiment(
        SimulatedAnnealingSolver,
        SA_CONFIG
    )

    benchmark.add_experiment(
        HybridSolver,
        HYBRID_CONFIG
    )

    # ---------------------------------------------
    # RUN
    # ---------------------------------------------

    results = benchmark.run()

    # ---------------------------------------------
    # PLOT BENCHMARK
    # ---------------------------------------------

    if PLOT_BENCHMARK:

        plot_benchmark(results)

    # ---------------------------------------------
    # SAVE RESULTS
    # ---------------------------------------------

    if SAVE_RESULTS:

        save_results(
            results,
            RESULT_PATH
        )

    # ---------------------------------------------
    # GENERATE REPORT
    # ---------------------------------------------

    report = generate_summary_report(
        benchmark.raw_results
    )

    print("\n")
    print(report)

    with open(REPORT_PATH, "w") as f:

        f.write(report)

    return results

# =====================================================
# RUN MULTIPLE DATASETS
# =====================================================

def run_multiple_datasets():

    print("=== MULTI DATASET BENCHMARK ===")

    datasets = [
        SMALL_DATASET,
        MEDIUM_DATASET,
        LARGE_DATASET,
    ]

    for dataset in datasets:

        print("\n")
        print("=" * 60)

        print(f"DATASET: {dataset}")

        print("=" * 60)

        problem = load_problem(dataset)

        run_benchmark(problem)

# =====================================================
# MAIN
# =====================================================

def main():

    # ---------------------------------------------
    # MULTI DATASET MODE
    # ---------------------------------------------

    if MULTI_DATASET_MODE:

        run_multiple_datasets()

        return

    # ---------------------------------------------
    # SINGLE DATASET
    # ---------------------------------------------

    problem = load_problem()

    # ---------------------------------------------
    # BENCHMARK MODE
    # ---------------------------------------------

    if RUN_BENCHMARK:

        run_benchmark(problem)

    else:

        run_single(problem)

# =====================================================
# ENTRY POINT
# =====================================================

if __name__ == "__main__":

    main()