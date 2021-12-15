from ursina import * #Import the ursina engine

class playerController(Entity):
	def __init__(self, **kwargs):
		super().__init__()
		#Player Stats
		self.speed = 5
		self.height = 1.7
		self.cameraPivot = Entity(parent=self, y=self.height)
		self.grounded = False
		self.airTime = 0

		#Input Settings
		self.mouseSensitivityX = 20 #Horizontal Speed
		self.mouseSensitivityY = 15 #Vertical Speed

		#Camera Stats
		camera.parent = self.cameraPivot
		camera.position = (0,0,0)
		camera.rotation = (0,0,0)
		camera.fov = 90
		mouse.locked = True
		self.mouseSensitivity = Vec2(self.mouseSensitivityY, self.mouseSensitivityX)

		#World Stats
		self.gravity = 1

		for key, value in kwargs.items():
			setattr(self, key ,value)

		# make sure we don't fall through the ground if we start inside it
		if self.gravity:
			ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
			if ray.hit:
				self.y = ray.world_point.y

	def update(self):
		#Camera rotation
		self.rotation_y += mouse.velocity[0] * self.mouseSensitivity[1]
		self.cameraPivot.rotation_x -= mouse.velocity[1] * self.mouseSensitivity[0]
		self.cameraPivot.rotation_x= clamp(self.cameraPivot.rotation_x, -90, 90)

		#Movement
		self.direction = Vec3(self.forward * (held_keys['w'] - held_keys['s'])
		+ self.right * (held_keys['d'] - held_keys['a'])).normalized()
		feetRay = raycast(self.position+Vec3(0,0.5,0), self.direction, ignore=(self,), distance=.5)
		headRay = raycast(self.position+Vec3(0,self.height-.1,0), self.direction, ignore=(self,), distance=.5)
		if not feetRay.hit and not headRay.hit:
			self.position += self.direction * self.speed * time.dt

		if self.gravity:
			ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))

			if ray.distance <= self.height+.1:
				if not self.grounded:
					self.land()
				self.grounded = True

				if ray.world_normal.y > .7 and ray.world_point < .5:
					self.y = ray.world_point[1]
					return
				else:
					self.grounded = False
			else:
				self.grounded = False

			self.y -= min(self.airTime, ray.distance-.05) * time.dt * 100
			self.airTime += time.dt * .25 * self.gravity

	def land(self):
		self.airTime = 0
		self.grounded = True