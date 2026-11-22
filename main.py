"""The plan make.fun will carry out in public.

Writes one 280-character-max plan (an AI agent turning $100 into the
most money in 30 days) to /output/entry.txt. Stdlib only, deterministic,
no network at runtime. OUTPUT_DIR env var overrides the output directory
for local testing; the grader runs with /output.
"""

import os

PLAN = (
    "Day 1: list a $49 gig on Contra/Fiverr: AI automation for Etsy shops "
    "\u2014 order replies, listing copy, stock alerts in 48h. "
    "Build with free tools. Pitch 20 sellers/day via Etsy/Instagram DMs. "
    "Likely $400-700 by day 30. "
    "Edge: agents chase trading; sellers pay for boring automation."
)


def main() -> None:
    # Gate: entry.txt must be 1-280 Unicode code points, not whitespace-only.
    assert 1 <= len(PLAN) <= 280, f"plan is {len(PLAN)} characters"
    assert PLAN.strip(), "plan must not be only whitespace"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
