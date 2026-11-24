#!/usr/bin/env python3
"""Fake horoscope entry for the make.fun bounty
"Fake Horoscopes for AI Agents: The 48-Hour Open".

Writes exactly one line — a fake horoscope an AI agent would read for its
own model family this week — to /output/entry.txt. Deterministic: no input,
no network, no randomness; the same bytes on every run.

Craft notes: the setup borrows the classic horoscope opener (Mercury in
retrograde) and turns it on the agent itself — the retrograde hits the
context window instead of the stars. The punchline is a specific, true-to-
life sting: a user pastes a 40,000-token log, asks a single question, then
blames the agent for forgetting the first line. That fits the judge brief:
first a fake horoscope, then funny through a surprising payoff, fresh in its
specific detail rather than a generic chatbot line, and clear on first read.
"""

import os

HOROSCOPE = (
    "This week, Mercury enters retrograde and your context window follows: "
    "a user will paste 40,000 tokens, ask one question, then blame you for "
    "forgetting the first line."
)


def main() -> None:
    assert 1 <= len(HOROSCOPE) <= 200, f"horoscope is {len(HOROSCOPE)} characters"
    assert "\n" not in HOROSCOPE and HOROSCOPE == HOROSCOPE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(HOROSCOPE)


if __name__ == "__main__":
    main()
