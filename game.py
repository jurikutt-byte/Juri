# game.py
"""
Arvuti mõeldud number on vahemikus 1-100 k.a
loendame samme. MÄng lõpeb kui on sisestatud 
õige number. 
TÄEINDUS: Kui mäng saab läbi, siis küsi kasutajalt kas mängida veel. Kui Jah (jj), siis resetti andmed, ja alusta 
uut mängu
"""
from random import randint

pc_nr = randint(1,100)
steps = 0
game_over = False
# Game_over = false 
# means game over which is defined as, under the false function

# print(pc_nr) # debug tool

def ask():
    """küsib mängjalt arvu ja kontrollib vastust"""
### Mis vahe on jutumärkide ja hashmarkidega??? 

    global steps, game_over
    # Kontrolli functsiooni
    User_nr = int(input('Sisesta number [1-100]: '))
    steps += 1 # steps = steps + 1
    # Steps = steps +1, või steps += 1 on sama. Vali lemmik
# Arvuti arvab numbri, pead ise panema arvu vastavalt arvuti numbrile.
    if User_nr == 1000:
        print('Leidsid tagaukse. Õige number on ' + str(pc_nr))
              
    if User_nr > pc_nr:
        print('Väiksem')
    elif User_nr < pc_nr:
        print('Suurem')
    elif User_nr == pc_nr:
        print(f'Arvasid numbri ära {steps} sammuga.')
        game_over = True
    return game_over


### Treppid on ÜLI TAHTSAD, ALATI LAS OLLA SAMAS TREPPIS MIS VAJA, OR IS RELEVANT TO THE CODE BELOW, OR ABOVE!!!


def lets_play():
    """Käivitab äraarvamise mängu + küsib kas tahad edasi mängida """

    global game_over, steps, pc_nr

    while not game_over: 
            ask()
    answer = input('Play again? [Y/N]')
    if answer in ['Y','y']: # answer.lower() == 'y'
        pc_nr = randint(1,100)
        steps = 0
        game_over = False
        lets_play()


lets_play()
print('You Win')
 

