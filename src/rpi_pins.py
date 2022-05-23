class motorPins:
  """Class initializing pins used for the L298N DC motor driver.

      EN - Enable:
        # GND - disabled
        # 5V - enabled
        # PWM - speed of motor

      INA - Input A:
        # 5V - Forward
        # GND - Reverse

      INB - Input B:
        # 5V - Reverse
        # GND - Forward           
  """
  #right - motor A
  MOTOR_RIGHT_EN = 18   #ENA
  MOTOR_RIGHT_IN1 = 4   #in1
  MOTOR_RIGHT_IN2 = 14  #in2

  #left - motor B
  MOTOR_LEFT_EN = 13      #ENB
  MOTOR_LEFT_IN1 = 16   #in3
  MOTOR_LEFT_IN2 = 19   #in4

class sensorPins:
  """Class initializing pins used for the IR sensors.
  Placement of the sensors:
                               │
                               │
                          ┌────┼────┐
                          │   XXX   │
                          │ X  │  X │
                          │    │    │
                          │    │    │
                          │    │    │
                          │    │    │
                          └────┼────┘
                               │
  """
  #front left
  LEFT_FAR = 27
  LEFT_CLOSE = 22
  #center
  CENTER = 10
  #right
  RIGHT_CLOSE = 9
  RIGHT_FAR = 11

