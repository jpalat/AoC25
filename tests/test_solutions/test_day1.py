# tests/test_solutions/test_day1.py

from aoc.solutions.day1 import part1, part2

def test_part1():
    test_input = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet"
    ]
    assert part1(test_input) == 142

def test_part2():
    test_input = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]
    assert part2(test_input) == 281