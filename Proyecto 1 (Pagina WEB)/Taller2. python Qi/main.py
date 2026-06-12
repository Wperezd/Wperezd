import sys
import math
from PyQt5 import QtWidgets
from calculadora_ui import Ui_Form   # ← cambia si no es Ui_Form

class Calculadora(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 🔗 Conectar botones
        self.ui.btn_suma.clicked.connect(self.sumar)
        self.ui.btn_resta.clicked.connect(self.restar)
        self.ui.btn_multiplicacion.clicked.connect(self.multiplicar)
        self.ui.btn_division.clicked.connect(self.dividir)
        self.ui.btn_residuo.clicked.connect(self.residuo)

        self.ui.btn_Sin.clicked.connect(self.seno)
        self.ui.btn_Cos.clicked.connect(self.coseno)
        self.ui.btn_Tan.clicked.connect(self.tangente)
        self.ui.btn_Cot.clicked.connect(self.cotangente)
        self.ui.btn_Sec.clicked.connect(self.secante)
        self.ui.btn_Csc.clicked.connect(self.cosecante)

    def obtener_valores(self):
        try:
            n1 = float(self.ui.lineEdit_num1.text())
            n2 = float(self.ui.lineEdit_num2.text())
            return n1, n2
        except:
            self.ui.label_resultado.setText("Error")
            return None, None

    # 🔢 Aritmética
    def sumar(self):
        n1, n2 = self.obtener_valores()
        if n1 is not None:
            self.ui.label_resultado.setText(str(n1 + n2))

    def restar(self):
        n1, n2 = self.obtener_valores()
        if n1 is not None:
            self.ui.label_resultado.setText(str(n1 - n2))

    def multiplicar(self):
        n1, n2 = self.obtener_valores()
        if n1 is not None:
            self.ui.label_resultado.setText(str(n1 * n2))

    def dividir(self):
        n1, n2 = self.obtener_valores()
        if n1 is not None:
            if n2 != 0:
                self.ui.label_resultado.setText(str(n1 / n2))
            else:
                self.ui.label_resultado.setText("Error: /0")

    def residuo(self):
        n1, n2 = self.obtener_valores()
        if n1 is not None:
            self.ui.label_resultado.setText(str(n1 % n2))

    # 📐 Trigonométricas
    def seno(self):
        n1, _ = self.obtener_valores()
        if n1 is not None:
            self.ui.label_resultado.setText(str(math.sin(n1)))

    def coseno(self):
        n1, _ = self.obtener_valores()
        if n1 is not None:
            self.ui.label_resultado.setText(str(math.cos(n1)))

    def tangente(self):
        n1, _ = self.obtener_valores()
        if n1 is not None:
            self.ui.label_resultado.setText(str(math.tan(n1)))

    def cotangente(self):
        n1, _ = self.obtener_valores()
        if n1 is not None:
            self.ui.label_resultado.setText(str(1 / math.tan(n1)))

    def secante(self):
        n1, _ = self.obtener_valores()
        if n1 is not None:
            self.ui.label_resultado.setText(str(1 / math.cos(n1)))

    def cosecante(self):
        n1, _ = self.obtener_valores()
        if n1 is not None:
            self.ui.label_resultado.setText(str(1 / math.sin(n1)))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec_())