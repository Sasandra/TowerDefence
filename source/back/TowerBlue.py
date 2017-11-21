from ..back import Tower


class TowerBlue(Tower):
    def __init__(self):
        super(TowerBlue, self).__init__(20, 10, 20, (0, 0, 255))

    def check_level(self):
        super(TowerBlue, self).check_level()

    def level_up(self):
        super(TowerBlue, self).level_up()
