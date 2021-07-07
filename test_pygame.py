import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()
print(f"camlist {camlist}")

cam = pygame.camera.Camera("/dev/video0",(640,480))
# cam = pygame.camera.Camera("/path/to/camera",(640,480))
cam.start()

image = cam.get_image()
