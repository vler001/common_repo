from pygame import *
import pyganim
import blocks
import monsters
from settings import MOVE_SPEED, MOVE_EXTRA_SPEED, WIDTH, HEIGHT, COLOR, JUMP_POWER, JUMP_EXTRA_POWER, GRAVITY, \
    ANIMATION_DELAY, ANIMATION_SUPER_SPEED_DELAY, ANIMATION_RIGHT, ANIMATION_LEFT, ANIMATION_JUMP_LEFT, \
    ANIMATION_JUMP_RIGHT, ANIMATION_JUMP, ANIMATION_STAY, SCREEN_START

# всі класи є нащадками в модулі sprite суперкласу Sprite модуля pygame

class Player(sprite.Sprite):
    def __init__(self, x, y):
        # sprite.Sprite.__init__(self)
        super().__init__()
        # швидкість переміщення: 0 – стояти на місці
        self.x_val = 0
        # швидкість вертикального переміщення
        self.y_val = 0
        # Початкова позиція Х, стане в пригоді коли переграватимемо рівень
        self.start_x = x
        self.start_y = y
        # Чи на землі я?
        self.on_ground = False
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        # Прямокутний об'єкт
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        # робимо фон прозорим
        self.image.set_colorkey(Color(COLOR))

        # Анімація руху ліворуч, використовуємо list comprehension оптимізуючи код
        bolt_anim = [(anim, ANIMATION_DELAY) for anim in ANIMATION_LEFT]
        bolt_anim_super_speed = [(anim, ANIMATION_SUPER_SPEED_DELAY) for anim in ANIMATION_LEFT]
        self.bolt_anim_left = pyganim.PygAnimation(bolt_anim)
        self.bolt_anim_left.play()
        self.bolt_anim_left_super_speed = pyganim.PygAnimation(bolt_anim_super_speed)
        self.bolt_anim_left_super_speed.play()

        # Анімація руху ліворуч, використовуємо list comprehension оптимізуючи код
        self.bolt_anim_right = pyganim.PygAnimation([(anim, ANIMATION_DELAY) for anim in ANIMATION_RIGHT])
        self.bolt_anim_right.play()
        self.bolt_anim_right_super_speed = pyganim.PygAnimation([(anim, ANIMATION_SUPER_SPEED_DELAY) for anim in
                                                                 ANIMATION_RIGHT])
        self.bolt_anim_right_super_speed.play()

        self.bolt_anim_stay = pyganim.PygAnimation(ANIMATION_STAY)
        self.bolt_anim_stay.play()

        # За замовчуванням стоїмо
        self.bolt_anim_stay.blit(self.image, SCREEN_START)
        self.bolt_anim_jump_left = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.bolt_anim_jump_left.play()
        self.bolt_anim_jump_right = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.bolt_anim_jump_right.play()
        self.bolt_anim_jump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.bolt_anim_jump.play()
        self.winner = False

    def update(self, left, right, up, running, platforms):
        if up:
            # стрибаємо, тільки коли можемо відштовхнутися від землі
            if self.on_ground:
                self.y_val = - JUMP_POWER
                # якщо є прискорення та ми рухаємося
                if running and (left or right):
                    # то стрибаємо вище
                    self.y_val -= JUMP_EXTRA_POWER
                self.image.fill(Color(COLOR))
                self.bolt_anim_jump.blit(self.image, SCREEN_START)

        if left:
            # Ліворуч = x - n
            self.x_val = - MOVE_SPEED
            self.image.fill(Color(COLOR))
            # якщо прискорення
            if running:
                # то пересуваємося швидше
                self.x_val -= MOVE_EXTRA_SPEED
                # і якщо не стрибаємо
                if not up:
                    # то відображаємо швидку анімацію
                    self.bolt_anim_left_super_speed.blit(self.image, SCREEN_START)
            # якщо не біжимо
            else:
                # і не стрибаємо
                if not up:
                    # відображаємо анімацію руху
                    self.bolt_anim_left.blit(self.image, SCREEN_START)
            # якщо ж стрибаємо
            if up:
                # відображаємо анімацію стрибка
                self.bolt_anim_jump_left.blit(self.image, SCREEN_START)

        if right:
            # Праворуч = x + n
            self.x_val = MOVE_SPEED
            self.image.fill(Color(COLOR))
            if running:
                self.x_val += MOVE_EXTRA_SPEED
                if not up:
                    self.bolt_anim_right_super_speed.blit(self.image, SCREEN_START)
            else:
                if not up:
                    self.bolt_anim_right.blit(self.image, SCREEN_START)
            if up:
                self.bolt_anim_jump_right.blit(self.image, SCREEN_START)

        # стоїмо, коли немає вказівок йти
        if not (left or right):
            self.x_val = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.bolt_anim_stay.blit(self.image, SCREEN_START)

        if not self.on_ground:
            self.y_val += GRAVITY

        # Ми не знаємо, коли ми на землі
        self.on_ground = False
        self.rect.y += self.y_val
        self.collide(0, self.y_val, platforms)
        # Переносимо своє становище на x_val
        self.rect.x += self.x_val
        self.collide(self.x_val, 0, platforms)

    def collide(self, x_val, y_val, platforms):
        for platform in platforms:
            # Якщо є перетин платформи з гравцем
            if sprite.collide_rect(self, platform):
                # Якщо пересічний блок - blocks.BlockDie або Monster
                if isinstance(platform, blocks.BlockDie) or isinstance(platform, monsters.Monster):
                    # Вмираємо
                    self.die()
                elif isinstance(platform, blocks.BlockTeleport):
                    self.teleporting(platform.go_x, platform.go_y)
                # Якщо торкнулися принцеси
                elif isinstance(platform, blocks.Princess):
                    # ПЕРЕМОГЛИ!
                    self.winner = True
                else:
                    # Якщо рухається праворуч
                    if x_val > 0:
                        # то не рухається праворуч
                        self.rect.right = platform.rect.left
                    # Якщо рухається вліво
                    if x_val < 0:
                        # то не рухається вліво
                        self.rect.left = platform.rect.right
                    # Якщо падає вниз
                    if y_val > 0:
                        # то не падає вниз
                        self.rect.bottom = platform.rect.top
                        # і стає на щось тверде
                        self.on_ground = True
                        # і енергія падіння зникає
                        self.y_val = 0
                    # Якщо рухається вгору
                    if y_val < 0:
                        # то не рухається вгору
                        self.rect.top = platform.rect.bottom
                        # і енергія стрибка зникає
                        self.y_val = 0

    def teleporting(self, go_x, go_y):
        self.rect.x = go_x
        self.rect.y = go_y

    def die(self):
        # Чекаємо
        time.wait(500)
        # Переміщуємося у початкові координати
        self.teleporting(self.start_x, self.start_y)
