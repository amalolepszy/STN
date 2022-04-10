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

  def ListGamepadEvents(): #listowanie inputow
    while(1):
      events = SterowanieZdalne.GetGamepadEvent()
      for event in events:
        print(event.ev_type, event.code, event.state)
      


if __name__ == "__main__":
  SterowanieZdalne.ListGamepads()
  SterowanieZdalne.ListGamepadEvents()