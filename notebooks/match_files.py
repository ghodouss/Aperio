import os
import re

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

def load_data:
    frames_list = []
    for frame in os.listdir(os.path.join(DIR_PATH, "notebooks", "data")):
        if frame.endswith(".jpg"):
            frames_list.append(frame)

    frames_list.sort(key=lambda file_str: int(re.sub("[^0-9]", "", file_str)))

    res = []
    for index, value in enumerate(frames_list):
        if index < 2:
            continue

        res.append([[frames_list[index - 2], frames_list[index]], frames_list[index - 1]])

print(res)
