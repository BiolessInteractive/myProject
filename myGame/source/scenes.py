from ursina import * #Import the game engine
from ursina.shaders import basic_lighting_shader #Import the shader

class scene1(Entity):
	def __init__(self, **kwargs):
		super().__init__()
		self.ground = Entity(model='plane', texture='assets/textures/prototypeMaterial', scale=(1000,1000,1000), collider='mesh', texture_scale = (1000,1000,1000), shader=basic_lighting_shader)

		self.pivot = Entity()
		DirectionalLight(parent=self.pivot, y=2, z=3, shadows=True)