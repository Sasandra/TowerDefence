from ..back import Tower


class TowerGreen(Tower):
    def __init__(self):
        super(TowerGreen, self).__init__(15, 5, 15, (0, 255, 0))

    def check_level(self):
        super(TowerGreen, self).check_level()

    def level_up(self):
        super(TowerGreen, self).level_up()
