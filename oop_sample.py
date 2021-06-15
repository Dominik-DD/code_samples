class Hero:
    def __init__(self, type, weapon, max_hp):
        self.type = type
        self.weapon = weapon
        self.max_hp = max_hp
        self.hp = max_hp


    def fight(self, other):
        if self == other:
            print("can´t fight myself")
        elif self.hp <= 0:
            print('can´t fight right now, give me some beer !')
        else:
            result = self.fight_result(self.weapon, other.weapon)
            if result == 'lose':
                self.hp = 0
                print(f"{self.type} you lose!")
            elif result == 'draw':
                self.hp -= 10
                other.hp -= 10
                print(f"fight between {self.type} and {other.type} is over. It's a draw.")
            elif result == 'win':
                other.hp = 0
                print(f"{self.type} you won.")


    def beer(self):
        if self.hp < self.max_hp:
            self.hp += self.max_hp - self.hp
            print(f"{self.type} recovered HP.")
        else:
            print(f"{self.type} HP is already full.")



    @staticmethod
    def fight_result(weapon_1, weapon_2):

        '''
        game logic:

        weapon |  strong vs |   weak vs
        -------------------------------
        sword  |  axe       |   bow
        axe    |  bow       |   sword
        bow    |  sword     |   axe

        socks = ultimate weapon

        same weapon type = draw
        '''

        # result mapping
        result_map = {0: "lose", 1: "win", 2: "draw"}
        # weapon mapping
        weapon_map = {"sword": 0, "axe": 1, "bow": 2, "socks": 3}
        # win-lose-draw matrix
        result_table = [
            [2, 1, 0, 0],  # sword
            [0, 2, 1, 0],  # axe
            [1, 0, 2, 0],  # bow
            [1, 1, 1, 2]   # socks
        ]
        result = result_table[weapon_map[weapon_1]][weapon_map[weapon_2]]
        return result_map[result]

    def __str__(self):
        return f"{self.type}, weapon: {self.weapon}, hp/max_hp {self.hp}/{self.max_hp}"

    def __repr__(self):
        return f"Hero('{self.type}', '{self.weapon}', {self.max_hp})"


if __name__ == "__main__":
    knight = Hero('Aragorn', 'sword', 100)
    elf = Hero('Legolas', 'bow', 90)
    dwarf = Hero('Gimli', 'axe', 120)
    hamster = Hero('Dedoles', 'socks', 1_000_000)
    breakpoint()
    #run from terminal