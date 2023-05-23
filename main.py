import random


"""MadLib"""


def madlib():
    colour = input("Colour: ")
    number = input("Number: ")
    plural_noun = input("Plural noun: ")
    place = input("Place: ")
    colour_2 = input("Colour: ")
    plural_noun_2 = input("Plural noun: ")
    verb = input("Verb/Action: ")
    sentence = (f"Sonic has a/an {colour} Ping-Pong table where he plays against ... himself. (His record is {number}\n"
                f"wins and zero losses!) And for that final touch, Sonic hung {plural_noun} all over his room walls.\n"
                f"He's got a photo of (the) {place} next to a poster of {colour_2} {plural_noun_2}. It may not be\n"
                f"much, but Sonic loves to {verb} in his room all the time!")
    print(sentence)
    play_again_or_menu(madlib)


"""Project 2 - User guesses number"""


def user_guesses_int():
    x = int(input("What is the maximum number the computer can pick? "))
    random_number = random.randint(1, x)
    pick_number = int(input(f"Guess a number between 1 and {x}: "))
    i = 1
    while pick_number != random_number:
        i += 1
        if pick_number < random_number:
            print("Higher")
        elif pick_number > random_number:
            print("Lower")
        pick_number = int(input("New guess: "))

    print(f"Yay ! You have guessed the correct number in {i} tries !")
    play_again_or_menu(user_guesses_int)


"""Project 3 - Computer guesses number"""


def computer_guesses_int():
    x = 1
    y = int(input("What is the maximum number the computer can try? "))
    i = 1
    print("Help me by typing  '+', '-' or '=' after each guess.")
    answer = "unknown"
    while answer != "=":
        random_number = random.randint(x, y)
        answer = input(f"Is it {random_number} ?")
        if answer != "=" and x == y:
            print(f"You must have made a mistake in the guidance, because {random_number} is the only choice left !")
        elif answer == "+":
            x = random_number + 1
            i += 1
        elif answer == "-":
            y = random_number - 1
            i += 1
        elif answer == "=":
            break
        else:
            answer = input(f" This is not a suitable answer, is it {random_number} ? '+', '-' or '=' ")

    print(f"Yay ! I have guessed the correct number in {i} tries !")
    play_again_or_menu(computer_guesses_int)


"""Project 4 - Rock, Paper, Scissors"""


def rock_paper_scissors():
    print("Not out yet.")
    play_again_or_menu(rock_paper_scissors)


"""General methods"""


def play_again_or_menu(game_name):
    play_again = input("Do you want to play again ? 'y/n'")
    if play_again == "Yes" or play_again == "yes" or play_again == "y":
        game_name()
    elif play_again == "No" or play_again == "no" or play_again == "n":
        print("Bye, then !\n")
        main_menu()


def main_menu():
    user_choice = input("Welcome to the main menu.\n\n"
                        "01 - MadLib\n"
                        "02 - User guesses a number\n"
                        "03 - Computer guesses a number\n"
                        "99 - Exit\n"
                        "What project do you want to open?\n")
    if user_choice == "1" or user_choice == "01":
        madlib()

    elif user_choice == "2" or user_choice == "02":
        user_guesses_int()

    elif user_choice == "3" or user_choice == "03":
        computer_guesses_int()

    elif user_choice == "4" or user_choice == "04":
        rock_paper_scissors()

    elif user_choice == "99":
        print("See you later!")
        exit()

    else:
        print("Not out yet")
        main_menu()


main_menu()
