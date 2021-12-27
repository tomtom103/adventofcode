from pathlib import Path

def part2(input: str):
    """
    Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course.
    """
    position = {
        'horizontal': 0,
        'depth': 0,
        'aim': 0,
    }

    # Populate dictionary with input
    for element in input.split('\n'):
        instruction, value = element.split(' ')
        if instruction == 'down':
            position['aim'] += int(value)
        elif instruction == 'up':
            position['aim'] -= int(value)
        elif instruction == 'forward':
            position['horizontal'] += int(value)
            position['depth'] += int(value) * position['aim']
    # What do you get if you multiply your final horizontal position by your final depth?
    return position['horizontal'] * position['depth']

def main(input: str):
    """
    Calculate the horizontal position and depth you would have after following the planned course.
    """
    position = {
        'forward': 0,
        'down': 0,
        'up': 0,
    }

    # Populate dictionary with input
    for element in input.split('\n'):
        instruction, value = element.split(' ')
        position[instruction] += int(value)

    # What do you get if you multiply your final horizontal position by your final depth?
    return position['forward'] * abs(position['down'] - position['up'])
    

if __name__ == "__main__":
    current_path = Path(__file__).parent.absolute()
    with open(current_path / "input.txt", "r") as f:
        input = f.read()
    print(main(input))
    print(part2(input))