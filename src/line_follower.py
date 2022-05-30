import argparse
from gamepad_control import GamepadControl
from motor_driver import MotorDriver
from sound_signals import Sounds

class LineFollower(GamepadControl, MotorDriver, Sounds):
  """Main class used for controlling the line follower.
  """
  def useGamePad(self):
    self.goDirection(self.getGamepadDirection())
  
  def playSounds(self):
    if(self.getPressedButton == "A"):
      self.playUwazaj()

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('use_gamepad')
  args = parser.parse_args()
  lineFollower = LineFollower()
  lineFollower.initMotorPins()
  if args.use_gamepad == 'use_gamepad':
    while True:
      lineFollower.useGamePad()
      lineFollower.playSounds()

if __name__ == "__main__":
  main()

