import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# users info
username = input("Enter your Amazon Username: ")
password = input("Enter your Amazon Password: ")

entered_correctly = input("Was your information entered correctly (type 'no' if not or hit enter to continue)? ")
print("\n")
# if the info was incorrectly entered
while entered_correctly == 'no':
    username = input("Enter your Amazon Username: ")
    password = input("Enter your Amazon Password: ")
    entered_correctly = input("Was your information entered correctly (type 'no' if not or hit enter to continue)? ")
    print("\n")

# opens google, types amazon into the search bar and presses enter
browser = webdriver.Chrome()
browser.get("https://www.google.com/")
browser.maximize_window()
search = browser.find_element_by_name("q")
search.send_keys("amazon")
time.sleep(1)
search.send_keys(Keys.RETURN)

# clicks on the amazon link
amazon = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a')
amazon.click()
time.sleep(1)

# clicks sign in on amazon
sign_in = browser.find_element_by_xpath('//*[@id="nav-link-accountList"]')
sign_in.click()
time.sleep(1)

# types the username and presses enter
uname = browser.find_element_by_xpath('//*[@id="ap_email"]')
uname.send_keys(username)
cont = browser.find_element_by_xpath('//*[@id="continue"]')
cont.click()
time.sleep(1)

# types the password and presses enter
# if the username was entered incorrectly, an error is thrown
try:
    pword = browser.find_element_by_css_selector("#ap_password")
    pword.send_keys(password)
except NoSuchElementException:
    raise NoSuchElementException("username entered incorrectly so the password page was not brought up")

finish = browser.find_element_by_xpath('//*[@id="signInSubmit"]')
finish.click()