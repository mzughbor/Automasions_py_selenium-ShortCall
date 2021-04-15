# this os not the last version || last one in PRIVATE 
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pyperclip
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TwitterSignup(object):
    def __init__(self):
        global driver
        driver  = webdriver.Chrome(executable_path='C:/WebDriver/chromedriver.exe') # for another OS CHANGE this Path
        self.driver = driver

    def Signup(self):
        self.driver.get("https://twitter.com/i/flow/signup")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[4]/span').click()
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/label/div/div[2]/div/input').send_keys('Nahnood')
        windows_before = driver.current_window_handle
        self.driver.execute_script("window.open('https://emailfake.com/')")
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        windows_after = self.driver.window_handles
        new_window = [x for x in windows_after if x != windows_before][0]
        self.driver.switch_to.window(new_window)
        self.driver.find_element_by_xpath('//*[@id="copbtn"]').click()
        email = pyperclip.paste()
        print(email)
        self.driver.switch_to.window(windows_before)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/label/div/div[2]/div/input').send_keys(email)
        element = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "Month")))
        Select(element).select_by_value("6")
        day = WebDriverWait(self.driver,6).until(EC.visibility_of_element_located((By.ID, "Day")))
        Select(day).select_by_value("14")
        year = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID, "Year")))
        Select(year).select_by_value("1999")
        time.sleep(1.5)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div').click()
        time.sleep(1.5)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/div').click()
        self.driver.switch_to.window(new_window)
        time.sleep(3)
        self.driver.refresh()
        verification = self.driver.find_element_by_xpath('//*[@id="email-table"]/div[1]/div[2]').text
        verification = verification.split()[0]
        driver.close()
        self.driver.switch_to.window(windows_before)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/label/div/div[2]/div/input').send_keys(verification)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div').click()
        time.sleep(2)

        global tester
        tester = 0
        elements = driver.find_elements_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[1]/span')
        if len(elements) > 0:
            tester = line
            driver.close()
        else:
            countryCode = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID, "Country code")))
            Select(countryCode).select_by_value("PS")
            self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/label/div/div[2]/div/input').send_keys(line)
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div').click()
            driver.close()

with open("D:\shortcall\\twitter_v3\\twitter_v3-01\\numbers.txt") as file_in:
    for line in file_in:
        print(line)
        try:
            test = TwitterSignup()
            test.Signup()
        except WebDriverException:
            print("page down")
        if tester == line:
            try:
                test = TwitterSignup()
                test.Signup()
            except WebDriverException:
                print("page down 2 ")
        else:
            continue
file_in.close()
