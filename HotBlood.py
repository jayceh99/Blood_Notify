import requests
from flask import Flask
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
class hot_blood ():
    def __init__(self) :
        self.headers = {
                "Authorization": "Bearer " + "YDvHAZh3EACktDHWAoMuUyWiIDBOYqbJnllwYr01DjS",
                "Content-Type": "application/x-www-form-urlencoded"} 

    def line_notify(self): 

        params = {'message':'test'}

        r = requests.post("https://notify-api.line.me/api/notify",headers=self.headers, params=params)

        return r.status_code



#app = Flask(__name__)
#@app.route("/m3",methods=['GET'])
#def m3():
#    hot_blood_q = hot_blood()
#    m3_r = str(hot_blood_q.line_notify())
#    return m3_r

#if __name__ == '__main__':
#    app.run(host='0.0.0.0',port=8080,debug=True,threaded=True)

def test():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("headless")
    chrome = webdriver.Chrome(r'C:\Users\alok\Desktop\test/chromedriver', chrome_options=options)
    chrome.get("https://www.tp.blood.org.tw/Internet/taipei/LocationWeek.aspx?site_id=2")
    time.sleep(2)
    x = chrome.find_element_by_id('CalendarContentWeek')
    #x = x.find_element_by_xpath('/table/tbody/tr[1]/td[2]')
    week = ['','星期日','星期一','星期二','星期三','星期四','星期五','星期六']
    x = str(x.text).split('星期')
    for i in range (0,len(x)):
        x[i] = x[i].split('\n')
    for j in range (1,8):
        #print (j)
        for i in range (0,len(x[j])):
            if '新莊區' in x[j][int(i)]:
                print (week[j],x[j][int(i)])


    #time.sleep(60)


def main ():
#    hot_blood_q =hot_blood()
#    hot_blood_q.line_notify()

    test()
if __name__ == '__main__':
    main()