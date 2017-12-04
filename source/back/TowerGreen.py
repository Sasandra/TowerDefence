from ..back import Tower
from ..texts import constatnts


class TowerGreen(Tower.Tower):
    def __init__(self, x, y):
        super(TowerGreen, self).__init__(constatnts.GREEN_TOWER_STRENGTH, constatnts.GREEN_TOWER_AREA,
                                         constatnts.GREEN_TOWER_COST, constatnts.GREEN_TOWER_IMAGE, x, y,
                                         constatnts.GREEN_TOWER_PERIOD)

    def check_level(self):
        return super(TowerGreen, self).check_level()

    def level_up(self):
        super(TowerGreen, self).level_up()

    def return_description(self):
        return super(TowerGreen, self).return_description()
