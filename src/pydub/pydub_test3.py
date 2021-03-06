import os
import glob
from pydub import AudioSegment
import shutil

video_dir = '../../video-source/'  # Path where the videos are located
extension_list = ('*.mp4', '*.flv')
os.chdir(video_dir)
for extension in extension_list:
    for video in glob.glob(extension):
        mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
        AudioSegment.from_file(video).export(mp3_filename, format='mp3')
        # shutil.move(mp3_filename,"../output/"+mp3_filename)

