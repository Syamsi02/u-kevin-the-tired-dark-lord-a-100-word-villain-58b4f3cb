#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

Writes one monologue to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when that variable is set). Pure standard library, fully deterministic:
the same text on every run. The monologue is exactly 100 words.
"""

import os
from pathlib import Path

MONOLOGUE = (
    "Come in. Mind the step \u2014 the third sighs. Never fixed it. "
    "I\u2019m Vey, keeper of the drowned causeway. "
    "Every soul crossing pays in years. "
    "I\u2019ve counted them all: four hundred winters of frozen ink, "
    "heroes at dawn, speeches rehearsed.\n"
    "\n"
    "You want the road. Everyone does. Sign here \u2014 no, there. "
    "The line moves slower than the tide, and the tide keeps its appointments.\n"
    "\n"
    "One day I\u2019ll raise the causeway and drown the kingdoms that forgot my name. "
    "Today the kettle is on, the ledger is heavy, my chair knows my shape. "
    "So sign, cross, and don\u2019t wake the toll."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = MONOLOGUE.strip() + "\n"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
