import argparse
from gamepad_control import GamepadControl
from motor_driver import MotorDriver
from reflective_sensor import ReflectiveSensor

class LineFollower(GamepadControl, ReflectiveSensor, MotorDriver):
  """Main class used for controlling the line follower.
  """
  def useGamePad(self):
    self.goDirection(self.getGamepadDirection())

def main():
  parser = argparse.ArgumentParser(description='Initialize the Line Follower')
  parser.add_argument('control', help="reflective for the reflective sensor, use_gamepad for gamepad")
  args = parser.parse_args()
  lineFollower = LineFollower()
  lineFollower.initMotorPins()
  if args.control == 'use_gamepad':
    while True:
      lineFollower.useGamePad()

  if args.control == 'reflective':
    lineFollower.initSensorPins()
    while True:
      lineFollower.ride_reflective()


if __name__ == "__main__":
  main()

