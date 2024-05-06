# source venv/bin/activate

import os
import time
from colorama import Fore

t = "Tank"
p = "\U0001F681"
sb = ""
sa = ""
ground = ""
sky = ""
str_space_left = ""
long_game = 70
bool_tank_destroy = None
bool_choose_system = None

t_R="\033[31m"
t_G="\033[32m"
t_Y="\033[33m"
t_B="\033[36m"
bg_G="\033[42m" #- зелёный
bg_LB="\033[46m" #- голубой
bg_B="\033[44m" #- синий
bg_R="\033[41m"
bg_W="\033[47m"
def_col="\033[0m" #- сбросить все до значений по умолчанию

banner="Air striker"
for i in range(1, long_game - len(banner) ):
    str_space_left += " "

name_game = f"{banner}"
os.system('cls||clear')

introduction = f"{t_G}Pilot, you need to destroy the tank. All hope is for you. Choose the right time of attack and destroy the target.\nTaking into account weather conditions, the time of attack varies from {t_Y}1{t_G} to {t_Y}{long_game}{t_G}.\n\nComplete the task and return to base.{def_col}"
# introduction = f"{t_G}You need... "
for i in range(1, len(introduction)):
    os.system('cls||clear')
    if i % 2 == True:
        indicate = f"{t_G}#"
    else:
        indicate = f"{def_col}#"

    print(f"{str_space_left}{t_R}>>>>{t_B} {name_game} {t_R}<<<<{def_col}\n")

    print(f"{t_G}{introduction[0:i]}{indicate}\n")

    time.sleep(0.05)
time.sleep(2)
os.system('cls||clear')

print(f"{str_space_left}{t_R}>>>>{t_B} {name_game} {t_R}<<<<{def_col}\n")
start_atack = int(input(f"{t_G}Pilot indicate time of attack ({t_Y}1{t_G} to {t_Y}{long_game}{t_G}):{def_col} "))

for a in range(1, long_game):
        sa += " "
        sky += "  "
        ground += "~~"

for i in range(1, long_game):
    print(f"{str_space_left}{t_R}>>>>{t_B} {name_game} {t_R}<<<<{def_col}\n")
    print(bg_LB, sky, def_col)
    if i < start_atack:
        print(sa *2 ,p ,sep="")
        print("")
        print("")
        print("")
        print("")
        print(sb, t, sep="")
    elif i < start_atack + 2:
        print("")
        print(sa *2 ,p ,sep="")
        print("")
        print("")
        print("")
        print(sb, t, sep="")
    elif i < start_atack + 4:
        print("")
        print(sa *2 ,p ,sep="")
        print(sa*2,"-")
        print("")
        print("")
        print(sb, t, sep="")
    elif i < start_atack + 6:
        print("")
        print(sa *2 ,p ,sep="")
        print("")
        print(sa*2,"-")
        print("")
        print(sb, t, sep="")
    elif i < start_atack + 7:
        print("")
        print(sa *2 ,p ,sep="")
        print("")
        print("")
        print(sa*2,"-")
        print(sb, t, sep="")
    elif i < start_atack + 8:
        print("")
        print(sa *2 ,p ,sep="")
        print("")
        print("")
        print("")
        if ( len(sa*2) == len(sb)): 
            print(sa*2,t_R,"W", def_col)
            bool_tank_destroy = True
        else: 
            print(sb, t, sep="")
    else:
        print(sa *2 ,p ,sep="")
        if bool_tank_destroy == True:
            t = ""
            print("")
            print(f"{str_space_left}\t{t_G}You WIN!{def_col}  ")
            print("")
            print("")
            print(sb, t, sep="")
            bool_game_win = True

        else:
            print("")
            print(f"{str_space_left}\t{t_R}You LOSE!{def_col}  ")
            print("")
            print("")
            print(sb, t, sep="")
            
    print(bg_G,t_G, ground, def_col)
    
    sb = sb + " "
    sa = sa[:-1]
    
    time.sleep(0.15)
    os.system('cls||clear')

