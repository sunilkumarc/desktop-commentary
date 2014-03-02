#!/usr/bin/python

from PyQt4 import QtGui, QtCore
import gui
import sys
import os
import threading
from bs4 import BeautifulSoup
from urllib3 import PoolManager
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
		m = PoolManager(10)
		html = m.request('GET', 'http://www.espncricinfo.com/netstorage/710301.html')
		soup = BeautifulSoup(html.data, "lxml")
		tab = soup.find("table", "commsTable")
		l = tab.findAll("p")
		comm = ""
		try:
		    
		    over = str(l[0]).split("<p class=\"commsText\">")[1].split("</p>")[0]
		    over = float(over)
		    comm = str(l[1]).split("<p class=\"commsText\">")[1].split("</p>")[0]
		    #comm = l.split("<p class=\"commsText\">")[1].split("</p>")[0]
		    try:
		        c = comm.split("<span class=\"commsImportant\">")
		        c1 = c[1].split("</span>")
		        comm = c[0] + c1[0] + c1[1]
		    except:
		        pass
		except:
		    comm = str(l)
		    try:
		        comm = comm.split("\">")[1].split("</p>")[0]
		    except:
		        temp = comm.split("\"")
		        comm = temp[0] + temp[1]

		string = comm.split('\n')
		comm = ""
		for line in string:
		    comm += line

		i = 1
		one_line = 50
		line_len = 50
		length = len(comm)
		while one_line < length:
		    comm = comm[:(i*line_len)] + '\n' + comm[(i*line_len):]
		    i += 1
		    one_line += line_len

		link = 'http://www.espncricinfo.com/ci/engine/match/710301.html'
		m = PoolManager(10)
		html = m.request('GET', link)
		source = str(html.data)
		page = source.split("<div class=\"topFrameTitle\">", 2)
		page2 = page[1].split("</div>")
		page3 = page2[0].split("data-text=\"")
		page4 = page3[1].split("\">Tweet")
		score = page4[0]
		split_scores = score.split(" v ")
		first_team = split_scores[0]
		second_team = split_scores[1]

		self.commentary = first_team + "\n" + second_team + "\n-------------------------------" +"\n" + comm
		os.system("/opt/desktop-commentary/./script.sh" + " " + "\"" + self.commentary + "\"")
		threading.Timer(30, self.get_commentary).start()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	o = Score()
	sys.exit(app.exec_())
