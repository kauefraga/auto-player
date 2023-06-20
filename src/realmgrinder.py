# Developed with 1366x786 (screen size).

import time
import keyboard
import pyautogui as pag
from numpy.random import uniform
from rich import print

from ui.icons import SCRIPT
from core.mouse import click
from core.counter import Counter


def main():
  initial_execution_time = time.time()

  counter = Counter()

  while keyboard.is_pressed('q') is not True:
    # Activate the skill "Holy Light" if the mana is bigger than 900
    if pag.pixel(1050, 45)[2] == 255:
      # rgb(75 96 255)
      keyboard.press_and_release('3')

    # x1100 y80

    # Get coins by touching on the realm
    click(650, 400, uniform(0.01, 0.03))
    counter.add_counter()

  print(f'{SCRIPT} Coins was collected: [green1]{counter.count}[/] times')
  print('[bright_black]---------------------------------------------')
  print(f'Time running: [green]{round(time.time() - initial_execution_time, 3)}s')


if __name__ == '__main__':

  main()
