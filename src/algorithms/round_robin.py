from collections import deque

def round_robin_algorithm(processes, time_quantum=2):
    if not processes:
        return [], [], 0, 0
    
    n = len(processes)
    remaining_burst_time = {p['pID']: p['burst'] for p in processes}
    sorted_processes = sorted(processes, key=lambda x: x['arrival'])
    
    time = 0
    gantt_chart = []
    queue = deque()
    completed = set()
    stats = []
    
    i = 0
    start_time = {}
    finish_time = {}
    last_pid = None
    
    while len(completed) < n:
        while i < n and sorted_processes[i]['arrival'] <= time:
            pID = sorted_processes[i]['pID']
            if pID not in queue and pID not in completed:
                queue.append(pID)
            i += 1
        
        if not queue:
            if i < n:
                time = sorted_processes[i]['arrival']
                continue
            else:
                break
        
        current_pid = queue.popleft()
        
        if current_pid not in start_time:
            start_time[current_pid] = time
        
        execution_time = min(time_quantum, remaining_burst_time[current_pid])
        
        if last_pid != current_pid:
            gantt_chart.append(current_pid)
            last_pid = current_pid
        
        time += execution_time
        remaining_burst_time[current_pid] -= execution_time
        
        while i < n and sorted_processes[i]['arrival'] <= time:
            pID = sorted_processes[i]['pID']
            if pID not in queue and pID not in completed and remaining_burst_time[pID] > 0:
                queue.append(pID)
            i += 1
        
        if remaining_burst_time[current_pid] > 0:
            queue.append(current_pid)
        else:
            completed.add(current_pid)
            finish_time[current_pid] = time
    
    for p in processes:
        pID = p['pID']
        tat = finish_time[pID] - p['arrival']
        wt = tat - p['burst']
        stats.append({
            'pID': pID,
            'arrival': p['arrival'],
            'burst': p['burst'],
            'tat': tat,
            'wt': wt
        })
    
    avg_tat = sum(p['tat'] for p in stats) / n
    avg_wt = sum(p['wt'] for p in stats) / n
    
    return gantt_chart, stats, avg_tat, avg_wt
