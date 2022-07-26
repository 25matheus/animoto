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

class makeVideo:
    def __init__(self, url, email, password, MyTitle):
        self.url = url
        self.email = email
        self.password = password
        self.MyTitle = MyTitle

    def goToAnimoto(self):
        driver.get(self.url)

        time.sleep(3)
        window_before = driver.window_handles[0]
        window_before_title = driver.title
        print(window_before_title)

        facebook = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div/div[1]/button').click()
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
        #time.sleep(10)


        #driver.get('https://animoto.com/builder/9lASRquPQXWP2SMfvePWmw')

        #driver.find_element_by_xpath('//*[@id="js-react-storyboard-selector"]/div/div[2]/div/div[1]/div[2]/div/div/button[3]').click()



    def newBlock(self):
        addBlock = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[1]/div/div/button').click()

        time.sleep(2)

        addTextBlock = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div[2]/div[1]/div/a[1]').click()

        time.sleep(2)

        actionChains = ActionChains(driver)
        actionChains.send_keys(Keys.ENTER).perform()

    def getTemplate(self):
        driver.get('https://animoto.com/projects')
        time.sleep(5)

        edit = driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div[3]/a').click()
        #edit = driver.find_element_by_xpath(
         #       '//*[@id="project_c8"]/div/div[1]/div[1]/div/div[3]/a').click()
        time.sleep(5)
        try:
            confirmEdit =  edit = driver.find_element_by_xpath(
                    '//*[@id="continue-editing"]').click()
            time.sleep(5)
        except:
            pass


        try:
            continueEditing = driver.find_element_by_xpath(
                '//*[@id="js-continue-editing"]').click()
            time.sleep(5)
        except:
            pass

        try:
            reset = driver.find_element_by_xpath(
                '//*[@id="js-edit-in-place"]').click()
            time.sleep(5)
            yes = driver.find_element_by_xpath(
                '//*[@id="continue-editing"]').click()
        except:
            pass



        time.sleep(30)
        try:
            T = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/canvas').click()
        except:
            time.sleep(60)
            T = driver.find_elements_by_tag_name('canvas')[1].click()
        actionChains = ActionChains(driver)
        actionChains.double_click(T).perform()
        time.sleep(2)


    def changeColours(self):

        pictures = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[1]/div[4]').click()
        time.sleep(2)

        select = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]').click()
        time.sleep(3)
        selectColour = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/div[4]/span[4]/span').click()
        time.sleep(2)

    def setBackground(self):
        print('Setting background...')

        media = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[1]/div[4]/div').click()


        #Imagepath = os.path.abspath('C:\\Users\Matheus\Downloads\\pinestreet.jpg')
        #input = driver.find_elements_by_xpath('//input[@type="file"]')
        #for i in input:
            #i.send_keys(Imagepath)
        #time.sleep(3)
    def skip(self):
        buttonNext = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/button[2]').click()


    def canvas1(self):
        print('Writing on the 1st canvas')

        text = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div').click()
        time.sleep(2)

        titleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/textarea').clear()
        titleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/textarea')

        titleArea.send_keys(self.MyTitle)
        time.sleep(2)

        subtitleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/textarea').clear()

        subtitleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/textarea')

        #subtitleArea.send_keys(self.MyDesc)
        #time.sleep(2)

        c = 0
        while c < 1:
            subtitleArea = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/textarea').clear()
            subtitleArea = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/textarea')

            #subtitleArea.send_keys(self.MyDesc)
            #time.sleep(2)
            c = c + 1

        buttonNext = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/button[2]').click()

    def canvas2(self):
        print('Writing on the 2nd canvas')
        text = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div').click()
        time.sleep(2)

        titleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/textarea').clear()
        titleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/textarea')

        titleArea.send_keys("Complete Dental Care For The Residents of Niagara Region")
        time.sleep(2)

        subtitleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/textarea').clear()

        c = 0
        while c < 1:
            subtitleArea = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/textarea').clear()
            subtitleArea = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/textarea')

            subtitleArea.send_keys('Located in Niagara region Providing Dental Services')
            time.sleep(2)
            c = c + 1

        buttonNext = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/button[2]').click()

    def canvas3(self):
        print('Writing on the 3rd canvas')

        text = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div').click()
        time.sleep(2)

        titleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/textarea').clear()
        titleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/textarea')

        titleArea.send_keys('Financial options to our dental patients to help make your smile affordable.')
        time.sleep(2)
        subtitleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/textarea').clear()


        buttonNext = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/button[2]').click()

    def canvas4(self):
        print('Writing on the 4th canvas')

        text = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div').click()
        time.sleep(2)

        titleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/textarea').clear()
        titleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/textarea')

        titleArea.send_keys('Please Call (905)227-0303')
        time.sleep(2)

        buttonNext = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/button[2]').click()

    def canvas5(self):
        print('Writing on the 5th canvas')
        text = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div').click()
        time.sleep(2)

        titleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/textarea').clear()
        titleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/textarea')

        titleArea.send_keys('9 Pine St N #33, Thorold, ON L2V 3Z9')
        time.sleep(2)

        subtitleArea = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/textarea')

    def canvasClose(self):
        print('Closing the last canvas')
        close = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div[3]/div/div[1]/div/div[1]/button').click()

    def previwe(self):
        print('Preview button...')

        try:
            time.sleep(20)
            preview = driver.find_element_by_xpath(
                '//*[@id="js-user-nav"]/div/div[3]/button[2]').click()
        except:
            time.sleep(20)
            preview = driver.find_element_by_xpath(
                '//*[@id="js-user-nav"]/div/div[3]/button[2]').click()



    def produce(self):
        time.sleep(20)
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
        desc.send_keys(self.MyTitle + ' http://pinestreetdental.ca ')
        try:
            ProduceConfirm = driver.find_element_by_xpath(
                '//*[@id="js-ConfirmEdit"]').click()

            time.sleep(15)
        except:
            pass
        try:
            finish = driver.find_element_by_xpath(
                '//*[@id="js-Finish"]').click()
            time.sleep(2)

            confirm = driver.find_element_by_xpath(
                '//*[@id="js-ConfirmEdit"]').click()
        except:
            pass

        #driver.close()

    def PostOnYoutube(self):
        time.sleep(120)
        Youtube = driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[1]/div[4]/button').click()
        time.sleep(2)

        #screen = driver.switch_to.active_element

        Export = driver.execute_script("document.getElementsByClassName('s-begin-export CTAButton_button__2schg border-radius_all__1XrK4 CTAButton_small__15IVf')[0].click()")

        time.sleep(120)


    def modifyTemplate(self):
#     _______________________      IMAGE SCREEN    ________________________________    #
        #makeVideo.changeColours(self)

        try:
            media = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div/div[1]/div[4]/div').click()
        except:
            pass


        #Imagepath = os.path.abspath('C:\\Users\Matheus\Downloads\\pineLogo.jpg')
        #input = driver.find_elements_by_xpath('//input[@type="file"]')
        #for i in input:
            #i.send_keys(Imagepath)
        #time.sleep(3)
        #buttonNext = driver.find_element_by_xpath(
            #'/html/body/div[5]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/button[2]').click()


        #makeVideo.setBackground(self)
        #driver.get('https://animoto.com/builder/xFWrOoTFAISY4ugZ5WB3Mg')
        #time.sleep(80)
        makeVideo.getTemplate(self)
        makeVideo.canvas1(self)
        makeVideo.setBackground(self)
        makeVideo.canvas2(self)
        makeVideo.setBackground(self)
        makeVideo.canvas3(self)
        makeVideo.setBackground(self)
        makeVideo.canvas4(self)
        makeVideo.setBackground(self)
        makeVideo.canvas5(self)
        makeVideo.canvasClose(self)
        time.sleep(20)
        makeVideo.previwe(self)
        time.sleep(20)
        makeVideo.produce(self)
        time.sleep(45)
        makeVideo.PostOnYoutube(self)


        with open(r'C:\Users\Matheus\PycharmProjects\proj\venv\postedVideoPine.txt', 'a') as postedVideoPine:
            postedVideoPine.write(file)
            postedVideoPine.write('\n')
        with open(r'C:\Users\Matheus\PycharmProjects\proj\venv\postedVideoPineURL.txt', 'a') as postedVideoPineURL:
            postedVideoPineURL.write(driver.current_url)
            postedVideoPineURL.write('\n')




with open(r'C:\Users\Matheus\PycharmProjects\proj\venv\DescForVideo.json') as cust:
    customer = json.load(cust)

directory_in_str = r'C:\Users\Matheus\PycharmProjects\proj\venv\dataPineStreet'
directory = os.fsencode(directory_in_str)
os.chdir(directory_in_str)

for file in glob.glob("*.txt"):
    try:
        driver = webdriver.Chrome(r"C:\Users\Matheus\Downloads\chromedriver_win32\chromedriver.exe")
        print('Make video -', file)
        with open(file, 'r', encoding="utf-8") as f:
            line = f.readlines()
            title = line[0].split('.')
            MyTitle = title[0]
        animoto = makeVideo('https://animoto.com/builder/PnJroAq2FgKsR0kzcFB31A', 'jtgsystems@gmail.com', 'Computers1a1!',
                            MyTitle)
        animoto.goToAnimoto()
        time.sleep(10)
        #animoto.modifyTemplate()
        animoto.getTemplate()
        time.sleep(10)
        animoto.skip()
        time.sleep(2)
        animoto.canvas1()
        time.sleep(2)
        animoto.skip()
        time.sleep(2)
        animoto.canvas2()
        time.sleep(2)
        animoto.skip()
        time.sleep(2)
        animoto.canvas3()
        time.sleep(2)
        animoto.canvas4()
        time.sleep(2)
        animoto.canvas5()
        time.sleep(2)
        animoto.canvasClose()
        time.sleep(2)
        animoto.previwe()
        time.sleep(2)
        animoto.produce()
        time.sleep(2)
        animoto.PostOnYoutube()
        time.sleep(2)
        driver.close()
        time.sleep(2)
    except:
        driver.close()
        pass
