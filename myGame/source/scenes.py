from ursina import * #Import the game engine

class scene1(Entity):
	def __init__(self, **kwargs):
		super().__init__()
		self.ground = Entity(model='plane', texture='assets/textures/prototypeMaterial', scale=(100,100,100), texture_scale=(100,100,100), collider='mesh')