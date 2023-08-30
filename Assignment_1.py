from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("C:/Users/Vishwanwnloads/chromedriver-win64/chromedriver-win64/msedgedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
print(driver.title)
driver.find_element(By.CLASS_NAME, "blinkingText").click()
driver.implicitly_wait(5)

openwindows = driver.window_handles
driver.switch_to.window(openwindows[1])
message = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
userid = message[19:48]

driver.switch_to.window(openwindows[0])
driver.find_element(By.XPATH, "//input[@id='username']").send_keys(userid)
driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Bharadwah@10")
driver.find_element(By.CSS_SELECTOR, "input[id='signInBtn']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
