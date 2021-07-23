from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

def scriping():


    options = Options()
    options.add_argument('--headless')


    browser = webdriver.Chrome(executable_path='chromedriver',chrome_options=options)
    browser.set_window_size(1920,1080)
    BASE_URL = 'https://www.esthe-ranking.jp/shibuya/'
    browser.get(BASE_URL)
    time.sleep(4)

    result = browser.get_screenshot_as_file("testscreenshot.png")
    result

    browser.quit()

if __name__ == '__main__':
    scriping()