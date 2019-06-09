import pygame

class Settings():
	"""储存游戏的所有设置的类"""
	def __init__(self):
		"""初始化游戏的静态设置"""

		#屏幕设置
		self.screen_width = 1000
		self.screen_height = 800
		self.bg_color = (41, 158, 179)

		#飞船的设置
		self.ship_speed = 0.6
		self.ship_limit = 3

		#子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (235,1,1)
		self.bullets_allowed = 4

		'''#外星人设置
		self.alien_speed_factor = 10
		self.fleet_drop_speed = 1.5
		#fleet_direction为1表示右移，为-1表示左移
		self.fleet_direction = 1'''

		'''动态设置'''
		#以什么样的速度加快游戏节奏
		self.speedup_scale = 1.2
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

		#计分
		self.alien_points = 50

	def initialize_dynamic_settings(self):
		'''初始化随游戏进行而变化的设置'''
		self.bullet_speed_factor = 1.3
		self.alien_speed_factor = 0.3
		self.fleet_drop_speed = 5

		#fleet_direction 为1向右，-1向左
		self.fleet_direction = 1

	def increase_speed(self):
		'''提高速度设置和外星人点数'''
		#self.ship_speed *= self.speedup_scale 飞船速度不该提高
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)

	def rever_point(self):
		#开始新游戏时清零外星人的等级分数
		self.alien_points = 50