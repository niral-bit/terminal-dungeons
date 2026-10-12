import random

def start_game():
    player_hp = 100
    enemy_hp = 30
    
    print("=== WELCOME TO TERMINAL DUNGEONS ===")
    print("A wild 'Segmentation Fault' monster appears!\n")
    
    while player_hp > 0 and enemy_hp > 0:
        print(f"Your HP: {player_hp} | Monster HP: {enemy_hp}")
        action = input("Action [1: Attack, 2: Heal]: ")
        
        if action == "1":
            damage = random.randint(10, 20)
            enemy_hp -= damage
            print(f"You hit the monster for {damage} damage!")
        elif action == "2":
            player_hp += 20
            print(f"You healed! Current HP: {player_hp}")
        else:
            print("Invalid command! You stumbled.")

        # Enemy attacks back
        if enemy_hp > 0:
            # BUG: here the enemy_damage take an rand interger between 15 to 1000 
            # Fix take between 15 to 25
            enemy_damage = random.randint(15, 25)
            player_hp -= enemy_damage
            print(f"The monster attacks you for {enemy_damage} damage!\n")


    if player_hp <= 0:
        # Bug 2: Since the player died the hp should be zero
        print(f"You died! Final HP: 0")
    else:
        print("You defeated the Segmentation Fault monster! You win!")

if __name__ == "__main__":
    start_game()
