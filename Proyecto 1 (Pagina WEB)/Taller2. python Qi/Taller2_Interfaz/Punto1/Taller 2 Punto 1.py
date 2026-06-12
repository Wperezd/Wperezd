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
        pixmap = QtGui.QPixmap("logo.png")
        if hasattr(self.ui, 'label_logo_1'):
            self.ui.label_logo_1.setPixmap(pixmap)
            self.ui.label_logo_1.setScaledContents(True)

        if hasattr(self.ui, 'label_logo_2'):
            self.ui.label_logo_2.setPixmap(pixmap)
            self.ui.label_logo_2.setScaledContents(True)

        if hasattr(self.ui, 'label_logo_3'):
            self.ui.label_logo_3.setPixmap(pixmap)
            self.ui.label_logo_3.setScaledContents(True)

        if hasattr(self.ui, 'label_logo_4'):
            self.ui.label_logo_4.setPixmap(pixmap)
            self.ui.label_logo_4.setScaledContents(True)

        if hasattr(self.ui, 'label_logo_5'):
            self.ui.label_logo_5.setPixmap(pixmap)
            self.ui.label_logo_5.setScaledContents(True)

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
            self.ui.label_resultado_3.setText(f"{n1 * n2:g}")
        except ValueError:
            self.ui.label_resultado_3.setText("Error")

    # --- LAS DEMÁS SIGUEN IGUAL (Asegúrate de que los nombres coincidan) ---

    def dividir(self):
        try:
            # Si la división está en otra pestaña, cambia estos nombres también
            n1 = float(self.ui.lineEdit_num1_6.text()) 
            n2 = float(self.ui.lineEdit_num1_7.text())
            if n2 != 0:
                self.ui.label_resultado_4.setText(f"{n1 / n2:g}")
            else:
                self.ui.label_resultado_4.setText("Error: /0")
        except ValueError:
            self.ui.label_resultado.setText("Error")

    def residuo(self):
        try:
            n1 = float(self.ui.lineEdit_num1_6.text())
            n2 = float(self.ui.lineEdit_num1_7.text())
            self.ui.label_resultado_5.setText(f"{n1 % n2:g}")
        except ValueError:
            self.ui.label_resultado_5.setText("Error")

    # --- TRIGONOMETRÍA ---
    def seno(self):
        try:
            n = float(self.ui.lineEdit_1.text())
            res = math.sin(math.radians(n))
            self.ui.label_resultado_6.setText(f"Sin({n}°) = {res:.4f}")
        except: self.ui.label_resultado_6.setText("Error")

    def coseno(self):
        try:
            # Entrada al lado de Cos: lineEdit_num1_9
            n = float(self.ui.lineEdit_2.text())
            res = math.cos(math.radians(n))
            self.ui.label_resultado_7.setText(f"Cos({n}°) = {res:.4f}")
        except: self.ui.label_resultado_7.setText("Error")

    def tangente(self):
        try:
            # Entrada al lado de Tan: lineEdit_num1_10
            n = float(self.ui.lineEdit_3.text())
            res = math.tan(math.radians(n))
            # Manejo de error para 90°, 270°, etc.
            if abs(res) > 1e10: raise ValueError
            self.ui.label_resultado_8.setText(f"Tan({n}°) = {res:.4f}")
        except: self.ui.label_resultado_8.setText("Error: Indefinido")

    def cotangente(self):
        try:
            # Entrada al lado de Cot: lineEdit_num1_11
            n = float(self.ui.lineEdit_4.text())
            res = 1 / math.tan(math.radians(n))
            self.ui.label_resultado_9.setText(f"Cot({n}°) = {res:.4f}")
        except: self.ui.label_resultado_9.setText("Error: Div/0")

    def secante(self):
        try:
            # Entrada al lado de Sec: lineEdit_num1_12
            n = float(self.ui.lineEdit_5.text())
            res = 1 / math.cos(math.radians(n))
            self.ui.label_resultado_10.setText(f"Sec({n}°) = {res:.4f}")
        except: self.ui.label_resultado_10.setText("Error: Div/0")

    def cosecante(self):
        try:
            # Entrada al lado de Csc: lineEdit_num1_13
            n = float(self.ui.lineEdit_6.text())
            res = 1 / math.sin(math.radians(n))
            self.ui.label_resultado_11.setText(f"Csc({n}°) = {res:.4f}")
        except: self.ui.label_resultado_11.setText("Error: Div/0")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec_())