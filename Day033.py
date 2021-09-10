class Warrior:
    def __init__(self, power, defence, hp):
        self.power = power
        self.defence = defence
        self.hp = hp

    def attack(self, enemy):
        if self.power > enemy.defence:
            enemy.hp = self.power - enemy.defence
        if enemy.hp <= 0:
            print("Enemy died")


Warrior_A = Warrior(100, 50, 80)
Warrior_B = Warrior(60, 80, 120)
print("=== Before Attack===")
print("Warrior_A HP = ", Warrior_A.hp)
print("Warrior_B HP = ", Warrior_B.hp)
Warrior_A.attack(Warrior_B)
Warrior_B.attack(Warrior_A)
print("=== After Attack===")
print("Warrior_A HP = ", Warrior_A.hp)
print("Warrior_B HP = ", Warrior_B.hp)
