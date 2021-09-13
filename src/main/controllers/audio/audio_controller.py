from vlc import Instance, MediaPlayer, Media
import os

from src.main.controllers.audio.audio_config import AudioConfig

from src.main.controllers.controller import Controller

class AudioController(Controller):

  def __init__(self, audioConfig: AudioConfig):
    self.audioConfig = audioConfig
    opts = "--aout=alsa --verbose=-1"
    self.vlc = Instance(opts)
    self.player: MediaPlayer = self.vlc.media_player_new()
    self.player.audio_set_volume(audioConfig.VOLUME)

  def start(self):
    if self.audioConfig.DEMO:
      self.demo()
    else:
      self.realtime()

  def stop(self):
    self.player.stop()

  def realtime(self):
    pass

  def demo(self):
    self.play()

  def play(self):
    file = os.path.expanduser(os.path.join(self.audioConfig.MEDIA, "night.mp3"))
    print("playing:", file)
    media: Media = self.vlc.media_new(file)
    self.player.set_media(media)
    self.player.play()