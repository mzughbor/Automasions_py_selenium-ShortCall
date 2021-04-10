from selenium import webdriver

class MyTest(object):
    def __init__(self):
        global driver
        driver  = webdriver.Chrome(executable_path='C:/WebDriver/chromedriver.exe') # for another OS CHANGE this Path
        self.driver = driver

    def login_process(self):
        self.driver.get("https://client.premiumy.net/login")
        # self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/form/div[1]/div/input').send_keys('mzughbor@gmail.com')  # ('test')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/form/div[2]/div/input').send_keys('') # ('premiumy_test')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/form/div[4]/div[1]/button').click()

    def query(self):
        self.driver.get("https://client.premiumy.net/accesses")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[1]/form/div/div[2]/div/div/div/input').send_keys('twitter')

test = MyTest()
try:
    test.login_process()
    checkTF = driver.find_elements_by_link_text("Report") # check if logged in or not
    #print(checkTF)
    if len(checkTF) == 0:
        #print('the list is empty')
        test.login_process()
except Exception as e:
  print("An exception occurred:Not logged in", e)

try:
    test.query()
except Exception as e:
    print("An exception occurred:", e)



#self.driver.close()