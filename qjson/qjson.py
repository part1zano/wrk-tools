#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os,simplejson,codecs
from PyQt4 import QtGui,QtCore,uic

class MainWin(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)

		self.ui = uic.loadUi('ui/qjson.ui')
		self.ui.show()
		self.tabfields = []
		for index in range(self.ui.tabWidget.count()):
			text = unicode(self.ui.tabWidget.tabText(index)).lower()
			if 'link' in text:
				self.tabfields.append('by')
			elif 'control' in text:
				self.tabfields.append('type')
			elif 'error' in text:
				self.tabfields.append('ok')
			elif 'result' in text:
				self.tabfields.append('method')
				
		self.tray = QtGui.QSystemTrayIcon(self)
		self.trayMenu = QtGui.QMenu()
		self.trayIcon = QtGui.QIcon('imgs/Database-blue-48.png')

		self.action_quit = QtGui.QAction(QtGui.QIcon('imgs/Exit-48.png'), u'&Quit', self)
		self.action_quit.setShortcut('Ctrl+Q')
		self.action_showhide = QtGui.QAction(QtGui.QIcon('imgs/Metro-Viewer-Blue-256.png'), u'&Toggle visibility', self)
		self.action_open = QtGui.QAction(QtGui.QIcon('imgs/open_256.png'), u'&Open a file', self)
		self.action_open.setShortcut('Ctrl+O')

		self.trayMenu.addAction(self.action_showhide)
		self.trayMenu.addAction(self.action_open)
		self.trayMenu.addAction(self.action_quit)

		self.tray.setContextMenu(self.trayMenu)
		self.tray.setIcon(self.trayIcon)
		self.tray.show()

		self.check(self.ui.tabWidget.currentIndex())
		self.connect(self.ui.tabWidget, QtCore.SIGNAL('currentChanged(int)'), self.check)
		self.connect(self.ui.btnAdd, QtCore.SIGNAL('clicked()'), self.add_row)
		self.connect(self.ui.btnRemove, QtCore.SIGNAL('clicked()'), self.remove_row)
		self.connect(self.ui.btnWrite, QtCore.SIGNAL('clicked()'), self.write)
		self.ui.closeEvent = self.closeEvent
		self.connect(self.action_quit, QtCore.SIGNAL('triggered()'), self.quit)
		self.connect(self.action_showhide, QtCore.SIGNAL('triggered()'), self.toggleVisibility)
		self.connect(self.action_open, QtCore.SIGNAL('triggered()'), self.openJson)

	def openJson(self):
		filename = QtGui.QFileDialog.getOpenFileName()
		if filename == '':
			return False

		try:
			fh = codecs.open(filename, encoding='utf-8')
		except IOError:
			print '%s: no such file or directory' % filename
			return False

		dataStructure = simplejson.load(fh)
		fh.close()
		for field in self.tabfields:
			try:
				print dataStructure[0][field]
				key = self.tabfields.index(field)
				break
			except KeyError:
				continue

		self.clearTable()
		self.ui.tabWidget.setCurrentIndex(key)
		self.check(key)
		for index in range(len(dataStructure)):
			self.table.insertRow(index)
			for name, value in dataStructure[index].items():
				item = QtGui.QTableWidgetItem()
				item.setText(value)
				self.table.setItem(index, self.fields.index(name), item)
				

	def closeEvent(self, event):
		self.toggleVisibility()
		event.ignore()

	def clearTable(self):
		for rowIndex in range(self.table.rowCount()):
			self.table.removeRow(rowIndex)

	def quit(self):
		reply = QtGui.QMessageBox.question(self, 'Quit', 'Save before quit?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

		if reply == QtGui.QMessageBox.No:
			sys.exit(0)
		else:
			self.write()
			sys.exit(0)

	def toggleVisibility(self):
		self.ui.setVisible(not self.ui.isVisible())

	def check(self, int_):
		if 'Link' in self.ui.tabWidget.tabText(int_):
			self.table = self.ui.tableLink
			self.fields = ['link', 'url', 'by']
			self.defaults = ['', '', 'id']
		elif 'Control' in self.ui.tabWidget.tabText(int_):
			self.table = self.ui.tableControl
			self.fields = ['name', 'value', 'type', 'clear', 'submit']
			self.defaults = ['', '', 'text', '0', '0']
		elif 'Error' in self.ui.tabWidget.tabText(int_):
			self.table = self.ui.tableError
			self.fields = ['name', 'value', 'ok']
			self.defaults = ['', '', '0']
		elif 'Result' in self.ui.tabWidget.tabText(int_):
			self.table = self.ui.tableResult
			self.fields = ['name', 'value', 'method']
			self.defaults = ['', '', 'grep']
	
	def write(self):
		outfile = QtGui.QFileDialog.getSaveFileName()
		if unicode(outfile) == '':
			return False
		print outfile
		fh = codecs.open(outfile, mode='w+', encoding='utf-8')
		valList = []
		for rindex in range(self.table.rowCount()):
			val = {}
			for cindex in range(self.table.columnCount()):
				try:
					text = unicode(self.table.item(rindex, cindex).text()) 
					if text == '':
						text = self.defaults[cindex]
#					print self.table.item(rindex, cindex).text()
				except AttributeError:
					item = QtGui.QTableWidgetItem()
					item.setText(self.defaults[cindex])
					text = unicode(item.text())
					self.table.setItem(rindex, cindex, item)

				val[self.fields[cindex]] = text

			valList.append(val)

		fh.write(simplejson.dumps(valList))		
		fh.close()

	def add_row(self):
		self.table.insertRow(self.table.rowCount())
	
	def remove_row(self):
		self.table.removeRow(self.table.currentRow())


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	mw = MainWin()
	sys.exit(app.exec_())

