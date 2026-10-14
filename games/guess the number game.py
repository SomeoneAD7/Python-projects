import random

num = random.randint(0, 4) 
tries = 0
answered = False 

try: 
    print("""Welcome toooooooo Guess The Lucky Number. 
From one to hundred, guess the number right and win. 
          """) 

    while tries < 5 and not answered:
        guess = int(input("> "))
        tries += 1

        if guess == num:
            print("Correct! You win. ")
            answered = True  

        elif tries < 5:
            print("Wrong! Try again.")

        else:
            print("Still wrong!!! You lose. ")  

except ValueError:
    print("Enter an integer. ") 

except KeyboardInterrupt:
    print("Error occured. We've closed. Try again later. ")  
