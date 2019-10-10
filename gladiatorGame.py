'''
    Main file/loop for gladiator game
'''

from cLibrary import *
from itemLibrary import *
from buildItems import * # Also runs file. Builds items 

def build_name_lst(filename):
    name_lst = []
    for line in open(filename):
        name_lst += [line.strip()]

    return name_lst


def generate_rnd_enemy_atb(atb_scale):
    atb = []
    for el in range(5):
        atb.append(r.randint(1, scale))
    
    return Attibutes(atb[0], atb[1], atb[2], atb[3], atb[4])


player_equip = Equipment(ironSwd, chainCP, chainLG, ironSH, chainHM)
player_stats = Attibutes(10, 10, 10, 10, 5)
player = Player("Player", player_equip, player_stats, "Location")

name_lst = build_name_lst('names.txt')

oppFirst_equip = Equipment(bronzeSwd, leatherCP, leatherLG, woodSH, leatherHM)

scale = int(input("Enemy scale?"))

while scale != -1:

    rnd_nm_idx = r.randint(0, len(name_lst)-1)
    rnd_name = name_lst[rnd_nm_idx]

    opp1 = Opponent(rnd_name, oppFirst_equip, generate_rnd_enemy_atb(scale))

    fight = Battle(player, opp1, "the Thunderdome!")
    fight.main_loop()

    scale = int(input("Enemy scale?"))
