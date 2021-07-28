import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def retry_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            return response
        elif option2 in response:
            return response


def valid_input(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            return response
        elif option2 in response:
            return response
        elif option3 in response:
            return response
        else:
            print_pause("Try again.")


def intro():
    print_pause("An alarm sound in the background, you find"
                " yourself running away from security"
                " drones trying to hide.")
    print_pause("Pokémons are fainted and escaping"
                " Team Rocket's hideout"
                " is not gonna be easy.")
    print_pause("Across the hallway "
                "one of Giovanni's grunts"
                " makes an attempt to catch you.")


def fight(items):
    print_pause("You knocked him out.")
    print_pause("You searched his body.")
    print_pause("-Found Security_Card-")
    items.append("Security_card")


def evade():
    print_pause("You dodged him and got away""!")


def turn_around():
    print_pause("You've turned around and found yourself"
                " surrounded by Team Rocket Elite's.")
    print_pause("Game over!")
    play_again()


def first_encounter(items):
    first_choice = valid_input("1.Turn around.\n"
                               "2.Try evade him.\n"
                               "3.Fight him.\n",
                               "1", "2", "3").lower()
    if first_choice == '1':
        turn_around()
    elif first_choice == '2':
        evade()
    elif first_choice == '3':
        fight(items)


def second_encounter(items):
    print_pause("Along the way you see"
                " a high-level security door.")
    if "Security_card" in items:
        print_pause("-Used Security_card"
                    " to open the door-")
        print_pause("Looking around for something"
                    " you can use, you see "
                    "a bunch of Pokéballs in a lab.")
        print_pause("You reach for a Pokéball.")
        print_pause("-Obtained Pokéball-")
        items.append("Pokéball")
    else:
        print_pause("The door is locked.")
        print_pause("You run into a dead end"
                    " and get captured.")
        print_pause("Game over!")
        play_again()


def last_encounter():
    pokemon = ["Electrode", "Mewtwo", "Magikarp"]
    pk = random.choice(pokemon)
    print_pause("Making your way out the enemy"
                " finally catches up to you.")
    print_pause("Looks like we have to fight.")
    print_pause("You throw the Pokéball and its...")
    print(pk)
    if pk == "Electrode":
        print_pause("Electrode use Self-destruct!")
        print_pause("You use the explosion"
                    " to cover your escape.")
        print_pause("You won!")
        play_again()
    elif pk == "Mewtwo":
        print_pause("Mewtwo uses Psychic and Teleport!.")
        print_pause("You're back in town.")
        print_pause("You won!")
        play_again()
    elif pk == "Magikarp":
        print_pause("Magikarp use Splash!")
        print_pause("Nothing happens.")
        print_pause("You get surrounded and captured.")
        print_pause("Game Over!")
        play_again()


def play_again():
    response = retry_input("Would you like to play again? "
                           "Please say 'yes' or 'no'.\n",
                           "yes", "no").lower()
    if "yes" in response:
        print_pause("Very good.")
        game()
    elif "no" in response:
        print_pause("Ok, goodbye!")
        exit()


def game():
    items = []
    intro()
    first_encounter(items)
    second_encounter(items)
    last_encounter()


game()
