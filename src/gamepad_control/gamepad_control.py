import xbox360_controller
import pygame


class GamepadControl(xbox360_controller.Controller):
  """[020] Rework the class to work with pygame.
  [002] Class containing methods to gather inputs from the x360 controller."""

  pygame.init()

  def getLeftStickDirection(self):
    left_stick_x, left_stick_y = self.get_left_stick()
    # print("left_stick_x = ", left_stick_x)
    # print("left_stick_y = ", left_stick_y)
    if(left_stick_y <= -0.5):
      return "forward"
    elif (left_stick_y >= 0.5):
      return "reverse"
    elif (left_stick_y < 0.5 and left_stick_y > -0.5):
      return "stay"
    

  def getRightStickDirection(self):
    right_stick_x, right_stick_y = self.get_right_stick()
    # print("right_stick_x = ", right_stick_x)
    # print("right_stick_y = ", right_stick_y)
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
    
    return


  def getPressedButton(self):
    pressed = self.get_buttons()
    #buttons
    a_btn = pressed[xbox360_controller.A]
    b_btn = pressed[xbox360_controller.B]
    x_btn = pressed[xbox360_controller.X]
    y_btn = pressed[xbox360_controller.Y]
    #bumpers
    lt_bump = pressed[xbox360_controller.LEFT_BUMP]
    rt_bump = pressed[xbox360_controller.RIGHT_BUMP]

    if(a_btn):
      return "A"
    elif(b_btn):
      return "B"
    elif(x_btn):
      return "X"
    elif(y_btn):
      return "Y"
    elif(lt_bump):
      return "LT"
    elif(rt_bump):
      return "RT"
    else:
      return "nobutton"


def main():
  Control = GamepadControl()
  while(1):
    for event in pygame.event.get():
      print(Control.getGamepadDirection())
if __name__ == "__main__":
  main()