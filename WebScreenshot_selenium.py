import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

#　INPUT,OUTPUT
filename = "web.txt"
shotfilename = "shot"

#　ファイルパス
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, filename)

#　現在の日付と時間
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
current_day = datetime.now().strftime("%Y%m%d")

#　ファイル存在チェック
if os.path.exists(file_path):

    #　フォルダ作成
    shotfile = current_directory + '\\' + shotfilename
    os.makedirs(shotfile, exist_ok=True)

    #　日付フォルダ作成
    shotfiletody = shotfile + '\\' + current_day
    os.makedirs(shotfiletody, exist_ok=True)
    #　実行開始時間ログ作成（フォルダ）
    log = shotfile + '\\' + current_day +'\\' + "実行開始時間 " + current_time
    os.makedirs(log, exist_ok=True)

    #　chromeの設定
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options = options)

    #　INPUTファイルを読み込む
    f = open(file_path)
    line = f.readline()

    while line:
        #　URL、見出しを分ける
        my_list = (line.strip()).split(",")
        driver.get(my_list[0])
        #　chromeの設定 （サイズ1000，1000）
        driver.set_window_size(1000,1000)
        time.sleep(3)
        screenshotname = shotfiletody +'\\' + my_list[1] + '_' + my_list[2] + '.png'
        driver.save_screenshot(screenshotname)
        line = f.readline()

    driver.quit()
    f.close()    
else:
        print("ファイル["+ filename+ "]がないため、実行できません.")
