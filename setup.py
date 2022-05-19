from setuptools import setup, find_packages

setup(
    name="EPass",
    version="0.1.0",
    packages=find_packages(
        include=["TUI", "TUI.*", "CORE", "CORE.*", "GUI", "GUI.*", "REST", "REST.*"]
    ),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "epass=TUI.__main__:main",
            "epass-help=TUI.__main__:help",
        ]
    },
)
