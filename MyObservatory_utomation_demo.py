# -*- coding : utf-8 -*-
'''
---------------------------------
  @time      :2020/4/19 10:52 上午
  @Author    :lan_huangfu
  @Email     :363517882@qq.com
  @file      :MyObservatory_utomation_demo.py
  @Software  :PyCharm
---------------------------------
'''
from appium import webdriver
import time
import datetime

desired_caps = {}

# 配置平台信息
desired_caps['platformName'] = 'Android'
#desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'wcozskivvwpr9doj'
desired_caps['noReset'] = True

# 获取应用的appPackage,appActivity
desired_caps['appPackage'] = 'hko.MyObservatory_v1_0'
desired_caps['appActivity'] = 'hko.MyObservatory_v1_0.AgreementPage'

'''
1.手动开启appium server 使其处于监听状态
2.模拟器/真机 在线 - 电脑能够识别到移动设备 adb devices命令检测设备
'''
# 与appium server建立连接，发送初始数据 将默认预置的4444端口更改为4723
driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                          desired_capabilities=desired_caps)
time.sleep(8)

el1 = driver.find_element_by_accessibility_id("Navigate up").click()#点击左上角按钮
time.sleep(8)

def getSize():  # 获取当前的width和height的x、y的值
    x = driver.get_window_size()['width']  # width为x坐标
    y = driver.get_window_size()['height']  # height为y坐标
    return (x, y)

def swipeUp(t):  # 当前向上滑动swipeup
    l = getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.25)
    driver.swipe(x1, y1, x1, y2, t)  # 设置时间为500
swipeUp(1300)#由于各机型不一样，滑动效果会存在一定差异，如需适配需要更改此参数
time.sleep(8)

el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                   "android.widget.FrameLayout/android.view.ViewGroup/"
                                   "android.widget.FrameLayout[2]/android.widget.FrameLayout/"
                                   "android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/"
                                   "android.widget.ListView/android.widget.LinearLayout[3]/"
                                   "android.widget.LinearLayout").click()#点击九天預報按钮

time.sleep(8)

el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                   "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/"
                                   "android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/"
                                   "android.widget.FrameLayout/android.widget.RelativeLayout/"
                                   "android.widget.LinearLayout/android.support.v4.view.ViewPager/"
                                   "android.widget.LinearLayout/android.widget.ListView/"
                                   "android.widget.LinearLayout[1]/android.widget.LinearLayout/"
                                   "android.widget.LinearLayout[1]/android.widget.TextView[1]").text#获取第一行数据日期


#将当前日期进行格式转换后，与第一行数据日期进行比较
today = datetime.date.today()
detester = today.strftime('%m')
detester1 = today.strftime('%d')
detester3 = (int(detester))
detester4 = (f"{detester3}月{detester1}日")
if el3 == detester4:
    print(f"数据验证成功，当前第一条数据显示的日期为：{el3}，当前日期为：{detester4}，用例执行成功！")
else:
    print(f"数据验证失败，当前第一条数据显示的日期为：{el3}，当前日期为：{detester4}，用例执行失败！")

