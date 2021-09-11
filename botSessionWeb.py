import json
from requests import Session
from botTools import query_token
from selenium import webdriver as wd


nga = Session()
nga_token = json.loads(query_token('nga'))
headers = nga_token['headers']
cookies = nga_token['cookies']
nga.headers.update(headers)
nga.cookies.update(cookies)


options = wd.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--user-data-dir=/home/kuma/data/chrome')

mobile_emulation = {'deviceName': 'iPhone 6/7/8 Plus'}
options.add_experimental_option('mobileEmulation', mobile_emulation)

preferences = {'download_restrictions': 3}
# disable all downloads: https://chromeenterprise.google/policies/?policy=DownloadRestrictions
options.add_experimental_option('prefs', preferences)

driver = wd.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)
