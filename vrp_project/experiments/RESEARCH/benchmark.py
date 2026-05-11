# experiments/RESEARCH/benchmark.py

import statistics

from experiments.RESEARCH.runner import (
    ExperimentRunner
)


class Benchmark:

    def __init__(
        self,
        problem,
        runs=5
    ):

        self.problem = problem

        self.runs = runs

        self.experiments = []

        # detailed benchmark data
        self.raw_results = []

    # =================================================
    # ADD EXPERIMENT
    # =================================================

    def add_experiment(
        self,
        solver_class,
        config=None
    ):

        self.experiments.append(
            (
                solver_class,
                config or {}
            )
        )

    # =================================================
    # RUN BENCHMARK
    # =================================================

    def run(self):

        all_results = []

        self.raw_results = []

        for (
            solver_class,
            config
        ) in self.experiments:

            costs = []

            times = []

            solver_name = (
                solver_class.__name__
            )

            print("\n")
            print("=" * 50)
            print(f"Running {solver_name}")
            print("=" * 50)

            # -----------------------------------------
            # MULTIPLE RUNS
            # -----------------------------------------

            for run_id in range(self.runs):

                runner = ExperimentRunner(
                    self.problem,
                    solver_class,
                    config
                )

                # IMPORTANT FIX
                result, solution = (
                    runner.run()
                )

                cost = result["cost"]

                elapsed = result["time"]

                costs.append(cost)

                times.append(elapsed)

                # save detailed result
                self.raw_results.append({

                    "solver": solver_name,

                    "run": run_id + 1,

                    "cost": cost,

                    "time": elapsed,

                    "vehicles": result["vehicles"]
                })

                print(
                    f"Run {run_id + 1} "
                    f"| Cost={cost:.2f} "
                    f"| Vehicles={result['vehicles']} "
                    f"| Time={elapsed:.4f}s"
                )

            # -----------------------------------------
            # SUMMARY
            # -----------------------------------------

            summary = {

                "solver": solver_name,

                "avg_cost": statistics.mean(
                    costs
                ),

                "best_cost": min(costs),

                "avg_time": statistics.mean(
                    times
                )
            }

            all_results.append(summary)

            print("\nSUMMARY")

            print(
                f"{summary['solver']} | "
                f"Best={summary['best_cost']:.2f} | "
                f"Avg={summary['avg_cost']:.2f} | "
                f"Time={summary['avg_time']:.4f}s"
            )

        return all_results