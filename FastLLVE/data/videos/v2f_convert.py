import cv2
vidcap = cv2.VideoCapture('Shooting007_x264.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("./Shooting7/%05d.png" % count, image)    
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

print("finish! convert video to frame")