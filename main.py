"""The One-Line Laugh: print the single joke stored in entry.txt."""

from pathlib import Path


def load_joke() -> str:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("entry.txt is empty — nothing to laugh at yet.")
    return text


def main() -> None:
    print(load_joke())


if __name__ == "__main__":
    main()
