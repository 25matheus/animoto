import glob, os
import linecache
import os
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import datetime
import sys

class video:
    def __init__(self, url, email, password, MyTitle):
        self.url = url
        self.email = email
        self.password = password
        self.MyTitle = MyTitle

    def goToAnimoto(self):
        print('Go to animoto')
        driver.get(self.url)

        time.sleep(3)
        window_before = driver.window_handles[0]
        window_before_title = driver.title
        print(window_before_title)

        facebook = driver.find_element_by_xpath('//*[@id="js-react-login"]/div/div/div/div/div[1]/button[2]').click()
        window_after = driver.window_handles[1]
        face = driver.switch_to.window(window_after)

        time.sleep(5)

        face = driver.find_element_by_id('email')
        face.send_keys(self.email)

        face = driver.find_element_by_id('pass')
        face.send_keys(self.password)

        face.find_element_by_xpath('//*[@id="u_0_0"]').click()
        driver.switch_to.window(window_before)
        window_after_title = driver.title
        print(window_after_title)

        time.sleep(5)
        #driver.get('https://animoto.com/builder/templates')
        time.sleep(2)

        driver.get('https://animoto.com/builder/X7I4DqKAi5G38i8Otu6esg')
        print('logged')

    def preview(self):
        time.sleep(20)
        print('preview')
        try:
            editing = driver.find_element_by_xpath('//*[@id="project_c8"]/div/div[1]/div[1]/div/div[3]/a').click()
            time.sleep(2)
            edit = driver.find_element_by_xpath('//*[@id="continue-editing"]').click()
            time.sleep(10)
        except:
            pass
        try:
            preview = driver.find_element_by_xpath(
                '//*[@id="js-user-nav"]/div/div[3]/button[2]').click()
        except:
            time.sleep(10)
            continue_editing = driver.find_element_by_xpath('//*[@id="js-continue-editing"]').click()
            time.sleep(5)
            preview = driver.find_element_by_xpath(
                '//*[@id="js-user-nav"]/div/div[3]/button[2]').click()
            pass

    def produce(self):
        time.sleep(20)
        print('produce')
        produce = driver.find_element_by_xpath(
            '//*[@id="js-ProduceVideo"]').click()

        time.sleep(15)
        title_ = driver.find_element_by_xpath(
            '//*[@id="js-Title"]').clear()

        title_ = driver.find_element_by_xpath(
            '//*[@id="js-Title"]')

        title_.send_keys(self.MyTitle)

        #date = driver.find_element_by_xpath(
          #  '//*[@id="js-Date"]').click()

        #time.sleep(2)
        #date = driver.find_element_by_xpath(
         #   '//*[@id="js-Date"]')
        #today = datetime.datetime.today().strftime('%Y-%m-%d')
        #date.send_keys('12/15/2018')

        producedBy = driver.find_element_by_xpath(
            '//*[@id="js-ProducerName"]').clear()

        producedBy = driver.find_element_by_xpath(
            '//*[@id="js-ProducerName"]')
        producedBy.send_keys('Matheus')

        desc = driver.find_element_by_xpath(
            '//*[@id="js-Description"]').clear()

        desc = driver.find_element_by_xpath(
            '//*[@id="js-Description"]')
        desc.send_keys('http://www.jtgsystems.com/ at (905) 892-4555')
        try:
            ProduceConfirm = driver.find_element_by_xpath(
                '//*[@id="js-ConfirmEdit"]').click()
        except:
            pass

        time.sleep(15)
        try:
            finish = driver.find_element_by_xpath(
                '//*[@id="js-Finish"]').click()
            time.sleep(2)

            confirm = driver.find_element_by_xpath(
                '//*[@id="js-ConfirmEdit"]').click()
        except:
            pass

        # driver.close()

    def postOnYoutube(self):
        time.sleep(60)
        Youtube = driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[1]/div[4]/button').click()
        time.sleep(2)

        # screen = driver.switch_to.active_element

        Export = driver.execute_script(
            "document.getElementsByClassName('s-begin-export CTAButton_button__2schg border-radius_all__1XrK4 CTAButton_small__15IVf')[0].click()")

        print("POSTED ON YOUTUBE -----------------------------------------")


directory_in_str = r'C:\Users\Matheus\PycharmProjects\proj\venv\links - Copy - Copy'
directory = os.fsencode(directory_in_str)
os.chdir(directory_in_str)
c = 2
while c < 153:
    try:
        with open('data'+str(c)+'.txt', 'r', encoding="utf-8") as reader:
            #file = reader.readlines()
            driver = webdriver.Chrome(r"C:\Users\Matheus\Downloads\chromedriver_win32\chromedriver.exe")

            printed = False
            line = reader.readlines()
            title = line[0].split('.')
            MyTitle = title[0]
            desc = line[2].split('.')
            MyDesc = desc[0]
            MyDesc1 = desc[0]
            number = desc[0]
            jtg = desc[0]
            credits = desc[0]

            print('title: ', MyTitle)

            animoto = video('https://animoto.com/projects', 'jtgsystems@gmail.com', 'Computers1a1!', MyTitle)
            animoto.goToAnimoto()
            animoto.preview()
            animoto.produce()
            animoto.postOnYoutube()
            time.sleep(120)
            driver.close()
    except:
        pass
