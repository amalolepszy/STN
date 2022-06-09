import RPi.GPIO as GPIO
from rpi_pins import sensorPins as sPins
from motor_driver import MotorDriver as mDriver

import os

class ReflectiveSensor(mDriver):
  """Class used for controlling and setting up the reflective sensors.
     Callback methods are used for interrupts.
  """
  fullSpeed = 50
  halfSpeed = 30
  quarterSpeed = 15

  def leftFarCallback(self):
    print("Left Far Sensor triggered")
    self._goForward()
    self.speedLeft.ChangeDutyCycle(0)
    self.speedRight.ChangeDutyCycle(self.fullSpeed)

  def leftCloseCallback(self):
    print("Left Close Sensor triggered")
    self._goForward()
    self.speedLeft.ChangeDutyCycle(0)
    self.speedRight.ChangeDutyCycle(self.fullSpeed)
    

  def centerCallback(self):
    print("Center Sensor triggered")
    self._goForward()
    self.speedLeft.ChangeDutyCycle(self.fullSpeed)
    self.speedRight.ChangeDutyCycle(self.fullSpeed)

  def rightCloseCallback(self):
    print("Right Close Sensor triggered")
    self._goForward()
    self.speedLeft.ChangeDutyCycle(self.fullSpeed)
    self.speedRight.ChangeDutyCycle(0)


  def rightFarCallback(self):
    self._goForward()
    print("Right Far Sensor triggered")
    self.speedLeft.ChangeDutyCycle(self.fullSpeed)
    self.speedRight.ChangeDutyCycle(0)

  def initSensorPins(self):
    """Initializing Pins used for the sensors.
        They are listed as inputs, digital data is being extracted from them.
    """
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #pin setup input
    GPIO.setup(sPins.LEFT_CLOSE, GPIO.IN)
    GPIO.setup(sPins.LEFT_FAR, GPIO.IN)
    GPIO.setup(sPins.RIGHT_CLOSE, GPIO.IN)
    GPIO.setup(sPins.RIGHT_FAR, GPIO.IN)
    GPIO.setup(sPins.CENTER, GPIO.IN)

    # #setting up interrupts
    # #GPIO.add_event_detect(sPins.LEFT_CLOSE, GPIO.RISING,
    # #                      callback = self.leftCloseCallback, bouncetime = 20)
    # #GPIO.add_event_detect(sPins.LEFT_FAR, GPIO.RISING,
    # #                      callback = self.leftFarCallback, bouncetime = 20)
    # #GPIO.add_event_detect(sPins.RIGHT_CLOSE, GPIO.RISING,
    #                       callback = self.rightCloseCallback, bouncetime = 20)
    # GPIO.add_event_detect(sPins.RIGHT_FAR, GPIO.RISING,
    #                       callback = self.rightFarCallback, bouncetime = 20)
    # GPIO.add_event_detect(sPins.CENTER, GPIO.RISING,
    #                       callback = self.centerCallback, bouncetime = 20)


  def getStatus(self, sensorPin):
    """Method getting status of reflective sensor

    Args:
        sensorPin (int): Pin of the sensor

    Returns:
        int : 1 when light gets reflected, 0 when nothing to reflect
    """
    sPin = int(sensorPin)
    GPIO.setup(sPin, GPIO.IN)
    print(GPIO.input(sPin))
    return GPIO.input(int(sensorPin))
  
  def ride_reflective(self):
    while(1):
      print("LEFT_FAR " + str(GPIO.input(sPins.LEFT_FAR)) +"\nLEFT_FAR " + str(GPIO.input(sPins.LEFT_CLOSE)) + "\nCENTER " + str(GPIO.input(sPins.CENTER)) + "\nRIGHT_CLOSE " + str(GPIO.input(sPins.RIGHT_CLOSE)) + "\nRIGHT_FAR " + str(GPIO.input(sPins.RIGHT_FAR)))
      if ((GPIO.input(sPins.RIGHT_FAR) and GPIO.input(sPins.LEFT_CLOSE) and GPIO.input(sPins.CENTER) and GPIO.input(sPins.LEFT_CLOSE) and GPIO.input(sPins.LEFT_FAR))):
        self._standStill()
      elif(GPIO.input(sPins.LEFT_FAR) == True):
        self._goLeft()
      elif (GPIO.input(sPins.LEFT_CLOSE) == True):
        self._goLeft()
      elif (GPIO.input(sPins.CENTER) == True):
        self._goForward()
      elif (GPIO.input(sPins.RIGHT_CLOSE) == True):
        self._goRight()
      elif (GPIO.input(sPins.RIGHT_FAR) == True):
        self._goRight()

      os.system('clear')
      

def main():
  # #argument parser for debugging
  # parser = argparse.ArgumentParser()
  # parser.add_argument('sensorPin')
  # parser.add_argument(' ', action='store_true')
  # args = parser.parse_args()

  # #testing sensor
  RSensor = ReflectiveSensor()
  RSensor.initSensorPins()
  # if not args.sensorPin:
  #   args = parser.parse_args('sensorPin')
  #   RSensor.getStatus(args.sensorPin)
  




if __name__ == "__main__":
  main()
