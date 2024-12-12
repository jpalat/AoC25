# tests/test_solutions/test_day2.py

from aoc.solutions.day2 import part1, part2

def test_part1():
    test_input = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9"
    ]
    assert part1(test_input) == 2

def test_part1():
    test_input = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9"
    ]
    assert part2(test_input) == 4