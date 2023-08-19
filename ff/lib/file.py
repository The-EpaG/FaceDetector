"""File library."""
import json
import os
import pickle
from typing import Any
from ff.lib.const import DEFAULT_SETTINGS

from ff.lib.settings import Settings


def get_files(folder_path: str) -> list:
    """
    Given a folder path, this function retrieves all files within the folder and its subdirectories.

    Parameters:
        folder_path (str): The path of the folder to search for files.

    Returns:
        list: A list of file paths found within the folder and its subdirectories.
    """
    file_list = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def get_file_by_extension(folder_path: str, extension: str) -> list:
    """
    Given a folder path and an extension, this function retrieves all files within the folder and
    its subdirectories with the specified extension.

    Parameters:
        folder_path (str): The path of the folder to search for files.
        extension (str): The extension of the files to retrieve.

    Returns:
        list: A list of file paths found within the folder and its subdirectories with the
        specified extension.
    """
    file_list = get_files(folder_path)
    return list(filter(lambda x: x.endswith("." + extension), file_list))


def get_file_name(file_path: str) -> str:
    """
    Get the file name from a given file path.

    Args:
        file_path (str): The path of the file.

    Returns:
        str: The file name extracted from the file path.
    """
    return os.path.basename(file_path)


def get_file_name_without_extension(file_path: str) -> str:
    """
    Get the file name without the extension from the given file path.

    Args:
        file_path (str): The path of the file.

    Returns:
        str: The file name without the extension.
    """
    return get_file_name(file_path).split(".")[0]


def save_pickle(dictionary: dict, file_name: str) -> None:
    """
    Save a dictionary object to a file in pickle format.

    Args:
        dictionary (dict): The dictionary object to be saved.
        file_name (str): The name of the file to save the dictionary.

    Returns:
        None
    """
    with open(file_name, "wb") as output_file:
        pickle.dump(dictionary, output_file)


def load_pickle(file_name: str) -> dict | None:
    """
    Load and return a dictionary object from a pickle file.

    Parameters:
        file_name (str): The name of the pickle file to load.

    Returns:
        dict: The dictionary object loaded from the pickle file, or None if the file does not exist.
    """
    if os.path.exists(file_name):
        return None

    with open(file_name, "rb") as input_file:
        if input_file is None:
            return None

        return pickle.load(input_file)


def add_or_edit_var(file_name: str, name: str, value: Any) -> None:
    """
    Adds or edits a variable in a dictionary and saves it to a pickle file.

    Parameters:
        file_name (str): The name of the pickle file.
        name (str): The name of the variable.
        value (Any): The value of the variable.

    Returns:
        None
    """
    dictionary: dict = load_pickle(file_name) or {}
    dictionary[name] = value
    save_pickle(dictionary, file_name)


def get_next_file_name(file_names: list[str]) -> str:
    """
    Generate the next file name based on the given list of file names.

    Args:
        file_names (list[str]): A list of file names.

    Returns:
        str: The next file name.
    """
    numeric_filenames = filter(lambda x: x.isdigit(), file_names)

    if not numeric_filenames:
        return "0"

    max_filename = max(numeric_filenames, key=int)
    next_index = int(max_filename) + 1
    return str(next_index)

def save_json(dictionary: dict, file_name: str) -> None:
    """
    Save the given dictionary as a JSON file.

    Args:
        dictionary (dict): The dictionary to be saved.
        file_name (str): The name of the file to save the dictionary as.

    Returns:
        None
    """
    with open(file_name, "wt", encoding="utf-8") as output_file:
        json.dump(dictionary, output_file)

def load_json(file_name: str) -> dict:
    """
    Load a JSON file and return its content as a dictionary.

    Parameters:
        file_name (str): The name of the JSON file to load.

    Returns:
        dict: The content of the JSON file as a dictionary.

    """
    if not os.path.exists(file_name):
        return {}

    with open(file_name, "rt", encoding="utf-8") as input_file:
        return json.load(input_file)

def save_settings(settings: Settings) -> None:
    """
    Save the settings object to a pickle file.

    Parameters:
        settings (Settings): The settings object to be saved.

    Returns:
        None
    """
    save_json(settings.to_dict(), "settings.json")


def load_settings() -> Settings:
    """
    Load the settings object from a pickle file.

    Returns:
        Settings: The settings object loaded from the pickle file.
    """

    dictionary = load_json("settings.json")

    if len(dictionary) == 0:
        return DEFAULT_SETTINGS

    return Settings.from_dict(dictionary)
