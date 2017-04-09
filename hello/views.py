from django.shortcuts import render


def toIndex(request):
	return render(request, 'index.html')

def toNextDay(request):
	return render(request, 'nextDay.html')

def toCommission(request):
	return render(request, 'commission.html')

def toCommission2(request):
	return render(request, 'commission2.html')