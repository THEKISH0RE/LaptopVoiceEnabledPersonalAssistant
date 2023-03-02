import  os, random
import numpy as np
from pyautogui import screenshot
import cv2
from random import randint


def music_path(title):
    musicdir = f"D:\\songs\\{title}"
    songs = os.listdir(musicdir)
    os.startfile(os.path.join(musicdir, random.choice(songs)))
  
def capture_screenshot():
  image = cv2.cvtColor(np.array(screenshot()), cv2.COLOR_RGB2BGR)
  cv2.imwrite(f"screenshot\\image_{randint(1,10)}.png", image) 