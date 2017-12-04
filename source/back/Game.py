from ..texts import constatnts

class Game:
    def __init__(self):
        self.game_state = True
        self.lives = constatnts.GAME_START_LIVES
        self.gold = constatnts.GAME_START_GOLD
        self.waves = 1
        self.towers_icons = []

    def decrease_lives(self):
        self.lives -= 1

    def increase_gold(self, amount):
        self.gold += amount

    def decrease_gold(self, amount):
        self.gold -= amount

    def check_gold(self, amount):
        return self.gold >= amount
