#!/usr/bin/python
# -#- coding: utf-8 _*_
#import RPi.GPIO as GPIO
import rospy
#rospy.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
#rospy.path.append('/opt/ros/kinetic/lib/python2.7')
import time
import subprocess
from std_msgs.msg import Int16


class a(object):
	def __init__(self):
		self._sub_number = rospy.Subscriber('/led', Int16, self._callback_led)

	def _callback_led(self, message):
		self._number = message.data
		print self._number
		for num in range(self._number):
#			GPIO.output(2, GPIO.HIGH)
#			cmd = "echo 1 > /dev/myled0"
#			subprocess.call(cmd, shell=True)

#			time.sleep(0.5)
#			GPIO.output(2, GPIO.LOW)
#			cmd = "echo 0 > /dev/myled0"
#			subprocess.call(cmd, shell=True)

			time.sleep(0.5)


if __name__=='__main__':
	rospy.init_node('led')
#	GPIO.setmode(GPIO.BCM)
#	GPIO.setup(2, GPIO.OUT)
	a = a()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		pass

#	GPIO.cleanup()
