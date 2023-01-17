from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

load_dotenv("C:/Users/krazy/Desktop/Code/.env.txt")
MY_GMAIL = os.getenv("linkedin_mail")
PASSWORD = os.getenv("linkedin_pass")

################### Adding options once browser opens #######################
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")

chrome_driver_path = Service(r"C:\Users\krazy\Desktop\Code\Development\chromedriver.exe")
# driver = webdriver.Chrome(options=options,service=chrome_driver_path)
driver = webdriver.Chrome(options=options)

driver.get("https://www.linkedin.com/home")

################### Login in to linkedin home page #######################

sign_in_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in_button.click()
time.sleep(2)

login_email = driver.find_element(By.NAME, "session_key")
login_email.send_keys(MY_GMAIL)
login_pass = driver.find_element(By.NAME, "session_password")
login_pass.send_keys(PASSWORD)

login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
login_button.click()
time.sleep(4)

################### At home page using search bar #######################

msg_minimize_list = driver.find_elements(By.CLASS_NAME, "msg-overlay-bubble-header__control")
msg_minimize_list[1].click()

search_job_title = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
search_job_title.send_keys("Python Developer")
time.sleep(1)
search_job_title.send_keys(Keys.ENTER)

time.sleep(4)
job_tab = driver.find_element(By.LINK_TEXT, "See all job results in United States")
job_tab.click()
time.sleep(3)

search_job_location = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__input--location "
                                                           ".jobs-search-box__text-input")
search_job_location.clear()
search_job_location.send_keys("Aurora, Colorado, United States")
search_button = driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/div[2]/button[1]')
search_button.click()
time.sleep(3)

################### Using filter to get entry level jobs #######################

drop_down_menus = driver.find_elements(By.CSS_SELECTOR, ".artdeco-hoverable-trigger--content-placed-bottom "
                                                        ".search-reusables__filter-pill-button")
experience_level_tab = drop_down_menus[2]
experience_level_tab.click()
entry_level_box = driver.find_element(By.ID, "experience-2")

# "driver.execute_script("arguments[0].click();", INSERT_VARIABLE)" works by bypassing validation check
# that may OBSTRUCT element, this code is talking with javascript that doesn't care and just clicks
# on the checkbox
driver.execute_script("arguments[0].click();", entry_level_box)
time.sleep(1)
# if button is not 'interactable' than must use WebDriverWait and expected_conditions from .support in webdriver. Than
# use the FULL XPath to use click method on the search results button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div[3]/section/div/div/'
                                                                      'div/ul/li[5]/div/div/div/div[1]/div/form/'
                                                                      'fieldset/div[2]/button[2]'))).click()
time.sleep(2)

################### Getting ALL job listings and saving them #######################

all_job_listings = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

for listing in all_job_listings:
    listing.click()
    time.sleep(1)
    save_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/'
                                                'section[2]/div/div/div[1]/div/div[1]/div/'
                                                'div[2]/div[3]/div/button')
    save_button.click()
    time.sleep(1)
