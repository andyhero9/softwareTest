# -*- coding: utf-8 -*-
from django.shortcuts import render
import csv
import datetime
import time

def nextDay():
    while True:
        year = input("请输入年：")
        if 1800<=year<=2100:
            month = input("请输入月：")
            if 1<=month<=12:
                day = input("请输入日：")
                if 1<=day<=31:
                    is_valied_date(year, month, day)
                    break
                else:
                    print "日错误"
            else:
                print "月错误"
        else:
            print "年错误"

def is_valied_date(year, month, day):
  '''判断是否是一个有效的日期字符串'''
  ndate = '-'.join([str(year), str(month), str(day)])
  try:
    time.strptime(ndate, "%Y-%m-%d")
    is_theNextDay(year, month, day)
  except:
    print "错误日期"

def is_theNextDay(year,month,day):
    thisDay = datetime.date(int(year),int(month),int(day))
    nextDay = thisDay + datetime.timedelta(days=1)
    print 'thisDay:',thisDay,'nextDay:',nextDay