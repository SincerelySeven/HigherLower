import random
import art
from game_data import data

# Code in main.py written by Seven Rocks
# art.py, game_data.py, and project concept from Angela Yu's 100 Days of Code program.

# Higher/Lower is a game in which the player has to guess which one of two subjects has a higher follower number.

def print_item(start, item, letter):
    """
    Prints out the items to compare.
    :param start: The start of the sentence ("Compare" or "Against")
    :param item: The item being printed.
    :param letter: The letter for comparison.
    :return: Nothing.
    """
    print(f"{start} {letter}: {item["name"]}, a {item["description"]}, from {item["country"]}")

def check_answer(a, b, answer):
    """
    Returns if the player was correct in their guess.
    :param a: Item A being compared.
    :param b: Item B being compared.
    :param answer: The answer the user chose ('a' or 'b')
    :return: Returns true if the answer was correct, else false.
    """
    if a["follower_count"] >= b["follower_count"] and answer == "a" or a["follower_count"] <= b["follower_count"] and answer == "b":
        return True
    else: # else keyword not necessary, but more readable
        return False

def game():
    """
    The core game loop.
    :return: Nothing.
    """

    print(art.logo)

    score = 0 # keeps track of number of wins
    current = random.choice(data) # get the first item

    correct = True

    while correct: # keep going until the player is wrong
        print_item("Compare", current, "A")

        print(art.vs)

        # get the new challenger
        opposite = random.choice(data)
        while opposite == current: # avoid duplicate item
            opposite = random.choice(data)

        print_item("Against", opposite, "B")

        # get user input for their guess (can be lowercase or uppercase A and B)
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        while not (answer == "a" or answer == "b"): # keep trying for valid response
            print("Invalid response.")
            answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        # determine whether the player was correct or not
        correct = check_answer(current, opposite, answer)

        # the logo is printed before telling the player if they were correct or not (as the example program does)
        print("\n" * 20)
        print(art.logo)

        # set the opposing item to the current for the next round
        current = opposite

        # handle the score if correct, or exit if incorrect
        if correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")

        # if incorrect, the while loop ends here and returns to the code below, otherwise we loop

#main:

keep_playing = True
while keep_playing: # while the user wants to keep playing, loop
    game()
    keep_playing = input("Keep playing? Type 'y' or 'n': ") == "y"
    print("\n" * 20) # clears screen enough