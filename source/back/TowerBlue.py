from ..back import Tower
from ..texts import constatnts


class TowerBlue(Tower.Tower):
    def __init__(self, x, y):
        super(TowerBlue, self).__init__(constatnts.BLUE_TOWER_STRENGTH, constatnts.BLUE_TOWER_AREA,
                                        constatnts.BLUE_TOWER_COST, constatnts.BLUE_TOWER_IMAGE, x, y,
                                        constatnts.BLUE_TOWER_PERIOD)

    def check_level(self):
        return super(TowerBlue, self).check_level()

    def level_up(self):
        super(TowerBlue, self).level_up()

    def return_description(self):
        return super(TowerBlue, self).return_description()
