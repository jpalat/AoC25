def read_input(day: int) -> str:
    """Read the input file for the given day."""
    with open(f"inputs/day_{day:02d}.txt") as f:
        return f.read().strip()

def read_input_lines(day: int) -> list[str]:
    """Read the input file for the given day as lines."""
    return read_input(day).split('\n')