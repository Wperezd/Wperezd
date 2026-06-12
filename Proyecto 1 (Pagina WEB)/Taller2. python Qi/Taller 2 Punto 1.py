import sys
import math
from PyQt5 import QtWidgets, QtGui
from calculadora_ui import Ui_Form

class Calculadora(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 🖼️ Logo ECCI
        pixmap = QtGui.QPixmap("ecci.png")
        if hasattr(self.ui, 'label_logo'):
            self.ui.label_logo.setPixmap(pixmap)
            self.ui.label_logo.setScaledContents(True)

        # 🔗 Conexión de Botones
        self.ui.btn_suma.clicked.connect(self.sumar)
        self.ui.btn_resta.clicked.connect(self.restar)
        self.ui.btn_multiplicacion.clicked.connect(self.multiplicar)
        self.ui.btn_division.clicked.connect(self.dividir)
        self.ui.btn_residuo.clicked.connect(self.residuo)

        # Trigonométricas
        self.ui.btn_Sin.clicked.connect(self.seno)
        self.ui.btn_Cos.clicked.connect(self.coseno)
        self.ui.btn_Tan.clicked.connect(self.tangente)
        self.ui.btn_Cot.clicked.connect(self.cotangente)
        self.ui.btn_Sec.clicked.connect(self.secante)
        self.ui.btn_Csc.clicked.connect(self.cosecante)

    # --- NUEVAS FUNCIONES DE LECTURA ESPECÍFICA ---

    def sumar(self):
        try:
            # Pestaña 1: lineEdit_num1 y lineEdit_num2
            n1 = float(self.ui.lineEdit_num1.text())
            n2 = float(self.ui.lineEdit_num2.text())
            self.ui.label_resultado.setText(f"{n1 + n2:g}")
        except ValueError:
            self.ui.label_resultado.setText("Error")

    def restar(self):
        try:
            # Pestaña 2: lineEdit_num1_2 y lineEdit_num1_3
            n1 = float(self.ui.lineEdit_num1_2.text())
            n2 = float(self.ui.lineEdit_num1_3.text())
            self.ui.label_resultado_2.setText(f"{n1 - n2:g}")
        except ValueError:
            self.ui.label_resultado_2.setText("Error")

    def multiplicar(self):
        try:
            # Pestaña 3: lineEdit_num1_4 y lineEdit_num1_5
            n1 = float(self.ui.lineEdit_num1_4.text())
            n2 = float(self.ui.lineEdit_num1_5.text())
            self.ui.label_resultado.setText(f"{n1 * n2:g}")
        except ValueError:
            self.ui.label_resultado.setText("Error")

    # --- LAS DEMÁS SIGUEN IGUAL (Asegúrate de que los nombres coincidan) ---

    def dividir(self):
        try:
            # Si la división está en otra pestaña, cambia estos nombres también
            n1 = float(self.ui.lineEdit_num1.text()) 
            n2 = float(self.ui.lineEdit_num2.text())
            if n2 != 0:
                self.ui.label_resultado.setText(f"{n1 / n2:g}")
            else:
                self.ui.label_resultado.setText("Error: /0")
        except ValueError:
            self.ui.label_resultado.setText("Error")

    def residuo(self):
        try:
            n1 = float(self.ui.lineEdit_num1.text())
            n2 = float(self.ui.lineEdit_num2.text())
            self.ui.label_resultado.setText(f"{n1 % n2:g}")
        except ValueError:
            self.ui.label_resultado.setText("Error")

    # --- TRIGONOMETRÍA ---
    def seno(self):
        try:
            n1 = float(self.ui.lineEdit_num1.text())
            self.ui.label_resultado.setText(f"{math.sin(math.radians(n1)):.4f}")
        except ValueError: self.ui.label_resultado.setText("Error")

    def coseno(self):
        try:
            n1 = float(self.ui.lineEdit_num1.text())
            self.ui.label_resultado.setText(f"{math.cos(math.radians(n1)):.4f}")
        except ValueError: self.ui.label_resultado.setText("Error")

    def tangente(self):
        try:
            n1 = float(self.ui.lineEdit_num1.text())
            self.ui.label_resultado.setText(f"{math.tan(math.radians(n1)):.4f}")
        except: self.ui.label_resultado.setText("Error")

    def cotangente(self):
        try:
            n1 = float(self.ui.lineEdit_num1.text())
            self.ui.label_resultado.setText(f"{1/math.tan(math.radians(n1)):.4f}")
        except: self.ui.label_resultado.setText("Error")

    def secante(self):
        try:
            n1 = float(self.ui.lineEdit_num1.text())
            self.ui.label_resultado.setText(f"{1/math.cos(math.radians(n1)):.4f}")
        except: self.ui.label_resultado.setText("Error")

    def cosecante(self):
        try:
            n1 = float(self.ui.lineEdit_num1.text())
            self.ui.label_resultado.setText(f"{1/math.sin(math.radians(n1)):.4f}")
        except: self.ui.label_resultado.setText("Error")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec_())