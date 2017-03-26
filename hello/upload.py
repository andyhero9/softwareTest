# -*- coding: utf-8 -*-
from django.shortcuts import render

import os
def loadCsv_Post(request):
    context = {}
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            context['nextDay'] = "no files for upload!"
            return render(request, 'nextDay.html', context)
        destination = open(os.path.join("E:/Django_project/softwareTest/upload", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        filePath = ''.join(["E:/Django_project/softwareTest/upload/",myFile.name])
        fo = open("E:/Django_project/softwareTest/upload/catalog.txt", "wb")
        fo.write(filePath)
        fo.close()
        context['nextDay'] = "upload over!"
        return render(request, 'nextDay.html', context)
    
def traingleCsv_Post(request):
    context = {}
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            context['button'] = "no files for upload!"
            return render(request, 'triangle.html', context)
        destination = open(os.path.join("E:/Django_project/softwareTest/upload", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        filePath = ''.join(["E:/Django_project/softwareTest/upload/",myFile.name])
        fo = open("E:/Django_project/softwareTest/upload/catalog.txt", "wb")
        fo.write(filePath)
        fo.close()
        context['button'] = "upload over!"
        return render(request, 'triangle.html', context)