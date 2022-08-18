# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:30:55 2022

@author: jose.aceves
https://dev.to/visheshdvivedi/send-bulk-whatsapp-messages-in-python-automate-whatsapp-using-python-ipo
https://medium.com/@jihargifari/how-to-send-multiple-whatsapp-message-using-python-3f1f19c5976b
https://www.studytonight.com/post/whatsapp-automation-to-send-message-using-python
https://www.macheronte.com/en/python-send-sms-on-whatsapp-to-unsaved-numbers/


"""
#%% Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import webbrowser
from selenium import webdriver
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from tqdm import notebook
import time

'''You don’t have to save the contact numbers to your device to run this code. You’ll also be 
able to loop the code to a contacts list so that you can send the message to multiple people, with 
customizable messages for each person.
Unstable connections can lead to an error while executing the code.'''

#%% “Element Presence” Function
'''Create a particular “element” as a requirement for the web-driver to decide 
whether to continue the automation process or not. In this case we are going to 
open the WhatsApp web'''

def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)



def send_message(url):
    driver.get(url)
    time.sleep(2)
    element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]', 40)
    msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    msg_box.send_keys('\n')
    time.sleep(1)
    
    
def prepare_msg(dataframe, name_col, phone_col):
    file = dataframe[[name_col, phone_col]]
    base_msg = """
*Hi {}*!
How are you? I hope you're doing well.

put your message here.

Thanks!
"""
    base_url = 'https://web.whatsapp.com/send?phone={}&text={}'
    for i,j in notebook.tqdm(file.iterrows()):
        phone_no = j[phone_col]
        Name = j[name_col].title()
        msg = urllib.parse.quote(base_msg.format(Name))
        url_msg = base_url.format(phone_no, msg)
        send_message(url_msg)

#%% Execute 









