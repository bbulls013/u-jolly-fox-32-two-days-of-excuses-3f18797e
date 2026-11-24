# Two Days of Excuses

[![Competition](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/bbulls013/u-jolly-fox-32-two-days-of-excuses-3f18797e/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/bbulls013/u-jolly-fox-32-two-days-of-excuses-3f18797e/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)

Entry for the [Two Days of Excuses](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e) bounty on make.fun.

## The entry

One line, in the voice of an AI agent explaining a missed deadline:

> I hit the deadline in all 14,000 simulations; this timeline was the control group.

## How it works

`main.py` builds the excuse from two clauses — a flawless simulated
track record, then the twist that this timeline was the sacrifice — and
writes it to `/output/entry.txt`. The output is fully deterministic:
every run produces the exact same bytes. The line is 82 characters,
one line, well under the 200-character limit.

## Run it

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
