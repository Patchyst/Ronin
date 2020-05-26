from termcolor import cprint
import sys
from time import sleep
import random
class Entity:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
    def attack(self):
        cprint("\n" + self.name + " attacked" + " for " + str(self.attack_damage) + " damage \n", "red", attrs=["bold"])
    def stats(self):
        cprint(self.name, "red", attrs=["bold"])
        type_key("Health: " + str(self.health) + "\n")
        slow_type_key("Attack " + str(self.attack_damage) + "\n")
        input("next... ")
    def take_damage(self, damage_dealt):
        self.health -= damage_dealt
    def heal(self):
        health_plus = random.randint(1, 50)
        cprint(self.name + " healed for " + str(health_plus))
        self.health += health_plus
    def isalive(self):
        if self.health <= 0:
            return False
        elif self.health >= 1:
            return True
def type_key(str):
    for i in str:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(random.uniform(0.06, 0.09))
def slow_type_key(str):
    for i in str:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(random.uniform(0.08, 0.1))
