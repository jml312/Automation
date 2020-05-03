from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ConfirmLogin
import pyautogui
import time

# gets login info
ConfirmLogin.confirmLogin("Instagram")

# gets account info
account_to_search = input("Enter the account that you would like to search: ")
correctly_entered = input("Was the account entered correctly (press 'no' if it was not or enter to continue)? ")
while correctly_entered == 'no':
    account_to_search = input("Enter the account that you would like to search: ")
    correctly_entered = input("Was the account entered correctly (press 'no' if it was not or enter to continue)? ")
    print("\n")

# opens chrome and instagram
browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')
browser.maximize_window()

time.sleep(1)

# logs into instagram
uName = ConfirmLogin.getUserName()
pWord = ConfirmLogin.getPassword()
login = browser.find_element_by_name("username")
login.send_keys(uName)
pw = browser.find_element_by_name('password')
pw.send_keys(pWord)
enter = browser.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
time.sleep(2)
time.sleep(2)

# enters the account to search
goto = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
goto.send_keys(account_to_search)
goto.send_keys(Keys.RETURN)
time.sleep(2)

# clicks on the first account
pyautogui.moveTo(795, 710)
pyautogui.click()

time.sleep(1)

# clicks on the not now option for the notification popup
pyautogui.moveTo(809, 227)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click()
time.sleep(1)

# gets the number of posts for th user
numberOfPosts = int(browser.find_element_by_class_name('g47SY ').text)

# keeps scrolling until the bottom of the page is reached
time.sleep(2)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
first_scroll_height = browser.execute_script('return document.body.scrollHeight;')
time.sleep(2)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
second_scroll_height = browser.execute_script('return document.body.scrollHeight;')
if first_scroll_height != second_scroll_height:
    while first_scroll_height != second_scroll_height:
        time.sleep(2.5)
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        first_scroll_height = browser.execute_script('return document.body.scrollHeight;')
        time.sleep(2.5)
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        second_scroll_height = browser.execute_script('return document.body.scrollHeight;')

# clicks on the picture on the left and clicks two photos to the right (if they exist)
pyautogui.moveTo(554, 760)
pyautogui.click()
time.sleep(2)
pyautogui.press(['right'])
time.sleep(0.4)
pyautogui.press(['right'])
time.sleep(1)

# moves through all posts and likes the picture
for i in range(numberOfPosts):
    time.sleep(1)
    like = browser.find_elements_by_class_name("wpO6b ")[1].click()
    time.sleep(2)
    pyautogui.press(['left'])
