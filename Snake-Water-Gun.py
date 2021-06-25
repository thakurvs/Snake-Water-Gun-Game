import random
import playsound

def winning_music():
    win_music = ["anime wow.mp3", "bruhh.mp3"]
    try:
        playsound.playsound(random.choice(win_music))
    except Exception as e:
        print(e)

def losing_music():
    lose_music = ["Nope.mp3", "Fart.mp3"]
    try:
        playsound.playsound(random.choice(lose_music))
    except Exception as e:
        print(e)

def tie_music():
    tie = ["Awkward Cricket.mp3"]
    try:
        playsound.playsound(random.choice(tie))
    except Exception as e:
        print(e)
if __name__ == "__main__":
    print("Welome To Snake Water Gun Game\n")
    attempt = 1
    computer_point = 0
    your_point = 0
    while(attempt <= 10):
        lst = ["Snake", "Water", "Gun"]
        a = random.choice(lst)

        choice = input("Enter your choice\nSnake\nWater\nGun\n")

        if choice == a:
            print("Draw")
            print(f"You choose {choice} and computer choose {a}")
            print("No one gets point\n")
            tie_music()

        elif choice == "Gun" and a == "Snake":
            print(f"You choose {choice} and computer choose {a}")
            print("Gun kill the snake")
            print("You won this round,you got 1 point\n")
            your_point = your_point + 1
            winning_music()

        elif choice == "Snake" and a == "Gun":
            print(f"You choose {choice} and computer choose {a}")
            print("Gun kill the snake")
            print("computer won this round,computer got 1 point\n")
            computer_point = computer_point + 1
            losing_music()

        elif choice == "Snake" and a == "Water":
            print(f"You choose {choice} and computer choose {a}")
            print("Snake drank water")
            print("You won this round,you got 1 point\n")
            your_point = your_point + 1
            winning_music()

        elif choice == "Water" and a == "Snake":
            print(f"You choose {choice} and computer choose {a}")
            print("Snake drank water")
            print("computer won this round,computer got 1 point\n")
            computer_point = computer_point + 1
            losing_music()

        elif choice == "Water" and a == "Gun":
            print(f"You choose {choice} and computer choose {a}")
            print("Gun sank into water")
            print("You won this round,you got 1 point\n")
            your_point = your_point + 1
            winning_music()

        elif choice == "Gun" and a == "Water":
            print(f"You choose {choice} and computer choose {a}")
            print("Gun sank into water")
            print("computer won this round,computer got 1 point\n")
            computer_point = computer_point + 1
            losing_music()

        else:
            print("Error!! Invalid Input")
            continue

        print("No. of attempt left", 10 - attempt)
        attempt += 1

        if attempt > 10:
            print("Game Over")

    print(f"Your score: {your_point}")
    print(f"Computer score: {computer_point}")
    if your_point > computer_point:
        print("You won and Computer lost")
        winning_music()
    elif your_point < computer_point:
        print("Computer won and You lost")
        losing_music()
    else:
        print("Oops!! It was a draw")
        tie_music()

