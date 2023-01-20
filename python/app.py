import cv2
import sys
import config
import subprocess
import utilities as tools
import face_recognition


# cascPath = sys.argv[1]

face_cascade = cv2.CascadeClassifier("C:/Users/peter/eng_thesis/face-reader/haarcascade_frontalface_default.xml")

if face_cascade.empty():
    print("not loaded")

cam_access = cv2.VideoCapture(config.camera_index)
while True:
    tools.take_picture(cam_access, face_cascade)

# print(config.action_performs[0].path)

# subprocess.Popen(config.action_performs[0].path)

cam_access.release()



# import win32com.client
 
# wmi = win32com.client.GetObject ("winmgmts:")
# for usb in wmi.InstancesOf ("Win32_USBHub"):
#     print(usb.DeviceID)

#     USB\VID_0C45&PID_636B\SN0001 - this is krux camera through all the hubs