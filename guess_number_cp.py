import random

def guess(x):
    ans=random.randint(1,x)
    guess=0
    while guess!=ans:
        guess=int(input(f'Guess a number betweem 1 and {x}:'))
        
        if guess>ans:
            print(f'your guessing {guess} is higher answer.')
        elif guess<ans:
            print(f'your guessing {guess} is lower answer.')
    print(f'Yes!The answer is {ans}')



guess_range=int(input("input a guess range:"))
guess(guess_range)