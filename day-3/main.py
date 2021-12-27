from pathlib import Path

def _mcb(vals: list) -> int:
    bit_count = [sum(int(num[i]) for num in vals) for i in range(len(vals[0]))]
    return [1 if cnt >= (len(vals) - cnt) else 0 for cnt in bit_count]

def reduce_reports(reports: list, invert: bool = False) -> int:
    for i in range(0, len(reports[0])):
        mcb = _mcb(reports)[i]
        bit = str(1 - mcb if invert else mcb)
        reports = [rep for rep in reports if rep[i] == bit]
        if len(reports) == 1:
            break
    return int(reports[0], 2)

def part1(vals: str) -> int:
    vals = vals.rsplit('\n')
    mcb = _mcb(vals)
    gamma = "".join(["1" if bit else "0" for bit in mcb])
    epsilon = "".join(["0" if bit else "1" for bit in mcb])
    return int(gamma, 2) * int(epsilon, 2)

def part2(vals: str) -> int:
    vals = vals.rsplit('\n')
    oxygen_generator_rating = reduce_reports(vals[:])
    co2_scrubber_rating = reduce_reports(vals[:], invert=True)
    return oxygen_generator_rating * co2_scrubber_rating

if __name__ == "__main__":
    current_path = Path(__file__).parent.absolute()
    with open(current_path / "input.txt", "r") as f:
        input = f.read()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")