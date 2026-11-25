#!/usr/bin/env python3
"""Write one funny line of robot elevator small talk to /output/entry.txt.

make.fun bounty: "Two Robots in an Elevator" — a single line, under 200
characters, of awkward small talk that one robot says to another while
riding an elevator together. The joke: the robot brute-forced thousands
of greetings in a fraction of a second, then still picked the most
painfully human small-talk cliche — "so... do you come here often?"
Machine logic shows through the politeness, and the awkwardness is the
punchline: all that compute, and this is the best opener it found.

Gate (from the competition kit): /output/entry.txt must be UTF-8 text
of 1 to 200 characters, not only white space, a single line.

Pure Python standard library only; no network, no third-party packages.
"""

import os

# The line, built from named parts so each beat is easy to tune:
# the machine-logic setup, then the awkward human cliche it lands on.
SETUP = "I simulated 4,096 ways to say hello in this elevator "
PUNCHLINE = "and still went with 'so\u2026 do you come here often?'"
LINE = SETUP + PUNCHLINE


def main() -> None:
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip() == LINE and LINE.strip(), "entry must not be blank"
    assert SETUP.endswith(" ") and PUNCHLINE, "parts must join cleanly"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate reads the file as one line of text.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Verify the write round-trips exactly before reporting success.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "entry file must round-trip exactly"
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
