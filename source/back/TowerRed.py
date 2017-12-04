from ..back import Tower
from ..texts import constatnts


class TowerRed(Tower.Tower):
    def __init__(self, x, y):
        super(TowerRed, self).__init__(constatnts.RED_TOWER_STRENGTH, constatnts.RED_TOWER_AREA,
                                       constatnts.RED_TOWER_COST, constatnts.RED_TOWER_IMAGE, x, y,
                                       constatnts.RED_TOWER_PERIOD)

    def check_level(self):
        return super(TowerRed, self).check_level()

    def level_up(self):
        super(TowerRed, self).level_up()

    def return_description(self):
        return super(TowerRed, self).return_description()
