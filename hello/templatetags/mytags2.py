from django import template

register = template.Library()
i = 0

@register.filter
def qwer2(value):
	global i
	print i
	if i < len(value):
		value = value[i]
		i = i + 1
		return str(value)
	else:
		i = 1
		return value[0]
