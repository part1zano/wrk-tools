# -*- coding: utf-8 -*-
import sys,re,random,datetime

phrases = [
['The', 'Le', 'Our', 'Their', 'This', 'My', 'Your', 'That', 'Obvious', 'Hilarious', 'Slutty'],
['quick', 'slow', 'crazy', 'sane', 'lazy', 'hard-working', 'telepathic', 'pathetic', 'apathetic', 'weird', 'unnamed'],
['fox', 'dog', 'plane', 'pencil', 'drawer', 'roll', 'dice', 'mother', 'son', 'father', 'daughter'],
['is', 'gets', 'likes', 'fakes', 'loves', 'hates', 'dislikes', 'can in', 'cannot in', 'flames', 'changes'],
['cake', 'love', 'god', 'math', 'physics', 'orgasm', 'mud', 'dirt', 'bitches', 'whores', 'sluts'],
['in', 'inside of', 'outside of', 'by', 'at', 'near', 'before', 'after', 'before', 'near', 'at'],
['plague', 'shadow', 'shade', 'the dark', 'the box', 'bed', 'shower', 'work', 'town', 'city', 'village']
]

locations = [
		[u'Западный', u'Восточный', u'Юго-восточный', u'Юго-западный', u'Северный', u'Южный', u'Северо-западный', u'Северо-восточный'],
		[u'Север', u'Юг', u'Запад', u'Восток', u'Северо-запад', u'Северо-восток', u'Юго-запад', u'Юго-восток']
		]

departments = [u'R&D', u'SWD', u'Research', u'Development', u'Департамент развития', u'Космодром', u'Ракетодром', u'Жопа мира']

streets = [u'проспект Проституток', u'улица Чёрны-Тян', u'площадь Наркозависимости', u'переулок Чикатило', u'Космодесантный проспект', u'улица Дарта Вейдера', u'Зиговский проезд', u'Штирлиц-авеню']

alphabet = 'qwertyuiopasdfghjklzxcvbnm'

def random_location():
	location = ''
	for row in locations:
		location += row[random.randint(0, len(row)-1)]+' '
	
	return location.rstrip()

def random_year(start='1900', end=datetime.date.today().strftime('%Y')):
	return str(random.randint(int(start), int(end)))

def random_office(city=None):
	if city is None:
		city = random_location()

	return departments[random.randint(0, len(departments)-1)]+' '+city

def random_address(city=None, max_house=99):
	if city is None:
		city = random_location()

	return city+', '+streets[random.randint(0, len(streets)-1)]+', '+str(random.randint(1, max_house))

def random_login(words=3, separator='_'):
	login = ''
	for i in range(words):
		index = random.randint(1, len(phrases)-1)
		login += re.sub(' ', separator, phrases[index][random.randint(0, len(phrases[index])-1)])+separator

	login = re.sub(separator+'$', '', login)
	
	return login

def random_phone():
	country_code = '+7' # FIXME :: hardcode
	city_code = '812' # FIXME :: hardcode
	number = country_code+' '+city_code+' ' # FIXME :: separator hardcode
	for i in range(7): # FIXME :: hardcode
		number += str(random.randint(0, 9))
		
		if i in (2, 4):
			number += ' ' # FIXME :: separator hardcode

	return number


def random_1lvl_domain(length=2):
	domain = ''
	for i in range(length):
		domain += alphabet[random.randint(0, len(alphabet)-1)]
	
	return domain

def random_domain(lvl=2, lvl1_length=2):
	domain = ''
	for i in range(lvl-1):
		index = random.randint(1, len(phrases)-1)
		domain += re.sub(' ', '-', phrases[index][random.randint(0, len(phrases[index])-1)])+'.'

	domain += random_1lvl_domain(lvl1_length)
	return domain

def random_email(login_len=3, login_separator='_', domain_lvl=2, lvl1_length=2):
	return random_login(login_len, login_separator)+'@'+random_domain(domain_lvl, lvl1_length)

def random_phrase(length = len(phrases)):
	phrase = ''
	for index in range(length):
		rnd_2 = random.randint(0, len(phrases[index])-1)
		phrase += ' '+phrases[index][random.randint(0, rnd_2)]

	return phrase.strip()

def random_num(length):
	number = ''
	for index in range(length):
		number += str(random.randint(0, 9))

	return int(number)

def coin():
	return bool(random.randint(0,9) % 2)
