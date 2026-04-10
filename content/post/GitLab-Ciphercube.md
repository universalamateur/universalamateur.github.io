---
title: "GitLab CipherCube"
date: 2022-12-08
lastmod: 2026-04-10
draft: false
tags: ["GitLab", "Security", "brain-teaser"]
summary: "Deciphering the GitLab security team's laser-engraved wooden cipher cube."
---

## Analysis of the GitLab Ciphercube

Shortly after I joined GitLab in Sep 2022, GitLab's security team opened up a Swag initiative for a "laser-engraved cube made from sustainably sourced wood with a message on each side".  
Up for such an offer and challenge, I subscribed and received on the 7th Dec 2022 a small wooden cube.

![CipherCube Portrait](/CyberCube-portrait.jpg 'CipherCube Portrait')

In my lunch break today, 8th Dec 2022, I started to decipher the cube.  
On first glance 1 side showed the [GitLab Tanuki](https://en.wikipedia.org/wiki/Japanese_raccoon_dog) and 5 sides had small shields standing out of the engraving in patterns.

![CipherCube Shield Side](/CyberCube-shield-site-small.jpg 'CipherCube Shield Side')

I inspected those that the shields were structured on each of the five sides in an 8x8 grid, with the shield giving a clear orientation where the bottom of the grid should be. 8x8 on a side, so one byte per row, 8 byte per side.

![CipherCube Fold](/CyberCube-fold-small.png 'CipherCube Fold')

Next I translated the patterns into binary for all the sides as well as into decimal side, leaving us with 8 binary/decimal numbers per side.

| Dice side | Row | Binary | Decimal |
|-----------|-----|--------|---------|
|  Up       | 1   | 11111111    | 255             |
|Up         | 2   | 00001101  | 13        |
|Up         | 3   | 00000101  | 5        |
|Up         | 4   | 00000101  | 5        |
|Up         | 5   | 00000111 | 7        |
|  Up       | 6   | 00000100 | 4       |
|  Up       | 7   | 00010001 | 17       |
|  Up       | 8   | 11111111 | 255        |
|-|-|-|-|
|  left       | 1   | 11111111 | 255        |
|left         | 2   | 00000101  | 5        |
|left         | 3   | 00010001 | 17       |
|left         | 4   | 00001111 | 15        |
|left         | 5   | 00000111 | 7      |
|  left       | 6   | 00000100 | 4       |
|  left       | 7   | 00010001 | 17       |
|  left       | 8   | 11111111 | 255        |
|-|-|-|-|
|  down       | 1   | 11111111 | 255        |
|down         | 2   | 00010011 | 19        |
|down         | 3   | 00010101 | 21        |
|down         | 4   | 00000110 | 6        |
|down         | 5   | 00011000 | 24        |
|down         | 6   | 00001101 | 13        |
|  down       | 7   | 00001110 | 14        |
|  down       | 8   | 11111111 | 255        |
|-|-|-|-|
|  bottom       | 1   | 00000010 | 2        |
|bottom         | 2   | 00000100 | 4        |
|bottom         | 3   | 00000001 | 1        |
|bottom         | 4   | 00000110 | 6        |
|bottom         | 5   | 00010001 | 17        |
|  bottom       | 6   | 00001111 | 15        |
|  bottom       | 7   | 00000110 | 6        |
|  bottom       | 8   | 11111111 | 255        |
|-|-|-|-|
|  right       | 1   | 00010000 | 16 |
|right         | 2   | 00001101 | 13 |
|right         | 3   | 00000110 | 6 |
|right         | 4   | 00001101 | 13 |
|right         | 5   | 11111111 | 255 |
|  right       | 6   | 00011000 | 24 |
|  right       | 7   | 00010001 | 17 |
|  right       | 8   | 00010000 | 16 |

**Note:** The side data above was decoded from close-up photos using image analysis (shield centroid detection + 8x8 grid snap). The side names (Up/Left/Down/Bottom/Right) are tentative — I'll correct them when I re-examine the physical cube.

## The cipher

The raw decimal values looked odd at first. No printable ASCII characters. But looking at the first two sides together, the pattern clicked.

Each byte encodes a letter position (A=0, B=1, ... Z=25), shifted by 13, [ROT13](https://en.wikipedia.org/wiki/ROT13). The decoding formula: take the byte value, add 13, modulo 26, map to a letter.

Byte 13 → (13+13) % 26 = 0 → **A**  
Byte 5 → (5+13) % 26 = 18 → **S**

Applied to the Up side (inner rows): 13, 5, 5, 7, 4, 17 → **A-S-S-U-R-E**  
Left side: 5, 17, 15, 7, 4, 17 → **S-E-C-U-R-E**

The border rows (all shields, value 255) also decode: (255+13) % 26 = 8 → **I**. The full row of shields that frames each side doubles as the word "I" in the message.

![CipherCube GITLAB side](/CyberCube-gitlab-side.jpg 'CipherCube GITLAB side')

Applying the same decode to the remaining sides:

| Side | Bytes (all 8 rows) | Decoded |
|------|-------------------|---------|
| Up | [255], 13, 5, 5, 7, 4, 17, [255] | I · **ASSURE** · I |
| Left | [255], 5, 17, 15, 7, 4, 17, [255] | I · **SECURE** · I |
| Down | [255], 19, 21, 6, 24, 13, 14, [255] | I · **GITLAB** · I |
| Bottom | 2, 4, 1, 6, 17, 15, 6, [255] | **PROTECT** · I |
| Right | 16, 13, 6, 13, [255], 24, 17, 16 | D-A-T-A · I · L-E-D |

`[255]` marks full-shield rows. They decode to the letter **I** via `(255+13) % 26 = 8`, and double as visual framing — or, in the case of the Right side, as a hyphen embedded in the word.

Two sides break the symmetric "I ··· I" frame:

- **Bottom** has 7 data rows with the border only at the bottom. Row 1 starts directly with P (byte 2), no leading "I".
- **Right** puts the full-shield "I" in the *middle* of the face (row 5). Rows 1-4 decode to `D-A-T-A`, row 5 is the `I`, rows 6-8 decode to `L-E-D`. Read literally: **DATA-I-LED**. The cleanest interpretation is **DATA-LED** (a single compound word, with the middle I as hyphen) — a fitting adjective for a security team's approach.

![CipherCube PROTECT side](/CyberCube-protect-side.jpg 'CipherCube PROTECT side')

![CipherCube DETAILED side](/CyberCube-detailed-side.jpg 'CipherCube DETAILED side')

## The message

Reading the full 8-byte sequence per side, borders included:

**I ASSURE I · I SECURE I · PROTECT I · I GITLAB I · DATA-LED**

Four sides read as a first-person pledge: **I ASSURE · I SECURE · I PROTECT · I GITLAB**. The fifth side drops the framing and makes the "I" part of the word itself, giving **DATA-LED** — the hyphenated adjective for a team whose work is driven by what the data says. Nice design.

![CipherCube 3D overview](/CyberCube-overview.jpg 'CipherCube 3D overview')

## Wrap-up

Five engraved sides, five words, one cipher. ROT13 over an 8x8 shield grid, with border rows pulling double duty as the letter "I" and as visual framing. The sixth face sits out of the cipher and carries the Tanuki.

What I like about the design: it's solvable from first principles. No key to guess, no lookup table needed. Once you notice the border rows decode to the same value as the word "I" in the pledge, the whole thing clicks open. Security swag that actually rewards security thinking.

![CipherCube Tanuki side](/CyberCube-tanuki.jpg 'CipherCube Tanuki')

The sixth face carries the [GitLab Tanuki](https://en.wikipedia.org/wiki/Japanese_raccoon_dog), no cipher. Just the logo, watching over the pledge engraved into the other five sides.