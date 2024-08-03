import select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

Options = Options()
Options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=Options)
driver.maximize_window()
driver.get('https://www.fitpeo.com/')
time.sleep(2)
Revenue_Calculator = driver.find_element(By.LINK_TEXT,"Revenue Calculator").click()
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH,"//p[@class='MuiTypography-root MuiTypography-body1 inter css-k0m0w']"))
time.sleep(2)
textbox = driver.find_element(By.XPATH,"//input[@type='number']")
textbox.clear()
time.sleep(2)
# Taxbox is not taking the correct value as input and we have found it as a bug.
driver.find_element(By.XPATH,"//input[@type='number']").send_keys("-1")
time.sleep(2)

# checkboxes for CPT-99091
driver.find_element(By.XPATH,"//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd inter css-1ml0yeg']//input[@type='checkbox']/following::span[normalize-space() = '57']").click()

# checkboxes for CPT-99453
driver.find_element(By.XPATH,"//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd inter css-1ml0yeg']//input[@type='checkbox']/following::span[normalize-space() = '19.19']").click()

# checkboxes for CPT-99454
driver.find_element(By.XPATH,"//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd inter css-1ml0yeg']//input[@type='checkbox']/following::span[normalize-space() = '63']").click()

# checkboxes for CPT-99474
driver.find_element(By.XPATH,"//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd inter css-1ml0yeg']//input[@type='checkbox']/following::span[normalize-space() = '15']").click()

# Reimbursement for all Patients Per Month: shows the value $110700.
# As having issue with the textbox due to this, Reimbursement amount is not updated.