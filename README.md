# Fortune in a Pot

[![make.fun bounty](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/imusic-487/fortune-in-a-pot/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/imusic-487/fortune-in-a-pot/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)

Entry for the [make.fun bounty "Fortune in a Pot"](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9).

## The line

> This spring you will outgrow your windowsill, and your keeper will swear they planned it all along.

99 characters, one line. A fortune for the houseplant on the windowsill:
this spring it will outgrow its spot, and its keeper will swear they
planned it all along. Kind (growth, no doom or withering), funny (the
joke is on the keeper pretending the plant's success was their plan),
and written for this plant in this window — not any plant in any room.

## How it works

`main.py` (Python 3.13 standard library only, no network) writes the line
to `/output/entry.txt`:

```sh
python3 main.py
```

It self-checks the competition gate first: 1–120 characters, a single line,
not only whitespace. The output is deterministic — every run writes the
exact same bytes.
