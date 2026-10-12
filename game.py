import random
import time

# Color Palette (ANSI Escape Codes)
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

ASCII_TITLE = f"""{CYAN}{BOLD}
  _____ _____ ____  __  __ _____ _  _   _    _     
 |_   _| ____|  _ \|  \/  |_   _| || | / \  | |    
   | | |  _| | |_) | |\/| | | | | || || _ \ | |    
   | | | |___|  _ <| |  | | | | |__   _/ ___ \| |___ 
   |_| |_____|_| \_\_|  |_| |_|    |_|/_/   \_\_____|
               D U N G E O N S
{RESET}"""

ASCII_MONSTER = f"""{RED}
      /\\___/\\
     (  o o  )
     (  =^=  ) 
      (------) [BUG MONSTER]
{RESET}"""

ENEMIES = [
    {"name": "Null Pointer Exception", "hp": 25, "atk": 12, "gold": 15},
    {"name": "Memory Leak", "hp": 35, "atk": 15, "gold": 25},
    {"name": "Segmentation Fault", "hp": 50, "atk": 22, "gold": 40},
]


def print_typewriter(text, delay=0.01):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def visit_shop(player):
    print_typewriter(
        f"\n{YELLOW}{BOLD}=== THE DEV SHOP ==={RESET}"
    )
    print(f"Your Gold: {YELLOW}{player['gold']}G{RESET}")
    print("1. Espresso Shot (+25 HP) - 15 Gold")
    print("2. Mechanical Keyboard (+5 Atk) - 30 Gold")
    print("3. Leave Shop")

    choice = input("Select item: ").strip()
    if choice == "1":
        if player["gold"] >= 15:
            player["gold"] -= 15
            player["hp"] = min(100, player["hp"] + 25)
            print_typewriter(
                f"{GREEN}Slurped Espresso! Current HP: {player['hp']}{RESET}"
            )
        else:
            print_typewriter(f"{RED}Not enough gold!{RESET}")
    elif choice == "2":
        if player["gold"] >= 30:
            player["gold"] -= 30
            player["atk"] += 5
            player["inventory"].append("Mechanical Keyboard")
            print_typewriter(
                f"{GREEN}Equipped Mechanical Keyboard! Base Attack increased to {player['atk']}{RESET}"
            )
        else:
            print_typewriter(f"{RED}Not enough gold!{RESET}")
    else:
        print_typewriter("Left the shop.")


def battle(player):
    enemy_data = random.choice(ENEMIES)
    enemy_name = enemy_data["name"]
    enemy_hp = enemy_data["hp"]
    enemy_atk = enemy_data["atk"]
    enemy_gold = enemy_data["gold"]

    print_typewriter(
        f"\n{RED}{BOLD}A wild '{enemy_name}' appears!{RESET}"
    )
    print(ASCII_MONSTER)

    while player["hp"] > 0 and enemy_hp > 0:
        print(
            f"\n{CYAN}Your HP: {player['hp']}{RESET} | {RED}{enemy_name} HP: {enemy_hp}{RESET} | Gold: {YELLOW}{player['gold']}G{RESET}"
        )
        action = (
            input("Choose action [1: Attack, 2: Heal, 3: Inventory, 4: Shop]: ")
            .strip()
        )

        if action == "1":
            damage = random.randint(player["atk"] - 5, player["atk"] + 5)
            enemy_hp -= damage
            print_typewriter(
                f"{GREEN}You hit {enemy_name} for {damage} damage!{RESET}"
            )
        elif action == "2":
            heal = random.randint(15, 25)
            player["hp"] = min(100, player["hp"] + heal)
            print_typewriter(
                f"{GREEN}You patched your code and restored {heal} HP! Current HP: {player['hp']}{RESET}"
            )
        elif action == "3":
            print(f"{YELLOW}Inventory:{RESET} {', '.join(player['inventory'])}")
            continue
        elif action == "4":
            visit_shop(player)
            continue
        else:
            print_typewriter(f"{YELLOW}Invalid input! You stumbled.{RESET}")

        # Enemy counterattack
        if enemy_hp > 0:
            e_damage = random.randint(enemy_atk - 3, enemy_atk + 5)
            player["hp"] -= e_damage
            print_typewriter(
                f"{RED}{enemy_name} strikes back for {e_damage} damage!{RESET}"
            )

    # Resolution
    if player["hp"] <= 0:
        # BUG: Player HP can go negative on death display without proper clamp check
        print_typewriter(
            f"\n{RED}{BOLD}GAME OVER! You were defeated by {enemy_name}. Final HP: {player['hp']}{RESET}"
        )
    else:
        player["gold"] += enemy_gold
        print_typewriter(
            f"\n{GREEN}{BOLD}VICTORY! You defeated {enemy_name} and earned {enemy_gold} Gold!{RESET}"
        )


def main():
    print(ASCII_TITLE)
    print_typewriter("Welcome to the Terminal Dungeons RPG!")

    player = {
        "hp": 100,
        "atk": 20,
        "gold": 20,
        "inventory": ["Debug Tool"],
    }

    while player["hp"] > 0:
        battle(player)
        if player["hp"] > 0:
            cont = input(
                f"\n{CYAN}Do you want to enter the next room? (y/n): {RESET}"
            ).lower()
            if cont != "y":
                print_typewriter("You safely exited the dungeon.")
                break


if __name__ == "__main__":
    main()