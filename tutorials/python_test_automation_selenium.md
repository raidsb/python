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

# overview of selenium features
The cheat sheet provided covers the most common and essential features of using Selenium with Python, but it does not encompass every possible feature or advanced usage scenario. Here's a breakdown of what is covered and what's not:

## Setup and page functions
1. **Basic Navigation:**
   - Opening URLs, refreshing, back and forward navigation
   - Getting current URL and page title
   - Closing browser sessions
  ```python
   from selenium import webdriver

   # Setting up Chrome Driver Example
   driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

   # Setting up Firefox Driver Example
   driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

   # Open a webpage
   driver.get('https://example.com')
   ```

2. **Refresh the Page**
    ```python
    driver.refresh()
    ```
	
3. **Navigate Forward and Backward**
    ```python
    driver.back()
    driver.forward()
	```
4. **Get Current URL**
    ```python
    current_url = driver.current_url
    ```

5. **Get Page Title**
    ```python
    title = driver.title
    ```

6. **Close Browser**
    ```python
    driver.close()  # Closes current tab
    driver.quit()   # Closes all tabs and quits the driver
    ```

## Finding elements
* Using different locators: ID, name, XPath, CSS selector, class name, tag name
* Finding single and multiple elements

1. **Find Element by ID**
    ```python
    element = driver.find_element_by_id('element_id')
    ```

2. **Find Element by Name**
    ```python
    element = driver.find_element_by_name('element_name')
    ```

3. **Find Element by XPath**
    ```python
    element = driver.find_element_by_xpath('//tag[@attribute="value"]')
    ```

4. **Find Element by CSS Selector**
    ```python
    element = driver.find_element_by_css_selector('css_selector')
    ```

5. **Find Element by Class Name**
    ```python
    element = driver.find_element_by_class_name('class_name')
    ```

6. **Find Element by Tag Name**
    ```python
    element = driver.find_element_by_tag_name('tag_name')
    ```

7. **Find Elements (Multiple Elements)**
    ```python
    elements = driver.find_elements_by_xpath('//tag')
	```
	
## Interacting with elements 
* Clicking, entering text, clearing text, submitting forms
* Getting attributes and text of elements
1. **Click an Element**
    ```python
    element.click()
    ```

2. **Enter Text in an Input Field**
    ```python
    element.send_keys('input text')
    ```

3. **Clear Text from an Input Field**
    ```python
    element.clear()
    ```

4. **Submit a Form**
    ```python
    element.submit()
    ```

5. **Get Element Attribute**
    ```python
    attribute_value = element.get_attribute('attribute_name')
    ```

6. **Get Text of an Element**
    ```python
    text = element.text
    ```


## Handling Alerts and Popups
* Accepting, dismissing alerts
* Retrieving alert text
1. **Switch to Alert and Accept**
    ```python
    alert = driver.switch_to.alert
    alert.accept()
    ```

2. **Switch to Alert and Dismiss**
    ```python
    alert.dismiss()
    ```

3. **Get Text from Alert**
    ```python
    alert_text = alert.text
    ```

## Handling Windows and Frames
* Switching between windows and frames
* Returning to default content
1. **Switch to a New Window**
    ```python
    driver.switch_to.window(driver.window_handles[1])
    ```

2. **Switch Back to the Original Window**
    ```python
    driver.switch_to.window(driver.window_handles[0])
    ```

3. **Switch to Frame by Name or ID**
    ```python
    driver.switch_to.frame('frame_name_or_id')
    ```

4. **Switch to Frame by Index**
    ```python
    driver.switch_to.frame(0)
    ```

5. **Switch to Default Content**
    ```python
    driver.switch_to.default_content()
    ```


## Executing JavaScript
* Running JavaScript commands
* Retrieving values from JavaScript
1. **Execute JavaScript Command**
    ```python
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ```

2. **Return Value from JavaScript Execution**
    ```python
    return_value = driver.execute_script("return document.title;")
    ```

## Waiting for Elements:**
* Implicit and explicit waits for better synchronization
1. **Implicit Wait**  
   Waits for a specified amount of time before throwing a `NoSuchElementException`.
    ```python
    driver.implicitly_wait(10)  # Waits up to 10 seconds
    ```

2. **Explicit Wait**  
   Waits for a specific condition to be true before proceeding.
    ```python
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, 'element_id')))
    ```
	
## Taking Screenshots
* Capturing full-page and element-specific screenshots
1. **Take a Screenshot of the Current Window**
    ```python
    driver.save_screenshot('screenshot.png')
    ```

2. **Take a Screenshot of an Element**
    ```python
    element.screenshot('element_screenshot.png')
    ```

## Handling Cookies
* Getting, adding, deleting cookies
1. **Get All Cookies**
    ```python
    cookies = driver.get_cookies()
    ```

2. **Add a Cookie**
    ```python
    driver.add_cookie({'name': 'myCookie', 'value': 'cookie_value'})
    ```

3. **Delete a Cookie by Name**
    ```python
    driver.delete_cookie('cookie_name')
    ```

4. **Delete All Cookies**
    ```python
    driver.delete_all_cookies()
    ```

## Handling Dropdowns
* Using the `Select` class for dropdown interaction
1. **Select Option by Visible Text**
    ```python
    from selenium.webdriver.support.ui import Select

    select = Select(driver.find_element_by_id('dropdown_id'))
    select.select_by_visible_text('Option Text')
    ```

2. **Select Option by Index**
    ```python
    select.select_by_index(1)
    ```

3. **Select Option by Value**
    ```python
    select.select_by_value('option_value')
    ```
	
## Keyboard and Mouse Actions
* Simulating key presses and mouse actions
* Drag-and-drop functionality
1. **Send Keys to an Element**
    ```python
    from selenium.webdriver.common.keys import Keys

    element.send_keys(Keys.RETURN)  # Presses Enter
    ```

2. **Mouse Hover Action**
    ```python
    from selenium.webdriver.common.action_chains import ActionChains

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    ```

3. **Drag and Drop**
    ```python
    source = driver.find_element_by_id('source_element_id')
    target = driver.find_element_by_id('target_element_id')
    actions.drag_and_drop(source, target).perform()
    ```

## **Advanced: Headless Browsing**
* Running browsers in headless mode for background execution
1. **Headless Mode with Chrome**
    ```python
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)
    ```

2. **Headless Mode with Firefox**
    ```python
    from selenium.webdriver.firefox.options import Options

    firefox_options = Options()
    firefox_options.headless = True
    driver = webdriver.Firefox(executable_path='/path/to/geckodriver', options=firefox_options)
    ```

## **Closing Thoughts**

- **Error Handling**: Always use `try-except` blocks to handle exceptions gracefully.
- **Resource Management**: Ensure you close the browser with `driver.quit()` after completing the test to free up resources.
- **Use Context Managers**: For handling WebDriver sessions, context managers can ensure clean startup and teardown.


### **Not Covered Features:**

1. **Advanced Locators and XPath:**
   - More complex XPath queries and CSS selectors

2. **Handling Complex Web Elements:**
   - Working with web components, shadow DOM, or iframes more deeply

3. **Advanced Actions:**
   - Handling multi-touch actions, complex drag-and-drop sequences, and multi-step keyboard actions

4. **Browser Profiles and Options:**
   - Customizing browser profiles and capabilities (e.g., disabling images, setting proxy settings)

5. **Browser DevTools Integration:**
   - Using DevTools for network interception, console logging, and more

6. **Custom WebDriver Executions:**
   - Customizing WebDriver commands and behaviors

7. **Logging and Debugging:**
   - Advanced logging, debugging, and taking videos of the browser session

8. **Grid and Parallel Execution:**
   - Running tests in parallel or on Selenium Grid for distributed testing

9. **Handling SSL Certificates:**
   - Bypassing SSL certificate errors and handling secure connections

10. **Handling File Uploads and Downloads:**
    - Automating file uploads/downloads using system dialogues and browser preferences

11. **Advanced Error Handling:**
    - Using custom exception handling, retry mechanisms, and recovery scenarios

12. **Accessibility Testing:**
    - Integrating accessibility testing tools to check for accessibility standards

13. **Reporting and Integration:**
    - Integrating with test reporting frameworks (e.g., Allure, ExtentReports)
    - CI/CD pipeline integration for automated test execution

# sample/cheat sheet of most selenium features
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up WebDriver options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')  # Disable GPU acceleration
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument('window-size=1920x1080')  # Set window size

# Initialize WebDriver
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)  # Explicit wait

try:
    # Open a website
    driver.get('https://example.com')
    logger.info(f"Opened website: {driver.current_url}")

    # Basic Navigation
    driver.refresh()
    logger.info("Page refreshed")

    # Finding elements using different locators
    element_by_id = driver.find_element(By.ID, 'element-id')
    element_by_name = driver.find_element(By.NAME, 'element-name')
    element_by_xpath = driver.find_element(By.XPATH, '//tag[@attribute="value"]')
    element_by_css = driver.find_element(By.CSS_SELECTOR, 'tag.classname')

    # Interacting with elements
    element_by_id.click()
    element_by_name.send_keys('Test Input')
    element_by_name.clear()
    element_by_name.send_keys(Keys.RETURN)

    # Wait for an element to be present
    wait.until(EC.presence_of_element_located((By.ID, 'dynamic-element-id')))

    # Handling dropdowns
    dropdown = Select(driver.find_element(By.ID, 'dropdown-id'))
    dropdown.select_by_visible_text('Option 1')

    # Handling checkboxes and radio buttons
    checkbox = driver.find_element(By.ID, 'checkbox-id')
    if not checkbox.is_selected():
        checkbox.click()

    radio_button = driver.find_element(By.NAME, 'radio-group-name')
    radio_button.click()

    # Handling alerts
    driver.find_element(By.ID, 'alert-button-id').click()
    alert = Alert(driver)
    alert_text = alert.text
    alert.accept()
    logger.info(f"Alert accepted with message: {alert_text}")

    # Handling multiple windows
    original_window = driver.current_window_handle
    driver.find_element(By.ID, 'new-window-button-id').click()
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    logger.info("Switched to new window")
    driver.close()
    driver.switch_to.window(original_window)

    # Executing JavaScript
    driver.execute_script("console.log('Hello from JavaScript!');")

    # Taking a screenshot
    driver.save_screenshot('screenshot.png')
    logger.info("Screenshot taken")

    # Handling cookies
    driver.add_cookie({'name': 'test_cookie', 'value': 'test_value'})
    cookies = driver.get_cookies()
    logger.info(f"Cookies: {cookies}")
    driver.delete_cookie('test_cookie')

    # File upload
    file_input = driver.find_element(By.ID, 'file-upload-id')
    file_input.send_keys('/path/to/file.txt')

    # Drag and drop
    source = driver.find_element(By.ID, 'source-id')
    target = driver.find_element(By.ID, 'target-id')
    ActionChains(driver).drag_and_drop(source, target).perform()
    logger.info("Drag and drop performed")

    # Error handling example
    try:
        non_existent_element = driver.find_element(By.ID, 'non-existent-id')
    except Exception as e:
        logger.error(f"Element not found: {e}")

    # Closing the browser
    driver.quit()

except Exception as e:
    logger.error(f"An error occurred: {e}")
    driver.quit()

```
