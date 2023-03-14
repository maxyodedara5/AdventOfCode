from __future__ import annotations
from itertools import combinations

class human:
    def __init__(self, health, dmg, armour, who) -> None:
        self.health = health
        self.dmg = dmg
        self.armour = armour
        self.who = who

    def got_atkd(self, person : human):
        dmg_dealth = person.dmg - self.armour
        if dmg_dealth <= 0:
            dmg_dealth = 1
        self.health = self.health - dmg_dealth
        if self.health < 0:
            self.health = 0
        
    def weilded_item(self, inv_item : item):
        self.dmg += inv_item.dmg
        self.armour += inv_item.armour

    def stats(self):
        print(self.health, self.dmg, self.armour)


class item:
    def __init__(self, cost, dmg, armour, what) -> None:
        self.cost = cost
        self.dmg = dmg
        self.armour = armour
        self.what = what

player = human(100,0,0,"player")
enemy = human(103,9,2,"enemy")

def main_loop(player, enemy):
    # Take turns for each person and returns True if player wins
    turn = True
    while (player.health != 0 and enemy.health != 0):
        if turn == True:
            enemy.got_atkd(player)
            turn = False
        else:
            player.got_atkd(enemy)
            turn = True
    if player.health == 0:
        return False
    return True

Dag = item(8,4,0,"Dag")
ShortS = item(10,5,0,"ShortS")
WarH = item(25,6,0,"WarH")
LongS = item(40,7,0,"LongS")
GreatA = item(74,8,0,"GreatA")

NoArm = item(0,0,0,"NoArmour")
Leather = item(13,0,1,"Leather")
ChainM = item(31,0,2,"ChainM")
SplintM = item(53,0,3,"SplintM")
BandedM = item(75,0,4,"BandedM")
PlateM = item(102,0,5,"PlateM")

NoRing = item(0,0,0,"NoRing")
NoRing2 = item(0,0,0,"NoRing2")
dr1 = item(25,1,0,"dr1")
dr2 = item(50,2,0,"dr2")
dr3 = item(100,3,0,"dr3")
df1 = item(20,0,1,"df1")
df2 = item(40,0,2,"df2")
df3 = item(80,0,3,"df3")

w_list = [Dag, ShortS, WarH, LongS, GreatA] 
a_list = [NoArm, Leather, ChainM, SplintM, BandedM, PlateM]
r_list = [NoRing, dr1, dr2, dr3, df1, df2, df3]

ring_combo_list = []
ring_combo_list.append((NoRing, NoRing2))
ring_combo_list.extend(list(combinations(r_list, 2)))


combos = 0
# Keep Current_cost max(e.g. 999) for Part 1 and 0 for Part 2
current_cost = 0
for i in w_list:
    for a in a_list:
        for c in ring_combo_list:

            player = human(100,0,0,"player")
            enemy = human(103,9,2,"enemy")
            player.weilded_item(i)
            player.weilded_item(a)
            player.weilded_item(c[0])
            player.weilded_item(c[1])
            cost = i.cost + a.cost + c[0].cost + c[1].cost

            # Part 1
            if main_loop(player, enemy) and cost < current_cost:
                print(f"W: {i.what}, A: {a.what}, R1: {c[0].what}, R2: {c[1].what}")
                print(f"Cost : {cost}")
                current_cost = cost

            # Part 2
            if not(main_loop(player, enemy)) and cost > current_cost:
                print(f"W: {i.what}, A: {a.what}, R1: {c[0].what}, R2: {c[1].what}")
                print(f"Cost : {cost}")
                current_cost = cost