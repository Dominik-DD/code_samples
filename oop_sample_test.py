import unittest
from oop_sample import Hero
#testovanie logiky a funkcii

class Test_Hero_methods(unittest.TestCase):

    def setUp(self):
        self.knight = Hero('Aragorn', 'sword', 100)
        self.elf = Hero('Legolas', 'bow', 90)

    def test_figh_logic(self):
        self.assertEqual(Hero.fight_result("sword","sword"),"draw")
        self.assertEqual(Hero.fight_result("sword", "axe"), "win")
        self.assertEqual(Hero.fight_result("sword", "bow"), "lose")
        self.assertEqual(Hero.fight_result("sword", "socks"), "lose")

        self.assertEqual(Hero.fight_result("axe", "sword"), "lose")
        self.assertEqual(Hero.fight_result("axe", "axe"), "draw")
        self.assertEqual(Hero.fight_result("axe", "bow"), "win")
        self.assertEqual(Hero.fight_result("axe", "socks"), "lose")

        self.assertEqual(Hero.fight_result("bow", "sword"), "win")
        self.assertEqual(Hero.fight_result("bow", "axe"), "lose")
        self.assertEqual(Hero.fight_result("bow", "bow"), "draw")
        self.assertEqual(Hero.fight_result("bow", "socks"), "lose")

        self.assertEqual(Hero.fight_result("socks", "sword"), "win")
        self.assertEqual(Hero.fight_result("socks", "axe"), "win")
        self.assertEqual(Hero.fight_result("socks", "bow"), "win")
        self.assertEqual(Hero.fight_result("socks", "socks"), "draw")

    def test_fight_method(self):
        self.knight.fight(self.elf)
        self.assertEqual(self.knight.hp,0)

    def test_beer_method(self):
        self.knight.hp = 0
        self.knight.beer()
        self.assertEqual(self.knight.hp,self.knight.max_hp)




if __name__ == '__main__':
    unittest.main()