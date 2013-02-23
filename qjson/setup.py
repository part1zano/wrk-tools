from distutils.core import setup

setup(name='qjson',
		version='0.2',
		description='A small PyQt4 application for some json shit',
		author='Maxim Kirenenko',
		author_email='part1zancheg@gmail.com',
		url='http://ya.ru',
		py_modules=['qjcommon.myrandom', 'qjcommon.util'],
		scripts=['qjson.py'],
		data_files=[('share/qjson/imgs', ['imgs/button-cross.png', 'imgs/database.png', 'imgs/floppy-disk.png', 'imgs/folder.png', 'imgs/question.png', 'imgs/quit.png', 'imgs/search.png', 'imgs/toggle-collapse-alt.png', 'imgs/toggle-expand-alt.png']), ('share/qjson/ui', ['ui/qjson.ui'])]
		)

