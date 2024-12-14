#!/usr/bin/env python3

import argparse
from pathlib import Path
import sys

SOLUTION_TEMPLATE = '''from aoc.utils.input_reader import read_input_lines

def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle."""
    pass

def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    pass

def solve() -> tuple[int, int]:
    """Solve both parts of the puzzle."""
    data = read_input_lines({day})
    return part1(data), part2(data)

if __name__ == "__main__":
    answer1, answer2 = solve()
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
'''

TEST_TEMPLATE = '''from aoc.solutions.day{day} import part1, part2

def test_part1():
    test_input = [
        # Add your test input here
        "sample1",
        "sample2"
    ]
    expected = 0  # Replace with expected result
    assert part1(test_input) == expected

def test_part2():
    test_input = [
        # Add your test input here
        "sample1",
        "sample2"
    ]
    expected = 0  # Replace with expected result
    assert part2(test_input) == expected
'''

def create_directory(path: Path) -> None:
    """Create directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)

def write_file(path: Path, content: str) -> None:
    """Write content to file and make it executable if it's a solution file."""
    path.write_text(content)
    if 'solutions' in str(path):
        path.chmod(path.stat().st_mode | 0o111)  # Make executable

def create_day(day: int) -> None:
    """Create template files for the specified day."""
    # Setup directories
    root = Path.cwd()
    solution_dir = root / "src" / "aoc" / "solutions"
    test_dir = root / "tests" / "test_solutions"
    input_dir = root / "inputs"
    
    # Create directories
    for directory in [solution_dir, test_dir, input_dir]:
        create_directory(directory)
    
    # Create files
    solution_file = solution_dir / f"day{day}.py"
    test_file = test_dir / f"test_day{day}.py"
    input_file = input_dir / f"day{day}.txt"
    
    write_file(solution_file, SOLUTION_TEMPLATE.format(day=day, answer1="{answer1}", answer2="{answer2}"))
    write_file(test_file, TEST_TEMPLATE.format(day=day))
    input_file.touch()
    
    # Print success message
    print(f"Created files:")
    print(f"  - {solution_file}")
    print(f"  - {test_file}")
    print(f"  - {input_file}")
    print()
    print(f"Ready to solve Day {day}! Don't forget to:")
    print(f"1. Add your puzzle input to {input_file}")
    print(f"2. Update the test cases with example data from the puzzle")
    print()
    print(f"Run tests with: pytest {test_file}")
    print(f"Run solution with: python {solution_file}")

def main():
    parser = argparse.ArgumentParser(description='Create Advent of Code solution template files')
    parser.add_argument('day', type=int, help='Day number to create templates for')
    
    args = parser.parse_args()
    
    if args.day < 1 or args.day > 25:
        print("Error: Day must be between 1 and 25")
        sys.exit(1)
    
    create_day(args.day)

if __name__ == "__main__":
    main()