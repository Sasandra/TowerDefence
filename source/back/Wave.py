class Wave:
    def __init__(self, monster, game_, screen_):
        self.monsters = []
        self.game = game_
        self.screen = screen_
        self.level_up_counter = -1
        self.wave_counter = 0
        self.fill_monsters(monster)

    def fill_monsters(self, monster):
        self.wave_counter += 1
        for i in range(1, 11):
            self.monsters.append(monster(880 + 30*i, 430))

        self.level_up_monsters()

    def level_up_monsters(self):
        if self.wave_counter % 3 == 1:
            self.level_up_counter += 1

        for i in range(self.level_up_counter):
            for m in self.monsters:
                m.level_up()
                print(m.health)

    def update_wave(self):
        temp_list = []
        for m in self.monsters:
            if m.check_health():
                self.game.increase_gold(m.prize)
            else:
                temp_list.append(m)

        self.monsters = temp_list

    def check_if_wave_end(self):
        if len(self.monsters) == 0:
            return True
        else:
            return False

    def update_positions(self):
        for m in self.monsters:
            if m.direction == 'down':
                m.y += m.speed

                if 220 <= m.y <= 225:
                    m.prev_direction = 'down'
                    m.direction = 'right'

                elif 270 <= m.y <= 275 and m.x < 140:
                    m.prev_direction = 'down'
                    m.direction = 'right'

                elif 355 <= m.y <= 360 and m.x > 500:
                    m.prev_direction = 'down'
                    m.direction = 'left'

                elif 475 <= m.y <= 480 and m.x > 140:
                    m.prev_direction = 'down'
                    m.direction = 'left'

            elif m.direction == 'up':
                m.y -= m.speed

                if 100 <= m.y <= 105:
                    m.prev_direction = 'up'
                    m.direction = 'right'

                elif 350 <= m.y <= 355:
                    m.prev_direction = 'up'
                    m.direction = 'left'

            elif m.direction == 'left':
                m.x -= m.speed

                if 635 <= m.x <= 640:
                    m.prev_direction = 'left'
                    m.direction = 'down'

                elif 775 <= m.x <= 780:
                    m.prev_direction = 'left'
                    m.direction = 'down'

                elif 380 <= m.x <= 385:
                    m.prev_direction = 'left'
                    m.direction = 'up'

                elif 122 <= m.x <= 127:
                    m.prev_direction = 'left'
                    m.direction = 'down'

            elif m.direction == 'right':
                m.x += m.speed

                if 380 <= m.x <= 385:
                    m.prev_direction = 'right'
                    m.direction = 'up'

                elif 638 <= m.x <= 643:
                    m.prev_direction = 'right'
                    m.direction = 'down'

                elif 765 <= m.x <= 770:
                    m.prev_direction = 'right'
                    m.direction = 'down'

            #if m.y > 626:
            #    self.game.decrease_lives()
            #    self.monsters.remove(m)

            m.update_coordinates(m.x, m.y)
            self.screen.blit(m.image, (m.x, m.y))
