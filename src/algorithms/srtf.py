import copy

def srtf_scheduling(processes):
    if not processes:
        return [], [], 0, 0
    
    processes = copy.deepcopy(processes)

    for p in processes:
        p['remaining_time'] = p['burst']
        p['complete'] = False
        p['end_time'] = -1
        p['waiting_time'] = 0
        p['turnaround_time'] = 0

    time = 0
    complete = 0
    n = len(processes)
    gantt_chart = []
    last_pid = None

    while complete < n:
        current = None
        min_remaining_time = float('inf')
        
        for p in processes:
            if p['arrival'] <= time and not p['complete']:
                if p['remaining_time'] < min_remaining_time:
                    min_remaining_time = p['remaining_time']
                    current = p
                elif p['remaining_time'] == min_remaining_time:
                    if current and p['arrival'] < current['arrival']:
                        current = p
                    elif current and p['arrival'] == current['arrival']:
                        if p['pID'] < current['pID']:
                            current = p

        if current:
            if last_pid != current['pID']:
                gantt_chart.append(current['pID'])
                last_pid = current['pID']

            current['remaining_time'] -= 1
            time += 1

            if current['remaining_time'] == 0:
                current['complete'] = True
                complete += 1
                current['end_time'] = time
                current['turnaround_time'] = current['end_time'] - current['arrival']
                current['waiting_time'] = current['turnaround_time'] - current['burst']
        else:
            time += 1
            if last_pid != "IDLE":
                gantt_chart.append("IDLE")
                last_pid = "IDLE"

    stats = [{
        'pID': p['pID'],
        'burst': p['burst'],
        'arrival': p['arrival'],
        'tat': p['turnaround_time'],
        'wt': p['waiting_time'],
    } for p in processes]

    avg_tat = sum(p['turnaround_time'] for p in processes) / n
    avg_wt = sum(p['waiting_time'] for p in processes) / n

    return gantt_chart, stats, avg_tat, avg_wt
