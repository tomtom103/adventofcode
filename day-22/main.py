from pathlib import Path

def main(input: str):
    pass

if __name__ == "__main__":
    current_path = Path(__file__).parent.absolute()
    with open(current_path / "input.txt", "r") as f:
        input = f.read()
    print(main(input))