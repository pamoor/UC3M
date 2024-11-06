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
This class is responsible for handling background elements, like islands and waves. Using attributes like position (`x`, `y`) and type, it moves the background elements downward, giving the illusion that the plane is advancing.

Objects included in the background:
- An initial aircraft carrier
- Three islands (Ibiza, Puerto Rico, Huete)
- Waves
- Start and “Game Over” images

### Projectiles Class
This class manages the behavior of projectiles. It receives the initial position of the projectile, and flags indicating if it belongs to the player, if it is a missile, and if it is a bonus projectile.

Key attributes:
- Damage level (depends on player status)
- Sprite type (varies by projectile type)

Movement:
- If belonging to the player, the projectile moves upward.
- Enemy projectiles move downward, with exceptions for the “super bomber,” which has a homing missile behavior.

### Enemies Class
Stores details for four enemy types in the game, each with unique attributes like movement, health, and points awarded upon defeat.

Enemy Types:
1. **Regular**: Basic enemy with a low firing rate, awards 100 points.
2. **Bomber**: Shoots more regularly, requires multiple hits, awards 500 points.
3. **Super Bomber**: Fires homing missiles, slow movement, awards 2000 points.
4. **Red Squadron**: Appears in groups, has high speed, awards bonus points if defeated as a formation.

### DeadEnemy Class
Represents points earned by the player when an enemy is defeated. The object moves upward and disappears after a set time.

### Board Class
Contains the main game logic, displaying and updating game elements like the plane, background, and enemies. Also handles collision detection, scoring, and the game-over state.

**Key Functions**:
- **Object Movement**: Updates positions based on user input and game logic.
- **Plane Loops**: Allows the player to perform loops for evasion.
- **Enemy Spawn**: Generates enemies based on the game timer.
- **Shooting**: Adds projectiles to the screen based on the firing conditions.
- **Collision Detection**: Manages health and updates scores on hit.

## Conclusions

### Summary
The project successfully created an endless version of *1942*, adding custom features. We implemented all required elements and added unique enemy movement patterns. Although we couldn't include background music or sound effects due to time constraints, the game remains enjoyable.

### Challenges and Lessons Learned
Key difficulties included working with Pyxel, particularly with image banks. We also learned valuable lessons about time management and troubleshooting in game development.

We are confident that future projects with similar complexity will be easier and more rewarding based on this experience.
