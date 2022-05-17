import random

def play():
    play=input("what's your choice? 'r' for Rock ,'p' for Pepper , 's' for Sissors:\n").lower()
    cp=random.choices(['r','s','p'])
    print(f'({play},{cp})')
    if play==cp:
        print('This game ended in a tie.')
    elif win(play,cp):
        print("This game's winner is you")
    else:
        print("This game's loser is you")


def win(player,oppnent):
    # p>r r>s s>p
    if(player=='p'and oppnent=='r')or(player=='r'and oppnent=='s')or(player=='s'and oppnent=='p'):
        return True

play()