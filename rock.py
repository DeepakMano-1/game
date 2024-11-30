import random

def play():
    while True:
        player = input("Enter rock(r), paper(p), scissor(s), or q to quit: ").lower()
        if player == 'q':
            print('thanks for playing✨.')
            break
        elif player not in ['r', 'p', 's']:
            print("Invalid input. Please try again.")
            continue

        choices = ['r', 'p', 's']
        computer = random.choice(choices)
        print(f"\nYou chose {player}, computer chose {computer}.\n")

        if player == computer:
            print(f"Both players selected {player}. It's a tie😮!")
        elif player == 'r':
            if computer == 's':
                print("Rock smashes scissors! You win🎉!")
            else:
                print("😢Paper covers rock! You lose.")
        elif player == 'p':
            if computer == 'r':
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif player == 's':
            if computer == 'p':
                print("Scissors cuts paper! You win🤩!")
            else:
                print("😌Rock smashes scissors! You lose.")

        play_again = input("Play again? (y/n): ").lower()
        if play_again == 'y':
                pass
        elif play_again == 'n':
                break

play()
