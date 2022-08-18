# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:49:42 2022
https://www.youtube.com/watch?v=1orv8yMPUp4&ab_channel=Dhazam

@author: jose.aceves
"""
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import re
from tabulate import tabulate
import numpy as np

#"C:\Users\jose.aceves\OneDrive - GRUPO DMI\Escritorio\Pruebas_spambot.xlsx"
#3319179675

#%% Information
print('[.........................................................SMAPBOT.........................................................]')    
print('')
address = str(input('Contacts address: '))
address = re.sub(r"""[!?'"@%&*/[/]""", "", 
                 address)  
data = pd.read_excel(address,  
                     usecols = ['telefono', 'nombre', 'apellido', 'asignadoa'])
data = data.astype('str')

for i in range(len(data)):
    data['telefono'][i] = re.sub(r"\s+", "", data['telefono'][i])
    
time.sleep(2)
if len(data) <= 5:
    print(tabulate(data, headers = 'keys', 
                   tablefmt = 'psql', 
                   stralign='center'))
else:
    print(tabulate(data.sample(frac=0.05), 
                   headers = 'keys', 
                   tablefmt = 'psql', 
                   stralign='center'))

#%% Metrics of information quality
resume = data.describe()
resume = resume.T
resume['dtypes'] = data.dtypes
resume['nan'] = data.isna().sum()
resume['Digits!='] = [np.nan, np.nan, str(len(data[data['telefono'].str.len() != 10])), np.nan]
resume = resume.T
print('')
time.sleep(2)
print(tabulate(resume, headers = 'keys', 
               tablefmt = 'psql',  
               stralign='center'))

#%% Clear scratch
scratch = data[data['telefono'].str.len() != 10]
data = data[data['telefono'].str.len() == 10]
data = data.drop_duplicates(subset = 'telefono')
data = data.reset_index(drop = True)
time.sleep(2)
print('')
time.sleep(1)
if str(input('Scratch review? (y/n): ')) == 'y':
    time.sleep(2)
    print(tabulate(scratch, headers = 'keys', tablefmt = 'psql',  stralign='center'))
else:
    pass

#%% KEYUSER TEST
time.sleep(2)
print('')
message = str(input('Message: '))
print('')
snd = 0
time.sleep(5)
keyuser = '3319179675'

web.open('https://web.whatsapp.com/send?phone='+keyuser+'&text='+message)
time.sleep(10)
pg.click(620,727)
pg.hotkey('ctrl')
pg.press('enter')
time.sleep(1)
pg.hotkey('ctrl', 'w')

#%% BULKING
bulking = str(input('Message in bulk? (y/n): '))
if bulking == 'y':
    print('EXPECTED RUNNING TIME: ', 11*len(data), 's')
    time.sleep(5)
    print('')
    for i in range(len(data)):
        step = ((i/len(data))*90)
        bar = str("█"*int(step)+"░"*(90-int(step)))
        web.open('https://web.whatsapp.com/send?phone='+data['telefono'][i]+'&text='+message)
        time.sleep(10)
        pg.click(620,727)
        pg.hotkey('ctrl')
        pg.press('enter')
        time.sleep(1)
        pg.hotkey('ctrl', 'w')
        print('Messagin:', bar, round((i/len(data))*100,0),'%')


#%% KEYUSER CONFIRMATION

time.sleep(3)
web.open('https://web.whatsapp.com/send?phone='+keyuser+'&text='+'TASK COMPLETED SUCCESSFULLY')
time.sleep(10)
pg.click(620,727)
pg.hotkey('ctrl')
pg.press('enter')
time.sleep(1)
pg.hotkey('ctrl', 'w')
qnt = 0

    
    

































































