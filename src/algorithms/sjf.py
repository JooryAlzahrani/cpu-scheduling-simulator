def run_sjf(processes):
    if not processes:
        return [], [], 0, 0
    
    processes = sorted(processes, key=lambda p: (p['arrival'], p['burst']))
    completed = []
    gantt_chart = []
    stats = []
    time = 0
    total_tat = 0
    total_wt = 0
    ready_queue = []
    i = 0
    n = len(processes)

    while len(completed) < n:
        while i < n and processes[i]['arrival'] <= time:
            ready_queue.append(processes[i])
            i += 1

        if ready_queue:
            ready_queue.sort(key=lambda p: p['burst'])
            p = ready_queue.pop(0)
        else:
            if i < n:
                time = processes[i]['arrival']
                continue
            else:
                break

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
        completed.append(p)

    avg_tat = total_tat / n
    avg_wt = total_wt / n
    
    return gantt_chart, stats, avg_tat, avg_wt
