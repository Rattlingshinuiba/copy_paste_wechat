import pyautogui
import time
import os
import json
import pysnooper

pyautogui.PAUSE=0.5
pyautogui.FAILSAFE=True
#特殊位置
typora = [1266, 1056]
g_chrome = [666, 1046]
adress_bar = [577,79]
site_body = [751,444]
typora_body = [680,504]
ls_20_urls = os.listdir('news_url')
@pysnooper.snoop()
def copy_paste(file_pos):
    for i in [ls_20_urls[file_pos]]:
        with open(f'news_url/{i}', 'r') as f:
            urls = json.load(f)
        for url in urls:        
            #打开浏览器，替换url
            pyautogui.click(*g_chrome)
            pyautogui.doubleClick(*adress_bar)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('del')
            pyautogui.typewrite(url)
            time.sleep(0.5) 
            pyautogui.hotkey('enter')
            time.sleep(3) #等待加载
            #进入网页后，复制其内容
            pyautogui.click(*site_body)
            #多次点击pagedown，以加载图片
            pyautogui.press("pagedown", presses=5, interval=0.5)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            #粘贴到typora
            pyautogui.click(*typora)
            time.sleep(1)
            pyautogui.click(typora_body)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(1)
            pyautogui.hotkey("enter")
            time.sleep(1)
            pyautogui.hotkey("ctrl", "w")
            time.sleep(1)
