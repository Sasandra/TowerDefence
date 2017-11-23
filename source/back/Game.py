class Game:
    def __init__(self):
        self.game_state = True
        self.lives = 30
        self.gold = 100
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
