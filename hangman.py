from ntpath import join
from turtle import right
from en_words import words
import operator

def hangman():
    judge_ans=0
    judge=False
    ans_list=list(words())
    print(str(ans_list))
    wrong_list=[]
    right_list=[]
    lives=7
    word_len=len(ans_list)
    for i in range(word_len):
        right_list.append('_')

    while lives!=0:
        print(f'Your lives : {lives}')
        guess=input('guess a character:(a~z)\n').lower()
        if guess in wrong_list:
            print("You have been guessed {}".format(guess))
            continue

        judge=False
        
        for i in range(word_len):
            if guess in ans_list:
                if ans_list[i]==guess:
                    right_list[i]=guess
                judge=True
        if operator.eq(''.join(right_list),(''.join(ans_list))):
            print(f"You're winner. {' '.join(right_list)}\n")
            break
        else:
            print(f'Guess right characters and location: {" ".join(right_list)}\n')

        if not(judge):
            wrong_list.append(guess)
            lives-=1
            print(f'You have guessed:{",".join(wrong_list)}. Those are not in answer\n')
    if lives==0:
        print(f"You lose the game. The answer is {''.join(ans_list)}")




hangman() 