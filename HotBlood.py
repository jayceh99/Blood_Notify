import time
import datetime
import requests
from flask import Flask
from selenium import webdriver
from dateutil.relativedelta import relativedelta
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

class hot_blood ():
    def __init__(self) :
        self.headers = {
                "Authorization": "Bearer " + "ttttttoken",
                "Content-Type": "application/x-www-form-urlencoded"} 

    def line_notify(self,message): 
        
        params = {'message':message}

        r = requests.post("https://notify-api.line.me/api/notify",headers=self.headers, params=params)

        return r.status_code

    def get_blood(self):
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("headless")
        chrome = webdriver.Chrome(r'./chromedriver', chrome_options=options)
        chrome.get("https://www.tp.blood.org.tw/Internet/taipei/LocationWeek.aspx?site_id=2")
        time.sleep(2)
        x = chrome.find_element_by_id('CalendarContentWeek')
        #x = x.find_element_by_xpath('/table/tbody/tr[1]/td[2]')
        week = ['','星期日','星期一','星期二','星期三','星期四','星期五','星期六']
        tmp = '\n'
        x = str(x.text).split('星期')
        for i in range (0,len(x)):
            x[i] = x[i].split('\n')
        for j in range (1,8):
            #print (j)
            for i in range (0,len(x[j])):
                if '林口區' in x[j][int(i)]:
                    tmp = tmp+week[j]+':  '+x[j][int(i)]+'\n'
        if tmp == '\n':
            tmp = '這週沒有捐血車~'
        return tmp
def monitor ():
    ip = 'iiiip'
    seconds_since_epoch = time.time()
    seconds_since_epoch = seconds_since_epoch * 1000000000
    seconds_since_epoch  = format(seconds_since_epoch , '.0f')
    data =  "BloodNotify,host=180 Live=1  %s" % (seconds_since_epoch)
    url = 'http://'+ip+':8086/write?consistency=any&db=telegraf' 
    response = requests.post(url, data,headers={'Connection':'close'},timeout = 5)

def check_time():
    pass
def main ():
    f = open('time.txt','r')
    time_q = f.read()
    if float(time_q) < time.time():
        hot_blood_q =hot_blood()
        hot_blood_q.line_notify(hot_blood_q.get_blood())
        monitor()
    else:
        monitor()
#    test()
if __name__ == '__main__':
    main()