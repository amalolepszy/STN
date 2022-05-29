import RPi.GPIO as GPIO
import time
import argparse
from rpi_pins import motorPins as mPins

class MotorDriver():
  speedRight = 0
  speedLeft = 0
  lastDirection = "forward"


  def initMotorPins(self):
    """Initializing Pins used for the motor.
    IN pins are logic GPIO.OUT values, used for steering the direction.
    EN pins are used for initializing the speed of the motors by modulating the PWM signal.
    """
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #IN pins
    GPIO.setup(mPins.MOTOR_LEFT_IN1, GPIO.OUT)
    GPIO.setup(mPins.MOTOR_LEFT_IN2, GPIO.OUT)
    GPIO.setup(mPins.MOTOR_RIGHT_IN1, GPIO.OUT)
    GPIO.setup(mPins.MOTOR_RIGHT_IN2, GPIO.OUT)

    #EN pins
    GPIO.setup(mPins.MOTOR_RIGHT_EN, GPIO.OUT)
    GPIO.setup(mPins.MOTOR_LEFT_EN, GPIO.OUT)
    self.speedRight = GPIO.PWM(mPins.MOTOR_RIGHT_EN, 1000)
    self.speedLeft = GPIO.PWM(mPins.MOTOR_LEFT_EN, 1000)

    #default values - stand still
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.LOW)
    self.speedRight.start(0)
    self.speedLeft.start(0)


  def _goForward(self):
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.LOW)
    print("[DEBUG] Going forward.")

  def _goForwardRight(self):
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.LOW)
    self.speedRight.ChangeDutyCycle(80)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.LOW)
    print("[DEBUG] Going forward - right.")

  def _goForwardRight(self):
    self.speedLeft.ChangeDutyCycle(80)
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.LOW)
    print("[DEBUG] Going forward - left.")

  def _goReverse(self):
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.HIGH)
    print("[DEBUG] Going reverse.")


  def _goRight(self):
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.LOW)
    print("[DEBUG] Going right.")


  def _goLeft(self):
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.LOW)
    print("[DEBUG] Going left.")


  def _rampSpeed(self, speed):
    """Method ramping up speed to avoid loss of control

    Args:
        speed (int): PWM Duty Cycle, from 0 do 100%
    """
    x = 0
    while(x <= speed):
      self.speedRight.ChangeDutyCycle(x)
      self.speedLeft.ChangeDutyCycle(x)
      x += 10
      time.sleep(0.001)


  def goDirection(self, direction):
    #buffer to not ramp up speed constantly
    if (direction == self.lastDirection):
      #same as before
      pass
    else:
      #forward
      if(direction == "forward"):
        self._goForward()
        self._rampSpeed(100)
      #reverse
      elif(direction == "reverse"):
        self._goReverse()
        self._rampSpeed(100)
      #left
      elif(direction == "left"):
        self._goLeft()
        self._rampSpeed(100)
      #right
      elif(direction == "right"):
        self._goRight()
        self._rampSpeed(100)
      
      self.lastDirection = direction

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('direction')
  args = parser.parse_args()
  motorDriver = MotorDriver()
  motorDriver.initMotorPins()
  motorDriver.goDirection(args.direction)

if __name__ == "__main__":
  main()
