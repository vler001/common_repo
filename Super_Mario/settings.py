import os

# налаштування для mario.
WIN_WIDTH, WIN_HEIGHT = 1100, 850
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = '#0190ff'
FPS = 60
SCREEN_START = (0, 0)
FILE_DIR = os.path.dirname(__file__)
ICON_DIR = os.path.dirname(__file__)
FILE_PATH = '%s/levels/1.txt' % FILE_DIR
MUSIC_PATH = 'audio/level_music.wav'

# налаштування для monsters.
MONSTER_WIDTH, MONSTER_HEIGHT, MONSTER_COLOR = 42, 32, '#000000'
ANIMATION_MONSTER_HORIZONTAL = [('%s/monsters/wmonstr.png' % ICON_DIR), ('%s/monsters/monstr.png' % ICON_DIR)]

# налаштування для blocks.
PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM_COLOR = 32, 32, '#000000'
ANIMATION_BLOCK_TELEPORT = [('%s/blocks/tunel.png' % ICON_DIR), ('%s/blocks/tunel1.png' % ICON_DIR)]
ANIMATION_PRINCESS = [('%s/blocks/princess_l.png' % ICON_DIR), ('%s/blocks/princess_r.png' % ICON_DIR)]
PATH_BLOCK_PLATFORM = '%s/blocks/platform.png' % ICON_DIR
ANIMATION_BLOCK_DIE = [('%s/blocks/fire1.png' % ICON_DIR),('%s/blocks/fire2.png' % ICON_DIR)]

# налаштування для player.
MOVE_SPEED = 7
MOVE_EXTRA_SPEED = 2.5
WIDTH, HEIGHT, COLOR = 32,42, '#888888'
JUMP_POWER, JUMP_EXTRA_POWER, GRAVITY = 10, 1, 0.25
ANIMATION_DELAY, ANIMATION_SUPER_SPEED_DELAY = 0.1, 0.05

PLATFORM_IMAGE = "%s/blocks/platform.png" % ICON_DIR

ANIMATION_LEFT = [('%s/mario/l1.png' % ICON_DIR),
                  ('%s/mario/l2.png' % ICON_DIR),
                  ('%s/mario/l3.png' % ICON_DIR),
                  ('%s/mario/l4.png' % ICON_DIR),
                  ('%s/mario/l5.png' % ICON_DIR)
                  ]

ANIMATION_RIGHT = [('%s/mario/r1.png' % ICON_DIR),
                   ('%s/mario/r2.png' % ICON_DIR),
                   ('%s/mario/r3.png' % ICON_DIR),
                   ('%s/mario/r4.png' % ICON_DIR),
                   ('%s/mario/r5.png' % ICON_DIR)
                   ]

ANIMATION_JUMP = [('%s/mario/j00.png' % ICON_DIR, ANIMATION_DELAY)]
ANIMATION_JUMP_LEFT = [('%s/mario/jl.png' % ICON_DIR, ANIMATION_DELAY)]
ANIMATION_JUMP_RIGHT = [('%s/mario/jr.png' % ICON_DIR, ANIMATION_DELAY)]
ANIMATION_STAY = [('%s/mario/00.png' % ICON_DIR, ANIMATION_DELAY)]

# Налаштування для pyganim. (ігрові стани)
PLAYING, PAUSED, STOPPED = 'playing', 'paused', 'stopped'
# Ці значення використовуються в методі anchor().
NORTH, SOUTH, WEST, EAST, CENTER = 'north', 'south', 'west', 'east', 'center'
NORTH_WEST, SOUTH_WEST, NORTH_EAST, SOUTH_EAST = 'northwest', 'southwest', 'northeast', 'southeast'
