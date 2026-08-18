import time
import sys
import random
import fish
#___________________________________________________________________________________________________
fish_inventory = []
item_inventory = []
game_time = 7
time_period = "Morning"
fish_away = False
money = 100
fishing_level = 1
fishing_zone = "Teddy Creek"
whaley_achievement = False
butter_quest = False
food_creek_unlocked = False
beary_triangle_achievement = False
beary_triangle_quest = False
junk_food_ocean_unlocked = False
weather = "Clear"
#___________________________________________________________________________________________________
def typewriter(text, base_speed=0.04, pause_chance=0.2, pause_duration=0.3, punct_pause=0.6):
    words = text.split(' ')
    punctuation = ".!?,"
    
    for i, word in enumerate(words):
        for char in word:
            sys.stdout.write(char)
            sys.stdout.flush()
 
            time.sleep(random.uniform(0.01, 0.1)) 
        
        last_char = word[-1] if word else ""
        
        if i < len(words) - 1:
            sys.stdout.write(' ')
            sys.stdout.flush()
            

            if last_char in punctuation:
                time.sleep(punct_pause)
            

            elif random.random() < pause_chance:
                time.sleep(pause_duration)
            else:
                time.sleep(0.01) 
    print()



def typewriter1(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # New line after text

def update_time(game_time):
    if game_time >= 6 and game_time < 12:
        return "Morning"

    elif game_time >= 12 and game_time < 18:
        return "Afternoon"

    elif game_time >= 18 and game_time < 21:
        return "Evening"

    else:
        return "Night"



#___________________________________________________________________________________________________
rarities = ["common", "uncommon", "rare", "epic", "legendary"]
rarity_chances = [65, 30, 4, 0.9, 0.1]

weathers = {
    "Clear"
    "Rainy"
    "Dry"
    "Storm"
    "Wet"
}

tackle_chances = {
    0: 0,
    1: 50,
    2: 75,
    3: 85,
    4: 95,
}

fish_prices = {
    "common": 5,
    "uncommon": 10,
    "rare": 15,
    "epic": 25,
    "legendary": 50
}

bait_prices = {
    "Whiteteddy Bait": 150,
    "ButterDoggy Bait": 300,
    "Teddy Bait": 500
}

bait_bonus = {
    "Whiteteddy Bait": 1,
    "ButterDoggy Bait": 2,
    "Teddy Bait": 3
}

zones = [
    "Teddy Creek",
    "Food Creek",
    "Junk Food Ocean",
]

fish_drops = {
    "Butter Doggy": {"item": "Butter", "chance": 15},
    "Teddy": {"item": "Teddy Fur", "chance": 25},
    "Beary Triangle": {"item": "Beary Triangles", "chance": 50},
}



#___________________________________________________________________________________________________

#intro
typewriter1("You arrive at the lake.")
typewriter1("The water is quiet. There is no one else around.")
typewriter1("You have a fishing rod, and little else.")
typewriter1("")
typewriter1("Available commands:")
typewriter1("fish - Fish in your current zone")
typewriter1("inventory - View your inventory")
typewriter1("shop - Visit the shop")
typewriter1("zone - Change your fishing zone")
typewriter1("help - View available commands")
typewriter1("pass time - Passes time, doesn't pass weather")
typewriter1("workshop - Visit the workshop at night")
typewriter1("quit - Exit the game")
typewriter1("")
player_name = input("What is your name? ")

#__________________________________________________________________________________________________

while True:
    command = input("> ").strip().lower()

    if game_time >= 23:
        game_time = 0

    if command == "fish" or command == "f":
        current_fishing_level = fishing_level

        # Use bait if you have some
        for bait in item_inventory:
            if bait in bait_bonus:
                current_fishing_level += bait_bonus[bait]
                item_inventory.remove(bait)
                break

        game_time += 1
        time_period = update_time(game_time)

        rarity = random.choices(rarities, weights=rarity_chances)[0]

        # Only choose fish that exist in the current zone
        matching_fish = [
            f for f in fish.all_fish
            if f.rarity == rarity and zones.index(fishing_zone) in f.zones
        ]

        if matching_fish:
            chosen_fish = random.choice(matching_fish)

            escape_time = max(7, random.uniform(chosen_fish.weight, chosen_fish.weight * 2))

            start_time = time.time()

            difficulty = chosen_fish.difficulty - current_fishing_level + 1

            if difficulty < 0:
                difficulty = 0

            # Make sure difficulty exists in tackle_chances
            if difficulty > max(tackle_chances):
                difficulty = max(tackle_chances)

            tackle_chance = tackle_chances[difficulty]

            progress = 0

            while progress < 100:

                if time.time() - start_time >= escape_time:
                    print("The fish got away!")
                    fish_away = True
                    break

                progress += random.randint(0, 35)

                if progress > 100:
                    progress = 100

                if random.random() < tackle_chance / 100:
                    progress -= random.randint(5, 15)

                    if progress < 0:
                        progress = 0

                print(
                    f"[{'█' * (progress // 5)}"
                    f"{'░' * (20 - progress // 5)}]"
                )

                time.sleep(0.4)

            if fish_away == False:
                fish_inventory.append(chosen_fish)

                chosen_fish.weight = random.uniform(
                    chosen_fish.min_weight,
                    chosen_fish.max_weight
                )

                print(f"You caught a {chosen_fish.name}!")
                print(f"Weight: {chosen_fish.weight:.2f} kg")
                print(f"Rarity: {chosen_fish.rarity}")

                if chosen_fish.name == "Junk Fish":
                    typewriter("You actually did it and wasted that much time?")
                    typewriter("Wow. Well anyway you finished the game congrats blah blah thank you for playing.")
                    typewriter("Prob more updates.")
                    typewriter("soon ofc.")

                if chosen_fish.name == "Chicky Nuggets" and not beary_triangle_achievement:
                    beary_triangle_achievement = True
                    beary_triangle_quest = True


                    print("________ QUEST UNLOCKED ________")
                    print("A new challenge awaits at the workshop.")

                if chosen_fish.name == "Whaley" and not whaley_achievement:
                    whaley_achievement = True
                    butter_quest = True

                    print()
                    print("________ ACHIEVEMENT ________")
                    print("RIP Whaley")
                    print("You caught a Whaley!")
                    print()
                    print("________ QUEST UNLOCKED ________")
                    print("Collect 5 Butter.")
                    print("Return to the workshop when you have enough.")

                # Fish drops
                # Only fish listed in fish_drops can drop items
                if chosen_fish.name in fish_drops:
                    drop = fish_drops[chosen_fish.name]

                    if random.randint(1, 100) <= drop["chance"]:
                        item_inventory.append(drop["item"])
                        print(f"You found a {drop['item']}!")

            fish_away = False
            print(f"Time: {game_time}:00")

    elif command == "inventory" or command == "i":
        fish_counts = {}

        for caught_fish in fish_inventory:
            if caught_fish.name in fish_counts:
                fish_counts[caught_fish.name] += 1
            else:
                fish_counts[caught_fish.name] = 1

        print("Fish:")

        for name, amount in fish_counts.items():
            print(f"{name} x{amount}")

        print(f"Money: ${money}")

        print("Items:")

        if item_inventory:
            item_counts = {}

            for item in item_inventory:
                if item in item_counts:
                    item_counts[item] += 1
                else:
                    item_counts[item] = 1

            for item, amount in item_counts.items():
                print(f"{item} x{amount}")
        else:
            print("No items.")

    elif command == "shop":
        if time_period == "Morning" or time_period == "Afternoon":
            typewriter(
                f"G'day {player_name}! Got any fish today, mate? "
                "Come on in and see what we've got."
            )

            print(f"Money: ${money}")
            print("[1] Bait")
            print("[2] Sell")
            print("[3] Leave")

            shop_choice = input("> ")

            if shop_choice == "1":
                print("Bait")
                print("[1] Whiteteddy Bait - $150")
                print("[2] Butterdoggy - $300")
                print("[3] Teddy Bait - $500")
                print("[4] Leave")

                bait_choice = input("> ")

                if bait_choice == "1":
                    price = bait_prices["Whiteteddy Bait"]

                    if money >= price:
                        money -= price

                        for _ in range(25):
                            item_inventory.append("Whiteteddy Bait")

                        print("You bought 25 Whiteteddy Bait!")
                        print(f"Money: ${money}")

                    else:
                        print("Sorry mate, but you don't have enough money.")

                elif bait_choice == "2":
                    price = bait_prices["ButterDoggy Bait"]

                    if money >= price:
                        money -= price

                        for _ in range(25):
                            item_inventory.append("ButterDoggy Bait")

                        print("You bought 25 ButterDoggy Bait!")
                        print(f"Money: ${money}")

                    else:
                        print("Sorry mate, but you don't have enough money.")

                elif bait_choice == "3":
                    price = bait_prices["Teddy Bait"]

                    if money >= price:
                        money -= price

                        for _ in range(25):
                            item_inventory.append("Teddy Bait")

                        print("You bought 25 Teddy Bait!")
                        print(f"Money: ${money}")

                    else:
                        print("Sorry mate, but you don't have enough money.")

                elif bait_choice == "4":
                    print("See you later, mate.")

                else:
                    print("Huh? Didn't catch what you said, mate.")

            elif shop_choice == "2":
                if not fish_inventory:
                    print("No fish to sell, mate.")

                else:
                    fish_counts = {}

                    for caught_fish in fish_inventory:
                        if caught_fish.name in fish_counts:
                            fish_counts[caught_fish.name] += 1
                        else:
                            fish_counts[caught_fish.name] = 1

                    print("What fish do you want to sell?")

                    fish_list = list(fish_counts.keys())

                    for number, fish_name in enumerate(fish_list, 1):
                        print(
                            f"[{number}] {fish_name} "
                            f"x{fish_counts[fish_name]}"
                        )

                    sell_choice = input("> ")

                    if (
                        sell_choice.isdigit()
                        and 1 <= int(sell_choice) <= len(fish_list)
                    ):
                        chosen_name = fish_list[int(sell_choice) - 1]

                        amount_input = input(
                            f"How many {chosen_name} do you want to sell? "
                        )

                        if amount_input.isdigit():
                            amount = int(amount_input)

                            if (
                                amount > 0
                                and amount <= fish_counts[chosen_name]
                            ):
                                chosen_fish = next(
                                    f for f in fish_inventory
                                    if f.name == chosen_name
                                )

                                price = fish_prices[chosen_fish.rarity]
                                total_money = price * amount

                                for _ in range(amount):
                                    fish_inventory.remove(chosen_fish)

                                money += total_money

                                print(
                                    f"You sold {amount} {chosen_name} "
                                    f"for ${total_money}."
                                )
                                print(f"Money: ${money}")

                            else:
                                print(
                                    "You don't have that many, mate."
                                )

                        else:
                            print(
                                "Huh? Didn't catch what you said, mate."
                            )

                    else:
                        print(
                            "Huh? Didn't catch what you said, mate."
                        )

            elif shop_choice == "3":
                print("Come back anytime, mate.")

            else:
                print("Huh? Didn't catch what you said, mate.")

        else:
            print(
                "The shop is closed, mate. "
                "Come back during the day."
            )

    elif command == "zone":
        print("Choose a fishing zone:")

        available_zones = ["Teddy Creek"]

        if food_creek_unlocked:
            available_zones.append("Food Creek")

        if junk_food_ocean_unlocked:
            available_zones.append("Junk Food Ocean")

        for number, zone in enumerate(available_zones, 1):
            print(f"[{number}] {zone}")

        print(f"[{len(available_zones) + 1}] Leave")

        zone_choice = input("> ")

        if zone_choice.isdigit():
            zone_number = int(zone_choice)

            if 1 <= zone_number <= len(available_zones):
                fishing_zone = available_zones[zone_number - 1]
                print(f"You are now fishing at the {fishing_zone}.")

            elif zone_number == len(available_zones) + 1:
                print("You stay where you are.")

            else:
                print("That's not a zone.")

    elif command == "help" or command == "h":
        typewriter1("Available commands:")
        typewriter1("fish - Fish in your current zone")
        typewriter1("inventory - View your inventory")
        typewriter1("shop - Visit the shop")
        typewriter1("zone - Change your fishing zone")
        typewriter1("help - View available commands")
        typewriter1("quit - Exit the game")
        typewriter1("pass time - Passes time, doesn't pass weather")
        typewriter1("workshop - Visit the workshop at night")
        typewriter1("")

    elif command == "quit":
        print("You can't Alt F4 life.")

    elif command == "pass time":
        game_time += 1
        time_period = update_time(game_time)

        print(f"Time: {game_time}:00")
        print(f"Time period: {time_period}")

    elif command == "workshop":
        if time_period == "Evening" or time_period == "Night":

            typewriter("Yeah, yeah... you're here. What do you want?")

            print("[1] View Rods")
            print("[2] Quests")
            print("[3] Leave")

            workshop_choice = input("> ")

            # ----------------------------------------
            # RODS
            # ----------------------------------------

            if workshop_choice == "1":
                print()
                print("________ RODS ________")
                print("Nothing here yet.")
                print()
                typewriter("Come back when I've actually got something to sell.")
                print()

            # ----------------------------------------
            # QUESTS
            # ----------------------------------------

            elif workshop_choice == "2":
                print()
                print("________ QUESTS ________")

                # ==============================
                # BUTTER QUEST
                # ==============================

                if butter_quest:

                    print()
                    print("________ BUTTER QUEST ________")
                    print("Collect 5 Butter and bring them here.")

                    butter_count = item_inventory.count("Butter")

                    print(f"Progress: {butter_count}/5")

                    if butter_count >= 5:
                        print()
                        typewriter("Hmph. You actually brought me the Butter.")

                        for _ in range(5):
                            item_inventory.remove("Butter")

                        butter_quest = False
                        food_creek_unlocked = True
                        fishing_level += 1

                        print()
                        print("QUEST COMPLETE!")
                        print("Food Creek has been unlocked!")
                        print("Fishing Level +1!")

                # ==============================
                # BEARY TRIANGLES QUEST
                # ==============================

                elif beary_triangle_quest:

                    print()
                    print("________ BEARY TRIANGLES QUEST ________")
                    print("Bring me 1 Beary Triangles.")

                    beary_triangles_count = item_inventory.count(
                        "Beary Triangles"
                    )

                    print(f"Progress: {beary_triangles_count}/1")

                    if beary_triangles_count >= 1:
                        print()
                        typewriter(
                            "A Beary Triangle... finally. "
                            "Hand it over."
                        )

                        item_inventory.remove("Beary Triangles")

                        beary_triangle_quest = False
                        junk_food_ocean_unlocked = True
                        fishing_level += 1

                        print()
                        print("QUEST COMPLETE!")
                        print("Junk Food Ocean has been unlocked!")
                        print("Fishing Level +1!")

                # ==============================
                # NO QUEST
                # ==============================

                else:
                    print()
                    print("No quests available.")
                    typewriter("Come back when you've actually done something.")

            # ----------------------------------------
            # LEAVE
            # ----------------------------------------

            elif workshop_choice == "3":
                typewriter("Finally. Now get out of here.")

            # ----------------------------------------
            # INVALID INPUT
            # ----------------------------------------

            else:
                print()
                print("The old man stares at you.")
                typewriter('"What?"')
                typewriter("He squints.")
                typewriter(
                    "I haven't got a clue what you're on about, mate."
                )

        # ----------------------------------------
        # WORKSHOP CLOSED
        # ----------------------------------------

        else:
            typewriter1("The workshop is closed.")
            typewriter1("A cold wind whips the old sign back and forth.")
            typewriter1("Squeak... squeak...")
            typewriter1("The faded sign swings toward you.")
            typewriter1("CLOSED - COME BACK TOMORROW")

    else:
        print("Unknown command.")