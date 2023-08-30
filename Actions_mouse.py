from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("C:/Users/Vishwanwnloads/chromedriver-win64/chromedriver-win64/msedgedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(3)
print(driver.title)
driver.maximize_window()
print(driver.current_url)

actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()             #hover the mouse on that element
actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()               #right click on the element
actions.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()  #click on the element
actions.double_click(driver.find_element(By.NAME, "checkBoxOption1")).click().perform()
