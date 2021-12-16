from ursina import * #Import the game engine and settings
from devInputs import devInputs #Import development inputs
from player import playerController #Import the player controller class
from scenes import * #Import all scenes

app = Ursina() #Initalize the application
universalInputs = devInputs() #Set entity as development inputs manager
player = playerController() #Set entity as player controller
selectedScene = scene1()#Set the selected scene as scene 1

app.run() #Run the frame