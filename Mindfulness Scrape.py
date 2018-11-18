#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:40:50 2018

@author: Karan Mehta
"""

# Import Libraries 
import pandas as pd
import urllib
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen, Request

# Request access to the page
page_url = "https://www.mindfulnessstudies.com/community/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
req = Request(url=page_url, headers=headers) 
comm_page = urlopen(req)

# Parse the About us Page
soup = BeautifulSoup(comm_page, 'html.parser')

name_box = soup.find('h1', attrs={'class': 'entry-title'})
name = name_box.text.strip()
# Gather all the paragraphs in the page
paragraphs = soup.find_all("p")

# Repeat for other pages in the website

# MBSR Page
page_url_2 = "https://www.mindfulnessstudies.com/personal/stress/mbsr/"
req_2 = Request(url = page_url_2, headers = headers)
comm_page_2 = urlopen(req_2)
MBSR = BeautifulSoup(comm_page_2, "html.parser")
MB = MBSR.find_all("p")

# Free info session page
page_url_3 = "https://www.mindfulnessstudies.com/personal/mindfulness-info-session/"
req_2 = Request(url = page_url_3, headers = headers)
comm_page_3 = urlopen(req_2)
page_txt = BeautifulSoup(comm_page_3, "html.parser")
sesh = page_txt.find_all('p')

# Beginner session
page_url_4 = "https://www.mindfulnessstudies.com/personal/intro/beginners/" 
req_3 = Request(url = page_url_4, headers = headers)
comm_page_4 = urlopen(req_3)
page_txt_2 = BeautifulSoup(comm_page_4, "html.parser")
sesh_1 = page_txt_2.find_all('p')





