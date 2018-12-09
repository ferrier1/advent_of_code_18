from datetime import datetime
from collections import defaultdict, Counter


def readin(file):
    with open(file) as f:
        input = f.read().splitlines()
        return input



def takeSecond(elem):
    return elem[1]

def date_time_getter(line):
    time_string = line.split('] ')[0].strip('[')
    date_time = datetime.strptime(time_string, '%Y-%m-%d %H:%M')
    return date_time

def guard_id_number(line):
    if 'Guard' in line:
        guard_id = int(line.split(' ')[3].strip('#'))
        return guard_id


def solver(input):
    input.sort()
    guards = defaultdict(Counter)
    data = []
    for line in input:
        if 'Guard' in line:
            guard_id, start_shift = guard_id_number(line), date_time_getter(line)
        elif 'falls' in line:
            start_sleep = date_time_getter(line)
        elif 'wakes' in line:
            ends_sleep = date_time_getter(line)
            sleep_time = ends_sleep.minute - start_sleep.minute
            mins_asleep = [min for min in range(start_sleep.minute, ends_sleep.minute)]
            days_data = [start_sleep.date(), mins_asleep]
            guards[guard_id].update(Counter(mins_asleep))
    for key, value in guards.items():
        data.append([key, sum(value.values()), guards[key].most_common()[0][0]])
    data.sort(key=takeSecond, reverse=True)
    return (data[0][0] * data[0][2])











def main():
    """
    input = 1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up.splitlines()
"""
    input = readin('inputs/input.txt')
    print(solver(input))




if __name__ == "__main__":
    main()
