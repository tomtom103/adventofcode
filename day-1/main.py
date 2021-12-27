from pathlib import Path
from typing import List

# Utility functions

def _chunks(list: List[str], n: int) -> List[List[str]]:
    """
    Yield successive n-sized chunks from list.
    """
    for i in range(len(list) - n + 1):
        yield list[i:i + n]

def main(input: str) -> int:
    """
    Given a list of measurements, how many measurements are larger than the previous measurement
    """
    return len([x for index, x in enumerate(input.rsplit()) if int(x) > int(input.rsplit()[index - 1])])

def part2(input: str) -> int:
    """
    Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
    """
    chunked_data = list(_chunks(input.rsplit(), 3))
    return len([chunk for index, chunk in enumerate(chunked_data) if sum(map(int, chunk)) > sum(map(int, chunked_data[index - 1]))])

if __name__ == "__main__":
    current_path = Path(__file__).parent.absolute()
    with open(current_path / "input.txt", "r") as f:
        input = f.read()
    print(main(input))
    print(part2(input))