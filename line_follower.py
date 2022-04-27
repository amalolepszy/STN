from ast import arg
from gamepad_control import GamepadControl
from motor_driver import MotorDriver

import argparse

class LineFollower:
  """Main class used for controlling the line follower.
  """
  def useGamePad(self):
    while(1):
      MotorDriver.goDirection(GamepadControl.getGamepadDirection())

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('UseGamePad')
  lineFollower = LineFollower()
  args = parser.parse_args()
  if('UseGamePad' in args):
    lineFollower.useGamePad()

if __name__ == "main":
  main()
