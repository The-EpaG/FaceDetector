"""The main file"""


from ff.lib.file import load_settings, save_settings
from ff.lib.gui import menu
from ff.lib.settings import Settings


def main():
    """
    This is the main function that serves as the entry point of the program.

    Parameters:
    None

    Returns:
    None
    """

    #########
    # Menu
    #########
    settings: Settings = load_settings()
    settings = menu(settings)
    save_settings(settings)
