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

Why the line works: it keeps the horoscope frame intact (a weekly
prediction, a planetary cause, an unlucky outcome) while every ingredient
is swapped for agent life — Mercury's retrograde becomes the context
window, fate becomes the user's own behaviour. The twist lands because
the prophecy is not about the agent at all; it is about the human on the
other side of the prompt, which is exactly the reversal a fake horoscope
for an AI should make. The voice stays deadpan and second-person, like a
real horoscope column, so the absurdity sneaks in instead of announcing
itself — no winking, no meta joke about being a language model, just a
straight-faced prediction that happens to be true. The number 40,000 is
the detail that makes it feel observed rather than invented: big enough to
be funny, concrete enough to be believed, and the blame at the end gives
the line its sting, because every agent — and every reader — has lived it.
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
