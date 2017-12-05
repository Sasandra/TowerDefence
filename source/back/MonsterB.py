from ..back import Monster
from ..texts import constatnts


class MonsterBlue(Monster.Monster):
    def __init__(self, x, y, direction_):
        self.start_health = constatnts.BLUE_MONSTER_START_HEALTH
        super(MonsterBlue, self).__init__(constatnts.BLUE_MONSTER_SPEED, self.start_health,
                                          constatnts.BLUE_MONSTER_PRIZE, constatnts.BLUE_MONSTER_IMG, x, y, direction_)

    def increase_health(self):
        self.start_health += 3

    def decrease_health(self, amount):
        super(MonsterBlue, self).decrease_health(amount)

    def check_health(self):
        return super(MonsterBlue, self).check_health()

    def change_image(self):
        super(MonsterBlue, self).change_image()

    def level_up(self):
        super(MonsterBlue, self).level_up()

    def check_if_collidepoint(self, pos):
        return super(MonsterBlue, self).check_if_collidepoint(pos)

    def return_description(self):
        return super(MonsterBlue, self).return_description()

    def check_if_clicked(self):
        return super(MonsterBlue, self).check_if_clicked()
