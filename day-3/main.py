from pathlib import Path
from typing import List


def gamma_rate(input: List[str]):
    """
    Return a binary string composed of the most common bits of the input.
    """
    result = ""
    binary_len = len(input[0])
    for i in range(binary_len):
        values = [val[i] for val in input]
        result += max(set(values), key=values.count)
    return result


def epsilon_rate(input: List[str]):
    """
    Return a binary string composed of the most common bits of the input.
    """
    result = ""
    binary_len = len(input[0])
    for i in range(binary_len):
        values = [val[i] for val in input]
        result += min(set(values), key=values.count)
    return result


def power_consumption(input: str) -> int:
    values = input.rsplit()

    gamma = gamma_rate(values)
    epsilon = epsilon_rate(values)

    return int(gamma, base=2) * int(epsilon, base=2)


def oxygen_generator_rate(input: List[str]):
    valid_inputs = input
    binary_len = len(input[0])
    for i in range(binary_len):
        values = [val[i] for val in input]
        most_common = max(set(values), key=values.count)
        if 

def co2_scrubber_rate(input: List[str]):
    pass


def life_support(input: str) -> int:
    pass

if __name__ == "__main__":
    current_path = Path(__file__).parent.absolute()
    with open(current_path / "input.txt", "r") as f:
        input = f.read()
    print(power_consumption(input))