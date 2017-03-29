from django import template

register = template.Library()
i = 0

@register.filter
def qwer2(value):
	global i
	print 'qwer2', i
	if i < len(value):
		value = value[i]
		i = i + 1
		return str(value)
	else:
		i = 1
		return value[0]


j = 0

@register.filter
def qwer22(value):
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
def qwer222(value):
	global k
	print 'qwer1', k
	if k < len(value):
		value = value[k]
		k = k + 1
		return str(value)
	else:
		k = 1
		return value[0]
