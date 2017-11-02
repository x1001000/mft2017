import Leap
import requests
from math import pi
from time import sleep

controller = Leap.Controller()

IP = '192.168.43.17:8080'

A = 20
B = 50
C = 70

while True:
    #sleep(0.1)
    frame = controller.frame()
    hands = frame.hands
    if len(hands)==1:
        if hands[0].pinch_strength:
            yaw = hands[0].direction.yaw * 180 / pi
            if yaw <= -C:
                #print 'Spin Left'
                requests.get('http://'+IP+'/j')
            elif -C < yaw <= -B:
                #print 'Turn Left'
                requests.get('http://'+IP+'/a')
            elif -B < yaw <= -A:
                #print 'Go Left'
                requests.get('http://'+IP+'/q')
            elif -A < yaw < A:
                #print 'Go'
                requests.get('http://'+IP+'/w')
            elif A <= yaw < B:
                #print 'Go Right'
                requests.get('http://'+IP+'/e')
            elif B <= yaw < C:
                #print 'Turn Right'
                requests.get('http://'+IP+'/d')
            elif C <= yaw:
                #print 'Spin Right'
                requests.get('http://'+IP+'/k')
        else:
            #print('OPEN hand')
            pass
    else:
        #print('NO/TWO hands')
        pass