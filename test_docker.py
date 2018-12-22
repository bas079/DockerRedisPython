from selenium import webdriver
import time

CHROME_DRIVER = "C://Users//Anna//Downloads//chromedriver_win32//chromedriver.exe"
SITE_NAME = "http://192.168.99.100:5000/"

#Open chrome driver
driver = webdriver.Chrome(executable_path=CHROME_DRIVER)

# Opening chrome browser on a desired page
driver.get(SITE_NAME)
# Maximize window
driver.maximize_window()
# Waiting for 2 seconds
time.sleep(2)

# Find string
element = driver.find_element_by_css_selector("body")
# Print string
print("String is:", element.text)

# Closing current tab
driver.close()

# Closing driver session
driver.quit()

