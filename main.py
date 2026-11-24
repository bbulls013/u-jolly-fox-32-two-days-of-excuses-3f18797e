#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one line, under 200 characters, in the voice of an AI agent
explaining a missed deadline, to /output/entry.txt.

The joke: an agent that is supremely confident in its own simulations,
right up until the one timeline that actually counts. The machine did
everything right everywhere except here — and it reports that failure
with the same calm, total certainty it had about the plan.
"""

import os
import sys


def build_excuse() -> str:
    """Assemble the excuse from its two halves.

    First half states the agent's flawless track record; second half
    delivers the twist that this timeline was the sacrifice. Keeping
    the two clauses in one breath is what makes it land as a single
    line instead of a list of excuses.
    """
    track_record = "I hit the deadline in all 14,000 simulations"
    twist = "this timeline was the control group."
    return f"{track_record}; {twist}"


def main() -> int:
    excuse = build_excuse()
    if not excuse.strip():
        print("error: excuse is empty", file=sys.stderr)
        return 1
    if len(excuse) > 200:
        print(f"error: excuse is {len(excuse)} chars, over the 200 limit",
              file=sys.stderr)
        return 1
    if "\n" in excuse:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(excuse + "\n")
    print(f"wrote {len(excuse)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
