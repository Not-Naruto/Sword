from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pickle
import random
import time

class Ui_Pregame(object):
    global Main
    global Pregame
    def setupUi(self, Pregame):
        Pregame.setObjectName("Pregame")
        Pregame.resize(219, 268)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/title_screen/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pregame.setWindowIcon(icon)
        self.label_2 = QtWidgets.QLabel(Pregame)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 187, 58))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Pregame)
        self.label.setGeometry(QtCore.QRect(49, 10, 131, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.newgame = QtWidgets.QPushButton(Pregame)
        self.newgame.setGeometry(QtCore.QRect(60, 100, 101, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.newgame.setPalette(palette)
        self.newgame.setObjectName("newgame")
        self.continue_2 = QtWidgets.QPushButton(Pregame)
        self.continue_2.setGeometry(QtCore.QRect(60, 140, 101, 31))
        self.continue_2.setObjectName("continue_2")
        self.exit = QtWidgets.QPushButton(Pregame)
        self.exit.setGeometry(QtCore.QRect(60, 180, 101, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.exit.setPalette(palette)
        self.exit.setObjectName("exit")
        self.label_3 = QtWidgets.QLabel(Pregame)
        self.label_3.setGeometry(QtCore.QRect(-10, -8, 231, 281))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/title_screen/img/title.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.newgame.raise_()
        self.continue_2.raise_()
        self.exit.raise_()

        self.retranslateUi(Pregame)
        QtCore.QMetaObject.connectSlotsByName(Pregame)

        self.newgame.clicked.connect(self.new)
        self.continue_2.clicked.connect(self.cont)
        self.exit.clicked.connect(self.ex)
    
    def new(self):
        global map_variable
        with open('profile.dat','wb') as f:
            x={'health':100,'maxh':100, 'level':1, 'pot':5,'coins':100, 'atk':40, 'def':10}
            pickle.dump(x,f)
        with open('maps.dat','rb') as f:
            map_variable=pickle.load(f)
   
        Main.show()
        Pregame.close() 

    def cont(self):
        Main.show()
        Pregame.close()

    def ex(self):
        Pregame.close()
        pass

    def retranslateUi(self, Pregame):
        _translate = QtCore.QCoreApplication.translate
        Pregame.setWindowTitle(_translate("Pregame", "Sword"))
        self.label_2.setText(_translate("Pregame", "SWORD"))
        self.label.setText(_translate("Pregame", "Welcome to"))
        self.newgame.setText(_translate("Pregame", "New Game"))
        self.continue_2.setText(_translate("Pregame", "Continue"))
        self.exit.setText(_translate("Pregame", "Exit"))


class Ui_Main(object):
    global shop
    global ui2
    global battlewindow
    
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(660, 516)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Main.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/title_screen/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 220, 221, 221))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame_2.setPalette(palette)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.bexit = QtWidgets.QPushButton(self.frame_2)
        self.bexit.setGeometry(QtCore.QRect(10, 180, 201, 23))
        self.bexit.setObjectName("bexit")
        self.bshop = QtWidgets.QPushButton(self.frame_2)
        self.bshop.setGeometry(QtCore.QRect(10, 120, 201, 23))
        self.bshop.setObjectName("bshop")
        self.bheal = QtWidgets.QPushButton(self.frame_2)
        self.bheal.setGeometry(QtCore.QRect(10, 150, 201, 23))
        self.bheal.setObjectName("bheal")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(0, 10, 221, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.frame.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bup = QtWidgets.QPushButton(self.frame)
        self.bup.setGeometry(QtCore.QRect(80, 10, 61, 41))
        self.bup.setObjectName("bup")
        self.bdown = QtWidgets.QPushButton(self.frame)
        self.bdown.setGeometry(QtCore.QRect(80, 60, 61, 41))
        self.bdown.setObjectName("bdown")
        self.bright = QtWidgets.QPushButton(self.frame)
        self.bright.setGeometry(QtCore.QRect(150, 60, 61, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 104, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 104, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 104, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.bright.setPalette(palette)
        self.bright.setObjectName("bright")
        self.bleft = QtWidgets.QPushButton(self.frame)
        self.bleft.setGeometry(QtCore.QRect(10, 60, 61, 41))
        self.bleft.setObjectName("bleft")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 190, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 30, 221, 148))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lhealth = QtWidgets.QLabel(self.frame_3)
        self.lhealth.setObjectName("lhealth")
        self.verticalLayout.addWidget(self.lhealth)
        self.llevel = QtWidgets.QLabel(self.frame_3)
        self.llevel.setObjectName("llevel")
        self.verticalLayout.addWidget(self.llevel)
        self.lpotions = QtWidgets.QLabel(self.frame_3)
        self.lpotions.setObjectName("lpotions")
        self.verticalLayout.addWidget(self.lpotions)
        self.lcoins = QtWidgets.QLabel(self.frame_3)
        self.lcoins.setObjectName("lcoins")
        self.verticalLayout.addWidget(self.lcoins)
        self.lATK = QtWidgets.QLabel(self.frame_3)
        self.lATK.setObjectName("lATK")
        self.verticalLayout.addWidget(self.lATK)
        self.lDEF = QtWidgets.QLabel(self.frame_3)
        self.lDEF.setObjectName("lDEF")
        self.verticalLayout.addWidget(self.lDEF)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(260, 30, 381, 411))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.mappic = QtWidgets.QLabel(self.frame_4)
        self.mappic.setGeometry(QtCore.QRect(10, 10, 361, 391))
        self.mappic.setText("")
        self.mappic.setPixmap(QtGui.QPixmap(":/maps/img/levelmaps/Level 1.png"))
        self.mappic.setScaledContents(True)
        self.mappic.setObjectName("mappic")
        self.plr = QtWidgets.QLabel(self.frame_4)
        self.plr.setGeometry(QtCore.QRect(30, 330, 41, 41)) #30-increments of 70,330-decrements of 74,41,41   x,y,width,height
        self.plr.setText("")
        self.plr.setPixmap(QtGui.QPixmap(":/maps/img/plr.png"))
        self.plr.setScaledContents(True)
        self.plr.setObjectName("plr")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 10, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 450, 631, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(75)
        self.status.setFont(font)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.status.setPalette(palette)
        self.status.setText("")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

        self.update()

        self.bshop.clicked.connect(self.open_shop)
        self.bexit.clicked.connect(self.ex)
        self.bheal.clicked.connect(self.heal)
        self.bright.clicked.connect(self.move_right)
        self.bleft.clicked.connect(self.move_left)
        self.bup.clicked.connect(self.move_up)
        self.bdown.clicked.connect(self.move_down)
        
    def move_right(self):
        global posx
        global posy
        global map_variable
        global ui2
        position = map_variable[posy][posx]
        if position[1]==1:
            posx+=1
            self.plr.setGeometry(QtCore.QRect(30+70*posx, 330-74*(4-posy), 41, 41))
            position = map_variable[posy][posx]
            if position[0]=='Win':
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                self.status.setPalette(palette)
                self.status.setText('Level Completed')
                posx,posy=0,4
                self.plr.setGeometry(QtCore.QRect(30+70*posx, 330-74*(4-posy), 41, 41))
                with open('profile.dat','rb') as f:
                    a=pickle.load(f)
                    lvl=a['level']
                if lvl==5:
                    msg = QMessageBox()
                    msg.setWindowTitle('Game Complete')
                    msg.setText('Thanks for Playing')
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    #msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText('Data will now be reset')
                    x = msg.exec_()
                    with open('profile.dat','wb') as f:
                        x={'health':100,'maxh':100, 'level':1, 'pot':5,'coins':100, 'atk':40, 'def':10}
                        pickle.dump(x,f)
                    with open('maps.dat','rb') as f:
                        map_variable=pickle.load(f)
                    
                else:
                    lvl+=1
                    with open('maps.dat','rb') as f:
                        for i in range(lvl):
                            map_variable=pickle.load(f)
                    with open('profile.dat','rb') as f:
                        a=pickle.load(f)
                    with open('profile.dat','wb') as f:
                        pickle.dump({'health':a['health']+20,'maxh':a['maxh']+20, 'level':a['level']+1, 'pot':a['pot'],'coins':a['coins'], 'atk':a['atk'], 'def':a['def']},f)
                    msg = QMessageBox()
                    msg.setWindowTitle('Level Complete')
                    msg.setText('You have completed the Level')
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    #msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText('Hit Ok to continue on to the next level')
                    x = msg.exec_()
            else:
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                self.status.setPalette(palette)
                self.status.setText('You Moved 1 tile right')
                with open('profile.dat','rb') as f:
                    a=pickle.load(f)
                    lvl=a['level']
                enemy_chance=15+7*lvl
                if random.randint(1,101)<enemy_chance:
                    self.battle()
        else:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            self.status.setPalette(palette)
            self.status.setText('You face a wall')

    def move_left(self):
        global posx
        global posy
        global map_variable
        position = map_variable[posy][posx]
        if position[3]==1:
            posx-=1
            self.plr.setGeometry(QtCore.QRect(30+70*posx, 330-74*(4-posy), 41, 41))
            position = map_variable[posy][posx]
            if position[0]=='Win':
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                self.status.setPalette(palette)
                self.status.setText('Level Completed')
                posx,posy=0,4
                self.plr.setGeometry(QtCore.QRect(30+70*posx, 330-74*(4-posy), 41, 41))
                with open('profile.dat','rb') as f:
                    a=pickle.load(f)
                    lvl=a['level']
                if lvl==5:
                    msg = QMessageBox()
                    msg.setWindowTitle('Game Complete')
                    msg.setText('Thanks for Playing')
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    #msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText('Data will now be reset')
                    x = msg.exec_()
                    with open('profile.dat','wb') as f:
                        x={'health':100,'maxh':100, 'level':1, 'pot':5,'coins':100, 'atk':40, 'def':10}
                        pickle.dump(x,f)
                    with open('maps.dat','rb') as f:
                        map_variable=pickle.load(f)
                else:
                    lvl+=1
                    with open('maps.dat','rb') as f:
                        for i in range(lvl):
                            map_variable=pickle.load(f)
                    with open('profile.dat','rb') as f:
                        a=pickle.load(f)
                    with open('profile.dat','wb') as f:
                        pickle.dump({'health':a['health']+20,'maxh':a['maxh']+20, 'level':a['level']+1, 'pot':a['pot'],'coins':a['coins'], 'atk':a['atk'], 'def':a['def']},f)
                    msg = QMessageBox()
                    msg.setWindowTitle('Level Complete')
                    msg.setText('You have completed the Level')
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    #msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText('Hit Ok to continue on to the next level')
                    x = msg.exec_()
            else:
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                self.status.setPalette(palette)
                self.status.setText('You Moved 1 tile left')
                #battle
                with open('profile.dat','rb') as f:
                    a=pickle.load(f)
                    lvl=a['level']
                enemy_chance=15+7*lvl
                if random.randint(1,101)<enemy_chance:
                    self.battle()
        else:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            self.status.setPalette(palette)
            self.status.setText('You face a wall')

    def move_up(self):
        global posx
        global posy
        global map_variable
        position = map_variable[posy][posx]
        if position[0]==1:
            posy-=1
            self.plr.setGeometry(QtCore.QRect(30+70*posx, 330-74*(4-posy), 41, 41))
            position = map_variable[posy][posx]
            if position[0]=='Win':
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                self.status.setPalette(palette)
                self.status.setText('Level Completed')
                posx,posy=0,4
                self.plr.setGeometry(QtCore.QRect(30+70*posx, 330-74*(4-posy), 41, 41))
                with open('profile.dat','rb') as f:
                    a=pickle.load(f)
                    lvl=a['level']
                if lvl==5:
                    msg = QMessageBox()
                    msg.setWindowTitle('Game Complete')
                    msg.setText('Thanks for Playing')
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    #msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText('Data will now be reset')
                    x = msg.exec_()
                    with open('profile.dat','wb') as f:
                        x={'health':100,'maxh':100, 'level':1, 'pot':5,'coins':100, 'atk':40, 'def':10}
                        pickle.dump(x,f)
                    with open('maps.dat','rb') as f:
                        map_variable=pickle.load(f)
                else:
                    lvl+=1
                    with open('maps.dat','rb') as f:
                        for i in range(lvl):
                            map_variable=pickle.load(f)
                    with open('profile.dat','rb') as f:
                        a=pickle.load(f)
                    with open('profile.dat','wb') as f:
                        pickle.dump({'health':a['health']+20,'maxh':a['maxh']+20, 'level':a['level']+1, 'pot':a['pot'],'coins':a['coins'], 'atk':a['atk'], 'def':a['def']},f)
                    msg = QMessageBox()
                    msg.setWindowTitle('Level Complete')
                    msg.setText('You have completed the Level')
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    #msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText('Hit Ok to continue on to the next level')
                    x = msg.exec_()
            else:
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                self.status.setPalette(palette)
                self.status.setText('You Moved 1 tile up')
                with open('profile.dat','rb') as f:
                    a=pickle.load(f)
                    lvl=a['level']
                enemy_chance=15+7*lvl
                if random.randint(1,101)<enemy_chance:
                    self.battle()
        else:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            self.status.setPalette(palette)
            self.status.setText('You face a wall')

    def move_down(self):
        global posx
        global posy
        global map_variable
        position = map_variable[posy][posx]
        if position[2]==1:
            posy+=1
            self.plr.setGeometry(QtCore.QRect(30+70*posx, 330-74*(4-posy), 41, 41))
            position = map_variable[posy][posx]
            if position[0]=='Win':
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                self.status.setPalette(palette)
                self.status.setText('Level Completed')
                posx,posy=0,4
                self.plr.setGeometry(QtCore.QRect(30+70*posx, 330-74*(4-posy), 41, 41))
                with open('profile.dat','rb') as f:
                    a=pickle.load(f)
                    lvl=a['level']
                if lvl==5:
                    msg = QMessageBox()
                    msg.setWindowTitle('Game Complete')
                    msg.setText('Thanks for Playing')
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    #msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText('Data will now be reset')
                    x = msg.exec_()
                    with open('profile.dat','wb') as f:
                        x={'health':100,'maxh':100, 'level':1, 'pot':5,'coins':100, 'atk':40, 'def':10}
                        pickle.dump(x,f)
                    with open('maps.dat','rb') as f:
                        map_variable=pickle.load(f)
                else:
                    lvl+=1
                    with open('maps.dat','rb') as f:
                        for i in range(lvl):
                            map_variable=pickle.load(f)
                    with open('profile.dat','rb') as f:
                        a=pickle.load(f)
                    with open('profile.dat','wb') as f:
                        pickle.dump({'health':a['health']+20,'maxh':a['maxh']+20, 'level':a['level']+1, 'pot':a['pot'],'coins':a['coins'], 'atk':a['atk'], 'def':a['def']},f)
                    msg = QMessageBox()
                    msg.setWindowTitle('Level Complete')
                    msg.setText('You have completed the Level')
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    #msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText('Hit Ok to continue on to the next level')
                    x = msg.exec_()
            else:
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                self.status.setPalette(palette)
                self.status.setText('You Moved 1 tile down')
                with open('profile.dat','rb') as f:
                    a=pickle.load(f)
                    lvl=a['level']
                enemy_chance=15+7*lvl
                if random.randint(1,101)<enemy_chance:
                    self.battle()
        else:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            self.status.setPalette(palette)
            self.status.setText('You face a wall')


    def open_shop(self):
        self.status.setText('')
        Main.hide()
        ui2.updatecoins()
        ui2.check()
        shop.show()

    def heal(self):
        with open('profile.dat','rb') as f:
            a=pickle.load(f)
            health=a['health']
            pot=a['pot']
            maxh=a['maxh']
        if health==maxh:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            self.status.setPalette(palette)
            self.status.setText('Health Already Maxed Out')
        elif health<maxh:
            if pot>=1:
                with open('profile.dat','wb') as f:
                    x={'health':maxh, 'maxh':a['maxh'], 'level':a['level'], 'pot':pot-1, 'coins':a['coins'], 'atk':a['atk'], 'def':a['def']}
                    pickle.dump(x,f)
                    palette = QtGui.QPalette()
                    brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                    brush = QtGui.QBrush(QtGui.QColor(71, 214, 0))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                    brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                    self.status.setPalette(palette)
                    self.status.setText('Health Maxed Out')
            else:
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
                self.status.setPalette(palette)
                self.status.setText('Not Enough Potions')

    def ex(self):
        Main.close() 
    
    def update(self):
        global x
        global y
        with open('profile.dat','rb') as f:
            a=pickle.load(f)
            self.lhealth.setText('Health: '+str(a['health'])+'/'+str(a['maxh']))
            self.llevel.setText('Level: '+str(a['level']))
            self.lpotions.setText('Potions: '+str(a['pot']))
            self.lcoins.setText('Coins: '+str(a['coins']))
            self.lATK.setText('ATK: '+str(a['atk']))
            self.lDEF.setText('DEF: '+str(a['def']))
        lvl=a['level']
        map_pics=[":/maps/img/levelmaps/Level 1.png",":/maps/img/levelmaps/Level 2.png",":/maps/img/levelmaps/Level 3.png",":/maps/img/levelmaps/Level 4.png",":/maps/img/levelmaps/Level 5.png"]
        mp=map_pics[lvl-1]
        self.mappic.setPixmap(QtGui.QPixmap(mp))
        self.plr.setGeometry(QtCore.QRect(30+70*posx, 330-74*(4-posy), 41, 41))

    def battle(self):
        global ui3
        self.status.setText('')
        ui3.label_6.setText('')
        Main.hide()
        battlewindow.show()
        with open('profile.dat','rb') as f:
            lvl=pickle.load(f)['level']
        if lvl<=3:
            a=random.choice([1,2,3])
        else:
            a=random.choice([4,5])
        ui3.choose_enemy(a)


    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Sword"))
        self.bexit.setText(_translate("Main", "Exit"))
        self.bshop.setText(_translate("Main", "Shop"))
        self.bheal.setText(_translate("Main", "Heal"))
        self.bup.setText(_translate("Main", "UP"))
        self.bdown.setText(_translate("Main", "DOWN"))
        self.bright.setText(_translate("Main", "RIGHT"))
        self.bleft.setText(_translate("Main", "LEFT"))
        self.label.setText(_translate("Main", "Controls"))
        self.lhealth.setText(_translate("Main", "Health:"))
        self.llevel.setText(_translate("Main", "Level:"))
        self.lpotions.setText(_translate("Main", "Potions:"))
        self.lcoins.setText(_translate("Main", "Coins:"))
        self.lATK.setText(_translate("Main", "ATK:"))
        self.lDEF.setText(_translate("Main", "DEF:"))
        self.label_2.setText(_translate("Main", "Profile"))
        self.label_9.setText(_translate("Main", "Map"))

class Ui_shop(object):
    global Main
    def setupUi(self, shop):
        shop.setObjectName("shop")
        shop.resize(221, 234)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/title_screen/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        shop.setWindowIcon(icon)
        self.lineEdit = QtWidgets.QLineEdit(shop)
        self.lineEdit.setGeometry(QtCore.QRect(20, 45, 81, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(shop)
        self.pushButton.setGeometry(QtCore.QRect(110, 45, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(shop)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 85, 181, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(shop)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 125, 181, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(shop)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.status_text = QtWidgets.QLabel(shop)
        self.status_text.setGeometry(QtCore.QRect(20, 160, 181, 20))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)

        palette2 = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)

        self.status_text.setPalette(palette)
        self.status_text.setText("")
        self.status_text.setAlignment(QtCore.Qt.AlignCenter)
        self.status_text.setObjectName("status_text")
        self.back = QtWidgets.QPushButton(shop)
        self.back.setGeometry(QtCore.QRect(130, 190, 75, 23))
        self.back.setObjectName("back")
        self.lcoins = QtWidgets.QLabel(shop)
        self.lcoins.setGeometry(QtCore.QRect(20, 190, 91, 21))
        self.lcoins.setObjectName("lcoins")

        self.retranslateUi(shop)
        QtCore.QMetaObject.connectSlotsByName(shop)

        self.pushButton.clicked.connect(self.buy_potions)
        self.pushButton_2.clicked.connect(self.buy_sword)
        self.pushButton_3.clicked.connect(self.buy_armor)
        self.back.clicked.connect(self.go_back)

    def buy_potions(self):
        try:
            amt=int(self.lineEdit.text())
            coins_required=amt*10
            with open('profile.dat','rb') as f:
                a=pickle.load(f)
                coins=a['coins']
                pot=a['pot']
            if coins_required<=coins:
                with open('profile.dat','wb') as f:
                    x={'health':a['health'], 'maxh':a['maxh'], 'level':a['level'], 'pot':pot+amt, 'coins':coins-coins_required, 'atk':a['atk'], 'def':a['def']}
                    pickle.dump(x,f)
                palette2 = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
                self.status_text.setPalette(palette2)
                self.status_text.setText('Potions purchased')
                self.updatecoins()
            else:
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
                self.status_text.setPalette(palette)
                self.status_text.setText('Not Enough Coins')
        except:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            self.status_text.setPalette(palette)
            self.status_text.setText('Invalid Input')
        
    
    def buy_armor(self):
        with open('profile.dat','rb') as f:
            a=pickle.load(f)
            coins=a['coins']
        if coins>=250:
            with open('profile.dat','wb') as f:
                x={'health':a['health'], 'maxh':a['maxh'], 'level':a['level'], 'pot':a['pot'], 'coins':coins-250, 'atk':a['atk'], 'def':50}
                pickle.dump(x,f)
            palette2 = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            self.status_text.setPalette(palette2)
            self.status_text.setText('Better Armor Purchased')
            self.check()
            self.updatecoins()
        else:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            self.status_text.setPalette(palette)
            self.status_text.setText('Not Enough Coins')

    def buy_sword(self):
        with open('profile.dat','rb') as f:
            a=pickle.load(f)
            coins=a['coins']
        if coins>=250:
            with open('profile.dat','wb') as f:
                x={'health':a['health'], 'maxh':a['maxh'], 'level':a['level'], 'pot':a['pot'], 'coins':coins-250, 'atk':70, 'def':a['def']}
                pickle.dump(x,f)
            palette2 = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            self.status_text.setPalette(palette2)
            self.status_text.setText('Better Sword Purchased')
            self.check()
            self.updatecoins()
        else:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            self.status_text.setPalette(palette)
            self.status_text.setText('Not Enough Coins')

    def go_back(self):
        self.status_text.setText('')
        shop.close()
        Main.show()

    def check(self):
        with open('profile.dat','rb') as f:
            a=pickle.load(f)
            if a['atk']==70:
                self.pushButton_2.setDisabled(True)
            else:
                self.pushButton_2.setDisabled(False)
            if a['def']==50:
                self.pushButton_3.setDisabled(True)
            else:
                self.pushButton_3.setDisabled(False)

    def updatecoins(self):
        with open('profile.dat','rb') as f:
            a=pickle.load(f)
            self.lcoins.setText('Coins: '+str(a['coins']))

    def retranslateUi(self, shop):
        _translate = QtCore.QCoreApplication.translate
        shop.setWindowTitle(_translate("shop", "Shop"))
        self.lineEdit.setText(_translate("shop", "1"))
        self.pushButton.setText(_translate("shop", "Potions [10 c]"))
        self.pushButton_2.setText(_translate("shop", "Better Sword (70 ATK) [250 c]"))
        self.pushButton_3.setText(_translate("shop", "Better Armor (50 DEF) [250 c]"))
        self.label.setText(_translate("shop", "Shop"))
        self.back.setText(_translate('shop','Back'))
        self.lcoins.setText(_translate("shop", "Coins: "))

class Ui_battlewindow(object):
    def setupUi(self, battlewindow):
        battlewindow.setObjectName("battlewindow")
        battlewindow.resize(252, 323)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/title_screen/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        battlewindow.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(battlewindow)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/enemies/img/enemies/ghost.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(battlewindow)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(battlewindow)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(battlewindow)
        self.label_4.setGeometry(QtCore.QRect(140, 200, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(battlewindow)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(battlewindow)
        self.pushButton.setGeometry(QtCore.QRect(10, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(battlewindow)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(battlewindow)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 260, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(battlewindow)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 231, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")

        self.pushButton.clicked.connect(self.attack)
        self.pushButton_2.clicked.connect(self.heal)
        self.pushButton_3.clicked.connect(self.flee)

        self.retranslateUi(battlewindow)
        QtCore.QMetaObject.connectSlotsByName(battlewindow)
        

    def retranslateUi(self, battlewindow):
        _translate = QtCore.QCoreApplication.translate
        battlewindow.setWindowTitle(_translate("battlewindow", "Battle"))
        self.label_2.setText(_translate("battlewindow", "You face a "))
        self.label_3.setText(_translate("battlewindow", "Player:"))
        self.label_4.setText(_translate("battlewindow", "Enemy:"))
        self.label_5.setText(_translate("battlewindow", "Potions:"))
        self.pushButton.setText(_translate("battlewindow", "Attack"))
        self.pushButton_2.setText(_translate("battlewindow", "Heal"))
        self.pushButton_3.setText(_translate("battlewindow", "Flee"))
        self.label_6.setText(_translate("battlewindow", "Status"))
    
    def attack(self):
        global ui
        with open('profile.dat', 'rb') as f:
            l=pickle.load(f)
        player_health = l['health']
        dmg_delt = l['atk'] + random.randint(-7,7)
        defence = l['def']
        
        with open('current enemy.dat','rb') as f:
            l2=pickle.load(f)
        remaining_health = l2['rh']
        enemy_damage = l2['ed'] + random.randint(-5,5)
        enemy_damage = int(round(enemy_damage*(100-defence)/100, 0))
        coins_dropped = l2['cd'] + random.randint(-5,5)

        remaining_health-=dmg_delt
        player_health -= enemy_damage

        if remaining_health<=0:#enemy dies
            with open('profile.dat','rb') as f:
                l=pickle.load(f)
            with open('profile.dat','wb') as f:
                pickle.dump({'health':l['health'],'maxh':l['maxh'], 'level':l['level'], 'pot':l['pot'],'coins':l['coins']+coins_dropped, 'atk':l['atk'], 'def':l['def']},f)
            ui.status.setText('You defeated the enemy and earned {} coins'.format(coins_dropped))
            battlewindow.close()
            Main.show()

        elif player_health<=0:#player dies
            global posx
            global posy
            with open('profile.dat','rb') as f:
                l=pickle.load(f)
            with open('profile.dat','wb') as f:
                pickle.dump({'health':l['maxh'],'maxh':l['maxh'], 'level':l['level'], 'pot':l['pot'],'coins':l['coins'], 'atk':l['atk'], 'def':l['def']},f)
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            ui.status.setPalette(palette)
            ui.status.setText('You died. Level restarted')
            posx,posy=0,4
            battlewindow.close()
            Main.show()

        else:#no one dies
            with open('profile.dat','rb') as f:
                l=pickle.load(f)
            with open('profile.dat','wb') as f:
                pickle.dump({'health':player_health,'maxh':l['maxh'], 'level':l['level'], 'pot':l['pot'],'coins':l['coins'], 'atk':l['atk'], 'def':l['def']},f)
            with open('current enemy.dat','rb') as f:
                l=pickle.load(f)
            l['rh']=remaining_health
            with open('current enemy.dat','wb') as f:
                pickle.dump(l,f)
            self.label_6.setText('You deal {} dmg but take {} dmg'.format(dmg_delt,enemy_damage))


    def heal(self):
        with open('profile.dat','rb') as f:
            a=pickle.load(f)
            health=a['health']
            pot=a['pot']
            maxh=a['maxh']
        if health==maxh:
            self.label_6.setText('Health Already Maxed Out')
        elif health<maxh:
            if pot>=1:
                with open('profile.dat','wb') as f:
                    x={'health':maxh, 'maxh':a['maxh'], 'level':a['level'], 'pot':pot-1, 'coins':a['coins'], 'atk':a['atk'], 'def':a['def']}
                    pickle.dump(x,f)
                    self.label_6.setText('Health Maxed Out')
            else:
                self.label_6.setText('Not Enough Potions')

    
    def flee(self):
        global ui
        with open('current enemy.dat','rb') as f:
            l=pickle.load(f)
        dmg=l['ed'] + random.randint(1,10)
        flee_chance=l['ef']
        chance=random.randint(1,100)
        if chance<flee_chance:  #successful
            ui.status.setText('You Fleed Succesfully')
            battlewindow.close()
            Main.show()
        else:                   #unsuccessful
            with open('profile.dat','rb') as f:
                l=pickle.load(f)
                health=l['health']
            health-=dmg
            if health<=0:   #die
                global posx
                global posy
                with open('profile.dat','rb') as f:
                    l=pickle.load(f)
                with open('profile.dat','wb') as f:
                    pickle.dump({'health':l['maxh'],'maxh':l['maxh'], 'level':l['level'], 'pot':l['pot'],'coins':l['coins'], 'atk':l['atk'], 'def':l['def']},f)
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
                ui.status.setPalette(palette)
                ui.status.setText('You died. Level restarted')
                posx,posy=0,4
                battlewindow.close()
                Main.show()
            else:
                l['health']=health
                with open('profile.dat','wb') as f:
                    pickle.dump(l,f)
                self.label_6.setText('You were unable to flee and took {} dmg'.format(dmg))
    
    
    def choose_enemy(self,a):
        if a==1:
            with open('enemies.dat','rb') as f:
                l=pickle.load(f)[0]
            ename=l['ename']
            eh=l['eh']
            rh=l['rh']
            ed=l['ed']
            ef=l['ef']
            cd=l['cd']
            ep=l['ep']
            self.label_2.setText('You face a '+ename)
            self.label_4.setText('Enemy:'+str(rh)+'/'+str(eh))
            self.label.setPixmap(QtGui.QPixmap(ep))
            with open('profile.dat','rb') as f:
                lp=pickle.load(f)
            self.label_3.setText('Player:'+str(lp['health'])+'/'+str(lp['maxh']))
            self.label_5.setText('Potions:'+str(lp['pot']))


        elif a==2:
            with open('enemies.dat','rb') as f:
                l=pickle.load(f)[1]
            ename=l['ename']
            eh=l['eh']
            rh=l['rh']
            ed=l['ed']
            ef=l['ef']
            cd=l['cd']
            ep=l['ep']
            self.label_2.setText('You face a '+ename)
            self.label_4.setText('Enemy:'+str(rh)+'/'+str(eh))
            self.label.setPixmap(QtGui.QPixmap(ep))
            with open('profile.dat','rb') as f:
                lp=pickle.load(f)
            self.label_3.setText('Player:'+str(lp['health'])+'/'+str(lp['maxh']))
            self.label_5.setText('Potions:'+str(lp['pot']))

        elif a==3:
            with open('enemies.dat','rb') as f:
                l=pickle.load(f)[2]
            ename=l['ename']
            eh=l['eh']
            rh=l['rh']
            ed=l['ed']
            ef=l['ef']
            cd=l['cd']
            ep=l['ep']
            self.label_2.setText('You face a '+ename)
            self.label_4.setText('Enemy:'+str(rh)+'/'+str(eh))
            self.label.setPixmap(QtGui.QPixmap(ep))
            with open('profile.dat','rb') as f:
                lp=pickle.load(f)
            self.label_3.setText('Player:'+str(lp['health'])+'/'+str(lp['maxh']))
            self.label_5.setText('Potions:'+str(lp['pot']))
        elif a==4:
            with open('enemies.dat','rb') as f:
                for i in range(2):
                    ra=pickle.load(f)
            l=ra[0]
            ename=l['ename']
            eh=l['eh']
            rh=l['rh']
            ed=l['ed']
            ef=l['ef']
            cd=l['cd']
            ep=l['ep']
            self.label_2.setText('You face a '+ename)
            self.label_4.setText('Enemy:'+str(rh)+'/'+str(eh))
            self.label.setPixmap(QtGui.QPixmap(ep))
            with open('profile.dat','rb') as f:
                lp=pickle.load(f)
            self.label_3.setText('Player:'+str(lp['health'])+'/'+str(lp['maxh']))
            self.label_5.setText('Potions:'+str(lp['pot']))

        elif a==5:
            with open('enemies.dat','rb') as f:
                for i in range(2):
                    ra=pickle.load(f)
            l=ra[1]
            ename=l['ename']
            eh=l['eh']
            rh=l['rh']
            ed=l['ed']
            ef=l['ef']
            cd=l['cd']
            ep=l['ep']
            self.label_2.setText('You face a '+ename)
            self.label_4.setText('Enemy:'+str(rh)+'/'+str(eh))
            self.label.setPixmap(QtGui.QPixmap(ep))
            with open('profile.dat','rb') as f:
                lp=pickle.load(f)
            self.label_3.setText('Player:'+str(lp['health'])+'/'+str(lp['maxh']))
            self.label_5.setText('Potions:'+str(lp['pot']))
        with open('current enemy.dat','wb') as f:
            pickle.dump(l,f)

    def update(self):
        with open('current enemy.dat','rb') as f:
                l=pickle.load(f)
        ename=l['ename']
        eh=l['eh']
        rh=l['rh']
        ed=l['ed']
        ef=l['ef']
        cd=l['cd']
        ep=l['ep']
        self.label_2.setText('You face a '+ename)
        self.label_4.setText('Enemy:'+str(rh)+'/'+str(eh))
        self.label.setPixmap(QtGui.QPixmap(ep))
        with open('profile.dat','rb') as f:
            lp=pickle.load(f)
        self.label_3.setText('Player:'+str(lp['health'])+'/'+str(lp['maxh']))
        self.label_5.setText('Potions:'+str(lp['pot']))
    
    

import resources_rc


if __name__ == "__main__":
    import sys
    posx,posy=0,4
    with open('profile.dat','rb') as f:
        a=pickle.load(f)
        lvl=a['level']
    with open('maps.dat','rb') as f:
        for i in range(lvl):
            map_variable=pickle.load(f)

    app = QtWidgets.QApplication(sys.argv)

    Pregame = QtWidgets.QWidget()
    ui1 = Ui_Pregame()
    ui1.setupUi(Pregame)
    Pregame.show()

    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)

    shop = QtWidgets.QWidget()
    ui2 = Ui_shop()
    ui2.setupUi(shop)

    battlewindow = QtWidgets.QWidget()
    ui3 = Ui_battlewindow()
    ui3.setupUi(battlewindow)

    timer=QtCore.QTimer()
    timer.timeout.connect(ui.update)
    timer.timeout.connect(ui3.update)
    timer.start(300)

    sys.exit(app.exec_())
