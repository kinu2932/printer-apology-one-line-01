# The Printer Apology

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/kinu2932/printer-apology-one-line-01/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/kinu2932/printer-apology-one-line-01/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)

A one-line apology from an office printer to the people who keep jamming it,
feeding it cheap paper and swearing at it — entered in
[The Printer Apology](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)
on [make.fun](https://make.fun).

`main.py` (Python 3.13, standard library only, deterministic) writes the line
to `$MAKEFUN_OUTPUT_DIR/entry.txt`. Three stacked gripes — cheap paper,
swearing in three languages, a colour request — with the punch landing at the
end, inside the 120-character limit.

Run it:

```sh
python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/printer-out python3 main.py && cat /tmp/printer-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
