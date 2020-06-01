from termcolor import cprint
from entity import Entity
from samurai import Samurai
import pyfiglet
from time import sleep
import random
import sys
import subprocess
def type_key(str):
    for i in str:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(random.uniform(0.06, 0.09))


def get_name():
    type_key("\nEnter name: ")
    user_name = input(" ")
    subprocess.call(["clear"])
    return user_name
name = get_name()
player = Samurai(name, health=150, attack_damage=30)
class gameLogic:
    def title_screen(self):
        cprint(pyfiglet.figlet_format("The Ronin", "Slant"), "red", attrs=["bold"])
        type_key("浪人はパトリックストーリーによって書かれたテキストベースのゲームです \n")
        print('                                 /)  ')
        print('                                //  ')
        print('              __*_             //  ')
        print('           /-(____)           //  ')
        print('          ////- -|\          //  ')
        print('       ,____o% -,_          //  ')
        print(r'     /  \\   |||  ;        //  ')
        print('     /____\....::./\      //  ')
        print('    _/__/#\_ _,,_/--\    //  ')
        print('    /___/######## \/""-(\ /)')
        print('   /___\  __  /___\/     |  ')
        print(r'  /____\\__//____\    ___|  ')
        cprint("\n[A] START \n", "red", attrs=["bold","blink"])
        cprint("[B] CREDITS \n", "red", attrs=["bold"])
        cprint("[C] EXIT \n", "red", attrs=["bold"])
        title_input = input("IN:  ")
        if title_input == "A" or title_input == "a":
            subprocess.call(["clear"])
            return True
        elif title_input == "B" or title_input == "b":
            cprint("\nGame Author: Patrick Story", "red")
            cprint("ASCII Art Author:  Tua Xiong", "red")
            cprint("ASCII Art location:  https://www.oocities.org/spunk1111/tuax.html \n", "red")
            return False
        elif title_input == "C" or title_input == "c":
            type_key("\nExiting game...  \n")
            type_key("Bye :C \n")
            return False
        else:
            cprint("\n[ERROR] Invalid Input. ", "blue", attrs=["bold"])
            cprint("Enter A, B or, C ", "blue", attrs=["bold"])
            return False
    def intro(self):
        type_key("\nA samurai has fallen in battle. ")
        sleep(1)
        type_key("\nNow he must face the ghosts of the men he has killed and win lest his soul be lost\n\n")
        sleep(1)
        output_file("beast.txt")
        cprint("\n" + player.name + " sets off in search of a way out \n", "magenta", attrs=["bold"])
        input("Press enter to continue... ")
        subprocess.call(["clear"])
    def part_one(self):
        cprint(pyfiglet.figlet_format("A BEAST APPEARS "), "red", attrs=["bold", "blink"])
        output_file("mon.txt")
        beast = Entity(name="Beast", health=100, attack_damage=30)
        beast.stats()
        print("\n")
        player.stats()
        cprint("\nWhat will " + player.name + " do? ", "magenta", attrs=["bold"])
        battle(player, beast)
def output_file(file):
    Ofile = open(file, "r")
    for line in Ofile.readlines():
        sleep(random.uniform(0.01, 0.05))
        print(line.strip("\n"))

def battle( player, enemy):
    while player.isalive() and enemy.isalive():
        player.display_moves()
        type_key("Make your move " + player.name + ": ")
        player_move = input("")
        player.move(player_move, enemy)
