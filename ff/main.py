"""The main file"""


from ff.manager.face_dataset_manager import FaceDatasetManager
from ff.lib.file import load_settings, save_settings
from ff.lib.gui import menu, refresh
from ff.lib.settings import Settings
from ff.manager.video_manager import VideoManager


def every_frame(_, current_frame, total_frames):
    if current_frame % int(total_frames / 100) == 0:
        text = (
            "Progress: "
            + str(int(current_frame / total_frames * 100))
            + "%\t\t["
            + str(current_frame)
            + "/"
            + str(total_frames)
            + "]"
        )
        refresh(text)


def not_skipped_frames(frame, current_frame, total_frames):
    if Settings().show:
        VideoManager.show(frame)


def main():
    """
    This is the main function that serves as the entry point of the program.

    Parameters:
    None

    Returns:
    None
    """

    ########
    # Menu #
    ########
    settings: Settings = load_settings()
    settings = menu(settings)
    save_settings(settings)

    ####################
    # Load known faces #
    ####################
    print("Load known faces...")
    face_dataset_manager: FaceDatasetManager = FaceDatasetManager(settings)
    face_dataset_manager.load_data()

    ##########################
    # Start Video Processing #
    ##########################
    print("Start video processing...")
    video_manager: VideoManager = VideoManager(settings)
    video_manager.start(
        for_every_frame=every_frame, for_not_skipped_frames=not_skipped_frames
    )

    ##################
    # Save detection #
    ##################
    print("Save detection...")
    face_dataset_manager.save_data()

    print("Done.")
