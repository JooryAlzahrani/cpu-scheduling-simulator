def run_fcfs(processes):
    if not processes:
        return [], [], 0, 0
    
    processes_sorted = sorted(processes, key=lambda p: p['arrival'])
    time = 0
    gantt_chart = []
    stats = []
    total_tat = 0
    total_wt = 0

    for p in processes_sorted:
        if time < p['arrival']:
            time = p['arrival']
        
        start_time = time
        end_time = time + p['burst']
        time = end_time
        
        tat = time - p['arrival']
        wt = tat - p['burst']
        
        gantt_chart.append(p['pID'])
        
        stats.append({
            'pID': p['pID'],
            'arrival': p['arrival'],
            'burst': p['burst'],
            'tat': tat,
            'wt': wt
        })
        
        total_tat += tat
        total_wt += wt

    avg_tat = total_tat / len(processes)
    avg_wt = total_wt / len(processes)
    
    return gantt_chart, stats, avg_tat, avg_wt
