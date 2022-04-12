from __future__ import print_function
from re import I
from inputs import get_gamepad
from inputs import devices

class GamepadControl():
  """[002] Klasa zawierająca funkcje do sterowania zdalnego za pomocą pada x360"""
  
  def ListGamepads(): #listowanie mozliwego sprzetu
    print("Detected devices:\n")
    for device in devices:
      print(device)

  def GetGamepadEvent():
    return get_gamepad()

  def LogGamepadEvents(): #listowanie inputow
    while(1):
      events = GamepadControl.GetGamepadEvent()
      for event in events:
        print(event.ev_type, event.code, event.state)
      
  def GetGamepadDirection():
    dir = ""
    events = GamepadControl.GetGamepadEvent()
    for event in events:
      #lewo-prawo
      if(event.ev_type == "Absolute" and event.code == "ABS_X"):
        if(event.state > 15000): #prawo
          dir = "right"
        elif(event.state < -15000): #lewo
          dir = "left"
      #gora-dol
      if(event.ev_type == "Absolute" and event.code == "ABS_Y"):
        if(event.state > 15000): #gora
          dir = "back"
        elif(event.state < -15000): #dol
          dir = "forward"
    return dir

  def LogGamepadDirection():
    while(1):
      print(GamepadControl.GetGamepadDirection())

if __name__ == "__main__":
  GamepadControl.ListGamepads()
  GamepadControl.LogGamepadDirection()