"""A script made with pag to play Idle Slayer automatically."""
# screen 1366x768
import pyautogui as pag
import keyboard
import time
from colorama import just_fix_windows_console, Fore, Style
from numpy.random import uniform

from core.mouse import click
from core.counter import Counter
from core.datetime import get_time_and_datetime


def main():
  initial_execution_time = time.time()
  initial_time, initial_datetime = get_time_and_datetime()

  counter = Counter()

  print('[script] The program is running... -', initial_time)

  print('[script] Taking screenshot...')
  pag.screenshot(f'{initial_datetime}.png') # hour.minute-day.month.year

  while keyboard.is_pressed('q') != True:
    # Get offline/temporally rewards
    if pag.pixel(710, 15)[2] == 0:
      pag.click(710, 15, button='left')
      pag.sleep(uniform(0.1, 0.3))

    # Check if the portal is available
    if pag.pixel(1240, 90)[2] == 153:
      # click in the portal icon
      pag.click(1240, 90)
      pag.sleep(uniform(0.1, 0.3))
      # press "yes"
      pag.click(580, 590)
      pag.sleep(uniform(0.5, 1))

    # Sprint
    if pag.pixel(100, 630)[2] == 155:
      pag.click(100, 630, button='left')

    # Jump and shoot with bow
    click(650, 380, uniform(0.1, 0.3))
    counter.add_counter()

  end_time, end_datetime = get_time_and_datetime()

  print('[script] Another screenshot...')
  pag.screenshot(f'{end_datetime}.png')
  print('[script] Done! Your screenshots are available at .')

  print(f'[script] Totally, you jump/shoot {Fore.RED}{counter.count}{Style.RESET_ALL} times')
  print('[script] The program has finished -', end_time)
  print(Fore.LIGHTBLACK_EX + '---------------------------------------------' + Style.RESET_ALL)
  print(f'Time running: {Fore.GREEN}{round(time.time() - initial_execution_time, 3)}s')


if __name__ == '__main__':
  # Settings
  pag.PAUSE = 0.1 # delay after all the commands
  just_fix_windows_console() # colorama

  main()
