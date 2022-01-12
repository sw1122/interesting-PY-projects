'''
autor: wsw
Time: 2021.12.12
浙江大学健康打卡小程序2.0加入GUI
'''
from selenium import webdriver
import time
import datetime
import xlrd
import os
import tkinter as tk
from tkinter import messagebox
import sys

def record(admin, password, set_ime, path, path1, minute):
    while 1:
        current_time = datetime.datetime.now()
        hour = current_time.hour
        minut = current_time.minute

        if hour == set_ime and minute == minut:
            if path1 == 'msedgedriver.exe':     #Edge 浏览器
                driver = webdriver.Edge(path)
            elif path1 == 'chromedriver.exe':     #Chrome 浏览器
                driver = webdriver.Chrome('chromedriver.exe')

            driver.get('https://healthreport.zju.edu.cn/ncov/wap/default/index')
            driver.set_window_size(400, 400)

            driver.find_element_by_xpath('//*[@id="username"]').send_keys(admin)
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
            driver.find_element_by_xpath('//*[@id="dl"]').click()  #点击登录
            try:
                driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[15]/div/div/div[1]/span[2]').click() #点击在校
            except:
                root.withdraw()  # 隐藏窗口
                messagebox.showinfo('错误', '请检查一下你的密码 @_@')
                sys.exit()
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[22]/div/div/div[2]/span[1]').click() #无14日内入境
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[34]/div/div/div/span[1]').click() #本人承诺
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[19]/div/input').click()  #获取定位
            time.sleep(3)
            try:
                driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[5]/div/a').click()   #提交信息
            except:
                messagebox.showinfo('错误', '获取位置信息失败，要不看看电脑定位开了没？ @_@')
                sys.exit()
            time.sleep(3)
            try:
                driver.find_element_by_xpath('//*[@id="wapcf"]/div/div[2]/div[2]').click()  #确认提交
                print('恭喜，今日打卡成功，明天再来 ^_^')
            except:
                root.withdraw()  # 隐藏窗口
                messagebox.showinfo('你在逗我', '你今天已经打过卡了 @_@')
            time.sleep(5)
            driver.quit()
            time.sleep(24*60*60-600)
if __name__ == '__main__':
    file = 'wsw打卡.xls'
    #打开文件
    wb = xlrd.open_workbook(filename=file)
    s1 = wb.sheet_by_index(0)
    admin = str(int(s1.row(1)[1].value))
    password = str(s1.row(2)[1].value)
    set_ime = s1.row(3)[1].value  #设置小时
    minute = s1.row(4)[1].value  #设置分钟
    path1 = s1.row(5)[1].value  #浏览器驱动
    path2 = s1.row(6)[1].value  #浏览器所在位置
    path = os.path.join(path2, path1)

    #driver = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
    root = tk.Tk()  # 新建窗口
    root.withdraw()  # 隐藏窗口
    messagebox.showinfo('欢迎使用wsw_打卡小程序', '点击确定程序开始运行 ^_^')
    record(admin, password, set_ime, path, path1, minute)  #调用打卡程序


