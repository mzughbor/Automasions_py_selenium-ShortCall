from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


def check_exists_by_xpath(xpath):
    try:
        element = driver.find_element_by_css_selector('div[style="min-height: 14px; height: 15%; transform: translate3d(0px, 446.25px, 0px); backface-visibility: hidden;"]')
        attributeValue = element.get_attribute("transform: translate3d(0px, 446.25px, 0px);")
        #print(attributeValue)
    except NoSuchElementException:
        return False
    return True


class NumbersForTest(object):
    def __init__(self):
        global driver
        driver  = webdriver.Chrome(executable_path='C:/WebDriver/chromedriver.exe') # for another OS CHANGE this Path
        self.driver = driver

    def login_process(self):
        self.driver.get("https://client.premiumy.net/login")
        # self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/form/div[1]/div/input').send_keys('mszughbor@gmail.com')  # ('test')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/form/div[2]/div/input').send_keys('N@*T&') # ('premiumy_test')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/form/div[4]/div[1]/button').click()

    def get_testNumbers(self):
        self.driver.get("https://client.premiumy.net/accesses")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/form/div/div[1]/div/div/div/div/a/span[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[6]/form/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[6]/form/div/div/input').send_keys('100')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[1]/form/div/div[2]/div/div/div/input').send_keys('Dominican Republic - Mobile - Claro')

        #x = 1
        #while x > 0:
            #self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[6]/ul/li[9]/a/span[1]/i').click()
            #هونا االفكره نه بيظهر شغلات بين الارقام فبتغير الاكس  باث رقم ل7 وهكزا... بيصير تسعه بعد تانيه ضغطه
            #self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[6]/ul/li[7]/a/span[1]/i').click()
            #time.sleep(2)
         #   x -= 1
          #  print(x)
           # if x == 0:
            #    print('finalX',x)
             #   break

    def scrape(self):
        scrollbar = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[2]/div[2]/div[2]/div")
        ActionChains(driver).move_to_element(scrollbar).perform()
        time.sleep(2)
        TestNumbers = self.driver.find_elements_by_class_name('rs-table-row')
        index = 0
        indecator = 0
        for TestNumber in TestNumbers:
            break
        while index < len(TestNumbers):
            index += 1
            if index == 16 :
                index = 3
                driver.find_element_by_class_name("rs-table-scrollbar-handle").location_once_scrolled_into_view
                TestNumbers = self.driver.find_elements_by_class_name('rs-table-row')
            else:
                number = TestNumber.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[5]/div[2]/div[1]/div['+ str(index) +']/div/div[4]').text
                print(number)
                continue

test = NumbersForTest()
test.login_process()
checkTF = driver.find_elements_by_link_text("Report") # check if logged in or not
while len(checkTF) == 0 :
    test.login_process()
    time.sleep(2)
    if len(checkTF) != 0:
        continue
    break

test.get_testNumbers()
test.scrape()

