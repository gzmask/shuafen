from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import random
import time

def get_screenshot(driver):
    get_screenshot.counter+=1
    # Take a screenshot after the video has played
    screenshot_path = '/screenshots/screenshot'+str(get_screenshot.counter)+'.png'
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")
get_screenshot.counter = 0

# Set up Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36')

print("started shua fen!")

# shuafen31@gmail.com
# gaoxiefeng906@gmail.com

# Manually set the path to chromedriver
driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=chrome_options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)

# Sign into YouTube
driver.get('https://www.youtube.com/signin')
wait = WebDriverWait(driver, 40)
email_input = wait.until(EC.element_to_be_clickable((By.NAME, "identifier")))
email_input.clear()  # Clears any pre-filled values, just in case
email_input.send_keys("gaoxiefeng906@gmail.com") 
#next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
next_button.click()

get_screenshot(driver)
time.sleep(20)
get_screenshot(driver)
passwd_input = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
passwd_input = wait.until(EC.element_to_be_clickable((By.NAME, "Passwd")))
passwd_input.clear()  # Clears any pre-filled values, just in case
passwd_input.send_keys("") 
get_screenshot(driver)

next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
next_button.click()

time.sleep(20)
get_screenshot(driver)

# Play a video
driver.get('https://www.youtube.com/watch?v=2Mr1lT3Prtg')
# driver.get('https://www.bilibili.com/video/BV1nsYJePEQi')


# Click somewhere on the page to ensure focus and then press "Space"
try:
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.SPACE)  # Simulate pressing space to play the video
    print("Space key pressed.")
except Exception as e:
    get_screenshot(driver)


# Wait for the video to play for at least 30 seconds
watch_time = random.randint(20, 60);
time.sleep(watch_time)

get_screenshot(driver)

# Check if the video page shows any robot verification
page_title = driver.title
print(f"Page title: {page_title}")

# Close the browser
driver.quit()

print("shua fen ended. watched time:" + str(watch_time) + " seconds.")
