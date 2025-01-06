import random

def cast_spell(spell, enemy):
  damage = {
    "fireball": {"goblin": 20, "troll": 10, "dragon": 5},
    "thunder": {"goblin": 5, "troll": 20, "dragon": 10},
    "tidal wave": {"goblin": 10, "troll": 5, "dragon": 20}
  }
  return damage[spell][enemy]

def encounter_enemy():
  enemies = ["goblin", "troll", "dragon"]
  return random.choice(enemies)

def choose_direction():
  print("\nYou've reached a crossroad. Which way do you want to go?")
  return input("Enter 'left', 'right', or 'forward': ").lower().strip()

def find_potion():
  return random.random() < 0.3  # 30% chance to find a potion
def play_game():
  print("Welcome, wizard! You're trapped in a labyrinth full of enemies and treasures.")
  print("Your goal is to reach the end and find the last treasure.")
  print("You have three spells: fireball, thunder, and tidal wave.")
  health = 100
  treasures = 0
  potions = 0
  rooms = 0
  max_rooms = 15
  while rooms < max_rooms:
    rooms += 1
    print(f"\n--- Room {rooms} ---")
    if find_potion():
      potions += 1
      print(f"You found a healing potion! You now have {potions} potion(s).")
    direction = choose_direction()
    if direction not in ['left', 'right', 'forward']:
      print("Invalid direction. Moving forward by default.")
    if random.random() < 0.7:  # 70% chance to encounter an enemy
      enemy = encounter_enemy()
      print(f"You encounter a {enemy}!")
      while True:
        action = input("Do you want to 'fight' or 'run'? ").lower().strip()
        if action == 'run':
          if random.random() < 0.5:  # 50% chance to escape
            print("You managed to escape!")
            break
          else:
            print("You couldn't escape. You must fight!")
        if action == 'fight':
          spell = input("Cast a spell (fireball/thunder/tidal wave): ").lower().strip()
          if spell in ["fireball", "thunder", "tidal wave"]:
            damage = cast_spell(spell, enemy)
            print(f"You cast {spell} and deal {damage} damage!")
            if damage >= 15:
              print(f"You defeated the {enemy}!")
              treasures += 1
              print(f"You found a treasure! Total treasures: {treasures}")
              break
            else:
              health -= 10
              print(f"Your spell wasn't very effective. You take 10 damage. Health: {health}")
              if health <= 0:
                print("You have been defeated. Game over!")
                return
          else:
            print("Invalid spell. Try again.")
        if health < 50 and potions > 0:
          use_potion = input("Your health is low. Do you want to use a healing potion? (yes/no) ").lower().strip()
          if use_potion == 'yes':
            health = min(100, health + 30)
            potions -= 1
            print(f"You used a potion. Your health is now {health}. Remaining potions: {potions}")
  print("\nCongratulations! You've reached the end of the labyrinth!")
  print(f"You collected {treasures} treasures and finished with {health} health.")

answer = input("Would you like to play a game? (yes/no) ")

if answer.lower().strip() == "yes":
  play_game()
else:
  print("That's too bad!")
