import asyncio
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys
import os
import shutil
import stat
import urllib
import threading
import requests
import json
import asyncio
import pickle
from pathlib import Path
import random
import string
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
from colorama import init
init()

#['Strict', 'Lax', 'None']

tv = 2
class mtab:
    def __init__(self):

        print("__init__===================================")
        #print ("===========================")
        self.id = sys.argv[3]
        self.mfile = ""
        self.options = Options()
        mpath = "F:\\envato\\"+sys.argv[2]
        self.rnd = ''.join(random.choice(string.ascii_lowercase)
                           for i in range(10))
        os.system(
            f'echo n | xcopy "C:\\Profile\Default\*.*" "C:\\temp\{self.rnd}\Default\\" /s/h/e/k/f/c > NUL')
        eks = f"C:\\temp\{self.rnd}"
        Path(mpath).mkdir(parents=True, exist_ok=True)
        self.options.add_argument("start-maximized")
        self.options.add_argument(f"user-data-dir={eks}")
        print("ext-start")
        print(f"user-data-dir={eks}")
        print("ext-end")
        self.downloadpath = mpath
        pref = {'download.default_directory': self.downloadpath}
        self.options.add_experimental_option('prefs', pref)
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        ser = Service("chromedriver.exe")
        self.driver = webdriver.Chrome(service=ser, options=self.options)

    def onerror(func, path, _):
    
        print("onerror===================================")
        os.chmod(path, stat.S_IWRITE)
        func(path)

    def wait_for_downloads(self):
        print("wait_for_downloads===================================")
        max_delay = 1500
        interval_delay = 0.5
        total_delay = 0
        file = ''
        done = False
        count = 0
        while not done and total_delay < max_delay:
            for dirpath, dirnames, files in os.walk(self.downloadpath):
                if files:
                    #print(files[0], 'has files')
                    if files[0].endswith('.crdownload'):
                        print(Fore.YELLOW + 'Download In Progress')
                        print(Style.RESET_ALL)
                    elif files[0].endswith('.tmp'):
                        print(Fore.YELLOW + 'Download In Progress')
                        print(Style.RESET_ALL)
                    else:
                        file = files[0]
                        self.mfile = file
                        done = True
                if not files:
                    print(dirpath, 'does not have files')
                    if count > 30:
                        self.setfailed()
                    count += 1

            time.sleep(interval_delay)
            total_delay += interval_delay
        if not done:
            print(Fore.RED + "File(s) couldn't be downloaded")
            print(Style.RESET_ALL)
            self.setfailed()

        if done:
            self.setDone()

    def setDone(self):
        print("setdone===================================")
        myobj = {'id': self.id, 'file': self.mfile}
        x = requests.post(
            'https://app.digitalpanel.id/inq/envato/update', data=myobj)
        # print(x.content)
        self.driver.quit()
        shutil.rmtree(f"C:\\temp\{self.rnd}",
                      ignore_errors=True, onerror=self.onerror)
        # os.system(f'del /f /s /q "C:\\temp\{self.rnd}"')
        print(Fore.GREEN + 'Download Finish')
        print(Fore.RED + 'System Exit')
        print(Style.RESET_ALL)

    def setfailed(self):
        print("setfailed===================================")
        myobj = {'id': self.id}
        x = requests.post(
            'https://app.digitalpanel.id/inq/envato/failed', data=myobj)
        # print(x.content)
        self.driver.quit()
        shutil.rmtree(f"C:\\temp\{self.rnd}",
                      ignore_errors=True, onerror=self.onerror)
        # os.system(f'del /f /s /q "C:\\temp\{self.rnd}"')
        sys.exit("exit app")

    async def opens(self):
        print("opens===================================")
        time.sleep(tv)
        test = os.listdir(self.downloadpath)
        for item in test:
            if item.endswith(".tmp"):
                os.remove(os.path.join(self.downloadpath, item))
            if item.endswith(".crdownload"):
                os.remove(os.path.join(self.downloadpath, item))

        if len(test) == 0:
            print("Directory is empty")
        else:
            print(test[0])
            self.mfile = test[0]
            self.setDone()

        idcoki = {'id': sys.argv[4]}
        coki = requests.post('https://app.digitalpanel.id/coki', data=idcoki)
        time.sleep(tv)
        self.driver.get("https://elements.envato.com/")
        time.sleep(tv)

        try:
            cookies = json.loads(coki.content)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            print("success login")
        except Exception as e:
            print("failed login")
            self.driver.quit()
            shutil.rmtree(f"C:\\temp\{self.rnd}",
                          ignore_errors=True, onerror=self.onerror)
        time.sleep(tv)

        self.driver.get(sys.argv[1])

        try:
            # time.sleep(5)
            self.driver.find_element(By.CSS_SELECTOR, ".mIe6goMR span").click()
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                (By.ID, 'findOrCreateField'))).send_keys("digitalpanel")
            self.driver.find_element(By.CSS_SELECTOR, ".W5gZzqV9").click()
            self.driver.find_element(By.CSS_SELECTOR, ".skmTuuLm").click()

            if (WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@title="reCAPTCHA"]')))):
                print("captcha detected")
                time.sleep(tv)
                wait = True
                while(wait==True):
                    page_source = self.driver.page_source
                    soup = BeautifulSoup(page_source, 'lxml')
                    cap_finish = soup.find_all('button', class_='QhDuzJVq')
                    time.sleep(tv)
                    if not cap_finish:
                        print("check done")
                        self.driver.find_element(By.CSS_SELECTOR, ".skmTuuLm").click()
                        wait = False
                        break

                    else:
                        print("check cap done")

                self.driver.find_element(By.CSS_SELECTOR, ".skmTuuLm").click()
                self.wait_for_downloads()
        except Exception as e:
            # self.driver.quit()
            #self.setfailed()
            self.wait_for_downloads()


if __name__ == '__main__':
    tmp = mtab()
    N = 10
    thread_list = list()

    for i in range(N):
        t = threading.Thread(name='ENVATO {}'.format(i), target=asyncio.run(tmp.opens()))
        t.start()
        time.sleep(5)
        thread_list.append(t)

    for thread in thread_list:
        thread.join()
