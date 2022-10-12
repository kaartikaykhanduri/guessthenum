import random
n = random.randrange(1,100)
guess = int(input("guess and enter any number between 1 to 100 "))
guessno = 0
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("WRONG GUESS! "))
        guessno+=1
    elif guess > n:
        print("Too high!")
        guess = int(input("WRONG GUESS! "))
        guessno+=1

    else:
        break
print("you guessed it right! in",guessno, "turns")