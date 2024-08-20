from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains  

def launch_driver(url, browser="chrome"):
    """
    Launches a browser driver for the specified URL.

    Args:
        url (str): The URL to navigate to.
        browser (str, optional): The browser to use. Defaults to "chrome".

    Returns:
        webdriver: The created WebDriver instance.
    """
    if browser == "firefox":
      # Assuming you have GeckoDriver installed and in your PATH
        driver = webdriver.Firefox()
      elif browser == "chrome":
        # Assuming you have ChromeDriver installed and in your PATH
        driver = webdriver.Chrome()
      else:
        print(f"Unsupported browser: {browser}")
        return None

  driver.get(url)
  return driver

# Example usage
driver = launch_driver("https://www.google.com")

# Use the driver for your automation tasks
# ...

# Quit the driver when done
driver.quit()

def test_google_speed_test_explicitly(browser="chrome"):
    global driver
    driver = launch_driver("https://www.google.com", browser)

    if driver is None:
        return

    # Explicit Waits
    short_wait = WebDriverWait(driver, short_timeout)
    long_wait = WebDriverWait(driver, long_timeout)

    # #1: Ensure search bar is visible
    try:
        short_wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    except TimeoutException:
        print("Search bar not found.")
        return

    # #2: Enter search term and submit
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("internet speed test" + Keys.RETURN)

    # #3: Ensure RUN SPEED TEST button is clickable
    try:
        run_speed_test_button = short_wait.until(
            EC.element_to_be_clickable((By.ID, "knowledge-verticals-internetspeedtest__test_button"))
        )
    except TimeoutException:
        print("\"RUN SPEED TEST\" button not found.")
        return

    # #4: Click RUN SPEED TEST button
    run_speed_test_button.click()

    # #5: Ensure CANCEL button is displayed
    try:
        cancel_button = short_wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR("g-raised-button[jsaction='dArJMd']")))
        )
    except TimeoutException:
        print("\"CANCEL\" button not found.")
        return

    # #6: Wait for test to finish (check if CANCEL button disappears)
    try:
        long_wait.until_not(EC.element_to_be_clickable((By.CSS_SELECTOR("g-raised-button[jsaction='dArJMd']"))))
    except TimeoutException:
        print("Speed test did not finish.")
        return

    # #7: Check for success or failure (based on displayed buttons)
    try:
        driver.find_element(By.CSS_SELECTOR("g-raised-button[jsaction='i0JLwd']"))  # RETRY button (failure)
        print("Speed test failed to run.")
    except NoSuchElementException:
        pass

    # #8: Check for TEST AGAIN button (success)
    try:
        driver.find_element(By.CSS_SELECTOR("g-raised-button[jsaction='iyDKIb']"))  # TEST AGAIN button (success)
        print("Speed test successful!")
    except NoSuchElementException:
        print("Speed test failed to run.")


def test_google_speed_test_implicitly(browser="chrome"):
    global driver
    driver = launch_driver("https://www.google.com", browser)

    if driver is None:
        return

    # Implicit Wait (consider using explicit waits for better control)
    driver.implicitly_wait(10)

    short_sleep = 6  # seconds
    long_sleep = 60  # seconds

    # #9: Enter search term and submit
    try:
        search_box = driver.find_element(By.CSS_SELECTOR("input[name='q']"))  # Using CSS selector
        search_box.send_keys("internet speed test" + Keys.RETURN)
    except NoSuchElementException:
        print("Search bar not found.")
        return

    # #10: Click "RUN SPEED TEST" button
    try:
        run_speed_test_button = driver.find_element(
            By.CSS_SELECTOR("#knowledge-verticals-internetspeedtest__test_button")
        )
        run_speed_test_button.click()
    except NoSuchElementException:
        print("\"RUN SPEED TEST\" button not found.")
        return

    # #11: Ensure "CANCEL" button is displayed (implicit wait might be insufficient)
    try:
        # Consider using explicit waits with `WebDriverWait` for better control
        # ActionChains(driver).pause(short_sleep).perform()  # Optional for implicit wait handling

        cancel_button = driver.find_element(By.CSS_SELECTOR("g-raised-button[jsaction='dArJMd']"))
        if not cancel_button.is_displayed():
            raise NoSuchElementException("\"CANCEL\" button not found.")
    except NoSuchElementException:
        print("\"CANCEL\" button not found.")
        return

    # #12: Check for "RETRY" button (failure)
    time.sleep(long_sleep)  # Replace with explicit waits if possible

    try:
        retry_button = driver.find_element(By.CSS_SELECTOR("g-raised-button[jsaction='i0JLwd']"))
        if retry_button.is_displayed():
            print("Speed test did not finish successfully.")
    except NoSuchElementException:
        pass

    # #13: Check for "TEST AGAIN" button (success)
    try:
        test_again_button = driver.find_element(By.CSS_SELECTOR("g-raised-button[jsaction='iyDKIb']"))
        if not test_again_button.is_displayed():
            print("Speed test did not finish successfully.")
    except NoSuchElementException:
        print("Speed test did not finish successfully.")
 

def test_calculator_explicitly(browser="chrome"):
    global driver
    driver = launch_driver("https://www.google.com", browser)

    if driver is None:
        return

    # Explicit Waits
    short_wait = WebDriverWait(driver, short_timeout)
    long_wait = WebDriverWait(driver, long_timeout)

    # #14: Ensure search bar is visible
    try:
        short_wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    except TimeoutException:
        print("Search bar not found.")
        return

    # #15: Enter "calculator" and press Enter
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("calculator" + Keys.RETURN)

    # #16: Ensure calculator is visible
    try:
        short_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "tyYmIf")))
    except TimeoutException:
        print("Calculator not found.")
        return

    calculator_text = driver.find_element(By.ID, "cwos")

    # #17: Enter "1" and verify in text field
    driver.find_element(By.XPATH, "//div[@jsname='N10B9']").click()  # Button with jsname="N10B9"
    try:
        short_wait.until(EC.text_to_be_present_in_element(calculator_text, "1"))
    except TimeoutException:
        print("\"1\" was not input.")

    # #18: Enter "+" and verify in text field
    driver.find_element(By.XPATH, "//div[@jsname='XSr6wc']").click()  # Button with jsname="XSr6wc"
    try:
        short_wait.until(EC.text_to_be_present_in_element(calculator_text, "1 +"))
    except TimeoutException:
        print("\"+\" was not input.")

    # #19: Enter "-" and verify in text field
    driver.find_element(By.XPATH, "//div[@jsname='pPHzQc']").click()  # Button with jsname="pPHzQc"
    try:
        short_wait.until(EC.text_to_be_present_in_element(calculator_text, "1 -"))
    except TimeoutException:
        print("\"-\" was not input.")

    # #20: Enter "2" and verify in text field
    driver.find_element(By.XPATH, "//div[@jsname='lVjWed']").click()  # Button with jsname="lVjWed"
    try:
        short_wait.until(EC.text_to_be_present_in_element(calculator_text, "1 - 2"))
    except TimeoutException:
        print("\"2\" was not input.")

    # #21: Enter "=" and verify result
    driver.find_element(By.XPATH, "//div[@jsname='Pt8tGc']").click()  # Button with jsname="Pt8tGc"
    try:
        short_wait.until(EC.text_to_be_present_in_element(calculator_text, "-1"))
    except TimeoutException:
        print("\"-1\" was not the solution.")

    # #22: Enter "AC" and verify cleared
    driver.find_element(By.XPATH, "//div[@jsname='SLn8gc']").click()  # Button with jsname="SLn8gc"
    try:
        short_wait.until(EC.text_to_be_present_in_element(calculator_text, "0"))
    except TimeoutException:
        print("Output not cleared to \"0\".")

    # #23-27: Implement similar logic for additional calculations
    # (Replace comments with your solution using explicit waits for buttons and expected results)

    # #23: Solve "87 + 52"
    #

    # Continue solving in the same format as above while clearing after solution is
	#  found. It's suggested to copy-and-paste to ensure correct format.
	#		
	
    #23: TODO (Solve "87 + 52" with correct usage of WebDriverWait)
	# /*CODE*/
		
	#24: TODO (Solve "63 × 21" with correct usage of WebDriverWait)
	# /*CODE*/
		
	#25: TODO (Solve "45 ÷ 9" with correct usage of WebDriverWait)
	# /*CODE*/
		
	#26: TODO (Solve "72 ÷ 10" with correct usage of WebDriverWait)
	#	/*CODE*/
		
	#27: TODO (Solve "log(58 × 6 ÷ 2 - 74)" with correct usage of WebDriverWait)
	#	// HINT: you don't need the last parentheses
	#	/*CODE*/
        
    
def test_calculator_implicitly(browser="chrome"):
    global driver
    driver = launch_driver("https://www.google.com", browser)

    if driver is None:
        return

    # Implicit Wait (consider using explicit waits for better control)
    driver.implicitly_wait(10)

    # #28: Enter "calculator" and press Enter
    try:
        search_box = driver.find_element(By.CSS_SELECTOR("input[name='q']"))
        search_box.send_keys("calculator" + Keys.RETURN)
    except NoSuchElementException:
        print("Search bar not found.")
        return

    # #29: Ensure calculator is visible (implicit wait might be insufficient)
    try:
        # Consider using explicit waits for better control
        # ActionChains(driver).pause(2).perform()  # Optional for handling slow element loading

        driver.find_element(By.CSS_SELECTOR("div.tyYmIf"))
    except NoSuchElementException:
        print("Calculator not found.")
        return

    calculator_text = driver.find_element(By.ID, "cwos")

    # #30: Enter "1" and verify in text field
    driver.find_element(By.CSS_SELECTOR("div[jsname='N10B9']")).click()  # Button with jsname="N10B9"
    try:
        # Implicit wait might not be enough for dynamic elements, consider explicit waits
        element = driver.find_element(By.XPATH, "//span[@id='cwos' and text()='1']")
    except NoSuchElementException:
        print("\"1\" was not input.")

    # #31-35: Follow similar logic for remaining calculations
    # (Replace comments with implicit wait handling and element verification)

    # #31: Enter "+" and verify
    driver.find_element(By.CSS_SELECTOR("div[jsname='XSr6wc']")).click()  # Button with jsname="XSr6wc"
    try:
        element = driver.find_element(By.XPATH, "//span[@id='cwos' and text()='1 + ']")
    except NoSuchElementException:
        print("\"+\" was not input.")

    # #32: Enter "-" and verify
    driver.find_element(By.CSS_SELECTOR("div[jsname='pPHzQc']")).click()  # Button with jsname="pPHzQc"
    try:
        element = driver.find_element(By.XPATH, "//span[@id='cwos' and text()='1 - ']")
    except NoSuchElementException:
        print("\"-\" was not input.")

    # #33: Enter "2" and verify
    driver.find_element(By.CSS_SELECTOR("div[jsname='lVjWed']")).click()  # Button with jsname="lVjWed"
    try:
        element = driver.find_element(By.XPATH, "//span[@id='cwos' and text()='1 - 2']")
    except NoSuchElementException:
        print("\"2\" was not input.")

    # #34: Enter "=" and verify result
    driver.find_element(By.CSS_SELECTOR("div[jsname='Pt8tGc']")).click()  # Button with jsname="Pt8tGc"
    try:
        element = driver.find_element(By.XPATH, "//span[@id='cwos' and text()='-1']")
    except NoSuchElementException:
        print("\"-1\" was not the solution.")

    # #35: Enter "AC" and verify cleared
    driver.find_element(By.CSS_SELECTOR("div[jsname='SLn8gc']")).click()  # Button with jsname="SLn8gc"
    try:
        element = driver.find_element(By.XPATH, "//span[@id='cwos' and text()='0']")
    except NoSuchElementException:


	#
	#  Continue solving in the same format as above while clearing after solution is
	#  found. It's suggested to copy-and-paste to ensure correct format.
	#

	# #36: TODO (Solve "87 + 52" with correct usage of ImplicitlyWait)
	#	/*CODE*/
		
	# #37: TODO (Solve "63 × 21" with correct usage of ImplicitlyWait)
	#	/*CODE*/
		
	# #38: TODO (Solve "45 ÷ 9" with correct usage of ImplicitlyWait)
	#	/*CODE*/
	
	# #39: TODO (Solve "72 ÷ 10" with correct usage of ImplicitlyWait)
	#	/*CODE*/
	
	# #40: TODO (Solve "log(58 × 6 ÷ 2 - 74)" with correct usage of ImplicitlyWait)
	# HINT: you don't need the last parentheses
	# /*CODE*/