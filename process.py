import cv2

vidcap = cv2.VideoCapture('notebooks/rat_video.mp4')
success, image = vidcap.read()
count = 0
success = True

frames = []

while success:
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    frames.append(image)
    # cv2.imwrite("frame%d.jpg" % count, image)
    count += 1

x = []
y = []
for index, value in enumerate(frames):
    if index < 2:
        continue

    x.append([frames[index - 2], frames[index]])
    y.append(frames[index - 1])
