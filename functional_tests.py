from selenium import webdriver
import os

chromedriver = "/usr/bin/chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
