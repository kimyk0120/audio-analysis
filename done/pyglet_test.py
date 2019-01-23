
import pyglet
import time

# simple play

# song = pyglet.media.load('mp3/noexcuses.mp3')
# song.play()
# pyglet.app.run()


player = pyglet.media.Player()
source = pyglet.media.load('mp3/noexcuses.mp3')
player.queue(source)
player.play()


# time.sleep(10)

# player.pause()

# time.sleep(1)

# player.seek(50)
# player.play()

# print(player.max_distance)
# print(player.position)
