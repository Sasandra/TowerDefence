from ..back import Tower


class TowerBlue(Tower.Tower):
    def __init__(self, x, y):
        super(TowerBlue, self).__init__(20, 10, 20, 'tower_blue.png', x, y)

    def check_level(self):
        return super(TowerBlue, self).check_level()

    def level_up(self):
        super(TowerBlue, self).level_up()

    def return_description(self):
        return super(TowerBlue, self).return_description()
