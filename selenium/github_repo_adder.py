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
    time.sleep(1)
    driver.sendKeys(Keys.RETURN)

#    action = action_chains.ActionChains(driver)
#    action.send_keys(Keys.COMMAND + Keys.ALT + 'i')
#    action.perform()
#    time.sleep(2)
#    action.send_keys(Keys.ENTER)
#    action.perform()


def add_repo(name, description, org=None):
    if org is None:
        driver.get("https://github.com/new")
    else:
        driver.get("https://github.com/organizations/{}/repositories/new".format(org))
    driver.find_element_by_id("repository_name").send_keys(name)
    driver.find_element_by_id("repository_description").send_keys(description)
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


def read_from_csv():
    form_csv = open(sys.argv[1], "r+")


def shokhmi_assign():
    teams = [{'team_name': 'هر چی می\u200cخوای', 'members': ['سپهر سماواتی', 'Saham Bahrami', 'alireza nadafian']}, {'team_name': 'UT Stat', 'members': ['مجید حاجی\u200cحیدری', 'آیسان بالود', 'علیرضا اسبریزی']}, {'team_name': 'espresso', 'members': ['امیرحسین ندیری', 'یاشار طالبی راد', 'علی ناصح']}, {'team_name': 'abracadata', 'members': ['نگار سخایی', 'فاطمه رحمانی', 'Zeinab Sadeghian']}, {'team_name': 'caracal', 'members': ['علی قندی', 'محمد بیات', 'amir hosseini']}, {'team_name': 'پنج به علاوه یک', 'members': ['آرش خوئینی', 'احسان حسین\u200cزاده', 'محمدحسین قنبری']}, {'team_name': 'Ostrichious', 'members': ['Ramin Akhtar', 'Arman Yanpi', 'Ali Barooni']}, {'team_name': 'همینو بذاریم؟', 'members': ['Sadegh Mahdavi', 'امیر مجتبی صبور', 'آرش محمودیان بیدگلی']}, {'team_name': 'Finding Neuron', 'members': ['علیرضا حیدری', 'alireza arvandi', 'امیررضا مزینی']}, {'team_name': 'Crystal', 'members': ['Vahid Masoumi', 'رخشان حریفی']}, {'team_name': 'اسیر شدیم به خدا تو شریف', 'members': ['محمدصادق آخوندزاده', 'محیا جمشیدیان', 'مریم مقدادی']}, {'team_name': 'deja vu', 'members': ['محسن یزدی نژاد', 'esmaeil zahedi', 'ساره هرمزان']}, {'team_name': 'KIVI', 'members': ['Ehsan Montahaei', 'Mohammad Taha Toghani']}, {'team_name': 'abracadabra', 'members': ['پیمان غلامی', 'رامین صفوی\u200cنژاد', 'ایمان غلامی']}, {'team_name': 'xyz', 'members': ['امیرحسین ستوده فر', 'علیرضا توفیقی محمدی', 'محمدکاظم فقیه خراسانی']}, {'team_name': 'Dataarchitect', 'members': ['فرید درویشی', 'Ali Farjad', 'زهرا اویسی']}, {'team_name': 'SholexNet', 'members': ['Mohammad Mahmoudi']}, {'team_name': 'موج', 'members': ['سعید ناصری', 'سارا عباس زاده', 'سهیلا سالاری']}, {'team_name': '123', 'members': ['مهدخت دارا', 'Mohammad Karrabi', 'هادی کلماتی']}, {'team_name': 'Diggers', 'members': ['احمد محمدزاده', 'محمد جعفری', 'محمد فهیمی نیا']}, {'team_name': 'Jafang', 'members': ['پارسا رازبان', 'عرفان قلی پور', 'سیاوش نجف زاده']}, {'team_name': 'CCL', 'members': ['زهرا غنائی', 'Ramin Zarei', 'ashkan sadeghi']}, {'team_name': 'dataAddict', 'members': ['ساتگین رستمی', 'yousef farhadi']}, {'team_name': 'Fartabi', 'members': ['Ozra Rasti', 'ابراهیم بادرستانی', 'مهتا شفیعی ثابت']}, {'team_name': 'sherlock_holmes', 'members': ['مرجان باغ گلشنی', 'ثمین حیدریان']}, {'team_name': 'HardCode', 'members': ['سینا تسلیمی', 'مهدی غزنوی', 'Soroush Taslimi']}, {'team_name': 'datadays_test', 'members': ['مینا قدیمی']}, {'team_name': 'd8a m8a', 'members': ['علیرضا موسوی حسینی', 'کیارش بنی هاشم', 'سروش وفایی\u200cتبار']}, {'team_name': 'Nodiolity', 'members': ['امین طالبی', 'حسین علی\u200cمدد', 'محمد صانعیان']}, {'team_name': 'LORENZ', 'members': ['پویا صفاریه', 'فرزاد فروغی', 'Ali Soleimani']}, {'team_name': 'OosGholam', 'members': ['mohammad dehghan', 'عادل مصطفوی', 'محمدامین صمدی']}, {'team_name': 'Deepmind', 'members': ['ali aghababaei', 'Mostafa Moradipour', 'امیراحسان خراشادی زاده']}, {'team_name': ';aslkfjsd;kfj;laskfj;dakf', 'members': ['سید نوید قاسمی', 'نیما وحیدی فردوسی', 'کیمیا همتی راد']}, {'team_name': 'SAP', 'members': ['سینا رسولی', 'Anahita Babaie', 'پویا رودکی']}, {'team_name': '8020', 'members': ['شهاب ابراهیمی', 'احمد رضایی']}, {'team_name': 'Humans of Late AI', 'members': ['محمدمهدی جهان\u200cآرا', 'محمدهادی سالاری', 'عرفان لقمانی']}, {'team_name': 'Just a lil bit', 'members': ['Arya Sadeghi', 'آشنا گرگان محمدی', 'امیر محمد اسعدی']}]

    for i, team in enumerate(teams, 1):
        team['team_rank'] = 'team-{:02d}'.format(i)
        team['desc'] = team['team_name']
        
    return teams
    

data = shokhmi_assign()


username = "mrtaalebi"
password = "asgharAsSareCarOmad"
sign_in(username, password)

for e in data:
#    try:
     add_repo(e['team_rank'], e['desc'], org='datadays2019')
#    except:
#        print("add_repo failed for {}".format(e['team_name']))
#    try:
#        add_collaborator(username=username, password=password, repo_name=e[4], collaborator=e[3])
#    except:
#        print("add_collaborator failed for {}".format(e[3]))

