# -*- coding: utf-8 -*-
from django.shortcuts import render
import csv
import os
import datetime


class output:
    def __init__(self):
        pass
    
    a = 0
    b = 0
    c = 0
    d = 0
    

def input_Num(x, y, z, resultLst):
    if 1 <= x <= 90:
        if 1 <= y <= 70:
            if 1 <= z <= 80:
                total_Sales(x, y, z, resultLst)
            else:
                result = "显示器数量错误"
                resultLst.append(result)
        else:
            result = "主机数量错误"
            resultLst.append(result)
    else:
        result = "外设数量错误"
        resultLst.append(result)


def csv_Num(x, y, z, resultLst):
    global output
    if 1 <= x <= 90:
        if 1 <= y <= 70:
            if 1 <= z <= 80:
                total_Sales(x, y, z, resultLst)
            else:
                result = "显示器数量错误"
                output.d = output.d + 1
                resultLst.append(result)
        else:
            result = "主机数量错误"
            output.d = output.d + 1
            resultLst.append(result)
    else:
        result = "外设数量错误"
        output.d = output.d + 1
        resultLst.append(result)


def total_Sales(x, y, z, resultLst):
    global output
    reward = 0
    total = x * 25 + y * 45 + z * 30
    if total < 1000:
        reward = total * 0.05
        output.a = output.a + 1
    elif 1000 <= total < 1800:
        reward = (total - 1000) * 0.1 + 50
        output.b = output.b + 1
    elif 1800 <= total:
        reward = (total - 1800) * 0.15 + 80 + 50
        output.c = output.c + 1
    # print "reward:",reward
    result = reward
    resultLst.append(result)


def csv_sales_Post(request):
    global output
    # upload files
    context = {}
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
    resultLst = []
    expectLst = []
    inputLst = []
    timeLst = []
    numberLst = []
    for line in reader:
        numberLst.append(line[0])
        x = int(line[1])
        y = int(line[2])
        z = int(line[3])
        csv_Num(x, y, z, resultLst)
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timeLst.append(nowTime)
        inputNum = ','.join([str(x), str(y), str(z)])
        inputLst.append(inputNum)
        expectLst.append(line[4])

    context['number'] = numberLst
    context['resultLst'] = resultLst
    context['inputLst'] = inputLst
    context['expectLst'] = expectLst
    context['timeLst'] = timeLst
    context['total'] = len(inputLst)
    context['wrongInput'] = output.d
    context['low'] = output.a
    context['medium'] = output.b
    context['high'] = output.c
    output.a = 0
    output.b = 0
    output.c = 0
    output.d = 0
    return render(request, 'commission.html', context)


def sales(request):
    return render(request, 'commission.html')


def sales_Post(request):
    try:
        int(request.POST["x"])
        int(request.POST["y"])
        int(request.POST["z"])
        x = int(request.POST["x"])
        y = int(request.POST["y"])
        z = int(request.POST["z"])
        resultLst = ['error']
        input_Num(x, y, z, resultLst)
        context = {}
        context['reward'] = resultLst[1]
        # context['time'] = nowTime
        return render(request, 'commission.html', context)
    except:
        context = {}
        context['reward'] = "错误输入"
        # context['time'] = nowTime
        return render(request, 'commission.html', context)

def reward_Post(request):
    
    resultLst = []
    total = int(request.POST["reward"])
    context = {}
    temp = 1
    
    print ("I am in reward post")
    
    if 100 <= total < 7800:
        for i in range(1, 91):
            x = total - i * 25
            if (x >= 75):
                for j in range(1, 71):
                    y = total - i * 25 - j * 45
                    if (y >= 30):
                        for k in range(1, 81):
                            z = (total - i * 25 - j * 45)
                            # print "z",z%30
                            if z % 30 == 0 and i * 25 + j * 45 + k * 30 == total:
                                num = "".join([str('ST'),str(temp).zfill(3)])
                                result = ",".join([str(num), str(i), str(j), str(k), str(total)])
                                temp = temp + 1
                                resultLst.append(result)

        expectLst = []
        inputLst = []
        numberLst = []

        with open('../softwareTest/upload/result001.csv', 'wb') as csvfiles:
            spamwriter = csv.writer(csvfiles, dialect='excel')
            spamwriter.writerow(['num', 'x', 'y', 'z', 'e'])
            for line in resultLst:
                spamwriter.writerow([line.split(",")[0], line.split(",")[1], line.split(",")[2], line.split(",")[3], line.split(",")[4]])
    
                numberLst.append(line.split(",")[0])
                inputLst.append(' , '.join([line.split(",")[1], line.split(",")[2], line.split(",")[3]]))
                expectLst.append(line.split(",")[4])
                
            csvfiles.close()

        # csvfile = file('../softwareTest/upload/result001.csv', 'rb')
        # csvfile.readline()
        # reader = csv.reader(csvfile)
        # resultLst = []
        # expectLst = []
        # inputLst = []
        # timeLst = []
        # numberLst=[]
        #
        # for line in reader:
        #     numberLst.append(line[0])
        #     csv_Num(x, y, z, resultLst)
        #     nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #     timeLst.append(nowTime)
        #     inputNum = '  ,  '.join([str(x), str(y), str(z)])
        #     inputLst.append(inputNum)
        #     expectLst.append(line[4])

        context['number'] = numberLst
        context['inputLst'] = inputLst
        context['expectLst'] = expectLst
        # context['timeLst'] = timeLst
        # context['total'] = len(inputLst)
        # context['wrongInput'] = output.d
        # context['low'] = output.a
        # context['medium'] = output.b
        # context['high'] = output.c
        # output.a = 0
        # output.b = 0
        # output.c = 0
        # output.d = 0
        return render(request, 'commission2.html', context)
    else:
        context = {}
        context['reward'] = "错误金额"
        # context['time'] = nowTime
        return render(request, 'commission2.html', context)
    