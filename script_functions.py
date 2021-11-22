import GUI
import requests, bs4, webbrowser
from GUI import choice
from script_settings import telegram_bot_token, telegram_chat_id, telegram_alert_status
from script_settings import Chromedriver_path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, SoftwareEngine, HardwareType, SoftwareType
import random
import threading
import pickle
import time

#DO NOT TOUCH ANYTHING HERE !!!!!!!!!!!!!


software_names = [SoftwareName.CHROME.value, SoftwareName.EDGE.value, SoftwareName.FIREFOX.value, SoftwareName.ANDROID.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
software_engines = [SoftwareEngine.GECKO.value, SoftwareEngine.WEBKIT.value, SoftwareEngine.BLINK.value]
hardware_types = [HardwareType.MOBILE.value, HardwareType.COMPUTER.value, HardwareType.SERVER.value]
software_types = [SoftwareType.WEB_BROWSER.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, hardware_types=hardware_types, software_engines=software_engines, software_types=software_types, limit=100)

def telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text):
    requests.get("https://api.telegram.org/bot" + str(telegram_bot_token) + "/sendMessage?chat_id=" + str(telegram_chat_id) + "&text=" + str(telegram_text))

def automaticjointelegramgroup(telegram_bot_token, telegram_chat_id, telegram_alert_status):
    PATH = Service(Chromedriver_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    Chromedriver = webdriver.Chrome(service=PATH, options=chrome_options)
    link = "https://t.me/hwgrouptech"
    Chromedriver.get(link)
    if telegram_alert_status == True:
        telegram_text = "Join our hardware community on Telegram!\n\n🔗Link: " + str(link)
        telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)


def automaticaddtocartldlc(link):
    PATH = Service(Chromedriver_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    Chromedriver = webdriver.Chrome(service=PATH, options=chrome_options)
    Chromedriver.get(link)
    wait = WebDriverWait(Chromedriver, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='product-page-price']/div[2]/button"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[2]/a[2]"))).click()

def automaticaddtocartmediaworld(link):
    PATH = Service(Chromedriver_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    Chromedriver = webdriver.Chrome(service=PATH, options=chrome_options)
    Chromedriver.get(link)
    wait = WebDriverWait(Chromedriver, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='onetrust-accept-btn-handler']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='block-mw-theme-content']/div/div/div/div/div[4]/div/div[4]/div/div/div[4]/a/span"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[17]/div[2]/div/a")))
    Chromedriver.get("https://www.mediaworld.it/checkout")


def automaticaddtocartunieuro(link):
    PATH = Service(Chromedriver_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    Chromedriver = webdriver.Chrome(service=PATH, options=chrome_options)
    Chromedriver.get(link)
    wait = WebDriverWait(Chromedriver, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Aggiungi al carrello')]"))).click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='warranty-modal']/div/div[3]/a[2]"))).click()

def check_availability_ldlc(link, requests_delay, telegram_bot_token, telegram_chat_id, telegram_alert_status):
    while link == link:
        time.sleep(int(requests_delay))
        headers = {'User-Agent':user_agent_rotator.get_random_user_agent()}
        r = requests.get(link, headers)
        content = bs4.BeautifulSoup(r.text, "html.parser")
        title = content.find("title")
        obj_title = title.text
        check_div = content.find('div', {"class": "modal-stock-web pointer stock stock-1"}) or \
                    content.find('div', {"class": "modal-stock-web pointer stock stock-2"}) or \
                    content.find('div', {"class": "modal-stock-web pointer stock stock-3"}) or \
                    content.find('div', {"class": "modal-stock-web pointer stock stock-4"}) or \
                    content.find('div', {"class": "modal-stock-web pointer stock stock-5"}) or \
                    content.find('div', {"class": "modal-stock-web pointer stock stock-6"}) or \
                    content.find('div', {"class": "modal-stock-web pointer stock stock-7"}) or \
                    content.find('div', {"class": "modal-stock-web pointer stock stock-8"}) or \
                    content.find('div', {"class": "modal-stock-web pointer stock stock-9"}) or \
                    content.find('div', {"class": "modal-stock-web pointer stock stock-10"})
        if check_div == content.find('div', {"class": "modal-stock-web pointer stock stock-2"}):
            print(str([time.ctime()]) + obj_title + "  Status: Object Available, add to cart in pending...")
            try:
                automaticaddtocartldlc(link)
                if telegram_alert_status == True:
                    telegram_text = "✅ " + str(obj_title) + " \n\n🛒Successfully added to cart🛒\n\n🔗Link: " + str(link)
                    telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)
            except:
                if telegram_alert_status == True:
                    telegram_text = "❌ " + str(obj_title) + " \n\n🛒Unable to add to cart🛒\n\n🔗Link: " + str(link)
                    telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)
            break
        if check_div == content.find('div', {"class": "modal-stock-web pointer stock stock-9"}):
            print(str([time.ctime()]) + obj_title + "  Status: Object Out of stock")
        if check_div == content.find('div', {"class": "modal-stock-web pointer stock stock-5"}):
            print(str([time.ctime()]) + obj_title + "  Status: Object Available within 7/15 days, add to cart in pending...")
            try:
                automaticaddtocartldlc(link)
                if telegram_alert_status == True:
                    telegram_text = "✅ " + str(obj_title) + " \n\n🛒Successfully added to cart🛒\n\n🔗Link: " + str(link)
                    telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)
            except:
                if telegram_alert_status == True:
                    telegram_text = "❌ " + str(obj_title) + " \n\n🛒Unable to add to cart🛒\n\n🔗Link: " + str(link)
                    telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)
            break
        if check_div == content.find('div', {"class": "modal-stock-web pointer stock stock-4"}):
            print(str([time.ctime()]) + obj_title + "  Status: Object Available in less than 7 days, add to cart in pending...")
            try:
                automaticaddtocartldlc(link)
                if telegram_alert_status == True:
                    telegram_text = "✅ " + str(obj_title) + " \n\n🛒Successfully added to cart🛒\n\n🔗Link: " + str(link)
                    telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)
            except:
                if telegram_alert_status == True:
                    telegram_text = "❌ " + str(obj_title) + " \n\n🛒Unable to add to cart🛒\n\n🔗Link: " + str(link)
                    telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)
            break
        if check_div == content.find('div', {"class": "modal-stock-web pointer stock stock-6"}):
            print(str([time.ctime()]) + obj_title + "  Status: Object Available in more than 15 days, add to cart in pending...")
            try:
                automaticaddtocartldlc(link)
                if telegram_alert_status == True:
                    telegram_text = "✅ " + str(obj_title) + " \n\n🛒Successfully added to cart🛒\n\n🔗Link: " + str(
                        link)
                    telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)
            except:
                if telegram_alert_status == True:
                    telegram_text = "❌ " + str(obj_title) + " \n\n🛒Unable to add to cart🛒\n\n🔗Link: " + str(link)
                    telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)
            break

def check_availability_mediaworld(link, requests_delay, telegram_bot_token, telegram_chat_id, telegram_alert_status):
    while link == link:
        time.sleep(int(requests_delay))
        headers = {'User-Agent': user_agent_rotator.get_random_user_agent()}
        r = requests.get(link, headers)
        content = bs4.BeautifulSoup(r.text, "html.parser")
        title = content.find("title")
        obj_title = title.text
        check_div = content.find('a', {"class": "openPopupAvvisami product-add-to-cart white-button avvisami-btn"}) or\
                    content.find('a', {"class": "product-add-to-cart mw-yellow-btn btn-size-md js-add-to-cart"})
        if check_div == content.find('a', {"class": "openPopupAvvisami product-add-to-cart white-button avvisami-btn"}):
            print(str([time.ctime()]) + obj_title + "  Status: Object Out of stock")
        if check_div == content.find('a', {"class": "product-add-to-cart mw-yellow-btn btn-size-md js-add-to-cart"}):
            print(str([time.ctime()]) + obj_title + "  Status: Object Available, add to cart in pending...")
            try:
                automaticaddtocartmediaworld(link)
                if telegram_alert_status == True:
                    telegram_text = "✅ " + str(obj_title) + " \n\n🛒Successfully added to cart🛒\n\n🔗Link: " + str(
                        link)
                    telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)
            except:
                if telegram_alert_status == True:
                    telegram_text = "❌ " + str(obj_title) + " \n\n🛒Unable to add to cart🛒\n\n🔗Link: " + str(link)
                    telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)
            break

def check_availability_unieuro(link, requests_delay, telegram_bot_token, telegram_chat_id, telegram_alert_status):
    while link == link:
        time.sleep(int(requests_delay))
        headers = {'User-Agent':user_agent_rotator.get_random_user_agent()}
        r = requests.get(link, headers)
        content = bs4.BeautifulSoup(r.text, "html.parser")
        title = content.find("title")
        obj_title = title.text[0:21]
        check_div = content.find('a', {"class": "btn btn-orange-normal pdp-right__btn js--warranty-btn"})
        if check_div == None:
            print(str([time.ctime()]) + obj_title + "  Status: Object Out of stock")
        else:
            print(str([time.ctime()]) + obj_title + "  Status: Object Available, add to cart in pending...")
            try:
                automaticaddtocartunieuro(link)
                if telegram_alert_status == True:
                    telegram_text = "✅ " + str(obj_title) + " \n\n🛒Successfully added to cart🛒\n\n🔗Link: " + str(link)
                    telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)
            except:
                if telegram_alert_status == True:
                    telegram_text = "❌ " + str(obj_title) + " \n\n🛒Unable to add to cart🛒\n\n🔗Link: " + str(link)
                    telegram_alert(telegram_bot_token, telegram_chat_id, telegram_text)
            break

def load_cookies(driver, link):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
