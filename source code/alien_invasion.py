import pygame

from settings import Settings

from ship import Ship

from pygame.sprite import Group

from alien import Alien

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

import game_functions as gf


def run_game():
    #初始化游戏并且创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("YYS IS TUZI")

    #创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    #创建一个用于储存游戏统计信息的实例
    stats = GameStats(ai_settings)
    #计分

    sb = Scoreboard(ai_settings, screen, stats)

    #创建一艘飞船
    ship = Ship(ai_settings,screen)

    #创建一个用于储存子弹的编组
    bullets = Group()

    #创建一个外星人
    alien = Alien(ai_settings, screen)

    #创建一个外星人编组
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)


    #开始游戏的主循环
    while True:
        #监视鼠 标退出事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button)

run_game()
