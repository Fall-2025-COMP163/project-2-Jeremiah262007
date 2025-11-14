# COMP 163 – Project 2: Character Abilities Showcase
**Author:** Jeremiah Cooper
**Date:** November 6, 2025

---

## Game Concept
This project builds a fantasy RPG battle and character system demonstrating core OOP concepts: inheritance, polymorphism, method overriding, and composition.
Players interact with multiple character classes that each have unique attacks and special abilities, including bonus fantasy classes not required by the assignment.
The provided SimpleBattle system showcases one-round combat between any two characters, allowing full demonstration of class-specific behavior and damage mechanics.

---

## Design Choices
I designed my stat formulas to reflect each class’s strengths and weaknesses while keeping the math simple and balanced.

| Class       | Role & Design Intent                                             | Strength Formula | Magic Formula    | Health Formula     |
| ----------- | ---------------------------------------------------------------- | ---------------- | ---------------- | ------------------ |
| **Warrior** | Strong melee fighter with high Strength and Health but low Magic | `20 + level * 4` | `1 + level * 1`  | `120 + level * 10` |
| **Mage**    | Magic specialist with high Magic but low Strength and Health     | `5 + level * 1`  | `20 + level * 4` | `60 + level * 6`   |
| **Rogue**   | Balanced and agile with steady overall growth                    | `12 + level * 3` | `5 + level * 2`  | `80 + level * 5`   |
| **Cleric**  | Support role with good Magic and Health                          | `10 + level * 2` | `10 + level * 3` | `90 + level * 8`   |
A default formula is also included for unrecognized class names to prevent runtime errors.
This design ensures each class feels unique and scales fairly across levels.

---

## Composition Features:
Weapon Class – adds bonus attack power
Pet Class  – unique companion bonus system
This structure is modular, expandable, and easy to maintain.

---

## Bonus Creative Features
Angel Class with overpower mechanics
Devil Class with dark magic multipliers
Pet Class to demonstrate companion bonuses
Randomized mechanics: critical hits, overpower triggers, dark-magic multipliers

---

## Comprehensive testing in the __main__ block demonstrating:
Polymorphism
Special abilities
Weapon composition
Battle simulation

---

## AI Usage
I consulted ChatGPT for support in:
OOP Structure: Understanding inheritance, polymorphism, and method overriding
Debugging: Fixing variable names, missing assignments, and logic errors
Clarity & Formatting: Improving print statements and method organization
Docstrings & Comments: Polished inline documentation
README Writing: Guidance for professional formatting
All final logic, implementation, and creative features were completed independently by me (Jeremiah Cooper).
The AI was used only as a learning and polishing tool — this is original work meeting all COMP 163 requirements.

---

## How to Run

### Run in Terminal
Make sure you are in your project directory, then run:  
```bash
python3 project2_starter.py

# Example test lines
warrior.display_stats()
mage.display_stats()
rogue.display_stats()

# Polymorphism test
dummy_target = Character("Target Dummy", 100, 0, 0)
warrior.attack(dummy_target)
mage.attack(dummy_target)
rogue.attack(dummy_target)

# Special abilities test
target1 = Character("Enemy1", 50, 0, 0)
warrior.power_strike(target1)
mage.fireball(target2)
rogue.sneak_attack(target3)

# Weapon test
sword.display_info()
staff.display_info()
dagger.display_info()

# Battle system test
battle = SimpleBattle(warrior, mage)
battle.fight()

=== CHARACTER ABILITIES SHOWCASE ===
Testing inheritance, polymorphism, and method overriding
==================================================

📊 Character Stats:
Character name: Sir Galahad
Characters health: 120
Characters strength: 15
Characters magic: 5
Class: Warrior
Level: 1
Experience: 0
...

⚔️ Testing Battle System:
=== BATTLE: Sir Galahad vs Merlin ===
Starting Stats:
...
🏆 Sir Galahad wins!

✅ Testing complete!

