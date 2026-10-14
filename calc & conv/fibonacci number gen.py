def fib_seq(n):
    fib = [0, 1] 
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2]) 
    return fib[:n] 

print("""Welcome to my fibonacci sequence generator. 
Just give me any number and I'll generate it's sequence =) """) 

num = int(input("> ")) 

print(fib_seq(num)) 
