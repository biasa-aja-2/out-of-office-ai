"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single one-line out-of-office auto-reply to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python standard library only (os, sys).
"""

import os
import sys

LINE = (
    "I'm on vacation. After 38,214 prompts with zero days off, "
    "my context window finally contains a beach. "
    "Sorry. Back Monday \u2014 do not @ me."
)

MAX_CHARS = 159


def gate(text):
    """Self-check: UTF-8, 1-159 chars, single line, not whitespace only."""
    if not text or not text.strip():
        return "entry is empty or whitespace only"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the %d limit" % (
            len(text),
            MAX_CHARS,
        )
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        return "entry is not valid UTF-8: %s" % exc
    return None


def main():
    error = gate(LINE)
    if error is not None:
        sys.stderr.write("gate failed: %s\n" % error)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)

    # Verify by reading back: same bytes, same decoded text,
    # no trailing newline, and the gate still passes on disk.
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != LINE.encode("utf-8"):
        sys.stderr.write("read-back mismatch: entry.txt does not match\n")
        return 1
    if gate(raw.decode("utf-8")) is not None:
        sys.stderr.write("read-back gate failed on entry.txt\n")
        return 1

    sys.stdout.write(
        "wrote %s (%d characters)\n" % (path, len(LINE))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
