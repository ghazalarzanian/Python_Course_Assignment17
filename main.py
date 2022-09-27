import random
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        loader=QUiLoader()
        self.ui=loader.load('tictactoe.ui',None)
        self.ui.show()
        self.game=[ [self.ui.btn_1,self.ui.btn_2,self.ui.btn_3],
                    [self.ui.btn_4,self.ui.btn_5,self.ui.btn_6],
                    [self.ui.btn_7,self.ui.btn_8,self.ui.btn_9]]
        self.draw=0
        self.player='O'
        self.player1=0
        self.player2=0
        self.you=0
        self.computer=0
        self.drawscore=0
        for i in range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.play,i,j))
                # self.game[i][j].setText(' ')
                # self.game[i][j].setStyleSheet('color:yellow;background-color:red')
        self.ui.btn_restart.clicked.connect(partial(self.newgame))
        self.ui.btn_help.clicked.connect(partial(self.help))
    def play(self,i,j):
        if self.game[i][j].text()=='':
            self.draw+=1
            if self.player=='X':
                self.game[i][j].setText('X')
                self.game[i][j].setStyleSheet('color:black;background-color:white')
                self.player='O'
            else :
                self.game[i][j].setText('O')
                self.game[i][j].setStyleSheet('color:white;background-color:black')
                self.player='X'                 
                if self.ui.radio_computer.isChecked() and self.draw<8:
                    if self.player=='X':
                        self.draw+=1
                        while True:
                            row = random.randint(0,2)
                            col = random.randint(0,2)
                            if self.game[row][col].text()=='':
                                self.game[row][col].setText('X')
                                self.game[row][col].setStyleSheet('color:black;background-color:white')
                                self.player='O'
                                break
        self.check()
    def check(self):
        if self.game[0][0].text()=='X' and self.game[0][1].text()=='X' and self.game[0][2].text()=='X':
            msgBox = QMessageBox()
            msgBox.setText("player 1 Wins")
            msgBox.exec()
            self.newgame()
            self.score(1)
        elif self.game[0][0].text()=='O' and self.game[0][1].text()=='O' and self.game[0][2].text()=='O':
            msgBox = QMessageBox()
            msgBox.setText("player 2 Wins")
            msgBox.exec()
            self.newgame()
            self.score(2)
        elif self.game[1][0].text()=='X' and self.game[1][1].text()=='X' and self.game[1][2].text()=='X':
            msgBox = QMessageBox()
            msgBox.setText("player 1 Wins")
            msgBox.exec()
            self.newgame()
            self.score(1)
        elif self.game[1][0].text()=='O' and self.game[1][1].text()=='O' and self.game[1][2].text()=='O':
            msgBox = QMessageBox()
            msgBox.setText("player 2 Wins")
            msgBox.exec()
            self.newgame()
            self.score(2)
        elif self.game[2][0].text()=='X' and self.game[2][1].text()=='X' and self.game[2][2].text()=='X':
            msgBox = QMessageBox()
            msgBox.setText("player 1 Wins")
            msgBox.exec()
            self.newgame()
            self.score(1)
        elif self.game[2][0].text()=='O' and self.game[2][1].text()=='O' and self.game[2][2].text()=='O':
            msgBox = QMessageBox()
            msgBox.setText("player 2 Wins")
            msgBox.exec()
            self.newgame()
            self.score(2)
        elif self.game[0][0].text()=='X' and self.game[1][0].text()=='X' and self.game[2][0].text()=='X':
            msgBox = QMessageBox()
            msgBox.setText("player 1 Wins")
            msgBox.exec()
            self.newgame()
            self.score(1)
        elif self.game[0][0].text()=='O' and self.game[1][0].text()=='O' and self.game[2][0].text()=='O':
            msgBox = QMessageBox()
            msgBox.setText("player 2 Wins")
            msgBox.exec()
            self.newgame()
            self.score(2)
        elif self.game[0][1].text()=='X' and self.game[1][1].text()=='X' and self.game[2][1].text()=='X':
            msgBox = QMessageBox()
            msgBox.setText("player 1 Wins")
            msgBox.exec()
            self.newgame()
            self.score(1)
        elif self.game[0][1].text()=='O' and self.game[1][1].text()=='O' and self.game[2][1].text()=='O':
            msgBox = QMessageBox()
            msgBox.setText("player 2 Wins")
            msgBox.exec()
            self.newgame()
            self.score(2)
        elif self.game[0][2].text()=='X' and self.game[1][2].text()=='X' and self.game[2][2].text()=='X':
            msgBox = QMessageBox()
            msgBox.setText("player 1 Wins")
            msgBox.exec()
            self.newgame()
            self.score(1)
        elif self.game[0][2].text()=='O' and self.game[1][2].text()=='O' and self.game[2][2].text()=='O':
            msgBox = QMessageBox()
            msgBox.setText("player 2 Wins")
            msgBox.exec()
            self.newgame()
            self.score(2)
        elif self.game[0][0].text()=='X' and self.game[1][1].text()=='X' and self.game[2][2].text()=='X':
            msgBox = QMessageBox()
            msgBox.setText("player 1 Wins")
            msgBox.exec()
            self.newgame()
            self.score(1)
        elif self.game[0][0].text()=='O' and self.game[1][1].text()=='O' and self.game[2][2].text()=='O':
            msgBox = QMessageBox()
            msgBox.setText("player 2 Wins")
            msgBox.exec()
            self.newgame()
            self.score(2)
        elif self.game[0][2].text()=='X' and self.game[1][1].text()=='X' and self.game[2][0].text()=='X':
            msgBox = QMessageBox()
            msgBox.setText("player 1 Wins")
            msgBox.exec()
            self.newgame()
            self.score(1)
        elif self.game[0][2].text()=='O' and self.game[1][1].text()=='O' and self.game[2][0].text()=='O':
            msgBox = QMessageBox()
            msgBox.setText("player 2 Wins")
            msgBox.exec()
            self.newgame()
            self.score(2)
        else:
            if self.draw>8:
                msgBox = QMessageBox()
                msgBox.setText("Draw")
                msgBox.exec()
                self.newgame()
                self.score('draw')
    def score(self,player):
        if self.ui.radio_computer.isChecked():
            if player==1:
                self.computer+=1
                self.ui.btn_computer.setText('Computer:'+str(self.computer))
            elif player==2:
                self.you+=1
                self.ui.btn_you.setText('You:'+str(self.you))
        else:
            if player==1:
                self.player1+=1
                self.ui.btn_player1.setText('Player1:'+str(self.player1))
            elif player==2:
                self.player2+=1
                self.ui.btn_player2.setText('Player2:'+str(self.player2))
            elif player=='draw':
                self.drawscore+=1
                self.ui.btn_draw.setText('Draw:'+str(self.drawscore))
    def newgame(self):
        self.draw=0
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('background-color:lightblue')
        self.player='O'
    def help(self):
            msgBox = QMessageBox()
            msgBox.setText('If you want to play with a partner choose radio button 2 play \n If you want to play with computer choose radio button play with computer \n \n Designed by Ghazal Arzanian \n 2022')
            msgBox.exec()
#yek App va Chnta Win mitounim dashte bashim
app=QApplication([])
window=TicTacToe()
app.exec_()