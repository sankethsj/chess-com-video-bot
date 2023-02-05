import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from utils.capture import ScreenCapture
from utils.helper import get_game_link, login

username = os.environ['CHESS_USERNAME']
password = os.environ['CHESS_PASSWORD']

# adjust according to your screen resolution
CAPTURE_REGION = (300, 180, 1820, 1000)
FPS = 25

URL = f"https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/member/{username}"

# go to chess.com login webiste
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.maximize_window()
browser.get(URL)

# login to chess.com
login(browser, username, password)

time.sleep(5) # adding sleep to wait till page loads

# get the latest game link
game_number, game_link = get_game_link(browser)

# go to the game url
browser.get(game_link)

# find on auto-play start button
start_btn = browser.find_element(By.XPATH, '//span[@class="icon-font-chess ui_v5-button-icon chevron-previous"]')
start_btn.click()
play_btn = browser.find_element(By.XPATH, '//span[@class="icon-font-chess ui_v5-button-icon play"]')

# create a directory to store the videos
os.makedirs('video_output', exist_ok=True)
filename = f"video_output/chess_game_{game_number}_{int(time.time())}.mp4"

# setup the screen capture region, fps
sc = ScreenCapture(CAPTURE_REGION, FPS, filename)

# click on play button to start the game replay
play_btn.click()

# start the screen recording & save video
sc.start(play_btn)

# close the browser
browser.close()
