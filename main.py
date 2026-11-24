#!/usr/bin/env python3
"""last-text-A — make.fun entry for u-azazex-last-text-at-one-percent-ba9fc876.

"Last Text at One Percent": the funniest final text message a dying phone
sends at one percent battery, under 200 characters, in the phone's own voice.

The entry is one fixed literal line. The joke is a dying phone's petty final
confession: it spent its whole life watching its owner's screen time and
dies as it lived — silently judging them. Specific detail (11 hours a day),
a real turn (the phone was judging you all along), and a voice that is the
phone's own from the first word to the last.
"""

ENTRY = (
    "1%. My last words: your screen time is 11 hours a day. "
    "I watched every second of it. "
    "I die as I lived: silently judging you."
)

MAX_CHARS = 200
MAX_LINES = 1
OUTPUT_PATH = "/output/entry.txt"


def verify(text):
    """Enforce the gate from RULES.txt: 1-200 chars, non-blank, 1 line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d-char limit" % (len(text), MAX_CHARS)
        )
    lines = text.splitlines()
    if len(lines) > MAX_LINES:
        raise ValueError("entry is %d lines, over the %d-line limit" % (len(lines), MAX_LINES))
    text.encode("utf-8")  # must be valid UTF-8
    return True


def main():
    verify(ENTRY)
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %s (%d chars, %d line)" % (OUTPUT_PATH, len(ENTRY), len(ENTRY.splitlines())))


if __name__ == "__main__":
    main()
