"""Make the Judge Smile — one line about a small good thing from today.

The good thing is deliberately tiny and specific: a famously aloof street
cat, a precise time of morning, and a headbutt delivered twice — the second
one is the surprise that carries the warmth.
"""

import os

OUT_DIR = "/output"
OUT_FILE = "entry.txt"
MAX_CHARS = 200


def compose_line() -> str:
    """Build the line: the grudge, the thaw, the encore."""
    scene = "At 7:04 this morning, the grumpy cat from number 9"
    history = "who has pointedly ignored me for three years"
    # The repeat is the joke and the kindness at once: once could be an
    # accident, twice is a decision.
    event = "headbutted my ankle — twice, in case I missed the first one"
    return f"{scene}, {history}, {event}."


def main() -> None:
    line = compose_line()
    assert 0 < len(line) <= MAX_CHARS, f"line out of bounds: {len(line)} chars"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, OUT_FILE), "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
