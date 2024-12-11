from aoc.utils.input_reader import read_input_lines

def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle."""
    pass

def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    pass

def solve() -> tuple[int, int]:
    """Solve both parts of the puzzle."""
    data = read_input_lines(1)  # adjust day number
    return part1(data), part2(data)

if __name__ == "__main__":
    answer1, answer2 = solve()
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}") 