import subprocess

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
    player = subprocess.Popen(["mplayer", path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("[DEBUG] Playing sound.")

  def playUwazaj(self):
    self.playSound("~/project_venv/STN/src/uwazaj.mp3")

def main():
  Sound = Sounds()
  Sound.playUwazaj()

if __name__ == "__main__":
  main()
