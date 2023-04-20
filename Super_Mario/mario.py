import pygame
from player import *
from blocks import *
from monsters import *
from settings import WIN_WIDTH, WIN_HEIGHT, DISPLAY, BACKGROUND_COLOR, FILE_PATH, MUSIC_PATH, FPS


class Camera:
    def __init__(self, camera_fn, width, height):
        self.camera_fn = camera_fn
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_fn(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = - l + WIN_WIDTH / 2, - t + WIN_HEIGHT / 2
    # Не рухаємось далі лівого кордону
    l = min(0, l)
    # Не рухаємося далі за правий кордон
    l = max(-(camera.width - WIN_WIDTH), l)
    # Не рухаємося далі за нижню межу
    t = max(-(camera.height - WIN_HEIGHT), t)
    # Не рухаємося далі за верхню межу
    t = min(0, t)

    return Rect(l, t, w, h)


def load_level():
    # оголошуємо глобальні змінні, це координати героя
    global player_x, player_y
    level_file = open(FILE_PATH)
    line = " "
    # commands = []
    # поки не знайшли символ завершення файлу
    while line[0] != "/":
        # зчитуємо порядково
        line = level_file.readline()
        # якщо знайшли символ початку рівня
        if line[0] == "[":
            # те, поки не знайшли символ кінця рівня
            while line[0] != "]":
                # зчитуємо рядковий рівень
                line = level_file.readline()
                # якщо немає символу кінця рівня
                if line[0] != "]":
                    # шукаємо символ кінця рядка
                    endLine = line.find("|")
                    # додаємо в рівень рядок від початку до символу "|"
                    level.append(line[0: endLine])
        # якщо рядок не порожній
        if line[0] != "":
            # розбиваємо його на окремі команди
            commands = line.split()
            # якщо кількість команд > 1, то шукаємо ці команди
            if len(commands) > 1:
                # якщо перша команда - player
                if commands[0] == "player":
                    # записуємо координати героя
                    player_x = int(commands[1])
                    player_y = int(commands[2])
                # якщо перша команда portal, то створюємо портал
                if commands[0] == "portal":
                    tp = BlockTeleport(int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4]))
                    entities.add(tp)
                    platforms.append(tp)
                    animated_entities.add(tp)
                # якщо перша команда монстра, то створюємо монстра
                if commands[0] == "monster":
                    mn = Monster(int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4]),
                                 int(commands[5]), int(commands[6]))
                    entities.add(mn)
                    platforms.append(mn)
                    monsters.add(mn)


def music():
    # Ініціалізація об'єкту mixer
    mixer.init()
    # Вказуємо шлях до файлу
    mixer.music.load(MUSIC_PATH)
    # Встановлюємо рівень відтворення звуку
    mixer.music.set_volume(0.1)
    # Повторюємо відтворення циклічно
    mixer.music.play(-1)


def main():
    load_level()
    # Ініціація PyGame, обов'язковий рядок
    pygame.init()
    # Створюємо віконце
    screen = pygame.display.set_mode(DISPLAY)
    # Пишемо шапку
    pygame.display.set_caption("S U P E R    M A R I O")
    # Створення видимої поверхні
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    # Заливаємо поверхню суцільним кольором
    bg.fill(Color(BACKGROUND_COLOR))

    music()
    # За замовчуванням - стоїмо
    left = right = up = running = False
    # Створюємо героя за (x, y) координатами
    hero = Player(player_x, player_y)
    entities.add(hero)

    timer = pygame.time.Clock()
    # Координати
    x = y = 0
    # Весь рядок
    for row in level:
        # Кожний символ
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "*":
                bd = BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)
                animated_entities.add(bd)
            if col == "P":
                pr = Princess(x, y)
                entities.add(pr)
                platforms.append(pr)
                animated_entities.add(pr)

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0  

    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)
    # Основний цикл програми, керування клавішами натискання
    while not hero.winner:
        # Оброблюємо події
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit("QUIT")
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    up = True
                if event.key == K_LEFT:
                    left = True
                if event.key == K_RIGHT:
                    right = True
                if event.key == K_LSHIFT:
                    running = True
            #  керування клавішами відпускання
            if event.type == KEYUP:
                if event.key == K_UP:
                    up = False
                if event.key == K_RIGHT:
                    right = False
                if event.key == K_LEFT:
                    left = False
                if event.key == K_LSHIFT:
                    running = False

        # Кожну ітерацію необхідно все перемальовувати
        screen.blit(bg, SCREEN_START)
        # показуємо анімацію
        animated_entities.update()
        # пересуваємо всіх монстрів
        monsters.update(platforms)
        # центруємо камеру щодо персонажа
        camera.update(hero)
        # пересування героя
        hero.update(left, right, up, running, platforms)

        for entity in entities:
            screen.blit(entity.image, camera.apply(entity))

        timer.tick(FPS)
        # оновлення та виведення всіх змін на екран
        pygame.display.update()


level = []
# те, у що ми врізатимемося або спиратимемося
platforms = []
# Всі об'єкти
entities = pygame.sprite.Group()
# Всі анімовані об'єкти, за винятком героя
animated_entities = pygame.sprite.Group()
# Всі об'єкти, що пересуваються
monsters = pygame.sprite.Group()


if __name__ == "__main__":
    main()
