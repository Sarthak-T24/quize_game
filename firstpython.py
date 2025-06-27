import random
import time
from datetime import datetime

# Ask for player's name
player_name = input("Enter your name: ")
start_time = datetime.now()  # Get current date and time
print(f"Quiz started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

score = 0  # Initial score

while True:
    root = random.randint(1, 100)
    number = root ** 2

    print(f"What is the square root of {number}?")
    question_start = time.time()

    try:
        user_answer = int(input("Your answer: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        continue

    question_end = time.time()
    time_taken = round(question_end - question_start, 2)

    if user_answer == root:
        print("✅ Correct!")
        score += 10
    else:
        print(f"❌ Wrong! The correct answer is {root}")
        score -= 5

    print(f"Time taken: {time_taken} seconds")
    print(f"Your current score is: {score}")

    # 🎯 Winner check: If score >= 50, show winner and exit
    if score >= 50:
        print(f"\n🎉 Congratulations {player_name}, You are the WINNER! 🎉")
        print(f"🏁 Final score: {score}")
        end_time = datetime.now()
        print(f"Quiz ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        break

    # Ask if user wants to continue
    cont = input("\nDo you want to continue the quiz? (yes/no): ").strip().lower()
    if cont != "yes":
        end_time = datetime.now()
        print(f"\nThanks for playing, {player_name}! 🎉 Your final score is: {score}")
        print(f"Quiz ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        break
