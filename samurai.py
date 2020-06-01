from entity import Entity
from termcolor import cprint
import random
class Samurai(Entity):
    def slash(self, opponent):
        cprint(self.name + " slashes " + opponent)
        damage = self.attack_damage + 5
        return damage
    def jab(self, opponent):
        damage_plus = random.randint(0, 45)
        cprint(self.name + " jabs " + opponent)
        if damage_plus == 0:
            cprint(self.name + " missed! ")
            return self.attack_damage - self.attack_damage
        else:
            damage = self.attack_damage + damage_plus
            return damage
    def display_moves(self):
        cprint("[A] heal", "red")
        cprint("[B] slash", "red")
        cprint("[C] jab", "red")
    def move(self, choice, enemy):
        if choice == "A" or choice == "a":
            self.heal()
        elif choice == "B" or choice == "b":
            self.slash(enemy)
        elif choice == "C" or choice == "c":
            self.jab(enemy)
        else:
            print("invalid input")
