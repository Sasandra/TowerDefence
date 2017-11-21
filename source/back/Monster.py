class Monster:
    def __init__(self, speed_, health_, prize_, color_):
        self.speed = speed_
        self.health = health_
        self.prize = prize_
        self.color = color_

    def decrease_health(self, amount):
        self.health -= amount

    def check_health(self):
        return self.health <= 0
