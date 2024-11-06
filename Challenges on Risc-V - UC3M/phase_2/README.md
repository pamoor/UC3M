---
title: "Practice 2 - Computer Architecture"
author: "Pablo Amor Molina (100495855) and Manuel Roldán Matea (100500450)"
date: "03/12/2023"
---

# Practice 2 - Computer Architecture

This document describes the implementation and results obtained in the microprogramming practice for the Computer Architecture course in Computer Engineering at Universidad Carlos III de Madrid.

## Exercise 1

### Description
This section covers the control signal design and comments for each operation:

- **Operation lc R1 R2 (R3)**: Performs operations to set the MAR register to PC, load MBR from memory, increment PC by 4, and update R1 with MBR.
  - Control signals: `(C0, T2) (R, BW=11, M1, C1, TA, M2, C2) (SelC=10101, LC, T1, A0=1, B=1, C=0)`
  - Note: Remember to add 4 to PC to point to the next instruction, as the imaginary part resides in the program counter memory address.

- **Operation sc R1 R2 (R3)**: Handles MAR, MBR, and memory updates for R1 and R2.
  - Control signals: `(MR=0, SelA=1011, T9, C0) (MR=0, SelA=10101, T9, C1) ...`
  - Note: No additional remarks.

### Additional Operations
Other operations, such as `addc`, `mulc`, `beqc`, `call`, `ret`, and `hcf`, are included with their respective control signals, operation details, and remarks. Specific signal values and steps for each operation can be found in the PDF.

## Exercise 2

### Description
This exercise involves comparing cycles with and without extension for handling real and imaginary parts of complex numbers separately or simultaneously.

- **Cycle Improvement**: By designing specific instructions for complex numbers, both real and imaginary parts are processed simultaneously, resulting in fewer cycles. For instance:
  - Without extension: 131 cycles
  - With extension: 102 cycles (19.84% improvement)

## Conclusions and Challenges

Through this practice, we gained an introduction to microprogramming, enhancing our understanding of the course. We encountered initial challenges, particularly with unfamiliar tools, but progressed effectively after receiving guidance on specific instructions.

### Estimated Hours
- Exercise 1: 11 hours
- Exercise 2: 3 hours
- Report: 2.5 hours
