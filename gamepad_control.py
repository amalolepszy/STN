from __future__ import print_function
from inputs import get_gamepad
from inputs import devices

class GamepadControl():
  """[002] Klasa zawierająca funkcje do sterowania zdalnego za pomocą pada x360"""
  lastDir = "forward"
  def listGamepads(self): #listowanie mozliwego sprzetu
    print("Detected devices:\n")
    for device in devices:
      print(device)

  def _getGamepadEvent(self):
    return get_gamepad()

  def logGamepadEvents(self): #listowanie inputow
    while(1):
      events = self._getGamepadEvent()
      for event in events:
        print(event.ev_type, event.code, event.state)
      
  def getGamepadDirection(self, sensitivity = 30000):
    dir = ""
    events = self._getGamepadEvent()
    for event in events:
      #lewo-prawo
      if(event.ev_type == "Absolute" and event.code == "ABS_X"):
        if(event.state > sensitivity): #prawo
          dir = "right"
        elif(event.state < -sensitivity): #lewo
          dir = "left"
        elif(event.state > -sensitivity and event.state < sensitivity):
          dir = "stand"
      #gora-dol
      if(event.ev_type == "Absolute" and event.code == "ABS_Y"):
        if(event.state > sensitivity): #gora
          dir = "reverse"
        elif(event.state < -sensitivity): #dol
          dir = "forward"
        elif(event.state > -sensitivity and event.state < sensitivity):
          dir = "stand"
      
    
    if (dir in ["right", "left", "reverse", "forward", "stand"]):
      self.lastDir = dir
    else:
      dir = self.lastDir
    return dir

  def logGamepadDirection(self):
    while(1):
      print(self.getGamepadDirection())

if __name__ == "__main__":
  Control = GamepadControl()
  Control.listGamepads()
  Control.logGamepadDirection()

