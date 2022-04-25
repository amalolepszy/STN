from rpi_pins import sensorPins as sPins
import RPi.GPIO as GPIO
import argparse

class ReflectiveSensor:
  """Class used for controlling and setting up the reflective sensors.
     Callback methods are used for interrupts.
  """
  def frontLeftCloseCallback(self):
    print("Front Left Close Sensor triggered")


  def frontLeftFarCallback(self):
    print("Front Left Far Sensor triggered")


  def frontRightClose(self):
    print("Front Right Close Sensor triggered")


  def frontRightFarCallback(self):
    print("Front Right Far Sensor triggered")


  def backRightCallback(self):
    print("Back Right Sensor triggered")


  def backLeftCallback(self):
    print("Back Left Close Sensor triggered")  


  def initSensorPins(self):
    """Initializing Pins used for the sensors.
        They are listed as inputs, digital data is being extracted from them.
    """
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #pin setup input
    GPIO.setup(sPins.FRONT_LEFT_CLOSE, GPIO.IN)
    GPIO.setup(sPins.FRONT_LEFT_FAR, GPIO.IN)
    GPIO.setup(sPins.FRONT_RIGHT_CLOSE, GPIO.IN)
    GPIO.setup(sPins.FRONT_RIGHT_FAR, GPIO.IN)
    GPIO.setup(sPins.BACK_RIGHT, GPIO.IN)
    GPIO.setup(sPins.BACK_LEFT, GPIO.IN)

    #setting up interrupts
    GPIO.add_event_detect(sPins.FRONT_LEFT_CLOSE, GPIO.RISING,
                          callback = self.frontLeftCloseCallback, bouncetime = 20)
    GPIO.add_event_detect(sPins.FRONT_LEFT_FAR, GPIO.RISING,
                          callback = self.frontLeftFarCallback, bouncetime = 20)
    GPIO.add_event_detect(sPins.FRONT_RIGHT_CLOSE, GPIO.RISING,
                          callback = self.frontRightClose, bouncetime = 20)
    GPIO.add_event_detect(sPins.FRONT_RIGHT_FAR, GPIO.RISING,
                          callback = self.frontRightFarCallback, bouncetime = 20)
    GPIO.add_event_detect(sPins.BACK_RIGHT, GPIO.RISING,
                          callback = self.backRightCallback, bouncetime = 20)
    GPIO.add_event_detect(sPins.BACK_LEFT, GPIO.RISING,
                          callback = self.backLeftCallback, bouncetime = 20)


  def getStatus(self, sensorPin):
    """Method getting status of reflective sensor

    Args:
        sensorPin (int): Pin of the sensor

    Returns:
        int : 1 when light gets reflected, 0 when nothing to reflect
    """
    return GPIO.input(int(sensorPin))

def main():
  #argument parser for debugging
  parser = argparse.ArgumentParser()
  parser.add_argument('sensorPin')
  args = parser.parse_args()

  #testing sensor
  RSensor = ReflectiveSensor()
  RSensor.getStatus(args.sensorPin)
  RSensor.initSensorPins()
  while(1):
    pass

if __name__ == "__main__":
  main()
