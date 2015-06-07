#!/usr/bin/python

from PyQt4 import QtGui, QtCore
import gui
import sys
import os
import threading
import urllib.request
import threading
import json
import textwrap

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
		url = "http://www.espncricinfo.com/ci/engine/match/" + self.match_no + ".json"
		page = urllib.request.urlopen(url).read().decode("utf-8")
		page = json.loads(page)
		each_ball = page["comms"][0]["ball"][0]

		current_match = page["other_scores"]["international"][0]
		team2_score = page["live"]["innings"]["runs"] + "/"+ page["live"]["innings"]["wickets"] + ", " +page["live"]["innings"]["overs"]
		self.commentary = current_match["team1_name"] + "(" + current_match["team1_desc"]+ " )" +  " Vs " + current_match["team2_name"] + "( " + str(team2_score) + " )" + "\n"

		players = page["centre"]["batting"]
		player1 = players[0]
		player2 = players[1]

		self.commentary += ''.join((player1["known_as"], " - ", player1["runs"],'(', player1["balls_faced"] ,')')) + "\n"
		self.commentary += ''.join((player2["known_as"], " - ", player2["runs"],'(', player2["balls_faced"] ,')')) + "\n\n"
		temp = ''.join((each_ball["overs_actual"], " : ", each_ball['players'],',',each_ball['event'], ',', each_ball["text"]))
		temp = '\n'.join(textwrap.wrap(temp, 64))
		self.commentary += temp

		os.system("/opt/desktop-commentary/./script.sh" + " " + "\"" + self.commentary + "\"")
		threading.Timer(30, self.get_commentary).start()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	o = Score()
	sys.exit(app.exec_())
