class People:
    def __init__(self, name, damage, hp):
        self.name=name
        self.damage=damage
        self.hp=hp

class Hero(People):
    def __init__(self, name, damage, hp, country):
        People.__init__(self, name, damage, hp)
        self.country = country

    def get_inf(self):
        print("姓名：{}".format(self.name))
        print("攻击力：{}".format(self.damage))
        print("当前血量：{}".format(self.hp))
        print("阵营：{}".format(self.country))

    def attack(self, enemy):
        print(self.name)
        print("攻击力为：{}".format(self.damage))
        print("{}目前血量为：{}".format(enemy.name, enemy.hp))
        print("{}攻击{}".format(self.name, enemy.name))
        enemy.hp -= self.damage
        print("{}剩余血量为：{}".format(enemy.name, enemy.hp))
        print("***********************************")

XB = People("小兵", 1, 10)
LB=Hero("吕布", 20, 100, "群雄")
ZF=Hero("张飞", 7, 80, "蜀国")

#练习1：新建一个武器类
class Weapon:
    def __init__(self, name, damage):
        """武器基础属性"""
        self.name = name
        self.damage = damage

    def take_weapon(self, hro):
        """将武器给予英雄，英雄攻击力提升"""
        print("将武器{}装备给英雄{}".format(self.name, hro.name))
        hro.damage+=self.damage
        print("{}的攻击力变为{}".format(hro.name, hro.damage))

#练习2：新建武器实例，并将武器赠与张飞
zbsm = Weapon('丈八蛇矛', 3)
zbsm.take_weapon(ZF)

#练习3：显示张飞目前信息，令张飞攻击吕布
ZF.get_inf()
ZF.attack(LB)

#提升练习 --“群英战吕布”
i = 0
heros = {'ZF':ZF}
while 1:
    i += 1
    new_hero = Hero("hero"+str(i), 15, 30, "反吕联盟")
    heros["hero"+str(i)] = new_hero
    if LB.hp <= 0:
        break
    for h in heros:
        while heros[h].hp > LB.damage:
            heros[h].attack(LB)
            if LB.hp <= 0:
                print('吕布被击败了！')
                break
            LB.attack(heros[h])
            if heros[h].hp <= LB.damage:
                print(f'{heros[h].name}被击败了！')
