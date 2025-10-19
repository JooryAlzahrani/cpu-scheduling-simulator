from algorithms import fcfs, sjf, round_robin, srtf
from utils import validation


def format_gantt_chart(gantt_chart):
    return " | ".join(
        p['pID'] if isinstance(p, dict) else str(p)
        for p in gantt_chart
    )


def print_results(algorithm_name, gantt_chart, stats, avg_tat, avg_wt, print_separator=True):
    print(f"\n== {algorithm_name} ==")
    print("Gantt Chart: " + format_gantt_chart(gantt_chart))
    print("\nProcess BT  AT  TAT WT")
    for p in stats:
        print(f"{p['pID']:7} {p['burst']:3} {p['arrival']:3} {p['tat']:3} {p['wt']:3}")
    print(f"\nAvg TAT = {avg_tat:.2f}")
    print(f"Avg WT = {avg_wt:.2f}")
    if print_separator:
        print("=" * 50)


def get_process_input():
    while True:
        try:
            n = int(input("\nEnter number of processes: "))
            if n < 1:
                print("Error: Number of processes must be at least 1")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer")
    
    processes = []
    for i in range(1, n + 1):
        while True:
            try:
                burst = int(input(f"Enter burst time for P{i}: "))
                arrival = int(input(f"Enter arrival time for P{i}: "))
                
                if not validation.is_valid_process(burst, arrival):
                    print("Error: Burst time and arrival time must be non-negative")
                    continue
                
                processes.append({
                    'pID': f'P{i}',
                    'arrival': arrival,
                    'burst': burst
                })
                break
            except ValueError:
                print("Error: Please enter valid integers")
    
    return processes


def main():
    print("CPU Scheduling Simulator")
    print("=" * 50)
    
    processes = get_process_input()
    
    gantt_chart, stats, avg_tat, avg_wt = round_robin.round_robin_algorithm(processes, time_quantum=2)
    print_results("Round Robin (TQ=2)", gantt_chart, stats, avg_tat, avg_wt)

    gantt_chart, stats, avg_tat, avg_wt = fcfs.run_fcfs(processes)
    print_results("First Come First Serve", gantt_chart, stats, avg_tat, avg_wt)

    gantt_chart, stats, avg_tat, avg_wt = sjf.run_sjf(processes)
    print_results("Shortest Job First", gantt_chart, stats, avg_tat, avg_wt)

    gantt_chart, stats, avg_tat, avg_wt = srtf.srtf_scheduling(processes)
    print_results("Shortest Remaining Time First", gantt_chart, stats, avg_tat, avg_wt, print_separator=False)


if __name__ == "__main__":
    main()