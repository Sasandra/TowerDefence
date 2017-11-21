class Tower:
    def __init__(self, strength_, area_, cost_, color_):
        self.strength = strength_
        self.area = area_
        self.level = 1
        self.cost = cost_
        self.color = color_

    def check_level(self):
        return self.level <= 5

    def level_up(self):
        self.area *= 1.5
        self.strength *= 1.5
        self.cost *= 1.5
