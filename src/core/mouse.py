"""Mouse handling"""

from time import sleep
from win32api import mouse_event, SetCursorPos
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP

def click(x: int, y: int, delay: int = 0.01):
  SetCursorPos((x, y))
  mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
  sleep(delay)
  mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)
