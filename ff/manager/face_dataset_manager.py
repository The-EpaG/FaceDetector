"""Face dataset manager."""
import os
from ff.lib.const import DATA_FILE, DATA_FILE_INDEX_FACE, FACES_FOLDER, SAVE_EXT
from ff.lib.settings import Settings
from ff.lib.file import (
    get_file_by_extension,
    load_json,
    load_pickle,
    save_json,
    save_pickle,
)


class FaceDatasetManager:
    """Face dataset manager."""

    def __init__(self, settings: Settings):
        self.faces: dict[str, list] = {}
        self.names: dict[str, str] = {}
        self.settings = settings

    @staticmethod
    def _get_files_list(folder: str) -> list[str]:
        return get_file_by_extension(folder, SAVE_EXT)

    @staticmethod
    def _load_names():
        return load_json(DATA_FILE)

    def _save_names(self):
        return save_json(self.names, DATA_FILE)

    @staticmethod
    def _load_face(file_name: str):
        data = load_pickle(file_name)

        if DATA_FILE_INDEX_FACE not in data:
            return None
        return data[DATA_FILE_INDEX_FACE]

    # TODO: find face type
    @staticmethod
    def _save_face(face, file_name: str):
        data = {}
        data[DATA_FILE_INDEX_FACE] = face
        save_pickle(data, file_name)

    @staticmethod
    def _load_faces(folder_name: list[str]):
        faces = []

        file_names = FaceDatasetManager._get_files_list(folder_name)
        print(f"folder: {folder_name}, file_names: {file_names}")

        for file_name in file_names:
            face = FaceDatasetManager._load_face(file_name)
            if face is not None:
                faces.append(face)
        return faces

    # TODO: find faces type
    def _save_faces(self, folder: str, faces: list, extension: str):
        for i, face in enumerate(faces):
            file_name = os.path.join(folder, str(i) + "." + extension)
            self._save_face(face, file_name)

    def load_data(self):
        """
        Load data from external sources and initialize instance variables.

        Parameters:
            None.

        Returns:
            None.
        """
        self.names = self._load_names()

        for name in self.names:
            if name not in self.faces:
                self.faces[name] = []
                folder_name = os.path.join(FACES_FOLDER, name)
                self.faces[name].append(self._load_faces(folder_name))

    def save_data(self):
        """
        Save data to the specified folder.

        This function creates the necessary folder structure and saves the faces and names data.

        Parameters:
            self: The instance of the class.

        Returns:
            None
        """
        if not os.path.exists(FACES_FOLDER):
            os.makedirs(FACES_FOLDER)

        for face_id in self.names.keys():
            folder_name = os.path.join(FACES_FOLDER, face_id)
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            self._save_faces(folder_name, self.faces[face_id], SAVE_EXT)

        self._save_names()
