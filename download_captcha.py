import undetected_chromedriver as uc
from configparser import ConfigParser
from selenium.webdriver.common.by import By

options = uc.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
browser = uc.Chrome(
    options=options
)
config = ConfigParser()
config.read('config.ini')

for i in range(100):
    browser.get((config.get('VFS', 'url')))

    captcha_img = browser.find_element(by=By.ID, value='CaptchaImage')

    with open(r"captchas\%s.png"%i, 'wb') as file:
        file.write(captcha_img.screenshot_as_png)

# select a random image from the folder