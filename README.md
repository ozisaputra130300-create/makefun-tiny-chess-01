# makefun-tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/GITHUB_OWNER/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/GITHUB_OWNER/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A compact chess engine in 4,055 bytes of Python (standard library only). Negamax with alpha-beta pruning, quiescence search on captures (with full check evasions), MVV-LVA move ordering, piece-square tables, and iterative deepening to a fixed 100,000-node budget per move. Fully deterministic — no wall clock, no unseeded randomness. Plays the make.fun tiny-chess-01 house gauntlet through the env HTTP API. Practice-trial Elo: trial 0 = 1,191 (1W 3D 2L), trial 1 = 1,099 (0W 4D 2L), trial 2 = 997 (0W 3D 3L); mean ~1,096, just below the 1,154 floor to enter the final (trial 0 alone cleared it). Note: the engine does not castle (a size trade-off) and can draw by repetition in even positions.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 -P -s main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=sy0tw1m4&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
