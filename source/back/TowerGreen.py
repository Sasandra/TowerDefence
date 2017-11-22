from ..back import Tower


class TowerGreen(Tower.Tower):
    def __init__(self, x, y):
        super(TowerGreen, self).__init__(15, 5, 15, 'tower_green.png', x, y)

    def check_level(self):
        return super(TowerGreen, self).check_level()

    def level_up(self):
        super(TowerGreen, self).level_up()

    def return_description(self):
        return super(TowerGreen, self).return_description()
