# -*- coding: utf-8 -*-
from django.shortcuts import render
import csv

def isTriangle(a,b,c,resultLst):
    side = sorted([a,b,c])
    if 1<=a<=100 and 1<=b<=100 and 1<=c<=100 :
        if side[0]+side[1]>side[2]:
            if a==b and b==c:
                #print "等边三角形"
                result = "等边三角形"
                resultLst.append(result)
            else:
                if a==b or a==c or b==c:
                    if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a :
                        #print "等腰直角三角形"
                        result = "等腰直角三角形"
                        resultLst.append(result)
                    else:
                        #print "等腰三角形"
                        result = "等腰三角形"
                        resultLst.append(result)
                else:
                    if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a :
                        #print "直角三角形"
                        result = "直角三角形"
                        resultLst.append(result)
                    else:
                        #print "一般三角形"
                        result = "一般三角形"
                        resultLst.append(result)
        else:
            #print "不是三角形"
            result = "不是三角形"
            resultLst.append(result)
    else:
        #print "输入数值有误(1<=a,b,c<=100)"
        result = "输入数值有误(1<=a,b,c<=100)"
        resultLst.append(result)

def triangle_post(request):
    #filePath = str(request.POST["filePath"])
    csvfile = file('triangle.csv', 'rb')
    csvfile.readline()
    reader = csv.reader(csvfile)
    sideLst = []
    resultLst = []
    expectLst = []
    for line in reader:
        a = line[0]
        b = line[1]
        c = line[2]
        eLst = line[3]
        expectLst.append(eLst)
        a, b, c = map(int, (a, b, c))
        isTriangle(a, b, c,resultLst)
        side = str(a) + ',' + str(b) + ',' + str(c)
        sideLst.append(side)
	context = {}
    context['button'] = "check to start"
    context['sideLst'] = sideLst
    context['resultLst'] = resultLst
    context['expectLst'] = expectLst
    return render(request, 'triangle.html', context)

def triangle(request):
    context = {}
    context['button'] = "check to start"
    return render(request, 'triangle.html', context)