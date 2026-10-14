import random 

options = ["rock", "paper", "scissors"] 
player = 0
computer = 0 
tries = 0 


try: 
    print("""Welcome toooooooo Rock, Paper, Scissors.    
    Make the right choice and win.    
            """) 

    while tries < 5: 
        choice = str(input("> ")).lower()
        ran_opt = random.choice(options).lower()  
        tries += 1 

        if choice.lower() == ran_opt.lower(): 
            print(f"You both played {ran_opt} and {choice}. ") 

        elif choice.lower() == options[0] and ran_opt.lower() == options[1]:
            print(f"The computer plays {ran_opt} and wins.")
            computer += 1 

        elif choice.lower() == options[0] and ran_opt.lower() == options[2]: 
            print(f"You beat {ran_opt}! ") 
            player += 1

        elif choice.lower() == options[1] and ran_opt.lower() == options[0]:
            print(f"You beat {ran_opt}! ")  
            player += 1 

        elif choice.lower() == options[1] and ran_opt.lower() == options[2]:
            print(f"The computer plays {ran_opt} and wins.") 
            computer += 1 

        elif choice.lower() == options[2] and ran_opt.lower() == options[0]:
            print(f"The computer plays {ran_opt} and wins.") 
            computer += 1 

        elif choice.lower() == options[2] and ran_opt.lower() == options[1]:
            print(f"You beat {ran_opt}! ") 
            player += 1 

        else:
            print("Make a valid choice. ")  

    if tries >= 5:
        print("\nGame has ended. ")
        if player > computer:
            print("You won!!! =) ") 

        elif computer > player:
            print("The computer won. :( ") 

        elif player == computer:
            print(f"You drew with {player} points. ")  

        else:
            print("Winner cannot be determined. ") 

except ValueError:
    print("Make a valid choice dude. ") 
     
except KeyboardInterrupt:
    print("Error occured. We've closed. Try again later. ")  

