#!/usr/bin/python

from PyQt4 import QtGui, QtCore
import gui
import sys
import os
import threading
import urllib.request
import threading
import json

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
		self.match_no = strings[len(strings)-1:][0].split(".")[0]
		self.close()
		self.get_commentary()

	def get_commentary(self):
		url = "http://www.espncricinfo.com/netstorage/" + self.match_no +".json?xhr=1"
		page = urllib.request.urlopen(url).read().decode("utf-8")
		page = json.loads(page)
		each_ball = page["comms"][0]["ball"][0]
		self.commentary = ""
		self.commentary = "Ind(288/7, 48.4) Vs Sri(286/8, 50)" + '\n'
		players = page["centre"]["batting"]
		player1 = players[0]
		player2 = players[1]

		self.commentary += ''.join((player1["known_as"], " - ", player1["runs"],'(', player1["balls_faced"] ,')')) + "\n"
		self.commentary += ''.join((player2["known_as"], " - ", player2["runs"],'(', player2["balls_faced"] ,')')) + "\n"
		self.commentary += ''.join((each_ball["overs_actual"], " : ", each_ball['players'],',',each_ball['event'], ',', each_ball["text"]))

		os.system("/opt/desktop-commentary/./script.sh" + " " + "\"" + self.commentary + "\"")
		threading.Timer(30, self.get_commentary).start()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	o = Score()
	sys.exit(app.exec_())
