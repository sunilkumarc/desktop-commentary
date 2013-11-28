#!/usr/bin/env python2

from PyQt4 import QtGui, QtCore
import gui
import sys
import os
import threading
from bs4 import BeautifulSoup
from urllib2 import urlopen
import threading

class Score(QtGui.QMainWindow):
	link = ""
	def __init__(self):
		super(Score, self).__init__()
		QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
		self.ui = gui.Ui_Form()
		self.ui.setupUi(self)
		self.ui.start.clicked.connect(self.get_match_no)
		self.centerOnScreen()
		self.show()

	def centerOnScreen(self):
		resolution = QtGui.QDesktopWidget().screenGeometry()
		self.move((resolution.width() / 2) - (self.frameSize().width() / 2), (resolution.height() / 2) - (self.frameSize().height() / 2))

	def get_match_no(self):
		self.link = str(self.ui.scoreurl.toPlainText())
		self.link = self.link.split("\x00")[0]
		strings = self.link.split("/")
		self.match_no = strings[len(strings)-1:][0]
		self.close()
		self.get_commentary()

	def get_commentary(self):
		l = None
		try:
			link = "http://www.espncricinfo.com/netstorage/" + self.match_no
			html = urlopen(link).read()
			soup = BeautifulSoup(html, "lxml")
			tab = soup.find("table", "commsTable")
			l = tab.findAll("p")
		except:
			os.system("/opt/desktop-commentary/./error.sh" + " " + "\"" +"Unable to find commentary for the entered match" + "\"")
			sys.exit()

		res = str(l[0])
		try:
			num = res
			num = float(num.split("<p class=\"commsText\">")[1].split("</p>")[0])
			str2 = str(l[1])
			str2 = str2.split("<p class=\"commsText\">")[1].split("</p>")[0]
			temp = str2.split("<span class=\"commsImportant\">")
			str3 = None
			try:
				str3 = temp[1]
			except:
				pass
			temp2 = res.split("<p class=\"commsText\">")[1].split("</p>")[0]
			if str3:
				str3 = str3.split("</span>")
				self.commentary = temp2 + " - " + temp[0].split("\n")[0] + str3[0] + str3[1]
			else:
				str4 = str2.split("\n")
				str2 = ""
				for string in str4:
					str2 += string
				self.commentary = temp2 + " - " + str2
		except:
			self.commentary = res.split("<p class=\"commsText\">")[1].split("</p>")[0].split('\n')[1]

		os.system("/opt/desktop-commentary/./script.sh" + " " + "\"" + self.commentary + "\"")
		threading.Timer(10, self.get_commentary).start()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	o = Score()
	sys.exit(app.exec_())
