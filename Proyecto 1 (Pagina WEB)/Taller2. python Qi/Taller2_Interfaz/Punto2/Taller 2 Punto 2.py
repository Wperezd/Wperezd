import sys
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from calculadora_ui import Ui_wibget_grafica

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        self.ax = fig.add_subplot(111)
        super().__init__(fig)


class MainApp(QtWidgets.QWidget, Ui_wibget_grafica):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ✅ LOGO
        pixmap = QPixmap("logo.png")  # cambia si tu archivo tiene otro nombre
        self.label_logo_1.setPixmap(pixmap)
        self.label_logo_1.setScaledContents(True)

        # ✅ CANVAS EN widget_plot
        self.canvas = MplCanvas(self)
        layout = QtWidgets.QVBoxLayout(self.widget_plot)
        layout.addWidget(self.canvas)

        # ✅ BOTÓN
        self.btn_graficar.clicked.connect(self.graficar)

    def graficar(self):
        try:
            x_min = float(self.lineEdit_min.text())
            x_max = float(self.lineEdit_max.text())

            x = np.linspace(x_min, x_max, 1000)
            opcion = self.combo_funcion.currentText()

            if opcion == "sin":
                y = np.sin(x)
            elif opcion == "cos":
                y = np.cos(x)
            elif opcion == "tan":
                y = np.tan(x)
            elif opcion == "cot":
                y = np.where(np.tan(x) != 0, 1 / np.tan(x), np.nan)
            elif opcion == "sec":
                y = np.where(np.cos(x) != 0, 1 / np.cos(x), np.nan)
            elif opcion == "csc":
                y = np.where(np.sin(x) != 0, 1 / np.sin(x), np.nan)

            self.canvas.ax.clear()
            self.canvas.ax.plot(x, y)
            self.canvas.ax.set_title(opcion)
            self.canvas.ax.grid()

            self.canvas.draw()

        except:
            QtWidgets.QMessageBox.warning(self, "Error", "Verifica los valores")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())