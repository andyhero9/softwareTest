# -*- coding: utf-8 -*-
from django.shortcuts import render
import csv
import codecs
import os
import datetime


def outCsv(num, input, expect, reality, time, staff, name):
	filename = ''.join(['../softwareTest/upload/', name, '.csv'])
	with open(filename, 'wb') as csvfiles:
		# csvfiles.write(codecs.ASCII)
		spamwriter = csv.writer(csvfiles, dialect='excel')
		spamwriter.writerow(['No.', 'X', 'Y', 'Z', 'Expect', 'Reality', 'Result', 'Time', 'Staff'])
		i = 0
		for line in input:
			if str(expect[i]) == str(reality[i]):
				result = 'True'
			else:
				result = 'False'
			spamwriter.writerow([
				num[i], line.split(',')[0], line.split(',')[1], line.split(',')[2], expect[i], reality[i], result,
				time[i], staff[i]
			])
			i = i + 1
		
		csvfiles.close()


def insertCsv(x, y, z, expect, reality, time, staff, name):
	
	filename = ''.join(['../softwareTest/upload/', name, '.csv'])
	
	if str(expect) == str(reality):
		result = 'True'
	else:
		result = 'False'
	
	
	with open(filename, 'ab+') as csvfiles:
		"""
		num = 0
		csvfiles.readline()
		reader = csv.reader(csvfiles)
		for line in reader:
			Number = line[0]
			num = str(int(Number[-1]) + 1).zfill(3)
		
		spamwriter = csv.writer(csvfiles, dialect='excel')
		spamwriter.writerow([num, x, y, z, expect, reality, result, time, staff])
		csvfiles.close()
		"""
		csvfiles.readline()
		reader = csv.reader(csvfiles)
		temp = ''
		for line in reader:
			Number = line[0]
		temp = Number
		num = str(int(temp[2:5]) + 1).zfill(3)
		Num = temp[0:2]+num

		spamwriter = csv.writer(csvfiles, dialect='excel')
		spamwriter.writerow([Num, x, y, z, expect, reality, result, time, staff])
		csvfiles.close()