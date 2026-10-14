print("""Welcome to my special calculator. 
Just enter your number and it will find it's summation. 
""") 

num = int(input("> ")) 

sum = 0
for i in range(num + 1):
    sum += i 

print(sum) 
      