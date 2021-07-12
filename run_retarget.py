import numpy as np
import os
import cv2
import fire

swd lo
def main():

	# Load the images (from somewhere)
	# Also load the hand vertices
	# in this case, load pre-saved guys from disk
	images, all_mano_verts = load_images_and_detections()