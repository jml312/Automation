from selenium import webdriver

which_class = input("Enter the number corresponding to the grade you would like to see:\n 1. "
                    "Physics\n 2. Java\n 3. "
                    "Math\n 4. Data Science\n")
print("\n")
while not which_class == '1' and not which_class == '2' and not which_class == '3' and not which_class == '4':
    print("Invalid Input")
    which_class = input(
        "Enter the number corresponding to the grade you would like to see:\n 1. "
        "Physics\n 2. Java\n 3. "
        "Math\n 4. Data Science\n")
    print("\n")

# users info
username = input("Enter your Canvas Username: ")
password = input("Enter your Canvas Password: ")

entered_correctly = input("Was your information entered correctly (type 'no' if not or hit enter to continue)? ")
print("\n")
# if the info was incorrectly entered
while entered_correctly == 'no':
    username = input("Enter your Canvas Username: ")
    password = input("Enter your Canvas Password: ")
    entered_correctly = input("Was your information entered correctly (type 'no' if not or hit enter to continue)? ")
    print("\n")

# logs into canvas
browser = webdriver.Chrome()
browser.get("https://login.case.edu/cas/login?service=https%3A%2F%2Fcanvas.case.edu%2Flogin%2Fcas")
browser.maximize_window()
uName = browser.find_element_by_id("username")
uName.send_keys(username)
pWord = browser.find_element_by_id("password")
pWord.send_keys(password)
enter = browser.find_element_by_name("submit")
enter.click()

if which_class == '1':
    search = browser.find_element_by_xpath('//*[@id="DashboardCard_Container"]/div/div[1]/div/a')
if which_class == '2':
    search = browser.find_element_by_xpath('//*[@id="DashboardCard_Container"]/div/div[3]/div/a')
if which_class == '3':
    search = browser.find_element_by_xpath('//*[@id="DashboardCard_Container"]/div/div[5]/div/a')
if which_class == '4':
    search = browser.find_element_by_xpath('//*[@id="DashboardCard_Container"]/div/div[6]/div/a')

search.click()

if which_class == '1':
    grades = browser.find_element_by_xpath('//*[@id="section-tabs"]/li[7]/a')
if which_class == '2':
    grades = browser.find_element_by_xpath('//*[@id="section-tabs"]/li[7]/a')
if which_class == '3':
    grades = browser.find_element_by_xpath('//*[@id="section-tabs"]/li[6]/a')
if which_class == '4':
    grades = browser.find_element_by_xpath('//*[@id="section-tabs"]/li[7]/a')

grades.click()

browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
