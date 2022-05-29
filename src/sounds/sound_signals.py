import pygame

class Sounds:
  """Class containing methods that play sounds through speakers.
  The sound files are located in root/src/sounds.
  Use by calling each method, or just playSound with path argument.

  """
  def playSound(self, path):
    """Play sound from path

    Args:
        path (string): Path to the mp3 file that should be played
    """
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.muxic.play()
    while pygame.mixer.music.get_busy():
      continue

  def playUwazaj(self):
    self.playSound("uwazaj.mp3")

def main():
  Sound = Sounds()
  Sound.playUwazaj()

if __name__ == "__main__":
  main()

