import cv2


def get_data(video_path):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    frames = []

    while success:
        success, image = vidcap.read()

        if success:
            frames.append(image)
            cv2.imwrite("frame.jpg", image)
            count += 1

    x = []
    y = []
    
    
    
    for index, value in enumerate(frames):
        if index < 2:
            continue

        x.append([frames[index - 2], frames[index]])
        y.append(frames[index - 1])
        
        
        
    return x, y