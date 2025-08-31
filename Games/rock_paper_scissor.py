# Building Rock Paper Scissor Game
import random
print("Wellcome to Rock Paper Scissor Game")
print("You have 10 rounds to paly")
print("Type 'end' to exit the game")
options = [ "rock", "paper", "scissor"]
user_score = 0
computer_score = 0
tie_score = 0

for round_number in range(1,11):
    print(f"-----Round Number {round_number}-----")
    user_choice = input("Please choose (Rock / Paper / Scissor) : ").lower()

    
    if user_choice == "end":
        print("Game Ended")
        break
    elif user_choice not in options:
        print("❌ Invalid Option. Please choose (Rock / Paper / Scissor)")
        continue
    computer_choice = random.choice(options)
    
    print(f"User Choice : {user_choice.capitalize()}")
    print(f"Computer Choice : {computer_choice.capitalize()}")
    
    if user_choice == computer_choice:
        print("It's Tie")
        tie_score +=1
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
         print("🎉 User win this round")
         user_score +=1
    else:
        print("🎉 Computer wins this round")
        computer_score +=1
        
print("======FINAL SCORE======")
print(f"User wins : {user_score}")
print(f"Computer wins : {computer_score}")
print(f"Tie : {tie_score}")

if user_score > computer_score:
    print(f"User wins the game")
elif user_score < computer_score:
    print(f"Computer wins the game")
elif user_score == computer_score:
    print(f"It's Tie")
else:
    print("System error")
        
print("Game End. Thank you for playing")
