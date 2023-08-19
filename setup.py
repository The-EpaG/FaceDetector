from setuptools import setup, find_packages

setup(
    name="ff",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "tqdm",
        "face_recognition",
        "opencv-python",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "fafi = ff.main:main",
        ],
    },
)
