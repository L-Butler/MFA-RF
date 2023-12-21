#   type these two lines into console to start the debugger session
#   cd C:\Program Files\Google\Chrome\Application
#   chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Users\lawrence.butler\OneDrive - mediaiqdigital.com\Documents\Chrome Data"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# import win32clipboard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import pandas as pd

s=Service("C:\\Users\\lawrence.butler\\Downloads/chromedriver_win32 (2)\\chromedriver.exe")
opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver=webdriver.Chrome(service=s,options=opt)
action=ActionChains(driver)
driver.implicitly_wait(5)

df=pd.DataFrame(columns=["URL" , "Document"])
#df=pd.read_csv(r"C:\Users\lawrence.butler\Documents\PycharmProjects\MFA\MFA_documents_1.csv")

def scrape(domain_name):
    #try:
    driver.get(domain_name)
    elements=driver.find_elements(By.XPATH ,'html/body')
    if len(elements)>0:
        for e in elements:
            #new_row=pd.DataFrame({"URL":[domain_name] , "Document" : [e.text]})
            new_row=[ domain_name , e.text]
            df.loc[len(df)] = new_row
            #pd.concat([df, new_row], ignore_index=True)
    # except:
    #     print("no dice")

MFA_sitelist=(pd.read_csv(r"C:\Users\lawrence.butler\Documents\PycharmProjects\MFA\uk_domains.csv")).iloc[669:]
MFA_sitelist["App/URL"]='https://'+MFA_sitelist["App/URL"]
#MFA_sitelist.drop(MFA_sitelist.loc[MFA_sitelist['App/URL']=='https://lowvolumeinventory/'].index, inplace=True)
URLs=(MFA_sitelist.iloc[:,2].values)#[175:]
#print(URLs)
n=1

for U in URLs:
    scrape(U)
    print(n)
    print(U)
    n+=1
    df.to_csv('MFA_documents_1.csv')
