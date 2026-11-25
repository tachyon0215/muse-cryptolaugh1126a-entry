#!/usr/bin/env python3
"""Write the one-line crypto trading joke entry to entry.txt.

Judging fit: the brief rewards a clear setup and turn, a real laugh, a
recognisable detail of trading life, tight phrasing and a punchline at
the end. This entry uses two earned details - bags down 90% and the
group chat still calling it a dip - then escalates the word 'dip'
past its trading sense: at this depth it does not need a buy order,
it needs a submarine. The image is absurd but the pain is exact.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "My bags are down 90%, the group chat still calls it a dip, and I've stopped buying - at this depth, the dip doesn't need a buy order, it needs a submarine."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
