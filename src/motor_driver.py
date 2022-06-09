import RPi.GPIO as GPIO
import time
import argparse
from rpi_pins import motorPins as mPins

class MotorDriver():
  speedRight = 0
  speedLeft = 0
  lastDirection = "forward"
  fullSpeed = 40
  halfSpeed = 30



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
    self.speedRight.ChangeDutyCycle(self.fullSpeed)
    self.speedLeft.ChangeDutyCycle(self.fullSpeed)
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.LOW)
    print("[DEBUG] Going forward.")

  def _goForwardLeft(self):
    self.speedRight.ChangeDutyCycle(self.halfSpeed)
    self.speedLeft.ChangeDutyCycle(self.fullSpeed)
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.LOW)
    print("[DEBUG] Going forward - left.")

  def _goForwardRight(self):
    self.speedLeft.ChangeDutyCycle(self.halfSpeed)
    self.speedRight.ChangeDutyCycle(self.fullSpeed)
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.LOW)
    print("[DEBUG] Going forward - right.")

  def _goReverse(self):
    self.speedLeft.ChangeDutyCycle(self.fullSpeed)
    self.speedRight.ChangeDutyCycle(self.fullSpeed)
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.HIGH)
    print("[DEBUG] Going reverse.")

  def _goReverseLeft(self):
    self.speedLeft.ChangeDutyCycle(self.fullSpeed)
    self.speedRight.ChangeDutyCycle(self.halfSpeed)
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.HIGH)
    print("[DEBUG] Going reverse - left.")

  def _goReverseRight(self):
    self.speedLeft.ChangeDutyCycle(self.halfSpeed)
    self.speedRight.ChangeDutyCycle(self.fullSpeed)
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.HIGH)
    print("[DEBUG] Going reverse - right.")

  def _goRight(self):
    self.speedLeft.ChangeDutyCycle(self.fullSpeed)
    self.speedRight.ChangeDutyCycle(self.fullSpeed)
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.LOW)
    print("[DEBUG] Going right.")

  def _goLeft(self):
    self.speedLeft.ChangeDutyCycle(self.fullSpeed)
    self.speedRight.ChangeDutyCycle(self.fullSpeed)
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.HIGH)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.LOW)
    print("[DEBUG] Going left.")

  def _standStill(self):
    self.speedLeft.ChangeDutyCycle(0)
    self.speedRight.ChangeDutyCycle(0)
    GPIO.output(mPins.MOTOR_LEFT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_LEFT_IN2, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN1, GPIO.LOW)
    GPIO.output(mPins.MOTOR_RIGHT_IN2, GPIO.LOW)
    print("[DEBUG] Standing still.")


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
      #forward-right
      elif(direction == "forward-right"):
        self._goForwardRight()
      #forward-left
      elif(direction == "forward-left"):
        self._goForwardLeft()
      #reverse-right
      elif(direction == "reverse-right"):
        self._goReverseRight()
      #reverse-left
      elif(direction == "reverse-left"):
        self._goReverseLeft()
      #standstill
      elif(direction == "stay"):
        self._standStill()
        self._rampSpeed(0)
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
