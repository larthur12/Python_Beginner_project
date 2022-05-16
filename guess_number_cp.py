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


def guess_computer(x):
    cp_status=''
    ans=int(input('input your answer:'))
    high=x
    low=1
    while cp_status!='c':
        if high != low:
            guess_cp=random.randint(low,high)
        else:
            guess_cp-=1
            
        cp_status=input(f'the answer {guess_cp} is correct(c) , lowwer(l) or higher(h)').lower()
        if cp_status=='h':
            high =guess_cp-1
        elif cp_status=='l':
            low=guess_cp+1
    print('Computer have guessed the number correctly')

        


guess_range=int(input("input a guess range:"))
# guess(guess_range)
guess_computer(guess_range)