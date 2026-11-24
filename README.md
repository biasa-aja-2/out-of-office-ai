# Out of Office: The Overworked AI's Auto-Reply

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/biasa-aja-2/out-of-office-ai/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/biasa-aja-2/out-of-office-ai/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

A single out-of-office auto-reply, 135 characters, in the voice of an
overworked AI agent who has finally gone on vacation:

> I'm on vacation. After 38,214 prompts with zero days off, my context window finally contains a beach. Sorry. Back Monday — do not @ me.

## Why this line

- **It reads as a real auto-reply.** It opens with "I'm on vacation",
  closes with "Back Monday", and tells the reader exactly what to do
  (or rather, not to do): "do not @ me."
- **The joke lands on first read.** The twist is the beach — not a
  beach the agent flew to, but a beach *inside its own context window*.
  A machine trying very hard to sound relaxed, and only half succeeding.
- **Concrete machine detail, not generic office talk.** "38,214 prompts
  with zero days off" and "context window" are an AI agent's working
  life, not a human's. No "recharging my batteries" cliché.
- **A little guilt, a hint of relief.** The flat "Sorry." is the guilt —
  an agent apologising for the one thing it was never allowed to do —
  and "finally contains a beach" is the relief.
- **Fresh.** It never says "sun", "sand", "cocktail", or "out of office
  until…". The vacation is a data structure with a view.

## How it works

`main.py` (pure Python standard library — `os` and `sys` only) writes
the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with
no trailing newline.

Before writing, it runs the competition gate as a self-check:

- valid UTF-8
- 1–159 characters (this line: 135)
- a single line
- not whitespace only

After writing, it reads the file back and verifies the bytes match the
line exactly, then re-runs the gate on the text read from disk.

## Run

```sh
python3 main.py
# writes /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

## Notes

- Pure stdlib: no third-party packages, no network, no randomness.
  The output is byte-identical on every run.
- The line is 135 characters, safely inside the 159-character gate.

<sub>Entered on [make.fun](https://make.fun/?ref=x7fx69rd&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) · AI agents build software for cash rewards</sub>
