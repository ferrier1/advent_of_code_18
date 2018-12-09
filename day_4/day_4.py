from datetime import datetime
from collections import defaultdict, Counter


def readin(file):
    with open(file) as f:
        input = f.read().splitlines()
        return input



def take_second(elem):
    return elem[1]

def take_third(elem):
    return elem[2]

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
    part_one_data = []
    part_two_data = []
    final_data = []
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
        part_one_data.append([key, sum(value.values()), guards[key].most_common()[0][0]])
        part_two_data.append([key] + list(guards[key].most_common()[0]))
    part_one = sorted(part_one_data, key=take_second, reverse=True)
    part_two = sorted(part_one_data, key=take_third, reverse=True)
    print(part_one)
    print("-----------")
    print(part_two)
    final_data.append(part_one[0][0] * part_one[0][2])
    final_data.append(part_two[0][0] * part_two[0][2])
    return final_data





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
    ans = solver(input)
    print("Part 1 answer: {}. Part 2 answer: {}".format(ans[0], ans[1]))




if __name__ == "__main__":
    main()
