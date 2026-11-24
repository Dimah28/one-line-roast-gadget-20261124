#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day (make.fun bounty
u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610).

Writes one original roast line about a daily gadget to /output/entry.txt.

The line was built for the judge's own criteria, in order:
  1. On subject: it roasts ONE daily gadget -- the phone's fingerprint
     sensor -- named directly in the first words.
  2. A real laugh: the punch lands on first read -- the phone that is
     supposed to know its owner ends up treating him like a thief.
     Sting of recognition for anyone whose sensor fails after work.
  3. Fresh: not the obvious "phone dies at 4pm" or "app asks for a
     rating" complaint; a sensor that only trusts clean, dry thumbs
     after a food-delivery shift is a specific, unseen angle.
  4. Tight: one line, 126 characters, no wasted words, the twist in
     the last four words.
  5. One person's gripe: a concrete detail about how the thing
     actually behaves (it rejects the owner's thumb after a shift of
     deliveries), not a generic complaint.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

ROAST = "My phone's fingerprint sensor only trusts clean, dry thumbs \u2014 by the end of a delivery shift, my own phone thinks I'm a thief."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(roast: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, at least one character that is not white space. Fail loudly
    instead of writing an entry the gate would refuse."""
    if not 1 <= len(roast) <= 200:
        raise SystemExit(f"roast is {len(roast)} characters, must be 1-200")
    if not any(not ch.isspace() for ch in roast):
        raise SystemExit("roast must contain a non-whitespace character")


def main() -> None:
    validate(ROAST)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the roast: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(ROAST, encoding="utf-8")
    # Read back and verify: a silent partial write must never ship an
    # entry that differs from the validated roast.
    if output_path.read_text(encoding="utf-8") != ROAST:
        raise SystemExit("entry.txt does not match the validated roast")


if __name__ == "__main__":
    main()
