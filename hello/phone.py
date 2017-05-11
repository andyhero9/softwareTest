# -*- coding: utf-8 -*-
from django.shortcuts import render
import csv
import os
import datetime
from outputCsv import insertCsv, outCsv

# levels in percentage
# l1: 0 < 通话时间 <= 60
# l2: 60 < 通话时间 <= 120
# l3: 120 < 通话时间 <= 180
# l4: 180 < 通话时间 <= 300
# l5: 300 < 通话时间

def phone_post(request):
	context = {}
	myfile = request.FILES.get("myFile", None)  # 获取上传的文件，如果没有文件，则默认为None
	if not myfile:
		context['isUploaded'] = "no files for upload!"
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
	sideLst = []
	resultLst = []
	percentage = []
	numberLst = []
	expectLst = []
	timeLst = []
	staffLst = []
	
				
	for line in reader:
		numberLst.append(line[0])
		holding_Time = int(line[1])
		owe_Num = int(line[2])
		month = int(line[3])
		eLst = line[4]
		expectLst.append(eLst)
		result = str(calculate_Bill_per(holding_Time, owe_Num, month, percentage))
		resultLst.append(result)
		nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		timeLst.append(nowTime)
		side = str(holding_Time) + ',' + str(owe_Num) + ',' + str(month)
		sideLst.append(side)
		staffLst.append('Tester')
	
	print percentage.count("l1")
	print percentage.count("l2")
	print percentage.count("l3")
	print percentage.count("l4")
	print percentage.count("l5")
	
	context['number'] = numberLst
	context['sideLst'] = sideLst
	context['resultLst'] = resultLst
	# context['total'] = len(resultLst)
	context['expectLst'] = expectLst
	context['timeLst'] = timeLst
	context['l1'] = percentage.count("l1")
	context['l2'] = percentage.count("l2")
	context['l3'] = percentage.count("l3")
	context['l4'] = percentage.count("l4")
	context['l5'] = percentage.count("l5")
	context['total'] = len(percentage)
	# context['isNotTriPer'] = percentage.count('isNotTri')
	# context['wrongInputPer'] = percentage.count('wrongInput')
	# context['isTriPer'] = percentage.count('isTri')
	# print(percentage)
	outCsv(numberLst, sideLst, expectLst, resultLst, timeLst, staffLst, 'PhoneResult')
	return render(request, 'phone.html', context)


def phone_input(request):
	try:
		
		int(request.POST["holding_Time"])
		int(request.POST["owe_Num"])
		int(request.POST["month"])
		holding_Time = int(request.POST["holding_Time"])
		owe_Num = int(request.POST["owe_Num"])
		month = int(request.POST["month"])
		
		result = str(calculate_Bill(holding_Time, owe_Num, month))
		
		nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		insertCsv(holding_Time, owe_Num, month, result, result, nowTime, 'Tester', 'Single_phone')
		
		context = {}
		context['result'] = result
				
		return render(request, 'phone.html', context)
	
	except:
		context = {}
		context['result'] = "输入有误"
		return render(request, 'phone.html', context)


def calculate_Bill_per(holding_Time, owe_Num, month, percentage):
	if int(owe_Num) > 11 or month > 12:
		return "time error"
	if int(owe_Num) < int(month):
		if 0 < int(holding_Time) <= 60:
			percentage.append("l1")
			if 0 <= int(owe_Num) <= 1:
				Fee = 25 + holding_Time * 0.15 * 0.99
				return Fee
			else:
				Fee = 25 + holding_Time * 0.15
				return Fee
		elif 60 < int(holding_Time) <= 120:
			percentage.append("l2")
			if 0 <= int(owe_Num) <= 2:
				Fee = 25 + holding_Time * 0.15 * 0.985
				return Fee
			else:
				Fee = 25 + holding_Time * 0.15
				return Fee
		elif 120 < int(holding_Time) <= 180:
			percentage.append("l3")
			if 0 <= int(owe_Num) <= 3:
				Fee = 25 + holding_Time * 0.15 * 0.98
				return Fee
			else:
				Fee = 25 + holding_Time * 0.15
				return Fee
		elif 180 < int(holding_Time) <= 300:
			percentage.append("l4")
			if 0 <= int(owe_Num) <= 3:
				Fee = 25 + holding_Time * 0.15 * 0.975
				return Fee
			else:
				Fee = 25 + holding_Time * 0.15
				return Fee
		elif 300 < int(holding_Time):
			percentage.append("l5")
			if 0 <= int(owe_Num) <= 6:
				Fee = 25 + holding_Time * 0.15 * 0.97
				return Fee
			else:
				Fee = 25 + holding_Time * 0.15
				return Fee
		elif int(holding_Time) <= 0:
			Fee = 25
			return Fee
	else:
		result = 'month:' + str(month) + '=> owe_Num:' + str(owe_Num)
		return result
	

def calculate_Bill(holding_Time, owe_Num, month):
	if int(owe_Num) > 11 or month > 12:
		return "time error"
	if int(owe_Num) < int(month):
		if 0 < int(holding_Time) <= 60:
			if 0 <= int(owe_Num) <= 1:
				Fee = 25 + holding_Time * 0.15 * 0.99
				return Fee
			else:
				Fee = 25 + holding_Time * 0.15
				return Fee
		elif 60 < int(holding_Time) <= 120:
			if 0 <= int(owe_Num) <= 2:
				Fee = 25 + holding_Time * 0.15 * 0.985
				return Fee
			else:
				Fee = 25 + holding_Time * 0.15
				return Fee
		elif 120 < int(holding_Time) <= 180:
			if 0 <= int(owe_Num) <= 3:
				Fee = 25 + holding_Time * 0.15 * 0.98
				return Fee
			else:
				Fee = 25 + holding_Time * 0.15
				return Fee
		elif 180 < int(holding_Time) <= 300:
			if 0 <= int(owe_Num) <= 3:
				Fee = 25 + holding_Time * 0.15 * 0.975
				return Fee
			else:
				Fee = 25 + holding_Time * 0.15
				return Fee
		elif 300 < int(holding_Time):
			if 0 <= int(owe_Num) <= 6:
				Fee = 25 + holding_Time * 0.15 * 0.97
				return Fee
			else:
				Fee = 25 + holding_Time * 0.15
				return Fee
		elif int(holding_Time) <= 0:
			Fee = 25
			return Fee
	else:
		result = 'month:' + str(month) + '=> owe_Num:' + str(owe_Num)
		return result
