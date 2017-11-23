from ..back import Tower


class TowerRed(Tower.Tower):
    def __init__(self, x, y):
        super(TowerRed, self).__init__(5, 60, 15, 'tower_red.png', x, y, 600)

    def check_level(self):
        return super(TowerRed, self).check_level()

    def level_up(self):
        super(TowerRed, self).level_up()

    def return_description(self):
        return super(TowerRed, self).return_description()
