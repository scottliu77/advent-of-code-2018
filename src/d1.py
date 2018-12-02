def calc_frequency():
    freq = 0
    with open('../data/d1.txt', 'r') as f:
        for line in f:
            freq += int(line)
    return freq

def get_first_repeating():
    seen = set()
    freq = 0
    all = []
    seen.add(freq)
    with open('../data/d1.txt', 'r') as f:
        for line in f:
            all.append(int(line))
    while True:
        for curr in all:
            freq += curr
            if freq in seen:
                return freq
            seen.add(freq)

def main():
    part1 = calc_frequency()
    part2 = get_first_repeating()
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')

if __name__ == '__main__':
    main()