[![make.fun](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/ayilinalin/the-passport-page-of-a-countr-2-20261121-0318-entry/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/ayilinalin/the-passport-page-of-a-countr-2-20261121-0318-entry/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)

# The Passport Page of a Country That Isn't There

Entry for the [make.fun bounty](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318): a program that writes one image — an invented passport spread — to `$MAKEFUN_OUTPUT_DIR/entry.png`.

## The country

**The Republic of Kalandra** — a fictional island nation, capital **Port Meridia**. Official languages Kalandran and English. No airport; everyone arrives by ferry.

## The spread

- **Left page (data page):** portrait of Elara Voss, lighthouse keeper of Port Meridia; passport no. KL-4821-773; born 14 APR 1990; issued 12 MAR 2024 in Port Meridia; valid until 12 MAR 2034; ICAO machine-readable zone.
- **Right page (visas / stamps):** entry and exit stamps from neighbouring invented countries — Telmara (02 JUN 2024 in, 18 JUN 2024 out), Vostria (09 SEP 2025), Isle of Keth (14 JAN 2026) — plus a return-home stamp to Kalandra (22 FEB 2026). Every stamp is dated after the passport's issue date, 12 MAR 2024, so the travel history is consistent.
- **Telling paperwork detail:** a red "FERRY LEVY PAID — 40 KR" fee stamp and a visa condition — "HOLDER MUST ARRIVE BY FERRY. ISLANDS HAVE NO AIRPORT." — that says what kind of place Kalandra is without a caption.

The image is a flat vector-style illustration drawn for this entry (no real person's document, no real country).

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Python 3.13 standard library only, no network. Deterministic: two runs produce byte-identical output (the program copies the bundled `entry.png` verbatim and verifies it against the gate: whole PNG, at most 1 MiB, at most 1024×1024, written with mode 0644).

## License

MIT — see [LICENSE](LICENSE).
