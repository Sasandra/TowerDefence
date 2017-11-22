from ..back import Tower


class TowerRed(Tower.Tower):
    def __init__(self, x, y):
        super(TowerRed, self).__init__(10, 5, 10, 'tower_red.png', x, y)

    def check_level(self):
        return super(TowerRed, self).check_level()

    def level_up(self):
        super(TowerRed, self).level_up()

    def return_description(self):
        return super(TowerRed, self).return_description()
