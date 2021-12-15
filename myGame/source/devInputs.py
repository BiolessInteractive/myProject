from ursina import * #Import the game engine

class devInputs(Entity):
	def __init__(self, **kwargs):
		super().__init__()

	def input(self, key):
		if key == 'escape':
			quit()