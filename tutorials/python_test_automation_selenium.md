# installation
```
pip install selenium
```

# sample code
```
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up driver
driver = webdriver.Firefox(executable_path=r'path/to/geckodriver.exe')

# GeckoDriver: This is a WebDriver implementation that allows Selenium to interact with the Firefox browser. It translates the WebDriver commands (like opening a URL, clicking a button, etc.) into actions that the Firefox browser can understand.

# Open URL
driver.get("https://www.coursera.org/learn/web-mobile-testing")

# Find element by link text and click
driver.find_element(By.LINK_TEXT, "here").click()

# Navigate back
driver.back()

# Find input element by tag name and send keys
driver.find_element(By.TAG_NAME, "input").send_keys("learn")

# Close driver
driver.quit()
```

# sample code 2
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver path
driver = webdriver.Firefox(executable_path='C:\\Apps\\geckodriver.exe')

# Open URL
driver.get('https://www.coursera.org/specialization/software-testing-automation')

# Wait for 5 seconds
time.sleep(5)

# Find search element and send 'Economics' text
search = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="What do you want to learn?"]')
search.send_keys('Economics')
search.send_keys(Keys.ENTER)

# Wait for 5 seconds
time.sleep(5)

# Close browser
driver.close()
```

