import time
import sys
import random
import fish1

'''
Please note!
I used AI to change my ORIGINAL version to a serious version.
My previous version contained food fish and teddies ;-;.
My previous version was also extremely messy and took 2569 lines of code (it only had 3 zones).
I used lists because I'm rusty and messed up and couldn't fix it beca-
use it was so tangled up. :/   

Most things are unAIed but typewriter isn't, i took like 15 hours tryna figure it out.

'''


#var/variables

fish_inventory = []
item_inventory = []

game_time = 7
time_period = "Morning"

fish_away = False

money = 100
fishing_level = 1

fishing_zone = "Clear Creek"


koi_achievement = False
first_quest = False


gar_achievement = False
gar_quest = False

swordfish_and_mahimahi_achievement = False
mahi_mahi_quest = True

roughwater_river_unlocked = False
rocky_river_unlocked = False
deepwater_lake_unlocked = False

weather = "Clear"  # start on clear otherwise the change will not be permanent

selected_bait = None


#i unAIed most of the stuff cause ai sucks but other then that this is ai because i spent 3 hours trying to figure it out

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


#time, determines whether you can go to workshop or shop or whatevers.

def update_time(game_time):

    if game_time >= 6 and game_time < 12:
        return "Morning"

    elif game_time >= 12 and game_time < 18:
        return "Afternoon"

    elif game_time >= 18 and game_time < 21:
        return "Evening"

    else:
        return "Night"


#rarities

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


#weather (effects the luck and stuff)

weathers = [
    "Clear",
    "Rainy",
    "Dry",
    "Storm",
    "Wet"
]

#tackle 

tackle_chances = {
    0: 0,
    1: 50,
    2: 75,
    3: 85,
    4: 95
}


#fish prices at shop

fish_prices = {
    "common": 5,
    "uncommon": 10,
    "rare": 15,
    "epic": 25,
    "legendary": 50
}


#bait

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


#zones

zones = [
    "Clear Creek",
    "Rocky River",
    "Roughwater River",
    "Deepwater Lake",
]


'''
drops here #drops here
'''

fish_drops = {

  
    "Koi": {
        "item": "Koi Scale",
        "chance": 15
    },

  
    "Trevally": {
        "item": "Trevally Fin",
        "chance": 25
    },

    "Mahi-Mahi": {
        "item": "River Pearl",
        "chance": 50
    },

    "Swordfish": {
        "item": "Sword",
        "chance": 15
    },

}



# intro well updated intro fr
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
print("bait - change your bait")

typewriter1("")
player_name = input("What is your name? ")


while True:

    command = input("> ").strip().lower()

    rarity_chances = [
    65,
    30,
    4,
    0.9,
    0.1
    ]

    if deepwater_lake_unlocked:
        print("Yo guys there is a legendary here fr fr go get it mannnnn.")

    if game_time == 6:
        if weather == "Rainy":
            fishing_level -= 1


        if weather == "Dry":
            fishing_level+=1


        if weather == "Storm":
            fishing_level += 1
            rarity_chances = [
                65,
                30,
                4,
                0.9,
                0.1
            ]


        weather = random.choice(weathers)


        if weather == "Clear":
            typewriter1("The sky is clear and luck is increased.")
            rarity_chances = [
                60,
                32,
                6.3,
                1.2,
                0.4
            ]
            
        elif weather == "Rainy":
            typewriter1("Rainy skies — fish are easier to catch!")
            fishing_level+=1

        elif weather == "Dry":
            typewriter1("The dry waters make fish harder to catch today.")
            fishing_level -=1

        elif weather == "Storm":
            typewriter1("Rough waters make fishing harder, and luck is against you!")
            fishing_level -=1
            rarity_chances = [
                75.2,
                24,
                2.2,
                0.5,
                0.08
            ]

        elif weather == "Wet":
            typewriter1("It's a wet day, fishing conditions are normal.")

        else:
            rarity_chances = [
                65,
                30,
                4,
                0.9,
                0.1
            ]
             
   #time reset

    if game_time >= 23:
        game_time = 0
        time_period = update_time(game_time)



    # fish func


    if command == "fish" or command == "f":

        current_fishing_level = fishing_level


        #bait

        if selected_bait is not None:

            if selected_bait in item_inventory:

                current_fishing_level += bait_bonus[selected_bait]

                item_inventory.remove(selected_bait)

                print(f"You used {selected_bait}.")

            else:

                print(f"You don't have any {selected_bait} left.")

                selected_bait = None


            #time 

        game_time += 1

        if game_time >= 24:
            game_time = 0

        time_period = update_time(game_time)


       #rarity

        rarity = random.choices(
            rarities,
            weights=rarity_chances
        )[0]


        #zone fish stuff

        matching_fish = [
            f
            for f in fish1.all_fish
            if (
                f.rarity == rarity
                and zones.index(fishing_zone) in f.zones
            )
        ]


            #choose random fish

        if matching_fish:

            chosen_fish = random.choice(matching_fish)

            #time till escape

            escape_time = max(
                7,
                random.uniform(
                    chosen_fish.weight,
                    chosen_fish.weight * 2
                )
            )

            start_time = time.time()


            #diff or difficulty

            difficulty = (
                chosen_fish.difficulty
                - current_fishing_level
                + 1
            )

            if difficulty < 0:
                difficulty = 0


         
            if difficulty > max(tackle_chances):
                difficulty = max(tackle_chances)


            tackle_chance = tackle_chances[difficulty]

            #fishing starting whatevs stuff

            progress = 0

            fish_away = False

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


         
                filled = progress // 5

                print(
                    f"[{'█' * filled}"
                    f"{'░' * (20 - filled)}]"
                )

                time.sleep(0.4)


            #success in fishing in fish

            if fish_away == False:

               
                caught_weight = random.uniform(
                    chosen_fish.min_weight,
                    chosen_fish.max_weight
                )

              
                # so different fish can have different weights
                caught_fish = type(chosen_fish)()

                caught_fish.weight = caught_weight

                fish_inventory.append(caught_fish)


                #catch message

                print()
                print(f"You caught a {caught_fish.name}!")
                print(f"Weight: {caught_fish.weight:.2f} kg")
                print(f"Rarity: {caught_fish.rarity}")

                #sure ik i messed up sooooooooo bad here like fr.

                #first quest

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

                    #you when you can't do it easily and have to manually do it x.x

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
                    print("Collect 3 Trevally Fin.")
                    print("Return to the workshop when you have enough.")
                    print()

                if ( 
                    caught_fish.name == "Swordfish"
                    and not swordfish_and_mahimahi_achievement
                ):
                    print("________ QUEST UNLOCKED _______")
                    print("Collect a sword and a River Pearl.")
                    print("Collect them from a Swordfish and a Mahi-Mahi")
                    print("Return to the workshop when you have enough.")

                    swordfish_and_mahimahi_achievement = True

                elif caught_fish.name == "Saccopharynx":
                    typewriter("Wow........ You actually went through all of that trouble to get the legendary..... Congratulations."
                    "You wasted like 3 hours of your life..... Unless you were really lucky. Great."
                    "Now I have to make more stuff. :////")
                


                #fish drop

                if caught_fish.name in fish_drops:

                    drop = fish_drops[caught_fish.name]

                    if random.randint(1, 100) <= drop["chance"]:

                        item_inventory.append(drop["item"])

                        print(
                            f"You found a {drop['item']}!"
                        )


        
            fish_away = False

            print()
            print(f"Time: {game_time}:00")
            print(f"Time period: {time_period}")


        else:

            print(
                "Nothing seems to be biting in this area."
            )

            print(f"Time: {game_time}:00")

        #inv or inventory

    elif command == "inventory" or command == "i":

        fish_counts = {}


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

        #shop

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


            #buy bait

            if shop_choice == "1":

                print()
                print("________ BAIT ________")

                print("[1] Minnow Bait - $150")
                print("[2] Blue Gill Bait - $300")
                print("[3] Arowana Bait - $500")
                print("[4] Leave")


                bait_choice = input("> ")




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


                    #leave

                    if (
                        sell_choice.isdigit()
                        and int(sell_choice)
                        == len(fish_list) + 1
                    ):

                        print(
                            "You decide not to sell anything."
                        )

                        # sell

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


        #zone

    elif command == "zone":

        print()
        print("________ FISHING ZONES ________")

        available_zones = [
            "Clear Creek"
        ]



        if rocky_river_unlocked:

            available_zones.append(
                "Rocky River"
            )



        if roughwater_river_unlocked:

            available_zones.append(
                "Roughwater River"
            )


        if deepwater_lake_unlocked:
            available_zones.append("Deepwater Lake")


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


            #help

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
        typewriter1("bait - change your bait")
        typewriter1("")



    # nice try


    elif command == "quit":

        print(
            "You can't Alt F4 life."
        )

        break



    # pass time


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



    # workshop


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



            # rods, not yet done


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



            # quests


            elif workshop_choice == "2":

                print()
                print("________ QUESTS ________")




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




                elif gar_quest:

                    print()
                    print(
                        "________ "
                        "TREVALLY QUEST ________"
                    )

                    print(
                        "Bring me 3 Trevally Fin."
                    )


                    trevally_fin_count = (
                        item_inventory.count(
                            "Trevally Fin"
                        )
                    )


                    print(
                        f"Progress: "
                        f"{trevally_fin_count}/3"
                    )


                    if trevally_fin_count >= 3:

                        print()

                        typewriter(
                            "Trevally Fins... finally. "
                            "Hand it over."
                        )


                        item_inventory.remove(
                            "Trevally Fin"
                        )

                        item_inventory.remove(
                            "Trevally Fin"
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


                elif mahi_mahi_quest:

                    print()
                    print("________ SWORD & RIVER PEARL QUEST ________")

                    print("Collect 1 Sword and 1 River Pearl.")
                    print("Return to the workshop when you have both.")

                    sword_count = item_inventory.count("Sword")
                    river_pearl_count = item_inventory.count("River Pearl")

                    print(f"Sword: {sword_count}/1")
                    print(f"River Pearl: {river_pearl_count}/1")

                    if sword_count >= 1 and river_pearl_count >= 1:

                        print()

                        typewriter1(
                            "Wait what!? "
                            "A sword? How'd you get that?"
                        )

                        item_inventory.remove("Sword")
                        item_inventory.remove("River Pearl")

                        mahi_mahi_quest = False
                        deepwater_lake_unlocked = True

                        fishing_level += 1

                        print()
                        print("QUEST COMPLETE!")
                        print("Deepwater Lake has been unlocked!")
                        print("Fishing Level +1!")


                else:

                    print()
                    print("No quests available.")

                    typewriter(
                        "Come back when you've "
                        "actually done something."
                    )



            elif workshop_choice == "3":

                typewriter(
                    "Finally. Now get out of here."
                )




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


    #bait here
    elif command == "bait":

        print()
        print("________ BAIT ________")

        available_bait = []

        for item in item_inventory:
            if item in bait_bonus and item not in available_bait:
                available_bait.append(item)

        if not available_bait:
            print("You don't have any bait.")
            print()
            continue

        for number, bait in enumerate(available_bait, 1):
            amount = item_inventory.count(bait)

            print(f"[{number}] {bait} x{amount}")

        print(f"[{len(available_bait) + 1}] No Bait")

        bait_choice = input("> ")

        if bait_choice.isdigit():

            choice = int(bait_choice)

            if 1 <= choice <= len(available_bait):

                selected_bait = available_bait[choice - 1]

                print()
                print(f"You selected {selected_bait}.")

            elif choice == len(available_bait) + 1:

                selected_bait = None

                print()
                print("You are no longer using bait.")

            else:
                print("That's not a bait option.")

        else:
            print("That's not a bait option.")







    else:

        print(
            "Unknown command."
        )
