from gamepad_control import GamepadControl
from motor_driver import MotorDriver
import RPi.GPIO as GPIO

from inputs import get_gamepad
from inputs import devices


class LineFollower():
  """Main class used for controlling the line follower.
  """
  def useGamePad(self):
    print("gowno")
    dir = GamepadControl.getGamepadDirection()
    print(dir)
    MotorDriver.goDirection(dir)



if __name__ == "main":
  lineFollower = LineFollower()
  lineFollower.useGamePad()
