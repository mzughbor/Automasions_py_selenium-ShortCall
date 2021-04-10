
from selenium import webdriver

#from getpass import getpass

username = "mzug146@gmail.com"
password = '*.S9U/C&4mLeQzp'

driver = webdriver.Chrome("C:\\Users\\hp\\PycharmProjects\\WebDrivers\\chrome_driver.exe")
driver.get("https://www.facebook.com/")

username_textbox = driver.find_element_by_id("email")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("pass")
password_textbox.send_keys(password)

login_button = driver.find_element_by_name('login')
login_button.submit()








#  Method - cdr_full:group_get_list
#
response = requests.post(
    url=URL,
    json={
        'jsonrpc': '2.0',
        'method': 'cdr_full:group_get_list',
        'params': {
            'page': 1,
            'per_page': 10
        },
        'id': None #"mzughbor@gmail.com"
    })

print(json.dumps(response.json()))