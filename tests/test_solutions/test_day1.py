# tests/test_solutions/test_day1.py

from aoc.solutions.day1 import part1, part2

def test_part1():
    test_input = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3"
    ]
    assert part1(test_input) == 11

# def test_part2():
#     test_input = [
#         "two1nine",
#         "eightwothree",
#         "abcone2threexyz",
#         "xtwone3four",
#         "4nineeightseven2",
#         "zoneight234",
#         "7pqrstsixteen"
#     ]
#     assert part2(test_input) == 281