# Legend of Pyronia: A Terminal RPG Adventure
import random
import time

print("🧙‍♂️ Welcome, brave adventurer, to the *Legend of Pyronia!*")
print("Your quest begins in the mysterious Forest of Bugs...\n")

player_name = input("Enter your character's name: ")
hp = 100
potions = 2

print(f"\nGreetings, {player_name}! Your current HP is {hp}. You carry {potions} healing potions.")

while hp > 0:
    print("\nYou hear a rustle in the trees...")
    time.sleep(1)
    enemy = random.choice(["Goblin", "BugBear", "Syntax Serpent"])
    enemy_hp = random.randint(30, 60)
    print(f"A wild {enemy} appears with {enemy_hp} HP!")

    while enemy_hp > 0:
        print("\nWhat will you do?")
        print("1. Attack")
        print("2. Block")
        print("3. Heal")
        action = input("Choose an action (1/2/3): ")

        if action == "1":
            dmg = random.randint(10, 25)
            enemy_hp -= dmg
            print(f"You strike the {enemy} for {dmg} damage!")
        elif action == "2":
            print("You brace yourself for the next attack!")
        elif action == "3":
            if potions > 0:
                heal = random.randint(15, 30)
                hp += heal
                potions -= 1
                print(f"You drink a potion and recover {heal} HP! Potions left: {potions}")
            else:
                print("You're out of potions!")
        else:
            print("Invalid choice! You stumble and do nothing...")

        if enemy_hp > 0:
            if action == "2":
                dmg = random.randint(5, 10)
            else:
                dmg = random.randint(10, 20)
            hp -= dmg
            print(f"The {enemy} attacks you for {dmg} damage! Your HP: {hp}")

        if hp <= 0:
            print("\n☠️ You have fallen in battle... Pyronia will remember your bravery.")
            break

    if hp > 0:
        print(f"\n🎉 You defeated the {enemy}!")
        choice = input("Do you want to continue your adventure? (yes/no): ").lower()
        if choice != "yes":
            break

print(f"\n🛡️ {player_name}, your journey ends here. Final HP: {hp}. Thank you for playing!")
