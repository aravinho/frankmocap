import pyrealsense2 as rs
import imageio
import numpy as np
import time

print(f"making pipe")
pipe = rs.pipeline()

# Configure streams
config = rs.config()
config.enable_stream(rs.stream.depth, 480, 640, rs.format.z16, 30)

print(f"starting profile")
profile = pipe.start()
try:
  for i in range(0, 100):
    print(f"i {i}")
    frames = pipe.wait_for_frames()
    print(f"got frames {frames}")
    for f in frames:
      print(f.profile)
    color_frame = frames.get_color_frame()
    color_img = np.asanyarray(color_frame.get_data())
    print(color_img.dtype, color_img.shape)
    imageio.imwrite(f"/tmp/c3_images/{i}.png", color_img)
finally:
    pipe.stop()

# What I want to do is:
"""
run calibration with the aruco board in the proper setup
get the intrinsics, i.e. the cam in robot aka cam in human pose.
do some motions with hand and capture images.
pass each image to frankmocap, save the output mano verts. also save viz
retarget the hand, keep that
extract the wrist pose, keep that.  make sure to add offset of wrists

in rviz, load the robot, and in a loop, pass the joint angles

"""