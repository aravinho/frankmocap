import rospy
import rospkg
import rospy
import roslib
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
import std_msgs
import numpy as np

class ROSWebcamReader:

    def __init__(self):
        self.image = None
        rospy.init_node('python_listener', anonymous=True)
        rospy.Subscriber("/camera/color/image_raw/", Image, self.callback)
        print(f"created sub")

    def callback(self, msg):
        # Try to convert the ROS Image message to a CV2 Image
        cv_im = np.flip(np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, -1),2)
        # set this as the latest
        print(f"setting the latest image")
        self.image = cv_im

    def read(self):
        return None, self.image

sub = ROSWebcamReader()
i = 0
rate = rospy.Rate(20)
while not rospy.is_shutdown():
    rate.sleep()
    i += 1
    _, image = sub.read()
    print(image)
    if i == 5:
        break
