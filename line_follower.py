from gamepad_control import GamepadControl
from motor_driver import MotorDriver
#import RPi.GPIO as GPIO

#from inputs import get_gamepad
#from inputs import devices


class LineFollower(GamepadControl, MotorDriver):
  """Main class used for controlling the line follower.
  """
  def useGamePad(self):
    print("gowno")
    dir = self.getGamepadDirection()
    print(dir)
    self.goDirection(dir)


def main():
  lineFollower = LineFollower()
  while(1):
    lineFollower.useGamePad()

if __name__ == "__main__":
  main()

