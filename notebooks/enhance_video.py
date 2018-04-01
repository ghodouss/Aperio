import PIL.ImageEnhance as enhance
from PIL import Image
import cv2
import numpy as np


vidcap = cv2.VideoCapture("data/rat_video.mp4")
out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 29, (360, 360), isColor=True)
success = True
while success:
    success, image = vidcap.read()
    if success:
        cv2_im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(cv2_im)
        enhancer = enhance.Sharpness(pil_im)
        enhanced = enhancer.enhance(4)
        cvImage = cv2.cvtColor(np.array(enhanced), cv2.COLOR_RGB2BGR)
        out.write(cvImage)

vidcap.release()
out.release()
