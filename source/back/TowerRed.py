from ..back import Tower


class TowerRed(Tower):
    def __init__(self):
        super(TowerRed, self).__init__(10, 5, 10, (255, 0, 0))

    def check_level(self):
        super(TowerRed, self).check_level()

    def level_up(self):
        super(TowerRed, self).level_up()
