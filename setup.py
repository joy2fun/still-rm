try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
VERSION = "0.1.6"
setup(
    name="still-rm",
    packages=["still_rm"],
    version=VERSION,
    description="",
    author="",
    author_email="",
    url="https://github.com/",
    download_url="https://github.com/joy2fun/still-rm/archive/v{}.tar.gz".format(
        VERSION
    ),
    keywords=[],
    classifiers=[],
    install_requires=[
        'opencv-python>=4.0',
        'ffmpeg-python>=0.1'
    ],
    entry_points={
        "console_scripts": ["still-rm = still_rm.__main__:main"]
    },
)
