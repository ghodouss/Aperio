import PIL.ImageEnhance as enhance
from PIL import Image
import cv2
import numpy as np
from keras.models import load_model
import keras.backend as K


def root_mean_squared_error(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true), axis=-1)) 


model = load_model("weights/deepCNN.h5py", custom_objects={'root_mean_squared_error': root_mean_squared_error})


def enhance_cv_img(cv2_img, factor=4):

    new_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(new_img.astype('uint8'))

    enhancer = enhance.Sharpness(pil_im)
    enhanced = enhancer.enhance(factor)
    cvImage = cv2.cvtColor(np.array(enhanced), cv2.COLOR_RGB2BGR)

    return cvImage


def get_interpolation(img1, img2):

    r1 = img1[:, :, 0]
    g1 = img1[:, :, 1]
    b1 = img1[:, :, 2]

    r2 = img2[:, :, 0]
    g2 = img2[:, :, 1]
    b2 = img2[:, :, 2]

    X = np.stack([r1, r2, g1, g2, b1, b2], axis=-1)

    X = np.array([X])

    interpolation = model.predict(X)[0]

    return interpolation


for iter in range(3):
    vidcap = cv2.VideoCapture("vid" + str(iter) + ".mp4")
    fps = float(vidcap.get(cv2.CAP_PROP_FPS))
    out = cv2.VideoWriter("vid" + str(iter+1) + ".mp4", cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps * 2, (360, 360), isColor=True)

    new_img = None
    success, prev_img = vidcap.read()

    count = 1

    while success:
        success, new_img = vidcap.read()

        if success:

            interp = get_interpolation(prev_img, new_img)

            enhanced_prev_img = enhance_cv_img(prev_img, factor=1)
            enhanced_interped = enhance_cv_img(interp, factor=2)

            out.write(enhanced_prev_img)
            out.write(enhanced_interped)

            prev_img = new_img

            print(count)
            count += 1

    vidcap.release()
    out.release()

