
import requests
import ntplib
import datetime
import time



def get_time_if_url_not_work():
    c = ntplib.NTPClient()
    response = c.request('0.ua.pool.ntp.org', version=3)
    t = datetime.fromtimestamp(response.tx_time).time().strftime('%H:%M:%S %p')
    d = datetime.fromtimestamp(response.tx_time).date().strftime('%Y-%m-%d')
    date = {"date": d, "time": t}
    return date


def check_time(d):
    if "time" in d.keys():
        print("Time is: ", d['time'])
    try:
        print("Date is: ", d['date'])
    except KeyError:
        print("No date in response!!!")
        raise KeyError


def main(url=''):
    if not url:
        print("No URL passed to function")
        return False

    try:
        r = requests.get(url=url)
    except requests.exceptions.RequestException as e:
        raise ConnectionError

    if r:
        check_time(r.json())
    else:
        check_time(get_time_if_url_not_work())
    return True



def time_check():
     currentTime = datetime.datetime.now()
     currentTime.hour
     if currentTime.hour < 12:
         print('Good Morning')
         return True
     elif 12 <= currentTime.hour:
         print('Good afternoon')
         return  True
     else:
         return False 


time_check()



def my_good_fun():
    return "success"


if __name__ == "__main__":
    a = "=" * 40
    print(a + "\nРезультат без параметрів: ")
    main()
    print(a + "\nРезультат з правильною URL: ")
    main('http://date.jsontest.com/')
    a = my_good_fun()
    print(a)
