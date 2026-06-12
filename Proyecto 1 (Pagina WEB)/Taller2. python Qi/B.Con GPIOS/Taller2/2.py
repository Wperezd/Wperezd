# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from gpiozero import LED, PWMLED

# -------- GPIO --------
led1 = LED(17)
led2 = LED(27)
led3 = PWMLED(18)
led4 = PWMLED(19)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(250, 410, 250, 31))

        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(350, 510, 100, 20))

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(300, 480, 200, 20))

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(280, 380, 250, 30))

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(290, 450, 200, 20))

        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(220, 50, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_28.setFont(font)

        self.label_imagen = QtWidgets.QLabel(self.centralwidget)
        self.label_imagen.setGeometry(QtCore.QRect(530, 350, 256, 192))  
        self.label_imagen.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imagen.setScaledContents(True)

        pixmap = QtGui.QPixmap("/home/raspberrypi/Downloads/Taller2/imagen.png")


        self.label_imagen.setPixmap(pixmap)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 250, 111, 61))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 250, 111, 61))

        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(80, 230, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)

        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(190, 230, 22, 160))
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 180, 120, 20))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 180, 120, 20))

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 180, 120, 20))

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 180, 120, 20))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)

        self.verticalSlider_2.setMinimum(0)
        self.verticalSlider_2.setMaximum(100)

        self.estado1 = False
        self.estado2 = False

        self.pushButton.clicked.connect(self.control_led1)
        self.pushButton_2.clicked.connect(self.control_led2)

        self.verticalSlider.valueChanged.connect(self.brillo_led3)
        self.verticalSlider_2.valueChanged.connect(self.brillo_led4)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label_24.setText(_translate("MainWindow", "William Perez, David Sierra, Camilo Ruiz"))
        self.label_21.setText(_translate("MainWindow", "2026 - 1"))
        self.label_17.setText(_translate("MainWindow", "Electiva de robótica"))
        self.label_15.setText(_translate("MainWindow", "Prof. Fabian Barrera Prieto (MSc)."))
        self.label_16.setText(_translate("MainWindow", "Ingeniería Mecatrónica"))
        self.label_28.setText(_translate("MainWindow", "Apagar Y Encender LEDS"))

        self.pushButton.setText(_translate("MainWindow", "ENCENDER"))
        self.pushButton_2.setText(_translate("MainWindow", "ENCENDER"))

        self.label.setText(_translate("MainWindow", "LED 1"))
        self.label_2.setText(_translate("MainWindow", "LED 2"))
        self.label_3.setText(_translate("MainWindow", "LED 3"))
        self.label_4.setText(_translate("MainWindow", "LED 4"))

    def control_led1(self):
        self.estado1 = not self.estado1

        if self.estado1:
            led1.on()
            self.pushButton.setText("APAGAR")
            self.pushButton.setStyleSheet("background-color: green; color: white;")
        else:
            led1.off()
            self.pushButton.setText("ENCENDER")
            self.pushButton.setStyleSheet("")

    def control_led2(self):
        self.estado2 = not self.estado2

        if self.estado2:
            led2.on()
            self.pushButton_2.setText("APAGAR")
            self.pushButton_2.setStyleSheet("background-color: green; color: white;")
        else:
            led2.off()
            self.pushButton_2.setText("ENCENDER")
            self.pushButton_2.setStyleSheet("")

    def brillo_led3(self):
        valor = self.verticalSlider.value()
        led3.value = valor / 100.0
        self.label.setText(f"LED 1: {valor}%")

    def brillo_led4(self):
        valor = self.verticalSlider_2.value()
        led4.value = valor / 100.0
        self.label_2.setText(f"LED 2: {valor}%")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
