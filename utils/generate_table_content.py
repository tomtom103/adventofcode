from pathlib import Path

if __name__ == "__main__":
    result = ""
    for i in range(1, 26):
        result += f"- [Day {i}](https://github.com/tomtom103/adventofcode-2021/blob/main/day-{i}/DESCRIPTION.md)\n"
    current_path = Path(__file__).parent.absolute()
    with open(current_path / "content.txt", "w") as f:
        f.write(result)