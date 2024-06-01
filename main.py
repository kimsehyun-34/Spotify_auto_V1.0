from selenium import webdriver
import os, time
import pandas as pd

def bot():

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36')
    options.add_argument("--user-data-dir=C:/Users/about/AppData/Local/Google/Chrome/User Data")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    driver.get('https://accounts.spotify.com/')
    print('로그인중....')
    time.sleep(3)

    login_btn = driver.find_element("xpath", '/html/body/div/div/div[2]/div/div/button[2]')
    login_btn.click()
    time.sleep(2)

    login_btn = driver.find_element("xpath", '/html/body/div[4]/div/div[2]/div[1]/nav/div[2]/div[1]/div[2]/div[2]/div/div[2]/ul/div/div[2]/li/div/div[1]')
    login_btn.click()
    time.sleep(3)


    data = pd.read_csv('2020-1.csv')

    for i in range(0,100):
        if i==0:
            n=0
        a=data.loc[n,"A"]
        nn=n+1
        aa=data.loc[nn,"A"]
        n=n+2

        name=aa+" - "+a

        input = driver.find_element("xpath", '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/div[1]/section/div[2]/div[3]/section/div/div/input')
        input.send_keys(name)
        time.sleep(1.5)
        input_on = driver.find_element("xpath", '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div[4]/button')
        input_on.click()
        time.sleep(0.5)

        input_out = driver.find_element("xpath", '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/div[1]/section/div[2]/div[3]/section/div/div/div/button')
        input_out.click()
        time.sleep(0.5)

        print(a+"-"+aa)

    print('모든 작업 완료')
    driver.quit()


bot()
os.system('pause')
