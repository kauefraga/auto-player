"""Mouse handling"""
import pyautogui as pag

def click(x: int, y: int, delay: float):
  """Press the left mouse button and release it at a specified delay.

  Args:
      x (int): x position
      y (int): y position
      delay (float): the delay between press and release the mouse button
  """
  pag.mouseDown(
    x, y,
    button='left',
  )
  pag.sleep(delay)
  pag.mouseUp()
