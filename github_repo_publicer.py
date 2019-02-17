from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

driver = webdriver.Chrome()


def sign_in(username, password):
    driver.get("https://github.com/login")
    driver.find_element_by_id("login_field").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_css_selector("input[value='Sign in']").click()
    

def hit_enter():
    action = action_chains.ActionChains(driver)
    action.send_keys(Keys.COMMAND + Keys.ALT + 'i')
    action.perform()
    time.sleep(1)
    action.send_keys(Keys.ENTER)
    action.perform()


def add_repo(name):
    driver.get("https://github.com/new")
    driver.find_element_by_id("repository_name").send_keys(name)
    driver.find_element_by_id("repository_public_false").click()
    hit_enter()


def add_collaborator(username, password, repo_name, collaborator):
    driver.get("https://github.com/{}/{}/settings/collaboration/".format(username, repo_name))
    driver.find_element_by_id("search-member").send_keys(collaborator)
    time.sleep(3)
    li = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-autocomplete-value='{}']".format(collaborator))))
    if li is None:
        print("username {} not found".format(collaborator))
        return
    driver.execute_script("arguments[0].click();", li)
    add = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='btn js-add-new-collab js-auto-complete-button']")))
    driver.execute_script("arguments[0].click();", add)


data = []
form_csv = open(sys.argv[1], "r+")
for line in form_csv:
    l = []
    for word in line.split(","):
        l.append(word.strip().replace('"', '').replace(' ', ''))
    data.append(l)

username = "sut-ce-fop-97"
password = "eybabamabanitamominadare"
sign_in(username, password)

for e in data:
    try:
        add_repo(e[4])
    except:
        print("add_repo failed for {}".format(e[4]))
    try:
        add_collaborator(username=username, password=password, repo_name=e[4], collaborator=e[3])
    except:
        print("add_collaborator failed for {}".format(e[3]))

