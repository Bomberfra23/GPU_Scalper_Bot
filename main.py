import GUI
import script_functions
from GUI import choice
from script_functions import automaticaddtocartldlc, automaticaddtocartmediaworld, automaticaddtocartunieuro, check_availability_ldlc, check_availability_mediaworld, check_availability_unieuro, automaticjointelegramgroup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from script_settings import telegram_bot_token, telegram_chat_id, telegram_alert_status
import random
import threading
import pickle
import time
import sys

if choice == "1":
    while True:
        try:
            LDLCLink = str(input("Now, insert your LDLC link: "))
        except:
            print("Error invalid link, try again!")
            continue
        try:
            LDLC_requests_delay = int(input("Now, insert the amount of delay beetween requests: "))
        except:
            print("Error invalid value, try again!")
            continue
        try:
            LDLC_multithreaded_requests = int(input("Now, insert the number of thread to run: "))
            for t in range(int(LDLC_multithreaded_requests)):
                t = threading.Thread(target=check_availability_ldlc(LDLCLink, LDLC_requests_delay, telegram_bot_token, telegram_chat_id,telegram_alert_status))
                t.start()
                t.join()
            break
        except:
            print("Error invalid value, try again!")
            continue
if choice == "2":
    while True:
        try:
            MediaWorldLink = str(input("Now, insert your MediaWorld link: "))
        except:
            print("Error invalid link, try again!")
            continue
        try:
            MediaWorld_requests_delay = int(input("Now, insert the amount of delay beetween requests: "))
        except:
            print("Error invalid value, try again!")
            continue
        try:
            Mediaworld_multithreaded_requests = int(input("Now, insert the number of thread to run: "))
            for t in range(int(Mediaworld_multithreaded_requests)):
                t = threading.Thread(target=check_availability_mediaworld(MediaWorldLink, MediaWorld_requests_delay, telegram_bot_token,telegram_chat_id, telegram_alert_status))
                t.start()
                t.join()
            break
        except:
            print("Error invalid value, try again!")
            continue

if choice == "3":
    while True:
        try:
            UnieuroLink = str(input("Now, insert your Unieuro link: "))
        except:
            print("Error invalid link, try again!")
            continue
        try:
            Unieuro_requests_delay = str(input("Now, insert the amount of delay beetween requests: "))
        except:
            print("Error invalid value, try again!")
            continue
        try:
            Unieuro_multithreaded_requests = input("Now, insert the number of thread to run: ")
            for t in range(int(Unieuro_multithreaded_requests)):
                t = threading.Thread(target=check_availability_unieuro(UnieuroLink, Unieuro_requests_delay, telegram_bot_token,telegram_chat_id, telegram_alert_status))
                t.start()
                t.join()
            break
        except:
            print("Error invalid value, try again!")
            continue

if choice == "4":
    print("Join our hardware community on telegram!")
    automaticjointelegramgroup(telegram_bot_token, telegram_chat_id, telegram_alert_status)
if choice == "5":
    print("Good Bye!")
    sys.exit()
