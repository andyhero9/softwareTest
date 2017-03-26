# -*- coding: utf-8 -*-
from django.shortcuts import render
import csv
import datetime
import re

def nextDay(year,month,day,resultLst):
    if 1800<=int(year)<=2100:
        if 1<=int(month)<=12:
            if 1<=int(day)<=31:
                is_valied_date(year, month, day,resultLst)
            else:
                result = "日错误"
                resultLst.append(result)
        else:
            result = "月错误"
            resultLst.append(result)
    else:
        result = "年错误"
        resultLst.append(result)

def csv_nextDay(year,month,day,resultLst, percentage):
    if 1800<=year<=2100:
        if 1<=month<=12:
            if 1<=day<=31:
                is_valied_date(year, month, day,resultLst)
            else:
                result = "日错误"
                percentage.append('1')
                resultLst.append(result)
        else:
            result = "月错误"
            percentage.append('1')
            resultLst.append(result)
    else:
        result = "年错误"
        percentage.append('1')
        resultLst.append(result)

def is_valied_date(year, month, day,resultLst):
  '''判断是否是一个有效的日期字符串'''
  y = str(year).zfill(4)
  m = str(month).zfill(2)
  d = str(day).zfill(2)
  ndate = '-'.join([str(y), str(m), str(d)])
  dateFormat = re.match(
      r'(([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29)',
      ndate)
  if dateFormat:
      is_theNextDay(year, month, day,resultLst)
  else:
      result = "错误日期"
      resultLst.append(result)
  """
  try:
    time.strptime(ndate, "%Y-%m-%d")
    is_theNextDay(year, month, day,resultLst)
  except:
    result = "错误日期"
    resultLst.append(result)
    traceback.print_exc()
   """

def is_theNextDay(year,month,day,resultLst):
    thisDay = datetime.date(int(year),int(month),int(day))
    nextDay = thisDay + datetime.timedelta(days=1)
    result = nextDay.isoformat()
    resultLst.append(result)

# def readCsv(resultLst):
#     filePath = str(request.POST["myfile"])
#     csvfile = file(filePath, 'rb')
#     csvfile.readline()
#     reader = csv.reader(csvfile)
#     for line in reader:
#         year = int(line[0])
#         month = int(line[1])
#         day = int(line[2])
#         csv_nextDay(year, month, day,resultLst)

def nextDay_Post(request):
    year = request.POST["year"]
    month = request.POST["month"]
    day = request.POST["day"]
    resultLst = ['error']
    nextDay(year, month, day, resultLst)
    context = {}
    context['nextDay'] = resultLst[1]
    return render(request, 'nextDay.html', context)

def nextDay_Post_Csv(request):
    resultLst = []
    percentage = []
    context = {}
    print 'aaaaaaaaaaaaaaaaa'
    csvfile = request.FILES.get("myfile", None)
    if not csvfile:
        context['nextDay'] = "no files for upload!"
        return render(request, 'nextDay.html', context)
    print type(csvfile)
    print csvfile.name
    csvfile.readline()
    reader = csv.reader(csvfile)
    for line in reader:
        year = int(line[0])
        month = int(line[1])
        day = int(line[2])
        csv_nextDay(year, month, day, resultLst, percentage)
    context['nextDayList'] = resultLst
    context['total'] = len(resultLst)
    context['trueDate'] = percentage.count('1')
    context['fakeDate'] = len(resultLst) - percentage.count('1')
    return render(request, 'nextDay.html', context)

def nextDay_Get(request):
    context = {}
    context['nextDay'] = "result"
    return render(request, 'nextDay.html', context)

