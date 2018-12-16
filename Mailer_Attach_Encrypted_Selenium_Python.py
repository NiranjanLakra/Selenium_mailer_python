from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import subprocess

cmd1="C:\\Users\\win10\\Documents\\SystemFile.xml"  # prerequisite is to create an encrypted xml file.
cmd2="$pass=Import-Clixml -Path "+cmd1+" ; $pass.GetNetworkCredential().password"
data=subprocess.Popen(["powershell", cmd2],stdout=subprocess.PIPE)
result=data.communicate()[0]

def inverter(result):
    list_1=list(result)
    list_2=[]
    list_3=[]
    for i in range(len(list_1)):
        list_2.insert(i, list_1[12-i])
    print list_2
    for j in range(len(list_1)):
        tmp=ord(list_2[j])+4
        list_3.insert(i,chr(tmp))
    data2=''.join(list_3)
    return data2
driver=webdriver.Chrome("C:\\Users\\win10\\Downloads\\ChromeDriver")    # path to the downloaded driver
driver.get("https://mail.protonmail.com/login")                         # email service you want to use

assert "ProtonMail" in driver.title                                     # checking that the title at the top contains "ProtonMail" or not
time.sleep(5)
driver.find_element_by_name("username").send_keys("kuchbhikuch")
driver.find_element_by_name("password").send_keys(result)
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
driver.switch_to_active_element().send_keys("niranjan.lakra19@gmail.com"+ Keys.RETURN + '\t' +"test" + '\t')    # Wrting "To" and "subject" section
time.sleep(2)
driver.switch_to_active_element().send_keys("test_message" + '\t' + Keys.RETURN)   # message as "bhabhi" and pressing Tab (\t) to reach SEND button
time.sleep(3)
keyboard.press_and_release('shift+s')
keyboard.press_and_release('y') # File Name scp  NOTE : THE ATTACHMENT FILE MUST BE  IN C:\Users\tom\scp
keyboard.press_and_release('s')
keyboard.press_and_release('t')
keyboard.press_and_release('e') # File Name scp  NOTE : THE ATTACHMENT FILE MUST BE  IN C:\Users\tom\scp
keyboard.press_and_release('m')
keyboard.press_and_release('shift+f')
keyboard.press_and_release('i') # File Name scp  NOTE : THE ATTACHMENT FILE MUST BE  IN C:\Users\tom\scp
keyboard.press_and_release('l')
keyboard.press_and_release('e')
time.sleep(2)
keyboard.press_and_release('return') # click on open the attachment
time.sleep(4)
driver.switch_to_active_element().send_keys('\t'*2) # press tab 5 times to reach send button
data3=inverter(result)
time.sleep(2)
driver.switch_to_active_element().click() # click send button
time.sleep(2)
driver.find_element_by_id("outsidePw").send_keys(data3+'\t')
time.sleep(0.5)
driver.find_element_by_id("outsidePwConfirm").send_keys(data3+'\t')
time.sleep(0.5)
driver.find_element_by_id("outsidePwHint").send_keys("i"+'\t'*2)
time.sleep(0.5)
driver.switch_to_active_element().click()
time.sleep(0.5)
driver.switch_to_active_element().send_keys('\t'*13)
time.sleep(0.5)
driver.switch_to_active_element().click() # click send button
time.sleep(5)
driver.quit()   #Closing the program