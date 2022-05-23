import argparse
from src.gamepad_control import GamepadControl
from src.motor_driver import MotorDriver

class LineFollower(GamepadControl, MotorDriver):
  """Main class used for controlling the line follower.
  """
  def useGamePad(self):
    self.goDirection(self.getGamepadDirection())

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('use_gamepad')
  args = parser.parse_args()
  lineFollower = LineFollower()
  lineFollower.initMotorPins()
  if args.use_gamepad == 'use_gamepad':
    while True:
      lineFollower.useGamePad()

if __name__ == "__main__":
  main()

