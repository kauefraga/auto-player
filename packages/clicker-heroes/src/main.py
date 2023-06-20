# Developed with 1366x786 (screen size).
import time
import keyboard
import pyautogui as pag
from numpy.random import uniform
from rich import print
from rich.panel import Panel
from rich.prompt import Confirm

from ui.icons import SCRIPT, INTERROGATIVE
from utils.mouse import click
from utils.counter import counter, travel_counter
from utils.datetime import get_time_and_datetime


def main():
  initial_execution_time = time.time()
  initial_time, initial_datetime = get_time_and_datetime()

  print(f'{SCRIPT} The program is running... - {initial_time}')

  print(f'{SCRIPT} Taking a screenshot...')
  pag.screenshot(f'{initial_datetime}.png') # hour.minute-day.month.year

  # Focus on game
  pag.click(600, 400)
  # Use skills
  for i in range(1, 10):
    keyboard.press_and_release(f'{i}')

  while keyboard.is_pressed('q') is not True:
    # Check if there is some new island to travel in
    if pag.pixel(1105, 30)[0] == 255:
      pag.click(1105, 30)
      travel_counter.add_counter()
    # Not necessary if the progression mode is available

    # Attack monsters
    pag.click(1000, 450)

    # Increase the counter before run again
    counter.add_counter()

  end_time, end_datetime = get_time_and_datetime()

  print(f'{SCRIPT} Another screenshot...')
  pag.screenshot(f'{end_datetime}.png')
  print(f'{SCRIPT} [bright_green]Done![/] Your screenshots are available at .')

  print(f'{SCRIPT} Monsters was attacked: [green1]{counter.count}[/] times')
  print(f'{SCRIPT} You travelled: [green1]{travel_counter.count}[/] times')
  print(f'{SCRIPT} The program has finished... - {end_time}')
  print('[bright_black]---------------------------------------------')
  print(f'Time running: [green]{round(time.time() - initial_execution_time, 3)}s')

if __name__ == '__main__':
  print(Panel(
    '- The game is on screen;\n' +
    '- You are in the right world;\n' +
    '- You do not need to do anything else while it is running.',
    title='[b magenta]Verify if'))

  if not Confirm.ask(f'{INTERROGATIVE} Are you ready to run it?'):
    exit(0)

  main()
