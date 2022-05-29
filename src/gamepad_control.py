import xbox


class GamepadControl(xbox.Joystick):
  """[021] Rework the class to work with xbox.
  [002] Class containing methods to gather inputs from the x360 controller."""


  def getLeftStickDirection(self):
    left_stick_y = self.leftY()
    if(left_stick_y <= -0.5):
      return "forward"
    elif (left_stick_y >= 0.5):
      return "reverse"
    elif (left_stick_y < 0.5 and left_stick_y > -0.5):
      return "stay"
    

  def getRightStickDirection(self):
    right_stick_x = self.rightX()
    if(right_stick_x < -0.5):
      return "left"
    elif (right_stick_x > 0.5):
      return "right"
    elif (right_stick_x < 0.5 and right_stick_x > -0.5):
      return "dontturn"
  
  def getGamepadDirection(self):
    """ Returns the direction that the robot should go:
    forward, reverse, stay, left, right, forward-left/right, reverse-left/right

    Returns:
        string: The direction that the robot should go.
    """
    if(self.getLeftStickDirection() == "forward" and self.getRightStickDirection() == "dontturn"):
      dir = "forward"
    elif(self.getLeftStickDirection() == "reverse" and self.getRightStickDirection() == "dontturn"):
      dir =  "reverse"
    elif(self.getLeftStickDirection() == "stay" and self.getRightStickDirection() == "dontturn"):
      dir =  "stay"
    elif(self.getLeftStickDirection() == "stay" and self.getRightStickDirection() == "left"):
      dir =  "left"
    elif(self.getLeftStickDirection() == "stay" and self.getRightStickDirection() == "right"):
      dir =  "right"
    elif(self.getLeftStickDirection() == "forward" and self.getRightStickDirection() == "right"):
      dir =  "forward-right"
    elif(self.getLeftStickDirection() == "forward" and self.getRightStickDirection() == "left"):
      dir =  "forward-left"
    elif(self.getLeftStickDirection() == "reverse" and self.getRightStickDirection() == "right"):
      dir =  "reverse-right"
    elif(self.getLeftStickDirection() == "reverse" and self.getRightStickDirection() == "left"):
      dir =  "reverse-left"
    
    return dir


  def getPressedButton(self):

    if(self.A):
      return "A"
    elif(self.B):
      return "B"
    elif(self.X):
      return "X"
    elif(self.Y):
      return "Y"
    elif(self.leftTrigger):
      return "LT"
    elif(self.rightTrigger):
      return "RT"
    else:
      return "nobutton"


def main():
  Control = GamepadControl()
  while(1):
      print(Control.getGamepadDirection())
if __name__ == "__main__":
  main()