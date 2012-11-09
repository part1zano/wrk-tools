#-*- coding: utf-8 -*-

def get_value(arg):
	arg = str(arg).lower().strip()
	if arg == 'true':
		return True
	elif arg == 'false':
		return False
	elif arg == 'none':
		return None
	else
		return arg
