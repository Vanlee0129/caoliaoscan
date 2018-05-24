#!/usr/bin/python  
# -*- coding: UTF-8 -*-  

import urllib.parse  
import urllib.request  
import time  
from lxml import etree
import requests
from selenium import webdriver
import random

# 短网址还原 

def revertShortLink(url):
	re = requests.head(url)
	return re.headers.get('location')

URL_1 = revertShortLink("http://qr02.cn/CbcUWe")


global url_path  
url_path = [3]  
  
def verif_ip(ip,port):    # 验证ip有效性  
	
	test_url = URL_1
	
	browser = webdriver.Chrome()

	browser.get(URL_1)
	browser.quit()
	time.sleep(random.randint(1,20))  

file = open("temp.txt")

counter = 0 




while 1:  
	lines = file.readlines(100000)  
	if not lines:  
		break  
	for data in lines:
		counter += 1  
		print((data.split(":")[0]))
		print("cishu:",counter)  
	
	   

	 
		verif_ip(data.split(":")[0],data.split(":")[1])