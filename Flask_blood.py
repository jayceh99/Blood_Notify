import requests
from flask import Flask
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


def get_blood():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("headless")
    chrome = webdriver.Chrome(r'./chromedriver', chrome_options=options)
    chrome.get("https://www.tp.blood.org.tw/Internet/taipei/LocationWeek.aspx?site_id=2")
    time.sleep(2)
    x = chrome.find_element_by_id('CalendarContentWeek')
    week = ['','星期日','星期一','星期二','星期三','星期四','星期五','星期六']
    tmp = '\n'
    x = str(x.text).split('星期')
    for i in range (0,len(x)):
        x[i] = x[i].split('\n')
    for j in range (1,8):
        for i in range (0,len(x[j])):
            if '新莊區' in x[j][int(i)]:
                tmp = tmp+week[j]+':  '+x[j][int(i)]+'\n'
    return tmp
    
app = Flask(__name__)
@app.route("/m3",methods=['GET'])
def m3():
    #hot_blood_q = get_blood()
    m3_r = get_blood()
    #hot_blood_q.line_notify(m3_r)
    return m3_r

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True,threaded=True)
