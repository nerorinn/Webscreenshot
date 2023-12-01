import webbrowser
import os
import webbrowser
from PIL import ImageGrab
from datetime import datetime
import time
#from selenium import webdriver

filename = "web.txt"
shotfilename = "shot"
#options = webdriver.ChromeOptions()
#options.add_argument('--incognito')
#driver = webdriver.Chrome(chrome_options=options)

# 获取当前文件所在目录
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, filename)
print (current_directory)
#时间
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
current_day = datetime.now().strftime("%Y%m%d")

shotfile = current_directory + '\\' + shotfilename
print (shotfile)
os.makedirs(shotfile, exist_ok=True)
shotfiletody = shotfile + '\\' + current_day
os.makedirs(shotfiletody, exist_ok=True)
# 检查文件是否存在
if os.path.exists(file_path):
    f = open(file_path)
    line = f.readline()
    count = 0
    while line:
        #for line in file:
        print(line.strip())  # strip() 用于去除行尾的换行符和空白字符
        # 打开指定的网页
        #driver.get(line)
        webbrowser.open(line)
        time.sleep(5)
        screenshot = ImageGrab.grab()
        print (current_time + 'screenshot.png')
        screenshotname = shotfiletody +'\\' + current_time + '_' + str(count) + '.png'
        screenshot.save(screenshotname)
        command = "taskkill /f /im chrome.exe"
        os.system(command)
        line = f.readline()
        count = count + 1
    f.close()
else:
        print("文件 '{filename}' 不存在.")


#class screenshot:
     