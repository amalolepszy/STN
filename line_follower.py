from gamepad_control import GamepadControl
from motor_driver import MotorDriver



class LineFollower:
  """Main class used for controlling the line follower.
  """
  def useGamePad(self):
    while(1):
      MotorDriver.goDirection(GamepadControl.getGamepadDirection())

def main():
  lineFollower = LineFollower()
  lineFollower.useGamePad()

if __name__ == "main":
  main()
