# Idle Slayer Script

> I made this script to play to Idle Slayer automatically because the game is very repetitive about shooting, jumping, collecting coins, etc.

### Features

- Jump and shoot! Get more coins and kills by using the bow.
- Run it, leave it alone and when you back to it, know exactly for how long it runs.
- Currently it's sprinting, jumping, shooting, verifying if there's a portal to use (then using if there is).
- Obtain the offline rewards if there are.
- Capture the screen and know exactly how much coins you had at the beginning.

## 🎲 Prerequisites

- Change the code magic numbers for your screen size (i build it with a laptop, so 1366x768).
  - Use `pyautogui.position` to get x and y coordinates;
  - Use `pyautogui.displayMousePosition` to get x, y and rgb colors.

## ⬇️ How to download and use it in your game

1. Open the game
2. Run the file `src/idleslayer.py`

```bash
python src/idleslayer.py # if you have python2, you should run py or python3 instead
```

## 📜 Coming soon

- If some key is pressed, open the ascension menu and then ascend (you can also check the vassals menu)
