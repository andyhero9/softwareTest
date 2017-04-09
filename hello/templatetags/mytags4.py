from django import template

register = template.Library()
i = 0


@register.filter
def qwer4(value):
	global i
	if i < len(value):
		value = value[i]
		i = i + 1
		return str(value)
	else:
		i = 1
		return value[0]


j = 0


@register.filter
def qwer44(value):
	global j
	if j < len(value):
		value = value[j]
		j = j + 1
		return str(value)
	else:
		j = 1
		return value[0]


k = 0


@register.filter
def qwer444(value):
	global k
	if k < len(value):
		value = value[k]
		k = k + 1
		return str(value)
	else:
		k = 1
		return value[0]
	
m = 0


@register.filter
def qwer4444(value):
	global m
	if m < len(value):
		value = value[m]
		m = m + 1
		return str(value)
	else:
		m = 1
		return value[0]

