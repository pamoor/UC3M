---
title: "Project README - 1942 Game Version"
author: "Álvaro Carrasco & Pablo Amor"
output: github_document
---

# Final Project: 1942

**Group 81**  
**Degree in Computer Engineering, UC3M**  
Created by Álvaro Carrasco and Pablo Amor  

## Table of Contents
- [Project Summary](#project-summary)
- [Classes and Components](#classes-and-components)
    - [Plane Class](#plane-class)
    - [Background Class](#background-class)
    - [Projectiles Class](#projectiles-class)
    - [Enemies Class](#enemies-class)
    - [DeadEnemy Class](#deadenemy-class)
    - [Board Class](#board-class)
- [Conclusions](#conclusions)

## Project Summary
We aimed to create a version of the classic game *1942*, adding some elements and features. The main objective is to achieve the highest score possible before running out of lives. The player controls a plane that can shoot and dodge enemy projectiles. Enemies appear randomly, each with unique movement and shooting patterns, requiring the player to adapt strategies.

The background features islands and waves generated randomly, enhancing visual appeal.

## Classes and Components

### Plane Class
Defines the properties and methods for the player-controlled plane. Includes attributes for position, speed, lives, loops, shooting rate, invulnerability status, and animation states.

Key methods:
- **Move**: Moves the plane based on direction.
- **Helices**: Alternates propeller sprites.
- **Loop**: Animates a flip, setting "loop" attribute to False after completion.
- **Impact**: Activates invulnerability and explosion animation.
- **Death**: Animates the plane's destruction, ending the game.

### Background Class
Handles background elements, such as islands and waves. Creates movement for these objects, enhancing the sense of forward motion.

### Projectiles Class
Manages projectile behavior, including direction, speed, and type (e.g., missile, bonus projectile). The `move` method defines the trajectory.

### Enemies Class
Defines four enemy types, each with unique attributes like movement pattern, health, and point values.

### DeadEnemy Class
Represents the points awarded upon enemy destruction, moving upward and disappearing after a set time.

### Board Class
The most comprehensive class, handling game state, object positioning, collisions, and scorekeeping. Includes animations for each object and displays scores and remaining lives.

## Conclusions
### Summary
The project successfully created an endless version of *1942*, adding our custom features. Implementing enemy movement patterns was challenging but rewarding. Though we couldn't include background music or sound effects, the game remains engaging.

### Challenges and Lessons Learned
We encountered difficulties with Pyxel, especially with image banks, and learned the value of time management. Future projects would likely be easier with this experience.
