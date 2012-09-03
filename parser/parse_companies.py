#!/usr/bin/env python
# -*- coding: utf-8 -*-

from testlib import testcase
import sys,re,codecs

fh = codecs.open('objlist.txt', encoding='utf-8')
firmlist = [elem.strip() for elem in fh.readlines()]
fh.close()

tc = testcase.TestObject('parser.conf')
for firm in firmlist:
	toPrint = ''
	if not tc.visit_plink(firm, 'member'):
		tc.log.write('error', 'no obj '+firm)
		tc.go(tc.url)
		continue
	
	table = tc.get_xpath_text('/html/body/table')
	if table is None:
		tc.log.write('error', 'no table')
		tc.go(tc.url)
		continue

	company = table.split('\n')[0].split(': ')[1]
	subject_rf = table.split('\n')[5].split(': ')[2]
	try:
		city = table.split('\n')[6].split(': ')[1].split(', ')[2]
	except IndexError:
		city = ''

	phone = tc.get_xpath_text('/html/body/ul[2]/li[1]')
	if phone is None:
		phone = ''
		continue

	person = tc.get_xpath_text('/html/body/ul[5]/li[1]')
	if person is None:
		person = ''
	person_arr = person.split(' ')
	try:
		surname = person_arr[0]
	except IndexError:
		surname = ''
	try:
		name_f = person_arr[1]+' '+person_arr[2]
	except IndexError:
		name_f = ''
#	print 'company: %s, phone: %s, person: %s' % (company, phone, person)

	for name in [company, surname, name_f, phone, '', '', city, subject_rf]:
		toPrint += name+','

	toPrint = re.sub('\,$', '', toPrint)
	print toPrint
	tc.go(tc.url)

