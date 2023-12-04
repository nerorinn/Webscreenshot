import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

#存放网页的文件夹名字
#web.txt里面每一行都要有三个数据
#1；网址
#2；名字1
#3；名字2
#生成的截图会包含 2和3

filename = "web.txt"
shotfilename = "shot"

# 获取当前文件所在目录
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, filename)
print (current_directory)

#获取当前时间
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
current_day = datetime.now().strftime("%Y%m%d")

#创建截图存放文件夹
shotfile = current_directory + '\\' + shotfilename
os.makedirs(shotfile, exist_ok=True)
#创建日期文件夹
shotfiletody = shotfile + '\\' + current_day
os.makedirs(shotfiletody, exist_ok=True)

#创建日期文件夹
log = shotfile + '\\' + current_day +'\\' + "実行開始時間 " + current_time
os.makedirs(log, exist_ok=True)

options = Options()
#无痕模式打开
options.add_argument('--incognito')
#无界面设置
options.add_argument('--headless')
#应用chrome设置
driver = webdriver.Chrome(options = options)

# 检查文件是否存在
if os.path.exists(file_path):
    f = open(file_path)
    line = f.readline()
    #count = 1
    while line:
        #将一行的3个数据切割 顺便删除改行
        my_list = (line.strip()).split(",")
        print(my_list)  
        driver.get(my_list[0])
        #检测网页高度 →固定1000，1000
        #height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.set_window_size(1000,1000)
        time.sleep(5)
        screenshotname = shotfiletody +'\\' + my_list[1] + '_' + my_list[2] + '.png'
        driver.save_screenshot(screenshotname)
        line = f.readline()
        #count = count + 1
    driver.quit()
    f.close()
else:
        print("文件 '{filename}' 不存在.")