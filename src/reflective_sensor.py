from tkinter import CENTER
import RPi.GPIO as GPIO
from rpi_pins import sensorPins as sPins
from motor_driver import MotorDriver as mDriver

class ReflectiveSensor(mDriver):
  """Class used for controlling and setting up the reflective sensors.
     Callback methods are used for interrupts.
  """
  
  def leftFarCallback(self):
    print("Left Far Sensor triggered")
    self._goForward()
    self.speedLeft.ChangeDutyCycle(20)
    self.speedRight.ChangeDutyCycle(100)

  def leftCloseCallback(self):
    print("Left Close Sensor triggered")
    self._goForward()
    self.speedLeft.ChangeDutyCycle(60)
    self.speedRight.ChangeDutyCycle(100)
    

  def centerCallback(self):
    print("Center Sensor triggered")
    self._goForward()
    self.speedLeft.ChangeDutyCycle(100)
    self.speedRight.ChangeDutyCycle(100)

  def rightCloseCallback(self):
    print("Right Close Sensor triggered")
    self._goForward()
    self.speedLeft.ChangeDutyCycle(100)
    self.speedRight.ChangeDutyCycle(60)


  def rightFarCallback(self):
    self._goForward()
    print("Right Far Sensor triggered")
    self.speedLeft.ChangeDutyCycle(100)
    self.speedRight.ChangeDutyCycle(20)

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
  while(1):
    if(GPIO.input(sPins.LEFT_FAR) == True):
      RSensor.leftFarCallback()
    elif (GPIO.input(sPins.LEFT_CLOSE)):
      RSensor.leftFarCallback()
    elif (GPIO.input(sPins.CENTER)):
      RSensor.centerCallback()
    elif (GPIO.input(sPins.RIGHT_CLOSE)):
      RSensor.rightCloseCallback()
    elif (GPIO.input(sPins.RIGHT_FAR)):
      RSensor.rightFarCallback()




if __name__ == "__main__":
  main()
