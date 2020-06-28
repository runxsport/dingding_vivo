# -*- encoding=utf8 -*-

# adb tcpip 5556
# adb connect 192.168.2.134:5556

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
__author__ = "admin"
from airtest.core.api import *
auto_setup(__file__)
sleep(7200)
keyevent("POWER")
sleep()
swipe((800,1800),(800,300))
sleep(3)
start_app('com.alibaba.android.rimet')
touch(Template(r"tpl1592391451035.png", record_pos=(-0.002, 0.918), resolution=(1080, 2160)))
touch(Template(r"tpl1592391328114.png", record_pos=(0.372, -0.061), resolution=(1080, 2160)))
try:
    touch(Template(r"tpl1592393729338.png", record_pos=(0.006, 0.096), resolution=(720, 1280)))
except:
    pass
try:
    touch(Template(r"tpl1592391491270.png", record_pos=(-0.323, 0.055), resolution=(1080, 2160)))
    touch(Template(r"tpl1592391499402.png", record_pos=(0.233, 0.093), resolution=(1080, 2160)))
except:
    pass