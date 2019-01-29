# dependencies

audioread    2.1.6
decorator    4.3.2
ffmpeg       1.4
future       0.17.1
joblib       0.13.1
librosa      0.6.2
llvmlite     0.27.0
numba        0.42.0
numpy        1.16.0
pip          19.0
PyAudio      0.2.11
pydub        0.23.1
pygame       1.9.4
pyglet       1.3.2
resampy      0.2.1
scikit-learn 0.20.2
scipy        1.2.0
setuptools   40.6.3
simpleaudio  1.0.2
six          1.12.0


# src/_portaudiomodule.c:29:10: fatal error: 'portaudio.h' file not found
'''
$ brew update
  brew install portaudio # cross-platform, open-source, audio I/O library.
  brew link portaudio
  pip install pyaudio
'''


# pyglet install
1. $ pip install pyglet
2. download avbin : https://avbin.github.io/AVbin/Home/Home.html
3. $ defaults write org.python.python ApplePersistenceIgnoreState NO


# Getting ffmpeg set up # cross-platform solution to record, convert and stream audio and video.

- libav
brew install libav --with-libvorbis --with-sdl --with-theora

OR

- ffmpeg
brew install ffmpeg --with-libvorbis --with-sdl2 --with-theora


# pycharm memory increase
MENU - Help - Edit custom VMoption -> -xmx edit.

