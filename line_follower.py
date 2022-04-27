from gamepad_control import GamepadControl
#from motor_driver import MotorDriver
#import RPi.GPIO as GPIO

#from inputs import get_gamepad
#from inputs import devices


class LineFollower(GamepadControl):
  """Main class used for controlling the line follower.
  """
  def useGamePad(self):
    print("gowno")
    dir = self.getGamepadDirection()
    print(dir)
    #MotorDriver.goDirection(dir)


def main():
  lineFollower = LineFollower()
  lineFollower.useGamePad()

if __name__ == "__main__":
  main()

