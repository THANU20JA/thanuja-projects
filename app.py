"""
Python Number Guessing Game
A simple console-based game where the user guesses a randomly generated number.
"""

from random import randrange

def play_guessing_game():
    """
    Main function to play the number guessing game.
    The computer generates a random number between 1 and 100,
    and the user has to guess it.
    """
    # Generate a random number between 1 and 100
    computer_guess = randrange(1, 100)
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print("I've selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            # Get user input
            user_input = input("\nEnter your guess (1-100): ")

            # Check if user wants to quit
            if user_input.lower() in ['quit', 'exit', 'q']:
                print(f"Game over! The number was {computer_guess}.")
                break

            # Convert input to integer
            user_guess = int(user_input)
            attempts += 1

            # Check the guess
            if user_guess < computer_guess:
                print("📉 Too low! Try a higher number.")
            elif user_guess > computer_guess:
                print("📈 Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed it right!")
                print(f"It took you {attempts} attempts.")
                break

        except ValueError:
            print("❌ Please enter a valid number between 1 and 100.")
        except KeyboardInterrupt:
            print(f"\nGame interrupted! The number was {computer_guess}.")
            break

def main():
    """Main function to run the game."""
    print("=" * 50)
    play_guessing_game()
    print("=" * 50)

if __name__ == "__main__":
    main()
        
        
