"""Constants."""

import os

from ff.lib.settings import InputSettings, Settings


DATA_FOLDER = "data"
FACES_FOLDER = os.path.join(DATA_FOLDER, "faces")
VIDEO_FOLDER = os.path.join(DATA_FOLDER, "video")
OUT_FOLDER = os.path.join(DATA_FOLDER, "out")

DEFAULT_SETTINGS = Settings(
    training=False,
    input_settings=InputSettings(name_video="a.mp4", fps=2),
    show=True,
    save_detection=False,
)
