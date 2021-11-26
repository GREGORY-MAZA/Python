import self


class Player:

    # ------------------------------------------------ Constructors

    def __init__(self, pv, attack, attackMagic, armor, armorMagic):
        # ------------------------------------------------ Attributes

        self.pv = int
        self.attack = int
        self.attackMagic = int
        self.armor = int
        self.armorMagic = int

    # ------------------------------------------------ getter method

    def get_pv(self):
        return self.pv

    def get_attack(self):
        return self.attack

    def get_attackMagic(self):
        return self.attackMagic

    def get_armor(self):
        return self.armor

    def get_armorMagic(self):
        return self.armorMagic

    # ------------------------------------------------ setter method

    def set_pv(self, newPv):
        self.pv = newPv

    def set_attack(self, newAttack):
        self.attack = newAttack

    def set_attackMagic(self, newAttackMagic):
        self.attackMagic = newAttackMagic

    def set_armor(self, newArmor):
        self.armor = newArmor

    def set_armorMagic(self, newArmorMagic):
        self.armorMagic = newArmorMagic


class Humain(Player):
    def __init__(self, pv, attack, attackMagic, armor, armorMagic):
        super().__init__(pv, attack, attackMagic, armor, armorMagic)


def main():
    Gregozorus = Humain(100, 10, 0, 100, 0)
    print(Humain.get_armor(Gregozorus))


if __name__ == '__main__':
    main()
