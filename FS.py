import time
import sys
import random
import fish1

'''
Please note!
I used AI to change my ORIGINAL version to a serious version.
My previous version contained food fish and teddies ;-;.
My previous version was also extremely messy and took 600 lines.
I used lists because I'm rusty and messed up and couldn't fix it beca-
use it was so tangled up. :/    

'''


# ============================================================
# GAME VARIABLES
# ============================================================

fish_inventory = []
item_inventory = []

game_time = 7
time_period = "Morning"

fish_away = False

money = 100
fishing_level = 1

fishing_zone = "Clear Creek"

# Achievements / quests
koi_achievement = False
first_quest = False

rocky_river_unlocked = False

gar_achievement = False
gar_quest = False

roughwater_river_unlocked = False

weather = "Clear"


# ============================================================
# TYPEWRITER
# ============================================================

def typewriter(
    text,
    base_speed=0.04,
    pause_chance=0.2,
    pause_duration=0.3,
    punct_pause=0.6
):
    words = text.split(" ")
    punctuation = ".!?,"

    for i, word in enumerate(words):

        for char in word:
            sys.stdout.write(char)
            sys.stdout.flush()

            time.sleep(random.uniform(0.01, 0.1))

        last_char = word[-1] if word else ""

        if i < len(words) - 1:
            sys.stdout.write(" ")
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

    print()


# ============================================================
# TIME
# ============================================================

def update_time(game_time):

    if game_time >= 6 and game_time < 12:
        return "Morning"

    elif game_time >= 12 and game_time < 18:
        return "Afternoon"

    elif game_time >= 18 and game_time < 21:
        return "Evening"

    else:
        return "Night"


# ============================================================
# RARITIES
# ============================================================

rarities = [
    "common",
    "uncommon",
    "rare",
    "epic",
    "legendary"
]

rarity_chances = [
    65,
    30,
    4,
    0.9,
    0.1
]


# ============================================================
# WEATHER
# ============================================================

weathers = {
    "Clear",
    "Rainy",
    "Dry",
    "Storm",
    "Wet"
}


# ============================================================
# FISHING DIFFICULTY
# ============================================================

tackle_chances = {
    0: 0,
    1: 50,
    2: 75,
    3: 85,
    4: 95
}


# ============================================================
# FISH SELL PRICES
# ============================================================

fish_prices = {
    "common": 5,
    "uncommon": 10,
    "rare": 15,
    "epic": 25,
    "legendary": 50
}


# ============================================================
# BAIT
# ============================================================

bait_prices = {
    "Minnow Bait": 150,
    "Blue Gill Bait": 300,
    "Arowana Bait": 500
}


bait_bonus = {
    "Minnow Bait": 1,
    "Blue Gill Bait": 2,
    "Arowana Bait": 3
}


# ============================================================
# FISHING ZONES
# ============================================================

zones = [
    "Clear Creek",
    "Rocky River",
    "Roughwater River"
]


# ============================================================
# FISH DROPS
# ============================================================

fish_drops = {

    # Koi can drop Koi Scales
    "Koi": {
        "item": "Koi Scale",
        "chance": 15
    },

    # Trevally can drop Trevally Fins
    "Trevally": {
        "item": "Trevally Fin",
        "chance": 25
    }

}


# ============================================================
# INTRO
# ============================================================

# intro
typewriter1("After a long walk, you finally reach the river.")
typewriter1("You stop at the edge of the water and take a look around.")
typewriter1("The river is wider than you expected, stretching far beyond the trees.")
typewriter1("The water moves slowly, but you can occasionally see something ripple beneath the surface.")
typewriter1("You don't know much about this place.")
typewriter1("You've heard that some pretty strange fish can be found in these waters.")
typewriter1("Whether that's true or not, there's only one way to find out.")
typewriter1("You tighten your grip on your fishing rod.")
typewriter1("Today might be the start of something interesting.")
typewriter1("")
typewriter1("Available commands:")
print("fish - Fish in your current zone")
print("inventory - View your inventory")
print("shop - Visit the shop")
print("zone - Change your fishing zone")
print("help - View available commands")
print("pass time - Passes time, doesn't pass weather")
print("workshop - Visit the workshop at night")
print("quit - Exit the game")
typewriter1("")
player_name = input("What is your name? ")


# ============================================================
# MAIN GAME LOOP
# ============================================================

while True:

    command = input("> ").strip().lower()


    # ========================================================
    # RESET TIME AFTER 23:00
    # ========================================================

    if game_time >= 23:
        game_time = 0
        time_period = update_time(game_time)


    # ========================================================
    # FISH
    # ========================================================

    if command == "fish" or command == "f":

        current_fishing_level = fishing_level


        # ----------------------------------------------------
        # USE BAIT
        # ----------------------------------------------------

        for bait in item_inventory:

            if bait in bait_bonus:

                current_fishing_level += bait_bonus[bait]

                item_inventory.remove(bait)

                print(f"You used {bait}.")

                break


        # ----------------------------------------------------
        # TIME PASSES
        # ----------------------------------------------------

        game_time += 1

        if game_time >= 24:
            game_time = 0

        time_period = update_time(game_time)


        # ----------------------------------------------------
        # CHOOSE RARITY
        # ----------------------------------------------------

        rarity = random.choices(
            rarities,
            weights=rarity_chances
        )[0]


        # ----------------------------------------------------
        # FIND FISH IN CURRENT ZONE
        # ----------------------------------------------------

        matching_fish = [
            f
            for f in fish1.all_fish
            if (
                f.rarity == rarity
                and zones.index(fishing_zone) in f.zones
            )
        ]


        # ----------------------------------------------------
        # IF A FISH EXISTS
        # ----------------------------------------------------

        if matching_fish:

            chosen_fish = random.choice(matching_fish)


            # ------------------------------------------------
            # ESCAPE TIME
            # ------------------------------------------------

            escape_time = max(
                7,
                random.uniform(
                    chosen_fish.weight,
                    chosen_fish.weight * 2
                )
            )

            start_time = time.time()


            # ------------------------------------------------
            # CALCULATE DIFFICULTY
            # ------------------------------------------------

            difficulty = (
                chosen_fish.difficulty
                - current_fishing_level
                + 1
            )

            if difficulty < 0:
                difficulty = 0


            # Make sure difficulty exists
            if difficulty > max(tackle_chances):
                difficulty = max(tackle_chances)


            tackle_chance = tackle_chances[difficulty]


            # ------------------------------------------------
            # FISHING MINIGAME
            # ------------------------------------------------

            progress = 0

            fish_away = False

            while progress < 100:

                # Fish escapes
                if time.time() - start_time >= escape_time:

                    print("The fish got away!")

                    fish_away = True

                    break


                # Increase progress
                progress += random.randint(0, 35)


                if progress > 100:
                    progress = 100


                # Fish fights back
                if random.random() < tackle_chance / 100:

                    progress -= random.randint(5, 15)

                    if progress < 0:
                        progress = 0


                # Progress bar
                filled = progress // 5

                print(
                    f"[{'█' * filled}"
                    f"{'░' * (20 - filled)}]"
                )

                time.sleep(0.4)


            # ------------------------------------------------
            # SUCCESS
            # ------------------------------------------------

            if fish_away == False:

                # Give the fish a fresh weight
                caught_weight = random.uniform(
                    chosen_fish.min_weight,
                    chosen_fish.max_weight
                )

                # Create a separate caught fish object
                # so different fish can have different weights
                caught_fish = type(chosen_fish)()

                caught_fish.weight = caught_weight

                fish_inventory.append(caught_fish)


                # --------------------------------------------
                # CATCH MESSAGE
                # --------------------------------------------

                print()
                print(f"You caught a {caught_fish.name}!")
                print(f"Weight: {caught_fish.weight:.2f} kg")
                print(f"Rarity: {caught_fish.rarity}")


                # ============================================
                # KOI ACHIEVEMENT / FIRST QUEST
                # ============================================

                if (
                    caught_fish.name == "Koi"
                    and not koi_achievement
                ):

                    koi_achievement = True
                    first_quest = True

                    print()
                    print("________ ACHIEVEMENT ________")
                    print("You caught a Koi!")
                    print()
                    print("________ QUEST UNLOCKED ________")
                    print("Collect 5 Koi Scales.")
                    print("Return to the workshop when you have enough.")
                    print()


                # ============================================
                # GAR ACHIEVEMENT / SECOND QUEST
                # ============================================

                if (
                    caught_fish.name == "Gar"
                    and not gar_achievement
                ):

                    gar_achievement = True
                    gar_quest = True

                    print()
                    print("________ ACHIEVEMENT ________")
                    print("You caught a Gar!")
                    print()
                    print("________ QUEST UNLOCKED ________")
                    print("Collect 1 Trevally Fin.")
                    print("Return to the workshop when you have enough.")
                    print()


                # ============================================
                # FISH DROPS
                # ============================================

                if caught_fish.name in fish_drops:

                    drop = fish_drops[caught_fish.name]

                    if random.randint(1, 100) <= drop["chance"]:

                        item_inventory.append(drop["item"])

                        print(
                            f"You found a {drop['item']}!"
                        )


            # Reset
            fish_away = False

            print()
            print(f"Time: {game_time}:00")
            print(f"Time period: {time_period}")


        else:

            print(
                "Nothing seems to be biting in this area."
            )

            print(f"Time: {game_time}:00")


    # ========================================================
    # INVENTORY
    # ========================================================

    elif command == "inventory" or command == "i":

        fish_counts = {}


        # Count fish
        for caught_fish in fish_inventory:

            if caught_fish.name in fish_counts:

                fish_counts[caught_fish.name] += 1

            else:

                fish_counts[caught_fish.name] = 1


        print()
        print("________ FISH ________")


        if fish_counts:

            for name, amount in fish_counts.items():

                print(
                    f"{name} x{amount}"
                )

        else:

            print("No fish.")


        print()
        print(f"Money: ${money}")

        print()
        print("________ ITEMS ________")


        if item_inventory:

            item_counts = {}


            for item in item_inventory:

                if item in item_counts:

                    item_counts[item] += 1

                else:

                    item_counts[item] = 1


            for item, amount in item_counts.items():

                print(
                    f"{item} x{amount}"
                )

        else:

            print("No items.")


        print()


    # ========================================================
    # SHOP
    # ========================================================

    elif command == "shop":

        if (
            time_period == "Morning"
            or time_period == "Afternoon"
        ):

            typewriter1(
                f"G'day {player_name}! "
                "Got any fish today, mate? "
                "Come on in and see what we've got."
            )


            print()
            print(f"Money: ${money}")
            print("[1] Bait")
            print("[2] Sell")
            print("[3] Leave")


            shop_choice = input("> ")


            # =================================================
            # BUY BAIT
            # =================================================

            if shop_choice == "1":

                print()
                print("________ BAIT ________")

                print("[1] Minnow Bait - $150")
                print("[2] Blue Gill Bait - $300")
                print("[3] Arowana Bait - $500")
                print("[4] Leave")


                bait_choice = input("> ")


                # ---------------------------------------------
                # MINNOW BAIT
                # ---------------------------------------------

                if bait_choice == "1":

                    price = bait_prices["Minnow Bait"]


                    if money >= price:

                        money -= price


                        for _ in range(25):

                            item_inventory.append(
                                "Minnow Bait"
                            )


                        print(
                            "You bought 25 Minnow Bait!"
                        )

                        print(
                            f"Money: ${money}"
                        )

                    else:

                        print(
                            "Sorry mate, "
                            "but you don't have enough money."
                        )


                # ---------------------------------------------
                # BLUE GILL BAIT
                # ---------------------------------------------

                elif bait_choice == "2":

                    price = bait_prices["Blue Gill Bait"]


                    if money >= price:

                        money -= price


                        for _ in range(25):

                            item_inventory.append(
                                "Blue Gill Bait"
                            )


                        print(
                            "You bought 25 Blue Gill Bait!"
                        )

                        print(
                            f"Money: ${money}"
                        )

                    else:

                        print(
                            "Sorry mate, "
                            "but you don't have enough money."
                        )


                # ---------------------------------------------
                # AROWANA BAIT
                # ---------------------------------------------

                elif bait_choice == "3":

                    price = bait_prices["Arowana Bait"]


                    if money >= price:

                        money -= price


                        for _ in range(25):

                            item_inventory.append(
                                "Arowana Bait"
                            )


                        print(
                            "You bought 25 Arowana Bait!"
                        )

                        print(
                            f"Money: ${money}"
                        )

                    else:

                        print(
                            "Sorry mate, "
                            "but you don't have enough money."
                        )


                elif bait_choice == "4":

                    print(
                        "See you later, mate."
                    )


                else:

                    print(
                        "Huh? Didn't catch what you said, mate."
                    )


            # =================================================
            # SELL FISH
            # =================================================

            elif shop_choice == "2":

                if not fish_inventory:

                    print(
                        "No fish to sell, mate."
                    )


                else:

                    fish_counts = {}


                    for caught_fish in fish_inventory:

                        if caught_fish.name in fish_counts:

                            fish_counts[caught_fish.name] += 1

                        else:

                            fish_counts[caught_fish.name] = 1


                    print()
                    print("What fish do you want to sell?")


                    fish_list = list(
                        fish_counts.keys()
                    )


                    for number, fish_name in enumerate(
                        fish_list,
                        1
                    ):

                        print(
                            f"[{number}] "
                            f"{fish_name} "
                            f"x{fish_counts[fish_name]}"
                        )


                    print(
                        f"[{len(fish_list) + 1}] Leave"
                    )


                    sell_choice = input("> ")


                    # -----------------------------------------
                    # LEAVE
                    # -----------------------------------------

                    if (
                        sell_choice.isdigit()
                        and int(sell_choice)
                        == len(fish_list) + 1
                    ):

                        print(
                            "You decide not to sell anything."
                        )


                    # -----------------------------------------
                    # SELL
                    # -----------------------------------------

                    elif (
                        sell_choice.isdigit()
                        and 1 <= int(sell_choice)
                        <= len(fish_list)
                    ):

                        chosen_name = fish_list[
                            int(sell_choice) - 1
                        ]


                        amount_input = input(
                            f"How many {chosen_name} "
                            "do you want to sell? "
                        )


                        if amount_input.isdigit():

                            amount = int(amount_input)


                            if (
                                amount > 0
                                and amount
                                <= fish_counts[chosen_name]
                            ):

                                # Find one fish of that type
                                chosen_fish = next(
                                    f
                                    for f in fish_inventory
                                    if f.name == chosen_name
                                )


                                price = fish_prices[
                                    chosen_fish.rarity
                                ]


                                total_money = (
                                    price * amount
                                )


                                # Remove fish
                                for _ in range(amount):

                                    fish_to_remove = next(
                                        f
                                        for f in fish_inventory
                                        if f.name == chosen_name
                                    )

                                    fish_inventory.remove(
                                        fish_to_remove
                                    )


                                money += total_money


                                print(
                                    f"You sold "
                                    f"{amount} "
                                    f"{chosen_name} "
                                    f"for ${total_money}."
                                )

                                print(
                                    f"Money: ${money}"
                                )


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


            # =================================================
            # LEAVE SHOP
            # =================================================

            elif shop_choice == "3":

                print(
                    "Come back anytime, mate."
                )


            else:

                print(
                    "Huh? Didn't catch what you said, mate."
                )


        else:

            print(
                "The shop is closed, mate. "
                "Come back during the day."
            )


    # ========================================================
    # ZONE
    # ========================================================

    elif command == "zone":

        print()
        print("________ FISHING ZONES ________")

        available_zones = [
            "Clear Creek"
        ]


        # Rocky River unlocked
        if rocky_river_unlocked:

            available_zones.append(
                "Rocky River"
            )


        # Roughwater River unlocked
        if roughwater_river_unlocked:

            available_zones.append(
                "Roughwater River"
            )


        for number, zone in enumerate(
            available_zones,
            1
        ):

            print(
                f"[{number}] {zone}"
            )


        print(
            f"[{len(available_zones) + 1}] Leave"
        )


        zone_choice = input("> ")


        if zone_choice.isdigit():

            zone_number = int(zone_choice)


            if (
                1 <= zone_number
                <= len(available_zones)
            ):

                fishing_zone = available_zones[
                    zone_number - 1
                ]

                print(
                    f"You are now fishing at "
                    f"{fishing_zone}."
                )


            elif (
                zone_number
                == len(available_zones) + 1
            ):

                print(
                    "You stay where you are."
                )


            else:

                print(
                    "That's not a zone."
                )


        else:

            print(
                "That's not a zone."
            )


    # ========================================================
    # HELP
    # ========================================================

    elif command == "help" or command == "h":

        typewriter1("")
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


    # ========================================================
    # QUIT
    # ========================================================

    elif command == "quit":

        print(
            "You can't Alt F4 life."
        )

        break


    # ========================================================
    # PASS TIME
    # ========================================================

    elif command == "pass time":

        game_time += 1


        if game_time >= 24:
            game_time = 0


        time_period = update_time(
            game_time
        )


        print(
            f"Time: {game_time}:00"
        )

        print(
            f"Time period: {time_period}"
        )


    # ========================================================
    # WORKSHOP
    # ========================================================

    elif command == "workshop":

        if (
            time_period == "Evening"
            or time_period == "Night"
        ):

            typewriter(
                "Yeah, yeah... you're here. "
                "What do you want?"
            )


            print()
            print("[1] View Rods")
            print("[2] Quests")
            print("[3] Leave")


            workshop_choice = input("> ")


            # =================================================
            # RODS
            # =================================================

            if workshop_choice == "1":

                print()
                print("________ RODS ________")
                print("Nothing here yet.")
                print()

                typewriter(
                    "Come back when I've actually "
                    "got something to sell."
                )

                print()


            # =================================================
            # QUESTS
            # =================================================

            elif workshop_choice == "2":

                print()
                print("________ QUESTS ________")


                # =============================================
                # KOI QUEST
                # =============================================

                if first_quest:

                    print()
                    print("________ KOI QUEST ________")

                    print(
                        "Collect 5 Koi Scales "
                        "and bring them here."
                    )


                    koi_scale_count = (
                        item_inventory.count(
                            "Koi Scale"
                        )
                    )


                    print(
                        f"Progress: "
                        f"{koi_scale_count}/5"
                    )


                    if koi_scale_count >= 5:

                        print()

                        typewriter(
                            "Hmph. You actually brought me "
                            "the Koi Scales."
                        )


                        for _ in range(5):

                            item_inventory.remove(
                                "Koi Scale"
                            )


                        first_quest = False

                        rocky_river_unlocked = True

                        fishing_level += 1


                        print()
                        print("QUEST COMPLETE!")
                        print(
                            "Rocky River has been unlocked!"
                        )
                        print(
                            "Fishing Level +1!"
                        )


                # =============================================
                # GAR / TREVALly QUEST
                # =============================================

                elif gar_quest:

                    print()
                    print(
                        "________ "
                        "TREVALly QUEST ________"
                    )

                    print(
                        "Bring me 1 Trevally Fin."
                    )


                    trevally_fin_count = (
                        item_inventory.count(
                            "Trevally Fin"
                        )
                    )


                    print(
                        f"Progress: "
                        f"{trevally_fin_count}/1"
                    )


                    if trevally_fin_count >= 1:

                        print()

                        typewriter(
                            "A Trevally Fin... finally. "
                            "Hand it over."
                        )


                        item_inventory.remove(
                            "Trevally Fin"
                        )


                        gar_quest = False

                        roughwater_river_unlocked = True

                        fishing_level += 1


                        print()
                        print("QUEST COMPLETE!")
                        print(
                            "Roughwater River "
                            "has been unlocked!"
                        )

                        print(
                            "Fishing Level +1!"
                        )


                # =============================================
                # NO QUEST
                # =============================================

                else:

                    print()
                    print("No quests available.")

                    typewriter(
                        "Come back when you've "
                        "actually done something."
                    )


            # =================================================
            # LEAVE
            # =================================================

            elif workshop_choice == "3":

                typewriter(
                    "Finally. Now get out of here."
                )


            # =================================================
            # INVALID INPUT
            # =================================================

            else:

                print()
                print(
                    "The old man stares at you."
                )

                typewriter(
                    '"What?"'
                )

                typewriter(
                    "He squints."
                )

                typewriter(
                    "I haven't got a clue "
                    "what you're on about, mate."
                )


        # ====================================================
        # WORKSHOP CLOSED
        # ====================================================

        else:

            typewriter1(
                "The workshop is closed."
            )

            typewriter1(
                "A cold wind whips the old sign "
                "back and forth."
            )

            typewriter1(
                "Squeak... squeak..."
            )

            typewriter1(
                "The faded sign swings toward you."
            )

            typewriter1(
                "CLOSED - COME BACK TOMORROW"
            )


    # ========================================================
    # UNKNOWN COMMAND
    # ========================================================

    else:

        print(
            "Unknown command."
        )
