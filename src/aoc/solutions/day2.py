from aoc.utils.input_reader import read_input_lines

def check_state(reports: list[str]) -> bool:

    current_state = ""
    report_state = ""
    for index, report in enumerate(reports):
        if index != len(reports) - 1:
            difference = int(report) - int(reports[index + 1])
            if abs(difference) > 3:
                return False
            if difference < 0:
                current_state = "decreasing"
            else: 
                if difference == 0:
                    return False
                else:
                    current_state = "increasing"
            if report_state == "":
                report_state = current_state
            else:
                if current_state != report_state:
                    return False
    return True



def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle."""
    status_list = []
    for row in data:
        reports = row.split(' ')
        status = check_state(reports)
        status_list.append(status)
    
    safe_count = 0
    print(status_list)
    for status in status_list:
        if status:
            safe_count = safe_count + 1
            print(safe_count)
    return safe_count



def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    pass

def solve() -> tuple[int, int]:
    """Solve both parts of the puzzle."""
    data = read_input_lines(2)  # adjust day number
    return part1(data), part2(data)

if __name__ == "__main__":
    answer1, answer2 = solve()
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}") 