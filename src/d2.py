from collections import Counter

def calc_checksum():
    num_twos, num_threes = 0, 0
    with open('../data/d2.txt', 'r') as f:
        for line in f:
            count = Counter(line)
            has_two, has_three = False, False
            for key, value in count.items():
                if value == 2:
                    has_two = True
                if value == 3:
                    has_three = True
            if has_two:
                num_twos += 1
            if has_three:
                num_threes += 1
    return num_twos * num_threes

def calc_common_letters():
    s = set() # values are (substring, missing index)
    with open('../data/d2.txt', 'r') as f:
        for line in f:
            for i in range(0, len(line)):
                curr = line[:i] + line[i+1:]
                if (curr, i) in s:
                    return curr
                s.add((curr, i))
    return 1



def main():
    part1 = calc_checksum()
    part2 = calc_common_letters()
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')

if __name__ == '__main__':
    main()