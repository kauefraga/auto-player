"""Mouse handling"""
import pyautogui as pag

def click(x: int, y: int, delay: float):
  """Press the left mouse button and release it at a specified delay"""
  pag.mouseDown(
    x, y,
    button='left',
    duration=0.75
  )
  pag.sleep(delay)
  pag.mouseUp()
