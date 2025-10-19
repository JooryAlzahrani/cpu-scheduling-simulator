import sys
sys.path.insert(0, '../')

from algorithms import fcfs, sjf, round_robin, srtf


def test_fcfs_basic():
    processes = [
        {'pID': 'P1', 'arrival': 0, 'burst': 8},
        {'pID': 'P2', 'arrival': 1, 'burst': 4},
        {'pID': 'P3', 'arrival': 2, 'burst': 2}
    ]
    
    gantt_chart, stats, avg_tat, avg_wt = fcfs.run_fcfs(processes)
    
    assert len(stats) == 3
    assert stats[0]['pID'] == 'P1'
    assert stats[0]['tat'] == 8
    assert stats[0]['wt'] == 0
    print("✓ FCFS basic test passed")


def test_fcfs_empty():
    processes = []
    gantt_chart, stats, avg_tat, avg_wt = fcfs.run_fcfs(processes)
    
    assert gantt_chart == []
    assert stats == []
    assert avg_tat == 0
    assert avg_wt == 0
    print("✓ FCFS empty test passed")


def test_sjf_basic():
    processes = [
        {'pID': 'P1', 'arrival': 0, 'burst': 8},
        {'pID': 'P2', 'arrival': 1, 'burst': 4},
        {'pID': 'P3', 'arrival': 2, 'burst': 2}
    ]
    
    gantt_chart, stats, avg_tat, avg_wt = sjf.run_sjf(processes)
    
    assert len(stats) == 3
    assert stats[0]['pID'] == 'P1'
    print("✓ SJF basic test passed")


def test_sjf_empty():
    processes = []
    gantt_chart, stats, avg_tat, avg_wt = sjf.run_sjf(processes)
    
    assert gantt_chart == []
    assert stats == []
    print("✓ SJF empty test passed")


def test_round_robin_basic():
    processes = [
        {'pID': 'P1', 'arrival': 0, 'burst': 8},
        {'pID': 'P2', 'arrival': 1, 'burst': 4},
        {'pID': 'P3', 'arrival': 2, 'burst': 2}
    ]
    
    gantt_chart, stats, avg_tat, avg_wt = round_robin.round_robin_algorithm(processes, time_quantum=2)
    
    assert len(stats) == 3
    assert len(gantt_chart) > 0
    print("✓ Round Robin basic test passed")


def test_round_robin_empty():
    processes = []
    gantt_chart, stats, avg_tat, avg_wt = round_robin.round_robin_algorithm(processes)
    
    assert gantt_chart == []
    assert stats == []
    print("✓ Round Robin empty test passed")


def test_srtf_basic():
    processes = [
        {'pID': 'P1', 'arrival': 0, 'burst': 8},
        {'pID': 'P2', 'arrival': 1, 'burst': 4},
        {'pID': 'P3', 'arrival': 2, 'burst': 2}
    ]
    
    gantt_chart, stats, avg_tat, avg_wt = srtf.srtf_scheduling(processes)
    
    assert len(stats) == 3
    assert len(gantt_chart) > 0
    print("✓ SRTF basic test passed")


def test_srtf_empty():
    processes = []
    gantt_chart, stats, avg_tat, avg_wt = srtf.srtf_scheduling(processes)
    
    assert gantt_chart == []
    assert stats == []
    print("✓ SRTF empty test passed")


def test_all_algorithms_same_input():
    processes = [
        {'pID': 'P1', 'arrival': 0, 'burst': 5},
        {'pID': 'P2', 'arrival': 0, 'burst': 3}
    ]
    
    fcfs_chart, fcfs_stats, fcfs_tat, fcfs_wt = fcfs.run_fcfs(processes)
    sjf_chart, sjf_stats, sjf_tat, sjf_wt = sjf.run_sjf(processes)
    rr_chart, rr_stats, rr_tat, rr_wt = round_robin.round_robin_algorithm(processes)
    srtf_chart, srtf_stats, srtf_tat, srtf_wt = srtf.srtf_scheduling(processes)
    
    assert len(fcfs_stats) == 2
    assert len(sjf_stats) == 2
    assert len(rr_stats) == 2
    assert len(srtf_stats) == 2
    print("✓ All algorithms test passed")


if __name__ == "__main__":
    test_fcfs_basic()
    test_fcfs_empty()
    test_sjf_basic()
    test_sjf_empty()
    test_round_robin_basic()
    test_round_robin_empty()
    test_srtf_basic()
    test_srtf_empty()
    test_all_algorithms_same_input()
    print("\n All tests passed!")