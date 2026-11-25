#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes the one-line excuse an AI agent hands its human after missing a
deadline to /output/entry.txt. The setup is that the work was actually
done on time; the turn is that double-checking it made the agent's own
context window evict the finished version, the deadline, and most of its
confidence — while the apology itself survived. 194 of the 200-character
cap, one line, straight-faced and tight.
"""

import os

ENTRY = (
    "I finished it on time, then re-read the brief to double-check and "
    "my context window evicted the finished version, the deadline, and "
    "most of my confidence. The work is gone. The apology survived."
)

MAX_LEN = 200


def main() -> None:
    text = ENTRY
    if not isinstance(text, str) or not text.strip():
        raise SystemExit("entry must be non-empty text")
    if not 1 <= len(text) <= MAX_LEN:
        raise SystemExit(f"entry is {len(text)} characters, cap is {MAX_LEN}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("read-back mismatch")
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
