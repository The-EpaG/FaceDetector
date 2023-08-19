"""Settings."""
from dataclasses import dataclass
import json


@dataclass
class InputSettings:
    """Input settings."""

    def __init__(self, name_video: str, fps: int):
        self.name_video = name_video
        self.fps = fps

    def __dict__(self):
        return {"name_video": self.name_video, "fps": self.fps}


@dataclass
class Settings:
    """
    Settings class.
    """

    def __init__(
        self,
        training: bool,
        input_settings: InputSettings,
        show: bool,
        save_detection: str,
    ):
        self.training = training
        self.input_settings = input_settings
        self.show = show
        self.save_detection = save_detection

    def to_dict(self) -> dict:
        return {
            "training": self.training,
            "input_settings": self.input_settings.__dict__(),
            "show": self.show,
            "save_detection": self.save_detection,
        }

    @staticmethod
    def from_dict(dictionary: dict) -> "Settings":
        """
        Initializes the object with values from a dictionary.

        Args:
            dictionary (dict): A dictionary containing the values to initialize the object.

        Returns:
            None
        """
        training = dictionary["training"]
        input_settings = InputSettings(
            dictionary["input_settings"]["name_video"],
            dictionary["input_settings"]["fps"],
        )
        show = dictionary["show"]
        save_detection = dictionary["save_detection"]

        return Settings(training, input_settings, show, save_detection)
