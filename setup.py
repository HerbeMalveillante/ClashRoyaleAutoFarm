import time
import pyautogui
import pickle
import os

def confirmBox(message):
    confirm = input(message + " (y/n): ")
    if confirm == "y":
        return True
    else:
        exit()

def waitLoop(seconds):
    for i in range(seconds):
        print("Waiting for " + str(seconds - i) + " seconds...")
        time.sleep(1)

def writePositions():
    confirmBox("Doing this will remove all previous configuration. Are you sure you want to continue ?")
    confirmBox("You will need to input the coordinates of a few spots on the screen. Are you ready ?")
    print("Please focus the clash royale window.")
    waitLoop(5)
    print("First point : middle of 'Party' button. Recording will take place in ten seconds.")
    waitLoop(10)
    x1, y1 = pyautogui.position()
    print("Second point : middle of your second card. Recording will take place in fifteeny seconds.")
    waitLoop(15)
    x2, y2 = pyautogui.position()
    print("Third point : position of the card on the bridge. Recording will take place in ten seconds.")
    waitLoop(10)
    x3, y3 = pyautogui.position()

    positionArray = [x1, y1, x2, y2, x3, y3]
    # remove "positions.craf" if it exists
    if os.path.exists("positions.craf"):
        os.remove("positions.craf")
        print("Previous positions.craf file removed.")

    # create a file with the positions
    with open("positions.craf", "wb") as f:
        pickle.dump(positionArray, f)
        print("positions.craf file created.")

if __name__ == "__main__":
    writePositions()