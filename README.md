# TaskVector: A CPU Scheduling Simulator

A comprehensive Python implementation of four fundamental CPU scheduling algorithms. This project demonstrates process scheduling strategies, generates visual Gantt charts, and calculates performance metrics including turnaround time and waiting time.

## Overview

CPU scheduling is a core operating system function that determines which process runs on the CPU at any given time. This simulator implements four different scheduling strategies and compares their performance on the same set of processes.

## Algorithms Implemented

### 1. **FCFS (First Come, First Served)**
- **Type:** Non-preemptive
- **Strategy:** Processes execute in the order they arrive
- **Best for:** Batch systems with predictable workloads
- **Pros:** Simple, fair, no starvation
- **Cons:** High average waiting time for short processes

### 2. **SJF (Shortest Job First)**
- **Type:** Non-preemptive
- **Strategy:** Process with shortest burst time executes first
- **Best for:** Minimizing average waiting time
- **Pros:** Minimal average waiting time (optimal for non-preemptive)
- **Cons:** Can cause starvation of long processes; requires burst time prediction

### 3. **Round Robin (RR)**
- **Type:** Preemptive
- **Strategy:** Each process gets a fixed time quantum (default: 2 units)
- **Best for:** Interactive systems and time-sharing
- **Pros:** Fair allocation, no starvation, responsive
- **Cons:** Context switching overhead, higher turnaround for long processes

### 4. **SRTF (Shortest Remaining Time First)**
- **Type:** Preemptive
- **Strategy:** Process with shortest remaining burst time executes
- **Best for:** Minimizing average waiting time in preemptive systems
- **Pros:** Better performance than SJF, prevents starvation
- **Cons:** High context switching, requires burst time knowledge

## Features

- **Interactive CLI:** User-friendly command-line interface for entering process data
- **Input Validation:** Robust error handling for invalid inputs
- **Gantt Charts:** Visual representation of process execution order
- **Performance Metrics:** Calculates turnaround time (TAT) and waiting time (WT)
- **Comparative Analysis:** Run all four algorithms on the same input for direct comparison
- **Comprehensive Testing:** Unit tests for algorithm correctness

## Project Structure

```
cpu-scheduling-simulator/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── main.py                  # Main application entry point
├── algorithms/              # Scheduling algorithm implementations
│   ├── __init__.py
│   ├── fcfs.py             # First Come First Served
│   ├── sjf.py              # Shortest Job First
│   ├── round_robin.py      # Round Robin
│   └── srtf.py             # Shortest Remaining Time First
├── utils/                   # Utility modules
│   ├── __init__.py
│   └── validation.py        # Input validation functions
└── tests/                   # Unit tests
    ├── __init__.py
    └── test_algorithms.py   # Algorithm tests
```

## Installation

### Prerequisites
- Python 3.6 or higher
- Git (optional, for cloning)

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/jooryalzahrani/cpu-scheduling-simulator.git
cd cpu-scheduling-simulator
```

Or download the ZIP file and extract it.

2. **No external dependencies required** — uses only Python standard library

## Usage

### Run the Interactive Simulator

```bash
python main.py
```

### Example Session

```
CPU Scheduling Simulator
==================================================

Enter number of processes: 3
Enter burst time for P1: 8
Enter arrival time for P1: 0
Enter burst time for P2: 4
Enter arrival time for P2: 1
Enter burst time for P3: 2
Enter arrival time for P3: 2

== Round Robin (TQ=2) ==
Gantt Chart: P1 | P2 | P3 | P1 | P2 | P1

Process BT  AT  TAT WT
P1        8   0   12  4
P2        4   1   11  7
P3        2   2    4  2

Avg TAT = 9.00
Avg WT = 4.33
==================================================
```

### Run Tests

```bash
python tests/test_algorithms.py
```

Expected output:
```
✓ FCFS basic test passed
✓ SJF basic test passed
✓ Round Robin basic test passed
✓ SRTF basic test passed
 All tests passed!
```

## Understanding the Output

### Gantt Chart
Shows the sequence of process execution with context switches represented by `|`

### Performance Metrics

- **BT (Burst Time):** Total CPU time required by the process
- **AT (Arrival Time):** Time when the process enters the ready queue
- **TAT (Turnaround Time):** Total time from arrival to completion
  - Formula: `TAT = Completion Time - Arrival Time`
- **WT (Waiting Time):** Time spent waiting in the ready queue
  - Formula: `WT = TAT - Burst Time`

### Average Metrics
- **Avg TAT:** Mean turnaround time across all processes (lower is better)
- **Avg WT:** Mean waiting time across all processes (lower is better)

## Algorithm Details

### Execution Model
- All algorithms assume:
  - Processes are independent
  - No process priority levels
  - CPU idle when no processes are ready
  - Context switching is instantaneous

### Tie-Breaking Rules
- **FCFS/SJF:** By arrival time, then process ID
- **Round Robin:** Maintains a queue-based order
- **SRTF:** By arrival time, then lexicographic process ID order

## Performance Comparison

| Algorithm | Best Case | Average Case | Worst Case | Starvation |
|-----------|-----------|--------------|-----------|-----------|
| FCFS      | O(n)      | O(n)         | O(n)      | No        |
| SJF       | O(n log n)| O(n log n)   | O(n log n)| Yes       |
| RR        | O(n)      | O(n)         | O(n)      | No        |
| SRTF      | O(n log n)| O(n log n)   | O(n log n)| No        |

## Testing

The project includes comprehensive unit tests covering:
- Basic algorithm functionality
- Empty input handling
- Cross-algorithm validation
- Performance metric accuracy

Run tests with:
```bash
python tests/test_algorithms.py
```

## Use Cases

- **Educational:** Learn operating system scheduling concepts
- **Simulation:** Test scheduling strategies on custom workloads
- **Comparison:** Analyze performance differences between algorithms
- **Interview Prep:** Understand scheduling algorithm implementations

##  Learning Resources

- **Operating System Concepts** - Silberschatz, Galvin, Gagne
- **CPU Scheduling Algorithms:** https://en.wikipedia.org/wiki/Scheduling_(computing)
- **Gantt Charts:** https://en.wikipedia.org/wiki/Gantt_chart

## Contributing

Contributions are welcome! Feel free to:
- Report bugs via issues
- Suggest new features
- Improve documentation
- Submit pull requests

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Author

Joory Alzahrani


