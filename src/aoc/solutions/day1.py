from aoc.utils.input_reader import read_input_lines

def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle."""
    list1 = []
    list2 = []
    for row in data:
        item1, item2 = row.split('   ')
        list1.append(int(item1))
        list2.append(int(item2))
    print(list1, list2)
    list1.sort() 
    list2.sort()
    print(list1, list2)

    sum = 0
    for idx, item in enumerate(list1):
        diff = abs( item - list2[idx])
        sum = diff + sum
        

    
    return sum

def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    return 282

def solve() -> tuple[int, int]:
    """Solve both parts of the puzzle."""
    data = read_input_lines(1)  # adjust day number
    return part1(data), part2(data)

if __name__ == "__main__":
    answer1, answer2 = solve()
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}") 