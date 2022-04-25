# the goal is to drag on three spots of the clash royale screen, as fast as possible.
# We want our cards to cycle equally so the cicle will be the following :
# - First card
# - First card placement (right bridge)
# - Second card
# - Second card placement (right bridge)
# - Third card
# - Third card placement (right bridge)
# - Fourth card
# - Fourth card placement (right bridge)
# - Replay/Choose mode
# - Loop

# As fast as possible obviously
# Note that you may need to manually unlock the "first mastery"
# That requires you to win five games with the card (which could be difficult
# as we're playing randomly...)

# Please note that you could also get banned while playing this way. I would
# be using an alt account for that but I don't have one with masteries unlocked
# and I don't have the courage to create one and up it

# I'm going to use a delay to not be flagged as a bot so the speeds are not
# going to be optimal, but it should be fine anyways


# ========== Herbe Malveillante ==========
# |--- https://herbemalveillante.com/ ---|
# | https://github.com/herbemalveillante |
# ________________________________________

from cgi import test
import pyautogui
import time
import pickle
import setup
import os
import intro



intro.main()


# check if there is no "positions.craf" file
if not os.path.exists("positions.craf"):
    print("No positions.craf file found. Creating one.")
    setup.writePositions()

# read from the file
with open("positions.craf", "rb") as f:
    positions = pickle.load(f)

x1, y1, x2, y2, x3, y3 = positions


def routine():

    delay = 0

    # drag on "Party" button
    pyautogui.moveTo(x1, y1)
    pyautogui.drag(0, 1, 0.2, button='left')
    # wait half a second
    time.sleep(delay)
    # drag again for second party mode
    pyautogui.moveTo(x1, y1)
    pyautogui.drag(0, 1, 0.2, button='left')
    # wait half a second
    time.sleep(delay)
    # drag on the second card
    pyautogui.moveTo(x2, y2)
    pyautogui.drag(0, 1, 0.2, button='left')
    # wait half a second
    time.sleep(delay)
    # drag on the bridge
    pyautogui.moveTo(x3, y3)
    pyautogui.drag(0, 1, 0.2, button='left')
    # wait half a second
    time.sleep(delay)


def test_rectangle(x1, y1, x2, y2):
    """
    Test if the rectangle is visible on the screen
    """
    
    # top-left corner is (x1, y1)
    # top right corner is (x2, y1)
    # bottom-right corner is (x2, y2)
    # bottom left corner is (x1, y2)

    duration = 0.7

    pyautogui.moveTo(x1, y1, duration=duration, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(x2, y1, duration=duration, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(x2, y2, duration=duration, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(x1, y2, duration=duration, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(x1, y1, duration=duration, tween=pyautogui.easeInOutQuad)


# test_rectangle(215, 554, 348, 617)
# test_rectangle(246, 397, 344, 440)

print("Starting routine in two seconds...")
time.sleep(2)
print("Starting routine. Slam your mouse on any of the corners of the screen to stop.")
i = 1
while True:
    print(f"Routine {i}. Slam your mouse on any of the corners of the screen to stop.")
    routine()
    i += 1
    