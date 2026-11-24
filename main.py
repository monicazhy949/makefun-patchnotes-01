"""One-line patch note for a bug in real life, for make.fun."""
import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "v2.4.1: fixed a bug where the bladder sent its low-battery warning "
    "only once you were already out the door."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
