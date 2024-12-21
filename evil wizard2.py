# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        self.health = min(self.health + 20, self.max_health)  # Heal up to max health
        print(f"{self.name} heals for 20 health! Current health: {self.health}")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power
        self.power_attack_used = False  # Track if power attack has been used

    def power_attack(self, opponent):
        if not self.power_attack_used:
            damage = self.attack_power * 2  # Double the attack power for the special move
            opponent.health -= damage
            print(f"{self.name} uses Power Attack and deals {damage} damage!")
            self.power_attack_used = True
        else:
            print(f"{self.name} cannot use Power Attack again until it cools down.")

    def reset_power_attack(self):
        self.power_attack_used = False  # Reset after a turn


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    def cast_spell(self, opponent):
        spell_damage = self.attack_power * 1.5  # Spell deals 1.5x damage
        opponent.health -= spell_damage
        print(f"{self.name} casts a spell and deals {spell_damage} damage!")


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")


# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)  # Moderate health and attack power

    def shoot_arrow(self, opponent):
        arrow_damage = self.attack_power * 1.8  # Arrow deals 1.8x damage
        opponent.health -= arrow_damage
        print(f"{self.name} shoots an arrow and deals {arrow_damage} damage!")


# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=18)  # High health, moderate attack

    def holy_strike(self, opponent):
        holy_damage = self.attack_power * 2  # Holy strike deals 2x damage
        opponent.health -= holy_damage
        print(f"{self.name} uses Holy Strike and deals {holy_damage} damage!")

    def heal_allies(self, ally):
        ally.health = min(ally.health + 30, ally.max_health)  # Heal ally for 30 health
        print(f"{self.name} heals {ally.name} for 30 health!")


# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                player.power_attack(wizard)
            elif isinstance(player, Mage):
                player.cast_spell(wizard)
            elif isinstance(player, Archer):
                player.shoot_arrow(wizard)
            elif isinstance(player, Paladin):
                player.holy_strike(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")


# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
 

import random


# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        heal_amount = random.randint(10, 30)  # Heal between 10 and 30 health points
        self.health = min(self.health + heal_amount, self.max_health)  # Heal but don't exceed max health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")

    def is_alive(self):
        return self.health > 0


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=30)
        self.power_attack_used = False

    def power_attack(self, opponent):
        if not self.power_attack_used:
            damage = self.attack_power * 2  # Double the damage for power attack
            opponent.health -= damage
            print(f"{self.name} uses Power Attack and deals {damage} damage!")
            self.power_attack_used = True
        else:
            print(f"{self.name} can't use Power Attack again yet.")

    def reset_power_attack(self):
        self.power_attack_used = False  # Reset after a turn


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=40)

    def cast_spell(self, opponent):
        spell_damage = self.attack_power * 1.5  # Spell deals 1.5x damage
        opponent.health -= spell_damage
        print(f"{self.name} casts a powerful spell dealing {spell_damage} damage!")


# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=25)

    def shoot_arrow(self, opponent):
        arrow_damage = self.attack_power * 1.8  # Arrow deals 1.8x damage
        opponent.health -= arrow_damage
        print(f"{self.name} shoots an arrow dealing {arrow_damage} damage!")


# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)

    def holy_strike(self, opponent):
        holy_damage = self.attack_power * 2  # Holy strike deals 2x damage
        opponent.health -= holy_damage
        print(f"{self.name} uses Holy Strike dealing {holy_damage} damage!")

    def heal_ally(self, ally):
        heal_amount = 30
        ally.health = min(ally.health + heal_amount, ally.max_health)
        print(f"{self.name} heals {ally.name} for {heal_amount} health!")


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=20)

    def regenerate(self):
        regenerate_health = 10  # Evil Wizard heals 10 health every turn
        self.health = min(self.health + regenerate_health, self.max_health)
        print(f"{self.name} regenerates {regenerate_health} health!")


# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.is_alive() and player.is_alive():
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                player.power_attack(wizard)
            elif isinstance(player, Mage):
                player.cast_spell(wizard)
            elif isinstance(player, Archer):
                player.shoot_arrow(wizard)
            elif isinstance(player, Paladin):
                player.holy_strike(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.is_alive():
            wizard.regenerate()
            wizard.attack(player)

        if not player.is_alive():
            print(f"{player.name} has been defeated!")
            break

    if wizard.is_alive():
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
    else:
        print(f"{player.name} has fallen in battle.")


# Main function to handle the flow of the game
def main():
    print("Welcome to the Battle Arena!")
    
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()

