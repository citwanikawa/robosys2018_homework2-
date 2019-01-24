#!/usr/bin/python

import rospy
from std_msgs.msg import Int16

class b(object):
	def __init__(self):
		self._pub_led = rospy.Publisher('/led', Int16, queue_size=1)

		while(1):
			self._Exe()

	def _Exe(self):
		print "input number"
		number = input()

		led = Int16()
		led.data = number
		self._pub_led.publish(led)

if __name__=='__main__':
	rospy.init_node('myled')
	print "aaaa"
	b = b()
	print "bbbb"
	try:
		rospy.spin()
	except KeyboardInterrupt:
		pass
