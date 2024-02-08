from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
self_url = "https://mail.ru/"

driver.get(self_url)
wait = WebDriverWait(driver, 15)
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mailbox"]/div[1]/button')))
element.click()

driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'ag-popup__frame__layout__iframe'))

username_input = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
username_input.send_keys('orisio26101@xmail.ru')

element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/form/div[2]/div[2]/div[3]/div/div/div[1]/button/span')))
element.click()

username_input_password = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
username_input_password.send_keys('ZX26101990zx26101990')

element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/div[3]/div/div/div[1]/div/button/span')))
element.click()
driver.switch_to.default_content()
mail = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-canvas"]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]')))
mail.click()

mail_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.container--H9L5q')))
mail_input.send_keys('orisio26101@xmail.ru')

text_input = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[3]/div[4]/div/div/div[2]/div[1]')))
text_input.send_keys('hello world')

send_mail = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.vkuiButton__content')))
send_mail.click()

time.sleep(2)
driver.quit()