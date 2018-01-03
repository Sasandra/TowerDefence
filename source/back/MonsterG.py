from ..back import Monster
from ..texts import constatnts


class MonsterGreen(Monster.Monster):
    def __init__(self, x, y, direction_):
        self.start_health = constatnts.GREEN_MONSTER_START_HEALTH
        super(MonsterGreen, self).__init__(constatnts.GREEN_MONSTER_SPEED, self.start_health,
                                           constatnts.GREEN_MONSTER_PRIZE, constatnts.GREEN_MONSTER_IMG, x, y,
                                           direction_)

    def increase_health(self):
        self.start_health += 2

    def decrease_health(self, amount):
        super(MonsterGreen, self).decrease_health(amount)

    def check_health(self):
        return super(MonsterGreen, self).check_health()

    def change_health_level(self):
        super(MonsterGreen, self).change_health_level()

    def level_up(self):
        super(MonsterGreen, self).level_up()

    def check_if_collidepoint(self, pos):
        return super(MonsterGreen, self).check_if_collidepoint(pos)

    def return_description(self):
        return super(MonsterGreen, self).return_description()

    def check_if_clicked(self):
        return super(MonsterGreen, self).check_if_clicked()

    def change_image(self):
        super(MonsterGreen, self).change_image()
