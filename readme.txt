
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


# tensorflow 설치
python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl