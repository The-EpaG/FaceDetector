"""Constants."""

import os

import cv2

PROJECT_NAME = "Find Faces"

DATA_FOLDER = "data"
DATA_FILE_NAME = "data.json"
FACES_FOLDER = os.path.join(DATA_FOLDER, "faces")
VIDEO_FOLDER = os.path.join(DATA_FOLDER, "video")
DATA_FILE = os.path.join(DATA_FOLDER, DATA_FILE_NAME)

DEFAULT_SETTINGS = '{"training": false, "input_settings": {"name_video": "a.mp4", "fps": 2}, "show": false, "save_detection": false}'

SAVE_EXT = "pkl"

DATA_FILE_INDEX_FACE = "face"

DETECTION_COLOR = (255, 255, 255)
DETECTION_RECT_THICKNESS = 2
DETECTION_TEXT_THICKNESS = 1
DETECTION_FONT = cv2.FONT_HERSHEY_SIMPLEX
