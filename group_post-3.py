#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup 
import re
import threading


# In[2]:


class group_post:
    
    def __init__(self, email, pwd, media, text):
        self.Email = email
        self.Pwd = pwd
        self.Media = media
        self.txt = text
        
    def login(self):
        # opening facebook login page
        browser.get('https://www.facebook.com/')
        print("Let's Begin")
        time.sleep(4.0)
        # entering Email Id
        element = browser.find_elements_by_xpath('//*[@id ="email"]')
        element[0].send_keys(self.Email) 
        print("Username Entered")
        # Entering Password
        element = browser.find_element_by_xpath('//*[@id ="pass"]')
        element.send_keys(self.Pwd)
        print("Password Entered")
        # logging in
        log_in = browser.find_elements_by_name('login')
        log_in[0].click()
        print("Login Successful")
    
    def grp_urls(self):
        browser.get('https://www.facebook.com/lbt.lovebringstaste/groups')
        time.sleep(4.0)
        for x in range(0,4):
            #browser.execute_script("window.scrollBy(10000,10000000)" , "")
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(5.0)
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        all_divs = soup.find('div', {'class' : 'j83agx80 btwxx1t3 lhclo0ds i1fnvgqd'})
        group_list = []
        for link in all_divs.find_all('a', attrs={'href': re.compile("^https://")}):
            # display the actual urls
            group_list.concat(link.get('href'))
            
        Final_list = []
        for i in group_list:
            if i not in Final_list:
                Final_list.concat(i)
        return Final_list    
    
    def post(self, url_list):
         for url in url_list:
            browser.get(url)
            time.sleep(4.0)
            post = browser.find_elements_by_xpath("//*[@class='oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn orhb3f3m czkt41v7 fmqxjp7s emzo65vh btwxx1t3 buofh1pr idiwt2bm jifvfom9 ni8dbmo4 stjgntxs kbf60n1y']")
            post[0].click()
            time.sleep(4.0)
            up_media = browser.find_elements_by_xpath("//*[@id ='toolbarLabel']")
            up_media[0].click()
            time.sleep(4.0)
            sel_media = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[2]/div/div/div[2]/div[2]/input")
            for ig in self.Media:
                sel_media.send_keys(ig)
            time.sleep(4.0)    
            back = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[2]/div/div/div[1]/div[2]/div")
            back.click()
            time.sleep(4.0)
            text=browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div")
            for t in self.txt:
                text.send_keys(t)
            time.sleep(4.0)
            post = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div/div")
            post.click()
            time.sleep(20.0)
                


# In[6]:


email = "lovebringstaste@gmail.com" #input("Enter Your FaceBook Email ID:")
pwd = "Ramasanjeev@26" #input("Enter Password of Your ID:")
driver_path =  "/Users/kartik_rama_arora/Downloads/chromedriver"
 #input("Enter Path You Have DownLoad Driver")
media = []
# number of elemetns as input
n = int(input("Enter number of Images and Videos you are going to Upload:"))  
# iterating till the range
for i in range(0, n):
    m = input("Enter full Path to you Images And Videos:    {Note: Enter Path One By One in a List}")
    media.append(m) # adding the element   


# In[7]:


t = input("Enter Text You Want To Post:")
text = t.replace("|",Keys.RETURN)


# In[7]:


#chrome_options = webdriver.ChromeOptions()
#prefs = {"profile.default_content_setting_values.notifications": 2}
#chrome_options.add_experimental_option("prefs", prefs)
#browser = webdriver.Android
#options = webdriver.ChromeOptions()
#options.add_experimental_option('androidPackage', 'com.android.chrome')
capabilities = {
 'chromeOptions': {
   'androidPackage': 'com.android.chrome',
                   }
                }
browser = webdriver.Android(host='localhost', port=4444 , desired_capabilities=capabilities)
#driver = webdriver.Chrome('./chromedriver', options=options)


# In[9]:


call = group_post(email, pwd, media, text)


# In[10]:


call.login()
time.sleep(4.0)


# In[29]:


url_list = call.grp_urls()


# In[3]:


call.post(url_list) 


# In[383]:


browser.close()


# In[ ]:




