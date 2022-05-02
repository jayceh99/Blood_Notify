import requests


class hot_blood ():
    def __init__(self) :
        self.headers = {
                "Authorization": "Bearer " + "???",
                "Content-Type": "application/x-www-form-urlencoded"} 

    def line_notify(self): 

        params = {'message':'test'}

        r = requests.post("https://notify-api.line.me/api/notify",headers=self.headers, params=params)

        print(r.status_code)


def main ():
    hot_blood_q =hot_blood()
    hot_blood_q.line_notify()
if __name__ == '__main__':
    main()