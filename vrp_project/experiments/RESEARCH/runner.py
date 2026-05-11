import time

class ExperimentRunner:
    def __init__(self, problem, solver_class, solver_config=None):
        self.problem = problem
        self.solver_class = solver_class
        self.solver_config = solver_config or {}

    def run(self):
        # init solver
        solver = self.solver_class(self.problem, **self.solver_config)

        start_time = time.time()
        solution = solver.solve()
        end_time = time.time()

        total_cost = self.problem.cost(solution)
        runtime = end_time - start_time

        result = {
            "solver": self.solver_class.__name__,
            "cost": total_cost,
            "vehicles": solution.total_vehicles(),
            "time": runtime
        }

        return result, solution