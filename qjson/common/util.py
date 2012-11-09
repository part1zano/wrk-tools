#-*- coding: utf-8 -*-
import myrandom

def get_value(arg):
	arg = str(arg).lower().strip()
	if arg == 'true':
		return True
	elif arg == 'false':
		return False
	elif arg == 'none':
		return None
	elif arg == '%%randomemail%%':
		return myrandom.random_email()
	elif arg == '%%randomphrase%%':
		return myrandom.random_phrase()
	else:
		return arg
