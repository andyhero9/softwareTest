from django import template

register = template.Library()
i = 0

@register.filter
def qwer1(value):
	global i
	print 'qwer1', i
	if i < len(value):
		value = value[i]
		i = i + 1
		return str(value)
	else:
		i = 1
		return value[0]
	
j = 0

@register.filter
def qwer11(value):
	global j
	print 'qwer1', j
	if j < len(value):
		value = value[j]
		j = j + 1
		return str(value)
	else:
		j = 1
		return value[0]
	

k = 0

@register.filter
def qwer111(value):
	global k
	print 'qwer1', k
	if k < len(value):
		value = value[k]
		k = k + 1
		return str(value)
	else:
		k = 1
		return value[0]


m = 0


@register.filter
def qwer1111(value):
	global m
	if m < len(value):
		value = value[m]
		m = m + 1
		return str(value)
	else:
		m = 1
		return value[0]
