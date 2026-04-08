---
title: "GitLab CipherCube"
date: 2022-12-08
draft: true
tags: ["GitLab", "Security", "brain-teaser"]
summary: "Deciphering the GitLab security team's laser-engraved wooden cipher cube."
---

## Analysis of the GitLab Ciphercube

Shortly after I joined GitLab in Sep 2022, GitLab's security team opened up a Swag intiative for a "laser-engraved cube made from sustainably sourced wood with a message on each side".  
Up for such an offer and challenge, I subscribed and received on the 7th Dec 2022 a small wooden cube.

![CipherCube Portrait](/CyberCube-portrait.jpg 'CipherCube Portrait')

In my lunch break today, 8th Dec 2022, I started to decipher the cube.  
On first glance 1 side showed the [GitLab Tanuki](https://en.wikipedia.org/wiki/Japanese_raccoon_dog) and 5 sides had small shields standing out of the engraving in patterns.

![CipherCube Shield Side](/CyberCube-shield-site-small.jpg 'CipherCube Shild Side')

I inspected those that the shields were structured on each of the fice sides in an 8x8 grid, with the shield giving a clear orientation where the bottom of the grid should be. 8x8 on a side, so one byte per row, 8 byte per side.

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
|  down       | 1   |        |         |
|down         | 2   |        |         |
|down         | 3   |        |         |
|down         | 4   |        |         |
|down         | 5   |        |         |
|  down       | 6   |        |         |
|  down       | 7   |        |         |
|  down       | 8   |        |         |
|-|-|-|-|
|  bottom       | 1   |        |         |
|bottom         | 2   |        |         |
|bottom         | 3   |        |         |
|bottom         | 4   |        |         |
|bottom         | 5   |        |         |
|  bottom       | 6   |        |         |
|  bottom       | 7   |        |         |
|  bottom       | 8   |        |         |
|-|-|-|-|
|  right       | 1   |        |         |
|right         | 2   |        |         |
|right         | 3   |        |         |
|right         | 4   |        |         |
|right         | 5   |        |         |
|  right       | 6   |        |         |
|  right       | 7   |        |         |
|  right       | 8   |        |         |