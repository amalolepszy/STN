from gamepad_control import GamepadControl
from motor_driver import MotorDriver
import RPi.GPIO as GPIO

from inputs import get_gamepad
from inputs import devices


class LineFollower(MotorDriver, GamepadControl):
  """Main class used for controlling the line follower.
  """
  def useGamePad(self):
    dir = self.getGamepadDirection()
    print(dir)
    self.goDirection(dir)



if __name__ == "main":
  while(1):
    LineFollower.useGamePad()
