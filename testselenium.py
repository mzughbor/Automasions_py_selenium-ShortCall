

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/WebDriver/chromedriver.exe')
driver.get("https://client.premiumy.net/login")
uuu= driver.find_elements_by_link_text("Forgot pasword?")
print(uuu)
if len(uuu) == 0:
    print('the list is empty')
else:
    print('لاقينا أمه')