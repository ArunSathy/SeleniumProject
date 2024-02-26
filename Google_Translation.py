import openpyxl
from openpyxl import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip
import pandas as pd
from tkinter import filedialog
from selenium.webdriver.common.keys import Keys

base_file=filedialog.askopenfilename(title='Select the Input file',filetypes=(("Excel Files","*.xlsx"),("CSV Files","*.csc"),("All Files","*.*")))
excel_data=pd.read_excel(base_file,sheet_name='Translate')

#---------------------------------
# for i in excel_data.index:
#     entry=excel_data.loc[i]
#     print(entry)
#---------------------------------

chromedriver=Service(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')

#Opening the Google chrome

browser=webdriver.Chrome(service=chromedriver)
browser.maximize_window()
browser.get('https://translate.google.co.in/')



#Tying the thing in the Translation Bar

for i in excel_data.index:
    trans_text=excel_data.loc[i]
    text_bar=browser.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
    text_bar.send_keys(trans_text['Language Copy'])

    time.sleep(2)

    copy_button_xpath='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div/div[6]/div/div[6]/div[2]/span[2]/button/div[3]'
    copy_button=WebDriverWait(browser,500).until(EC.presence_of_element_located((By.XPATH,copy_button_xpath)))
    copy_button.click()

    x=pyperclip.paste()
    print(x)

    text_bar.send_keys(Keys.CONTROL+'a')
    text_bar.send_keys(Keys.BACKSPACE)

    output_file=filedialog.askopenfilename(title='Select the Input file',filetypes=(("Excel Files","*.xlsx"),("CSV Files","*.csc"),("All Files","*.*")))
    wb=openpyxl.load_workbook(output_file)
    ws=wb['Translate']




time.sleep(20)

