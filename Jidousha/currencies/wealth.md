---
type: currency
id: wealth
status: drafted
confidence: played
last-reviewed: 2026-08-29
tags: [conf/played]
---
# Wealth
Held by the player (treasury) and every character (wallet). Dual role:
currency and motivator. Gold-only v1.

**The flow map (decided 2026-08-29)**: mint at sources, burn at sinks,
conserved between holders; every port named here.
- **Mints**: site quest pots (-> treasury, per treasury-margin); the
  generic industry's wages (-> worker wallets).
- **Treasury-margin (M2)**: pots land in the treasury; promised shares
  pay out to wallets; the remainder is the player's primary income —
  the player as contractor; the payout dialog shows pot/shares/margin
  from the sim's own numbers.
- **Conserved transfers**: wages/shares (treasury -> wallets);
  petition rewards (petitioner wallet -> satisfier — poor petitioners
  pay in regard); petition gifts (treasury -> wallet).
- **Burns**: upkeep (wallets; trait-modulated); industry construction
  (treasury); declared petition consequences where stated.
- **Levy knob (M4)**: per-industry cut to treasury — drawer constant,
  **default 0**; passive income is upgraded into, not given.
- **Guard (M6)**: economy sweeps (see [[needs]]).

Variant on the table: a true circular economy (upkeep flows to shops,
goods, prices) — one-module experiment, not v1.

Open: starting balances (scenario data) · denominations/intervals
(drawer).
