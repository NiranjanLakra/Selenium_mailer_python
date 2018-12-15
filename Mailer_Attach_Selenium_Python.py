'''
This program is tested on :
platform    : windows 10
Arch        : X64
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard     # Used for injecting keystrokes on the windows Dialog Box

driver=webdriver.Chrome("C:\\Users\\win10\\Downloads\\ChromeDriver")    # path to the downloaded driver
driver.get("https://mail.protonmail.com/login")                         # email service you want to use

assert "ProtonMail" in driver.title                                     # checking that the title at the top contains "ProtonMail" or not
driver.find_element_by_name("username").send_keys("your_username")
driver.find_element_by_name("password").send_keys("your_password")
driver.find_element_by_id("login_btn").click()
assert "No results found." not in driver.page_source
for i in range(60):     # for loop to wait until the mail Dashboard loads, and clicks Compose button
    try:
        driver.find_element_by_xpath('//*[@id="pm_sidebar"]/button').click()
        break
    except:
        pass
    time.sleep(1)
time.sleep(5)
driver.switch_to_active_element().send_keys("reciever@gmail.com"+ Keys.RETURN + '\t' +"test" + '\t')    # Wrting "To" and "subject" section
time.sleep(0.5)
driver.switch_to_active_element().send_keys("test_message" + '\t' + Keys.RETURN)   # message as "bhabhi" and pressing Tab (\t) to reach SEND button
time.sleep(3)
keyboard.press_and_release('s')
keyboard.press_and_release('c') # File Name scp  NOTE : THE ATTACHMENT FILE MUST BE  IN C:\Users\tom\scp
keyboard.press_and_release('p')
keyboard.press_and_release('return') # click on open the attachment
time.sleep(2)
driver.switch_to_active_element().send_keys('\t'*5) # press tab 5 times to reach send button
time.sleep(0.5)
driver.switch_to_active_element().click() # click send button
time.sleep(5)
driver.quit()   #Closing the program
