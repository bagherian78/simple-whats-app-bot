import os
from selenium import webdriver
chromedriver = "C:\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
snsure=input("are u sure to send request?[Y/n]")
if(snsure.lower()=="y"):
    driver =webdriver.Chrome(chromedriver)
    driver.get("https://web.whatsapp.com")
    name=input("maseage to who?\n")
    msg=input("what do u want to send?\n")
    count=int(input("how many?\n"))
    msg_acs=input("are u sure u want to send?[Y/n]")
    if(msg_acs.lower()=="y"):
        user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        user.click()
        msg_box=driver.find_elements_by_class_name('_2S1VP')[1]
        for i in range(count):
            msg_box.send_keys(msg)
            send_but=driver.find_elements_by_class_name('_35EW6')[y]
            send_but.click()
    else:
        pass
else:
    pass