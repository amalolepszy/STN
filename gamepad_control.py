from __future__ import print_function
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

  def LogGamepadEvents(this): #listowanie inputow
    while(1):
      events = this.GetGamepadEvent()
      for event in events:
        print(event.ev_type, event.code, event.state)
      
  def GetGamepadDirection():
    events = GamepadControl.GetGamepadEvent()
    for event in events:
      #lewo-prawo
      if(event.ev_type == "ABSOLUTE" and event.code == "ABS_X"):
        if(event.code > 27000): #prawo
          return "right"
        elif(event.code < -27000): #lewo
          return "left"
      #gora-dol
      if(event.ev_type == "ABSOLUTE" and event.code == "ABS_Y"):
        if(event.code > 27000): #dol
          return "back"
        elif(event.code < -27000): #gora
          return "forward"

  def LogGamepadDirection():
    print(GamepadControl.GetGamepadDirection())

if __name__ == "__main__":
  GamepadControl.ListGamepads()
  GamepadControl.LogGamepadDirection()