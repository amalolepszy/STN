import playsound

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
    playsound.playsound(path)

  def playUwazaj(self):
    self.playSound("uwazaj.mp3")

def main():
  Sound = Sounds()
  Sound.playUwazaj()

if __name__ == "__main__":
  main()

