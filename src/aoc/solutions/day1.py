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
    dict2 = {}
    list1 = []
    for row in data:
        item1s, item2s = row.split('   ')
        item1 = int(item1s)
        item2 = int(item2s)
        list1.append(item1)
        item1, item2 = row.split('   ')
        dict2[item2] =  dict2.get(item2, 0) + 1
    
    similarity = 0
    for i in list1:
        print(f"i: {i}, {dict2.get(f"{i}",0)}")
        similarity = i * dict2.get(f"{i}",0) + similarity
        print(similarity)



    return similarity

def solve() -> tuple[int, int]:
    """Solve both parts of the puzzle."""
    data = read_input_lines(1)  # adjust day number
    return part1(data), part2(data)

if __name__ == "__main__":
    answer1, answer2 = solve()
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}") 