from random import randint

n = 500
count = 0 #number of free chocolates
trials = 0

while trials < n:
    a = randint(1, 5)
    if a == 1:
        count += 1
    trials += 1

print(n/count)
    
    
