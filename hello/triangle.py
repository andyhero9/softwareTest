# -*- coding: utf-8 -*-
from django.shortcuts import render
import csv
import os
import datetime


def isTriangle(a, b, c, resultLst, percentage):
	side = sorted([a, b, c])
	
	if 1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100:
		if side[0] + side[1] > side[2]:
			if a == b and b == c:
				# print "等边三角形"
				result = "等边三角形"
				percentage.append("isTri")
				resultLst.append(result)
			else:
				if a == b or a == c or b == c:
					# print "等腰三角形"
					result = "等腰三角形"
					percentage.append("isTri")
					resultLst.append(result)
				else:
					if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
						# print "直角三角形"
						result = "直角三角形"
						percentage.append("isTri")
						resultLst.append(result)
					else:
						# print "一般三角形"
						result = "一般三角形"
						percentage.append("isTri")
						resultLst.append(result)
		else:
			# print "不是三角形"
			result = "不是三角形"
			percentage.append("isNotTri")
			resultLst.append(result)
	else:
		# print "输入数值有误(1<=a,b,c<=100)"
		result = "输入数值有误(1<=a,b,c<=100)"
		percentage.append("wrongInput")
		resultLst.append(result)


def triangle_post(request):
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
	#filePath = ''.join(['upload', myfile.name])
	#fo = open('upload/catalog.txt', "wb")
	fo.write(filePath)
	fo.close()
	context['isUploaded'] = "upload over!"


	# return render(request, 'triangle.html', context)

	# filePath = str(request.POST["filePath"])

	csvfile = file(filePath, 'rb')
	csvfile.readline()
	reader = csv.reader(csvfile)
	sideLst = []
	resultLst = []
	percentage = []
	expectLst = []
	timeLst = []
	for line in reader:
		a = line[0]
		b = line[1]
		c = line[2]
		eLst = line[3]
		expectLst.append(eLst)
		a, b, c = map(int, (a, b, c))
		isTriangle(a, b, c, resultLst, percentage)
		nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		timeLst.append(nowTime)
		side = str(a) + ',' + str(b) + ',' + str(c)
		sideLst.append(side)

	context['sideLst'] = sideLst
	context['resultLst'] = resultLst
	context['total'] = len(resultLst)
	context['expectLst'] = expectLst
	context['timeLst'] = timeLst
	context['isNotTriPer'] = percentage.count('isNotTri')
	context['wrongInputPer'] = percentage.count('wrongInput')
	context['isTriPer'] = percentage.count('isTri')
	#print(percentage)
	return render(request, 'index.html', context)  #
	# def triangle(request):
	# 	context = {}
	# 	context['button'] = "check to start"
	# 	return render(request, 'triangle.html', context)

def triangle_input(request):
	try:
		int(request.POST["a"])
		int(request.POST["c"])
		int(request.POST["c"])
		a = int(request.POST["a"])
		b = int(request.POST["b"])
		c = int(request.POST["c"])
		# print type(a),b,c

		side = sorted([a, b, c])
		if 1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100:
			if side[0] + side[1] > side[2]:
				if a == b and b == c:
					# print "等边三角形"
					result = "等边三角形"
				else:
					if a == b or a == c or b == c:
						result = "等腰三角形"
					else:
						if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
							# print "直角三角形"
							result = "直角三角形"
						else:
							# print "一般三角形"
							result = "一般三角形"
			else:
				# print "不是三角形"
				result = "不是三角形"
		else:
			# print "输入数值有误(1<=a,b,c<=100)"
			result = "输入数值有误(1<=a,b,c<=100)"
		# nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		context = {}
		context['result'] = result
		#print result
		# context['time'] = nowTime
		return render(request, 'index.html', context)

	except:
		context = {}
		context['result'] = "输入有误"
		# print result
		# context['time'] = nowTime
		return render(request, 'index.html', context)