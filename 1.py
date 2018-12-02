# https://adventofcode.com/2018/day/1

with open('1.txt', 'r') as f:
    print(sum(map(int, f.readlines())))

with open('1.txt', 'r') as f:
    freq = 0
    seen = set([0])
    changes = list(map(int, f.readlines()))
    found = False
    while not found:
        for change in changes:
            freq += change
            if freq in seen:
                print(freq)
                found = True
                break
            seen.add(freq)