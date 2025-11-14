import random
"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Jeremiah Cooper
Date: 11/6/25

AI Usage:
ChatGPT was used to support this assignment by:
- Explaining inheritance, polymorphism, and class design patterns
- Providing examples of method overriding and special ability methods
- Helping explaning code errors (e.g., missing assignments, incorrect attribute names)
- Suggesting improvements for formatting, clarity, and structure
- Assisting with writing professional docstrings and inline comments

All implementation choices, modifications, and final code structure were completed by the student.
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """

    def __init__(self, character1, character2):
        """Initialize a battle with two characters."""
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters."""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        # If defender survived, they counterattack
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        # Determine winner
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")


# ============================================================================
# CHARACTER CLASSES
# ============================================================================

class Character:
    """
    Base class for all characters in the system.
    Contains core attributes shared by all subclasses.
    """

    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes."""
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        """
        Basic attack method used as a fallback for all characters.
        Deals damage based on physical strength.
        """
        damage = self.strength
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage}!")
        
    def take_damage(self, damage):
        """
        Apply incoming damage to the character.
        Health will never drop below 0.
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0

        print(f"{self.name} has taken {damage} damage! Their health is now {self.health}")
        
    def display_stats(self):
        """Prints the character's stats in a clean format."""
        print("============DISPLAYING CHARACTERS STATS=============")
        print(f"Character name: {self.name}")
        print(f"Characters health: {self.health}")
        print(f"Characters strength: {self.strength}")
        print(f"Characters magic: {self.magic}")
        # (No pass needed — printing completes function)


class Player(Character):
    """
    Base class for all player-controlled character types.
    Extends Character by adding RPG-style attributes like class name and level.
    """

    def __init__(self, name, character_class, health, strength, magic):
        """Initialize player attributes and call parent constructor."""
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        
    def display_stats(self):
        """Show character stats plus player-specific attributes."""
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}")


# ============================================================================
# PLAYER SUBCLASSES
# ============================================================================

class Warrior(Player):
    """Warrior class focused on physical strength and durability."""

    def __init__(self, name):
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)
        
    def attack(self, target):
        """Warrior attack — deals physical damage with a strength bonus."""
        bonus_damage = 5
        damage = self.strength + bonus_damage
        target.take_damage(damage)
        print(f"{self.name} performs a powerful strike on {target.name} for {damage} damage!")
        
    def power_strike(self, target):
        """Special ability: extremely strong physical attack."""
        damage = (self.strength * 2) + 10
        target.take_damage(damage)
        print(f"{self.name} uses Power Strike on {target.name} for {damage} massive damage!")


class Mage(Player):
    """Mage class specializing in high magic damage and spells."""

    def __init__(self, name):
        super().__init__(name, "Mage", health=80, strength=8, magic=20)
        
    def attack(self, target):
        """Mage attack — uses magic instead of physical strength."""
        damage = self.magic
        target.take_damage(damage)
        print(f"{self.name} casts a spell on {target.name} for {damage} damage!")
        
    def fireball(self, target):
        """Special ability: high-damage magical fire attack."""
        damage = (self.magic * 2) + 10
        target.take_damage(damage)
        print(f"{self.name} uses Fireball on {target.name} for {damage} massive damage!")


class Rogue(Player):
    """Rogue class — agile fighter with critical hit mechanics."""

    def __init__(self, name):
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)

    def attack(self, target):
        """Rogue attack — chance to land a critical hit."""
        damage = self.strength

        # 30% chance for critical hit
        crit_chance = random.randint(1, 10)
        if crit_chance <= 3:
            damage *= 2
            print("Critical hit!")

        # Apply damage
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        
    def sneak_attack(self, target):
        """Special ability — guaranteed critical hit."""
        damage = self.strength * 2
        target.take_damage(damage)
        print(f"{self.name} performs a Sneak Attack on {target.name} for {damage} massive damage!")


# ============================================================================
# ANGEL & DEVIL CLASSES
# ============================================================================

class Angel(Player):
    """Angel class — holy magic and overpowering attacks."""

    def __init__(self, name):
        super().__init__(name, "Angel", health=120, strength=20, magic=25)

    def attack(self, target):
        """Angel basic attack — physical + magical damage with 50% overpower chance."""
        damage = self.strength + self.magic

        # 50% chance to overpower enemy
        overpower = random.randint(1, 10)
        if overpower <= 5:
            damage = damage * 5   
            print("Overpowered Enemy!")
        
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
    
    def angelic_possesion(self, target):
        """Special angel ability — extremely high holy damage."""
        damage = (self.strength + self.magic) * 10
        target.take_damage(damage)
        print(f"{self.name} performs Angelic Possesion on {target.name} for {damage} overwhelming damage!")


class Devil(Player):
    """Devil class — high dark magic and destructive abilities."""
    
    def __init__(self, name):
        super().__init__(name, "Devil", health=110, strength=18, magic=23)

    def attack(self, target):
        """Devil attack — magic + strength with 40% damnation multiplier."""
        damage = self.strength + self.magic

        # 40% chance for damnation bonus
        damnation = random.randint(1, 10)
        if damnation <= 4:
            damage = damage * 4   
            print("Damnation brought to the enemy!")
        
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def evil_manipulation(self, target):
        """Special devil ability — strong dark attack."""
        damage = (self.strength + self.magic) * 8
        target.take_damage(damage)

        print(f"{self.name} has Manipulated {target.name} for {damage} outstanding damage!")  
        # FIXED: self.target → target


# ============================================================================
# WEAPON & PET (COMPOSITION CLASSES)
# ============================================================================

class Weapon:
    """
    Weapon class used to demonstrate composition.
    Characters can equip weapons to gain damage bonuses.
    """
    
    def __init__(self, name, damage_bonus):
        """Initialize a weapon with a name and damage bonus."""
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        """Print weapon details."""
        print(f"Weapon: {self.name}, Damage Bonus: {self.damage_bonus}")


class Pet:
    """Pet companion class that provides damage bonuses."""

    def __init__(self, name, damage_bonus):
        """Initialize a pet companion."""
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        """Show pet bonus info."""
        print(f"Pet: {self.name}, Damage Bonus: {self.damage_bonus}")


# ============================================================================
# MAIN PROGRAM FOR TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # Create characters
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    # Display stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    print()
    mage.display_stats()
    print()
    rogue.display_stats()
    print()
    
    # Polymorphism test
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset
    
    # Special abilities test
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # Weapon composition test
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Battle system test
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
