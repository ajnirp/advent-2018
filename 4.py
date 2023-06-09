# python3 4.py < 4.txt
'''
Assumptions
1. Shifts never overlap
2. Every time a guard sleeps, they wake before the next shift starts
3. A guard never falls asleep before 00:00
''' 

with open(0) as file:
    data = [line.strip() for line in file.readlines()]
    data.sort()

def day_from_line(line):
    x = line.split()[0].split('-')
    return x[1] + '-' + x[2]

def guard_id_from_line(line):
    return int(line.split()[3][1:])

def minute_from_line(line):
    return int(line.split()[1].split(':')[1][:-1])

def init_guard(guard_id, sleep_map):
    if guard_id not in sleep_map:
        sleep_map[guard_id] = [0 for _ in range(60)]

def process_shift_sleeps(guard_id, sleeps, sleep_map):
    init_guard(guard_id, sleep_map)
    for i in range(0, len(sleeps), 2):
        start = sleeps[i]
        end = sleeps[i+1]
        for j in range(start, end):
            sleep_map[guard_id][j] += 1

def process_shift(shift, sleep_map):
    guard_id = guard_id_from_line(shift[0])
    sleeps = []
    for line in shift:
        if 'falls' in line or 'wakes' in line:
            minute = minute_from_line(line)
            sleeps.append(minute)
    process_shift_sleeps(guard_id, sleeps, sleep_map)
    return (guard_id, sleeps)

def sleepiest_minute(guard_id, sleep_map):
    histogram = sleep_map[guard_id]
    return max(range(len(histogram)), key=lambda i: histogram[i])

shifts = []
for line in data:
    if 'Guard' in line:
        shifts.append([line])
    else:
        shifts[-1].append(line)

sleep_map = {}
shifts = list(map(lambda x: process_shift(x, sleep_map), shifts))

result_1_guard = -1
max_minutes_slept = 0
for key, val in sleep_map.items():
    minutes_slept = sum(val)
    if minutes_slept > max_minutes_slept:
        max_minutes_slept = minutes_slept
        result_1_guard = key

result_1 = result_1_guard * sleepiest_minute(result_1_guard, sleep_map)
print(result_1)

max_sleepiest_minute = 0
max_sleepiest_minute_val = 0
result_2_guard = 0
for minute in range(60):
    for guard_id in sleep_map:
        guard_sleep = sleep_map[guard_id][minute]
        if guard_sleep > max_sleepiest_minute_val:
            max_sleepiest_minute_val = guard_sleep
            max_sleepiest_minute = minute
            result_2_guard = guard_id

result_2 = result_2_guard * max_sleepiest_minute
print(result_2)
