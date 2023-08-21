"""Video manager."""
import os
import sys
from typing import Callable
import cv2
from ff.lib.const import (
    DETECTION_COLOR,
    DETECTION_FONT,
    DETECTION_RECT_THICKNESS,
    DETECTION_TEXT_THICKNESS,
    PROJECT_NAME,
    VIDEO_FOLDER,
)
from ff.lib.position import Position
from ff.lib.settings import Settings


class VideoManager:
    """Video manager."""

    def __init__(self, settings: Settings):
        self.settings = settings
        self.video_capture = None

    def load_video(self):
        """
        Load a video file and initialize a video capture object.

        Args:
            None

        Returns:
            None
        """
        file_name = os.path.join(VIDEO_FOLDER, self.settings.input_settings.name_video)
        self.video_capture = cv2.VideoCapture(file_name)

    def start(
        self, for_every_frame: Callable, for_not_skipped_frames: Callable
    ) -> None:
        """
        Start the video processing.

        Parameters:
            for_every_frame (Callable): A function that will be called for every frame of the video.
            for_not_skipped_frames (Callable): A function that will be called for frames that are not skipped.

        Returns:
            None
        """
        if self.video_capture is None:
            self.load_video()

        while True:
            ret, frame = self.video_capture.read()
            if not ret:
                break

            current_frame = int(self.video_capture.get(cv2.CAP_PROP_POS_FRAMES))
            total_frames = int(self.video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

            for_every_frame(frame, current_frame, total_frames)

            if current_frame % self.settings.input_settings.fps == 0:
                for_not_skipped_frames(frame, current_frame, total_frames)
        return frame

    @staticmethod
    def scale(frame, scale: float) -> None:
        """
        Scales the given frame using the provided scale factor.

        Parameters:
            frame: The frame to be scaled.
            scale (float): The scale factor to be applied to the frame.

        Returns:
            None
        """
        return cv2.resize(frame, (0, 0), fx=scale, fy=scale)

    @staticmethod
    def show(frame) -> None:
        """
        Show the given frame in a window with the project name as the title.

        Parameters:
            frame: The frame to be shown.

        Returns:
            None
        """
        cv2.imshow(PROJECT_NAME, frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Closed by user.")
            sys.exit(0)

    @staticmethod
    def save(frame, file_name: str) -> None:
        """
        Save an image frame to a file.

        Args:
            frame: The image frame to be saved.
            file_name: The name of the file to save the image frame to.

        Returns:
            None
        """
        cv2.imwrite(file_name, frame)

    @staticmethod
    def write_detection(frame, name: str, position: Position) -> None:
        cv2.rectangle(
            frame,
            (position.left, position.top),
            (position.right, position.bottom),
            DETECTION_COLOR,
            DETECTION_RECT_THICKNESS,
        )
        cv2.putText(
            frame,
            name,
            (position.left, position.bottom + 25),
            DETECTION_FONT,
            1.0,
            DETECTION_COLOR,
            DETECTION_TEXT_THICKNESS,
        )
