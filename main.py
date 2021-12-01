# Course: CS 30
# Period: 3
# Date created: 11/16/21
# Date last modified: 11/22/21
# Name: Ahsan Shamim
# Description: Batman X Green Lantern - Escape



import os
import sys


# prints the introduction of the game


print("""
Batman and Green Lantern are on a mission to find an underground enemy base.
While they are looking for the base, the enemy is notified of their mission
Batman and Green Lantern need to find their way out and escape the base.
You can go only four directions to escape:
forward, backward, right, left
You also have an option to quit the game. The option is provided in the menu.
An option to find your location in the map is accessible in the menu
""")


# This inventory is paired with specific characters
inventory = {"Batman": {"Night Vision Goggles":
                        {"description": """ Use the Night Vision Goggles to see
                        in the dark and find your way """, }},
             "Green Lantern": {"Power Ring":
                               {"description":
                                "Use it as a flashlight to find their way", }}}

# This dictionary includes the descriptions of Batman


character = {"Batman":
             {"description":
              "I am a vigilante and my real name is Bruce Wayne!"}}

# This dictionary includes the description of Green Lantern


character_2 = {"Green Lantern":
               {"description":
                "My name is Hal Jordan. I come from the Planet Mogo"}}


def player_inventory(player, inventory):
    """Print out the inventory for the chosen character"""
    for item in inventory[player]:
        description = inventory[player][item]["description"]
        print(f"{player}'s {item} - {description}")


def character_inventory(player, character):
    """ prints out the description for Batman """
    for item in character[player]:
        description = character[player]["description"]
        print(f"{player}'s {item} - {description}")


def character_inventory_2(player_2, character_2):
    """ prints out the description for Green Lantern """
    for item in character_2[player_2]:
        description_2 = character_2[player_2]["description"]
        print(f"{player_2}'s {item} - {description_2}")

# This prints out the current location of the user
location = {
  "line 1": "Your location is Tile 1. 9 more to go!",
  "line 2": "Your location is Tile 2. 8 more to go!",
  "line 3": "Your location is Tile 3. 7 more to go!",
  "line 4": "Your location is Tile 4. 6 more to go!",
  "line 5": "Your location is Tile 5. 5 more to go!",
  "line 6": "Your location is Tile 6. 4 more to go!",
  "line 7": "Your location is Tile 7. 3 more to go!",
  "line 8": "Your location is Tile 8. 2 more to go!",
  "line 9": "Your location is Tile 9. 1 more to go!",
}

# This takes the input for the character selection


inventory_input = input("Batman or Green Lantern: ")


# valid directions and actions to move


valid_actions = ["forward", "backward", "left", "right", "quit", "location"]


# valid action or hint for Batman


valid_hint = ["goggles"]


# valid action or hint for Green Lantern


valid_hint_2 = ["ring"]


def character_intro():
    """ Prints out the character intro for Batman """
    print("""
  You have chosen Batman as you character. You will use Batman to get out
  of this maze. You can use a hint to complete a level.
  """)


def character_intro_2():
    """ Prints out the character intro for Green Lantern """
    print("""
    You have chosen Green Lantern as you character. You will use Green Lantern
        to get out of this maze. You can use a hint to complete a level.
         """)


def menu():
    """ prints out the menu of all the possible directions """
    print("""Choose an action:
    """)
    for action in valid_actions:
        print(f"* {action}")


def menu_2():
    """ Prints out the inventory item for Batman in the menu """
    for action in valid_hint:
        print(f"* {action}")


def menu_3():
    """ Prints out the inventory item for Green Lantern in the menu """
    for action in valid_hint_2:
        print(f"* {action}")


def end_script():
    """ This prints out an ending message when you have completed the game """
    print("""
    You have successfully escaped out of the temple and
    you have completed the game.
    """)


def action_1():
    """ Prints out the menu for input action to move in the map at Level 1 """
    print("""
      LEVEL 1
      """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Wall ahead ")
        action_1()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_1()
    if action_input.lower() in valid_actions[2]:
        print(f" You are turning to the left side of the temple")
        action_2()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_1()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 1"]
        print(y)
        action_1()
    if action_input.lower() in valid_hint[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This helps you see better and gives you a hint for your
            next direction. The direction is left.
            Enter left when the menu restarts.""")
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        action_1()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_1()


def action_2():
    """ Prints out the menu for input action to move in the map at Level 2 """
    print("""
        LEVEL 2
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking ahead ")
        action_3()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_2()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_2()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_2()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 2"]
        print(y)
        action_2()
    if action_input.lower() in valid_hint[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This helps you see better and gives you a hint for your
            next direction. The direction is forward.
            Enter forward when the menu restarts.""")
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        action_2()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_2()


def action_3():
    """ Prints out the menu for input action to move in the map at Level 3 """
    print("""
        LEVEL 3
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking ahead")
        action_4()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_3()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_3()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_3()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 3"]
        print(y)
        action_3()
    if action_input.lower() in valid_hint[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This helps you see better and gives you a hint for your
            next direction. The direction is forward.
            Enter forward when the menu restarts.""")
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        action_3()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_3()


def action_4():
    """ Prints out the menu for input action to move in the map at Level 4 """
    print("""
        LEVEL 4
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Dead end ")
        action_4()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_4()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_4()
    if action_input.lower() in valid_actions[3]:
        print(f" Turn right to walk towards the exit ")
        action_5()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 4"]
        print(y)
        action_4()
    if action_input.lower() in valid_hint[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This helps you see better and gives you a hint for your
            next direction. The direction is right.
            Enter right when the menu restarts.""")
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        action_4()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_4()


def action_5():
    """ Prints out the menu for input action to move in the map at Level 5 """
    print("""
        LEVEL 5
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking")
        action_6()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_5()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_5()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_5()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 5"]
        print(y)
        action_5()
    if action_input.lower() in valid_hint[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This helps you see better and gives you a hint for your
            next direction. The direction is forward.
            Enter forward when the menu restarts.""")
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        action_5()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_5()


def action_6():
    """ Prints out the menu for input action to move in the map at Level 6 """
    print("""
        LEVEL 6
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking")
        action_7()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_6()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_6()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_6()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 6"]
        print(y)
        action_6()
    if action_input.lower() in valid_hint[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This helps you see better and gives you a hint for your
            next direction. The direction is forward.
            Enter forward when the menu restarts.""")
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        action_6()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_6()


def action_7():
    """ Prints out the menu for input action to move in the map at Level 7 """
    print("""
        LEVEL 7
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" wall ahead ")
        action_7()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_7()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_7()
    if action_input.lower() in valid_actions[3]:
        print(f" turn right towards the exit ")
        action_8()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 7"]
        print(y)
        action_7()
    if action_input.lower() in valid_hint[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This helps you see better and gives you a hint for your
            next direction. The direction is right.
            Enter right when the menu restarts.""")
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        action_7()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_7()


def action_8():
    """ Prints out the menu for input action to move in the map at Level 8 """
    print("""
        LEVEL 8
        """)
    menu()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" wall ahead ")
        action_8()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_8()
    if action_input.lower() in valid_actions[2]:
        print(f" Turn left. You are getting closer!")
        action_9()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_8()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 8"]
        print(y)
        action_8()
    if action_input.lower() in valid_hint[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This helps you see better and gives you a hint for your
            next direction. The direction is left.
            Enter left when the menu restarts.""")
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        action_8()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_8()


def action_9():
    """ Prints out the menu for input action to move in the map at Level 9 """
    print("""
        LEVEL 9
        """)
    menu()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f""" You found the exit! """)
        end_script()
        quit()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_9()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_9()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_9()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 9"]
        print(y)
        action_9()
    if action_input.lower() in valid_hint[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This helps you see better and gives you a hint for your
            next direction. The final direction is forward.
            Enter forward when the menu restarts."""
              )
        action_9()
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        action_1()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_9()


def actions_1():
    """ Prints out the menu for input action to move in the map at Level 1 """
    print("""
      LEVEL 1
      """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Wall ahead ")
        actions_1()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_1()
    if action_input.lower() in valid_actions[2]:
        print(f" You are turning to the left side of the temple")
        actions_2()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_1()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 1"]
        print(y)
        actions_1()
    if action_input.lower() in valid_hint_2[0]:
        print("""You have chosen to use the Power Ring.
      This ring is used a flashlight and gives you a hint for your
      next direction. The direction is left.
      Enter left when the menu restarts. """)
    if action_input.lower not in valid_hint_2:
        print("Invalid direction!")
        actions_1()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_1()


def actions_2():
    """ Prints out the menu for input action to move in the map at Level 2 """
    print("""
        LEVEL 2
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking ahead ")
        actions_3()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_2()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_2()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_2()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 2"]
        print(y)
        actions_2()
    if action_input.lower() in valid_hint_2[0]:
        print("""You have chosen to use the Power Ring.
      This ring is used a flashlight and gives you a hint for your next
      direction. The direction is forward.
      Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint_2:
        print("Invalid direction!")
        actions_2()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_2()


def actions_3():
    """ Prints out the menu for input action to move in the map at Level 3 """
    print("""
        LEVEL 3
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking ahead")
        actions_4()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_3()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_3()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_3()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 3"]
        print(y)
        actions_3()
    if action_input.lower() in valid_hint_2[0]:
        print("""You have chosen to use the Power Ring.
      This ring is used a flashlight and gives you a hint for your next
      direction. The direction is forward.
      Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint_2:
        print("Invalid direction!")
        actions_3()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_3()


def actions_4():
    """ Prints out the menu for input action to move in the map at Level 4 """
    print("""
        LEVEL 4
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Dead end ")
        actions_4()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_4()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_4()
    if action_input.lower() in valid_actions[3]:
        print(f" Turn right to walk towards the exit ")
        actions_5()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 4"]
        print(y)
        actions_4()
    if action_input.lower() in valid_hint_2[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight and gives you a hint for your next
      direction. The direction is right.
      Enter right when the menu restarts. """)
    if action_input.lower not in valid_hint_2:
        print("Invalid direction!")
        actions_4()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_4()


def actions_5():
    """ Prints out the menu for input action to move in the map at Level 5 """
    print("""
        LEVEL 5
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking")
        actions_6()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_5()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_5()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_5()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 5"]
        print(y)
        actions_5()
    if action_input.lower() in valid_hint_2[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight and gives you a hint for your next
      direction. The direction is forward.
      Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint_2:
        print("Invalid direction!")
        actions_5()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_5()


def actions_6():
    """ Prints out the menu for input action to move in the map at Level 6 """
    print("""
        LEVEL 6
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking")
        actions_7()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_6()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_6()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_6()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 6"]
        print(y)
        actions_6()
    if action_input.lower() in valid_hint_2[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight and gives you a hint for your next
      direction. The direction is forward.
      Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint_2:
        print("Invalid direction!")
        actions_6()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_6()


def actions_7():
    """ Prints out the menu for input action to move in the map at Level 7 """
    print("""
        LEVEL 7
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" wall ahead ")
        actions_7()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_7()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_7()
    if action_input.lower() in valid_actions[3]:
        print(f" turn right towards the exit ")
        actions_8()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 7"]
        print(y)
        actions_7()
    if action_input.lower() in valid_hint_2[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight and gives you a hint for your next
      direction. The direction is right.
      Enter right when the menu restarts. """)
    if action_input.lower not in valid_hint_2:
        print("Invalid direction!")
        actions_7()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_7()


def actions_8():
    """ Prints out the menu for input action to move in the map at Level 8 """
    print("""
        LEVEL 8
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" wall ahead ")
        actions_8()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_8()
    if action_input.lower() in valid_actions[2]:
        print(f" Turn left. You are getting closer!")
        actions_9()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_8()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 8"]
        print(y)
        actions_8()
    if action_input.lower() in valid_hint_2[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight and gives you a hint for your next
      direction. The direction is left.
      Enter left when the menu restarts. """)
    if action_input.lower not in valid_hint_2:
        print("Invalid direction!")
        actions_8()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_8()


def actions_9():
    """ Prints out the menu for input action to move in the map at Level 9 """
    print("""
        LEVEL 9
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f""" You found the exit! """)
        end_script()
        quit()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_9()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_9()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_9()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions[5]:
        y = location["line 9"]
        print(y)
        actions_9()
    if action_input.lower() in valid_hint_2[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight and gives you a hint for your next
      direction. The direction is forward.
      Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint_2:
        print("Invalid direction!")
        actions_9()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_9()


while True:
    if inventory_input == "Batman":
        character_intro()
        player_inventory("Batman", inventory)
        character_inventory("Batman", character)
        action_1()
        action_2()
        action_3()
        action_4()
        action_5()
        action_6()
        action_7()
        action_8()
        action_9()
        quit()
    if inventory_input == "Green Lantern":
        character_intro_2()
        player_inventory("Green Lantern", inventory)
        character_inventory_2("Green Lantern", character_2)
        actions_1()
        actions_2()
        actions_3()
        actions_4()
        actions_5()
        actions_6()
        actions_7()
        actions_8()
        actions_9()
        quit()
    else:
        print("invalid action")
        os.execl(sys.executable, sys.executable, *sys.argv)