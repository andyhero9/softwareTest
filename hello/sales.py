# -*- coding: utf-8 -*-
from django.shortcuts import render
import csv
import os
import datetime

def input_Num(x,y,z,resultLst):
    if 1<=x<=90:
        if 1<=y<=70:
            if 1<=z<=80:
                total_Sales(x, y, z,resultLst)
            else:
                result = "外设数量错误"
                resultLst.append(result)
        else:
            result = "主机数量错误"
            resultLst.append(result)
    else:
        result = "显示器数量错误"
        resultLst.append(result)

def csv_Num(x,y,z,resultLst):
    if 1<=x<=90:
        if 1<=y<=70:
            if 1<=z<=80:
                total_Sales(x, y, z,resultLst)
            else:
                result = "外设数量错误"
                resultLst.append(result)
        else:
            result = "主机数量错误"
            resultLst.append(result)
    else:
        result = "显示器数量错误"
        resultLst.append(result)

def total_Sales(x,y,z,resultLst):
    reward = 0
    total = x*25 + y*45 + z*30
    if total<1000:
        reward = total*0.05
    elif 1000<=total<1800:
        reward = (total-1000) * 0.1 + 50
    elif 1800<=total:
        reward = (total - 1800) * 0.15 + 80 + 50
    #print "reward:",reward
    result = reward
    resultLst.append(result)

def csv_sales_Post(request):
    #upload files
    context={}
    myfile = request.FILES.get("myFile", None)  # 获取上传的文件，如果没有文件，则默认为None
    if not myfile:
        context['isUploaded'] = "no files for upload!"
    # return render(request, 'triangle.html', context)

    destination = open(os.path.join("../softwareTest/upload", myfile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
    for chunk in myfile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    filePath = ''.join(["../softwareTest/upload/", myfile.name])
    fo = open("../softwareTest/upload/catalog.txt", "wb")
    fo.write(filePath)
    fo.close()
    context['isUploaded'] = "upload over!"

    csvfile = file(filePath, 'rb')
    csvfile.readline()
    reader = csv.reader(csvfile)
    resultLst=[]
    expectLst = []
    inputLst = []
    timeLst = []
    for line in reader:
        x = int(line[0])
        y = int(line[1])
        z = int(line[2])
        csv_Num(x, y, z,resultLst)
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timeLst.append(nowTime)
        inputNum = ','.join([str(x), str(y), str(z)])
        inputLst.append(inputNum)
        expectLst.append(line[3])
    context['reward'] = resultLst
    context['inputLst'] = inputLst
    context['expectLst'] = expectLst
    context['timeLst'] = timeLst
    return render(request, 'sales.html', context)

def sales(request):
    return render(request, 'sales.html')

def sales_Post(request):
    x = request.POST["x"]
    y = request.POST["y"]
    z = request.POST["z"]
    resultLst = ['error']
    input_Num(x,y,z,resultLst)
    context = {}
    context['reward'] = resultLst[1]
    # context['time'] = nowTime
    return render(request, 'sales.html', context)