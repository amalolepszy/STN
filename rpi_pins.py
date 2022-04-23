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
  MOTOR_RIGHT_EN = 5      #ENA
  MOTOR_RIGHT_IN1 = 4   #in1
  MOTOR_RIGHT_IN2 = 14  #in2

  #left - motor B
  MOTOR_LEFT_EN = 16      #ENB
  MOTOR_LEFT_IN1 = 17   #in3
  MOTOR_LEFT_IN2 = 18   #in4

class sensorPins:
  """Class initializing pins used for the IR sensors.
  Placement of the sensors:
                               │
                               │
                          ┌────┼────┐
                          │   X│X   │
                          │ X  │  X │
                          │    │    │
                          │    │    │
                          │    │    │
                          │   X│X   │
                          └────┼────┘
                               │
  """
  #front left
  FRONT_LEFT_CLOSE = 1
  FRONT_LEFT_FAR = 2
  #front right
  FRONT_RIGH_CLOSE = 3
  FRONT_RIGHT_FAR = 4
  #back
  BACK_RIGHT = 5
  BACK_LEFT = 6
