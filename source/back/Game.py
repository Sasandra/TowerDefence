from ..back import MonsterB, MonsterG, MonsterR


class Game:
    def __init__(self):
        self.game_state = True
        self.lives = 5
        self.gold = 100
        self.waves = 1

    def decrease_lives(self):
        self.lives -= 1

    def increase_gold(self, amount):
        self.gold += amount
