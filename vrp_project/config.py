# config.py

import os

# =====================================================
# BASE PATH
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

RESULT_DIR = os.path.join(
    BASE_DIR,
    "results"
)

LOG_DIR = os.path.join(
    RESULT_DIR,
    "logs"
)

PLOT_DIR = os.path.join(
    RESULT_DIR,
    "plots"
)

REPORT_DIR = os.path.join(
    RESULT_DIR,
    "reports"
)

# -----------------------------------------------------
# CREATE DIRECTORIES
# -----------------------------------------------------

os.makedirs(DATA_DIR, exist_ok=True)

os.makedirs(RESULT_DIR, exist_ok=True)

os.makedirs(LOG_DIR, exist_ok=True)

os.makedirs(PLOT_DIR, exist_ok=True)

os.makedirs(REPORT_DIR, exist_ok=True)

# =====================================================
# DATASET CONFIG
# =====================================================

USE_BENCHMARK_FILE = False

# -----------------------------------------------------
# CSV DATASETS
# -----------------------------------------------------

SMALL_DATASET = os.path.join(
    DATA_DIR,
    "small.csv"
)

MEDIUM_DATASET = os.path.join(
    DATA_DIR,
    "medium.csv"
)

LARGE_DATASET = os.path.join(
    DATA_DIR,
    "large.csv"
)

# default dataset
DATA_PATH = MEDIUM_DATASET

# -----------------------------------------------------
# BENCHMARK VRP FILE
# -----------------------------------------------------

BENCHMARK_PATH = os.path.join(
    DATA_DIR,
    "benchmark",
    "A-n32-k5.vrp"
)

# =====================================================
# VEHICLE CONFIG
# =====================================================

VEHICLE_CAPACITY = 100

# =====================================================
# MULTI-OBJECTIVE WEIGHTS
# =====================================================

MULTI_OBJECTIVE_CONFIG = {

    # penalize many vehicles
    "vehicle_weight": 100,

    # penalize overload
    "capacity_penalty_weight": 1000,
}

# =====================================================
# GENETIC ALGORITHM CONFIG
# =====================================================

GA_CONFIG = {

    "population_size": 50,

    "generations": 100,

    "mutation_rate": 0.1,

    "use_local_search": True,
}

# =====================================================
# SIMULATED ANNEALING CONFIG
# =====================================================

SA_CONFIG = {

    "initial_temp": 1000,

    "cooling_rate": 0.995,

    "iterations": 500,

    "use_local_search": True,
}

# =====================================================
# HYBRID SOLVER CONFIG
# =====================================================

HYBRID_CONFIG = {

    "population_size": 50,

    "generations": 100,

    "mutation_rate": 0.1,
}

# =====================================================
# EXPERIMENT CONFIG
# =====================================================

RUN_BENCHMARK = True

BENCHMARK_RUNS = 5

MULTI_DATASET_MODE = False

# =====================================================
# VISUALIZATION CONFIG
# =====================================================

PLOT_SOLUTION = True

PLOT_BENCHMARK = True

PLOT_CONVERGENCE = True

# =====================================================
# OUTPUT CONFIG
# =====================================================

SAVE_RESULTS = True

# -----------------------------------------------------
# RESULT FILES
# -----------------------------------------------------

RESULT_PATH = os.path.join(
    LOG_DIR,
    "results.json"
)

SOLUTION_PATH = os.path.join(
    RESULT_DIR,
    "solution.json"
)

REPORT_PATH = os.path.join(
    REPORT_DIR,
    "benchmark_report.txt"
)

# =====================================================
# RANDOM SEED
# =====================================================

RANDOM_SEED = 42