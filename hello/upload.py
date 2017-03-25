# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import os
def loadCsv_Post(request):
    context = {}
    context['nextDay'] = "result"
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("E:\Django_project\softwareTest\upload", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")
    #return render(request, 'nextDay.html', context)