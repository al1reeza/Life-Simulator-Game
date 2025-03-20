import random

# Our starting charactersitics (Scores are out of 100)
starting_characteristic = {
    "wealth": 50,
    "relationships": 50,
    "purpose": 50,
    "health": 50
}

# Our choices and resulting outcomes
choices = [
    {"description": "Work overtime for extra money", 
     "effects": {
        "wealth": +10,
        "health": -5, 
        "relationships": -5
        }
    },
    {"description": "Spend time with friends and family", 
     "effects": {
        "wealth": -5,
        "relationships": +10 
        }
    },
    {"description": "Pursue your dreams", 
     "effects": {
        "purpose": +10,
        "wealth": -5
        }
    },
    {"description": "Go to the gym", 
     "effects": {
        "health": +10,
        "wealth": -5
        }
    },
]

# Our random events and resulting outcomes
random_outcomes = [
    {"description": "You got sick!",
     "effects": {"health": -20}
    },
    {"description": "You won the lottery!", 
     "effects": {"wealth": +20}
    },
    {"description": "Your bestfriend passed away!", 
     "effects": {
        "purpose": -20, 
        "relationships": -10
        }
    },
    {"description": "You reconnected with an old friend!", 
     "effects": {"relationships": +20}
    },
    {"description": "You were kicked out of your job!", 
     "effects":{
        "relationships": -10,
        "purpose": -10,
        "wealth": -30
        }
    }
]

# This will be our main method, which is where everything happens
def main():
    print("Welcome!\nIn this game you will be living life all over again!" +
    "Your goal in this game is to balance your life in terms of wealth, relationships, purpose, and health!"+
    "\nLets see how you do!!!")
    game()
    print(f"\nGame Over! Your final characterisitcs: {starting_characteristic}")

# Here the game will happen
def game():
     global starting_characteristic, choices, random_outcomes
     # Every player gets 50 rounds, which represent years 
     for round in range(1, 50):
        print(f"\nRound {round}!")
        # This will print our starting characteristics
        print(f"Current characteristics: {starting_characteristic}")
        # Present choices
        print("\nChoose an action:")
        # Loops through and prints our choice options
        for i, choice in enumerate(choices):
            print(f"{i + 1}: {choice['description']}")
        # The player chooses what choice they want
        choosen_num = int(input("Please enter which choice, by its respective number, " +
        "you want to choose (1 through 4): "))
        while choosen_num > 4 or choosen_num <= 0:
            choosen_num = int(input("Please make sure your index is between 1 and 4"))
        choosen_choice = choices[choosen_num - 1] # Our choice
        # The effects of the choice will be applied
        for charactersitic, effect in choosen_choice["effects"].items():
            starting_characteristic[charactersitic] += effect
            # Makes sure the player never exceeds the maximum score
            if(starting_characteristic[charactersitic] >= 100):
                starting_characteristic[charactersitic] = 100
        # This will be the random event
        happening = random.random() < .6 # This will tell us if our random event will happen (60% chance)
        if happening:
            # Picks on random what random thing happens
            random_num = random.randint(0,4)
            # The effects of the random outcome will be applied
            random_result = random_outcomes[random_num]
            print(random_result["description"])
            for characteristic, effect in random_result["effects"].items():
                starting_characteristic[characteristic] += effect
                # Makes sure the player never exceeds the maximum score
                if(starting_characteristic[charactersitic] >= 100):
                    starting_characteristic[charactersitic] = 100
        # If any of the characteristics becomes less than 0
        if any(value < 0 for value in starting_characteristic.values()):
            print("You lost!")
            break

# Runs the main method
if __name__ == "__main__":
    main()