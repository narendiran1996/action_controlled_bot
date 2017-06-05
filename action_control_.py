import cv2
import serial
import time

ser= serial.Serial('/dev/ttyUSB1',57600)

def stop():
	global ser
	ser.write('stop')
	time.sleep(0.01)

def forward():
	global ser
	ser.write('forward')
	time.sleep(0.01)
def back():
	global ser
	ser.write('back')
	time.sleep(0.01)

cascadePath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascadePath)

cap = cv2.VideoCapture(0)

while(True):

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    if len(faces)>0:
	    x,y,w,h=faces[0]
	    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	    	 
	    centrex,centrey=x+w/2,y+h/2
	    print centrex,centrey
	    if centrex<250:
		print " - forward"
		forward()
	    elif centrex>350:
		print " - back"
		back()
	    else:
		print " - stop"
		stop()
	
    else:
	    print 'Out of Frame'

    cv2.imshow('Move Your head up or down to control.',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
