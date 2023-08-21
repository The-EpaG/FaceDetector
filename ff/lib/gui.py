"""GUI library."""
from enum import Enum
import os
import sys
from ff.lib.const import PROJECT_NAME, VIDEO_FOLDER
from ff.lib.file import save_settings

from ff.lib.settings import Settings


class Command(Enum):
    """Command enum."""

    START = 0
    TRAINING = 1
    FPS = 2
    MODIFY_INPUT_FILE = 3
    SHOW_RESULT = 4
    SAVE_DETECTION = 5
    SAVE_SETTINGS = 6
    QUIT = 7


COMMANDS = [command.value for command in list(Command)]


def menu(settings: Settings) -> Settings:
    """
    Generates the menu for user interaction and modifies the provided settings object accordingly.

    Parameters:
        settings (Settings): The settings object to be modified.

    Returns:
        Settings: The modified settings object.

    Raises:
        ValueError: If an invalid menu choice is entered.
        SystemExit: If the user chooses to quit the menu.
    """
    choice = -1
    while choice != 0:
        while True:
            text = [
                "##" + len(PROJECT_NAME) * "#" + "##",
                "# " + PROJECT_NAME + " #",
                "##" + len(PROJECT_NAME) * "#" + "##",
                "",
                "0. Start",
                "1. Training\t\t\t[" + str(settings.training) + "]",
                "2. Fps\t\t\t\t[" + str(settings.input_settings.fps) + "]",
                "3. Modify InputFile\t\t[" + settings.input_settings.name_video + "]",
                "4. Show result in real time\t[" + str(settings.show) + "]",
                "5. Save detection\t\t[" + str(settings.save_detection) + "]",
                "6. Save settings",
                "7. Quit (no save)",
                ""
            ]
            text = "\n".join(text)
            refresh(text)

            choice = int(input("choice: "))
            if choice in COMMANDS:
                break

        if choice == Command.TRAINING.value:
            settings.training = not settings.training
        elif choice == Command.FPS.value:
            settings.input_settings.fps = int(input("Enter fps: "))
        elif choice == Command.MODIFY_INPUT_FILE.value:
            print("File must be in " + VIDEO_FOLDER)
            settings.input_settings.name_video = input("File name: ")
        elif choice == Command.SHOW_RESULT.value:
            settings.show = not settings.show
        elif choice == Command.SAVE_DETECTION.value:
            settings.save_detection = not settings.save_detection
        elif choice == Command.SAVE_SETTINGS.value:
            save_settings(settings)
        elif choice == Command.QUIT.value:
            sys.exit(0)

    refresh()
    return settings


def refresh(text: str = ""):
    """
    Clears the console and prints the specified text if provided.

    Parameters:
        text (str): The text to be printed (default is an empty string).

    Returns:
        None
    """
    os.system("clear")
    if text != "":
        print(text)
