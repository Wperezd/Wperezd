import sys
import os
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg


class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # 🔥 Cargar UI
        ruta = os.path.dirname(__file__)
        loadUi(os.path.join(ruta, "calculadora.ui"), self)

        # 🔥 Crear gráfica
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)

        # 🔥 Agregar al widget DERECHO
        self.layout = QVBoxLayout(self.layoutGrafica)
        self.layout.addWidget(self.canvas)

        # 🔥 Conectar ComboBox
        self.comboBox.currentIndexChanged.connect(self.cambiar_robot)

        self.cambiar_robot()

    def cambiar_robot(self):
        robot = self.comboBox.currentText()

        self.fig.clear()
        ax = self.fig.add_subplot(111)

        ruta = os.path.dirname(__file__)

        if robot == "Cartesiano":
            self.label.setText(
                "Robot Cartesiano\n"
                "Articulaciones: 3\n"
                "Tipo: PPP (3 Prismáticas)"
            )
            img = mpimg.imread(os.path.join(ruta, "Cartesiano.png"))

        elif robot == "Cilíndrico":
            self.label.setText(
                "Robot Cilíndrico\n"
                "Articulaciones: 3\n"
                "Tipo: RPP (1 Rotacional + 2 Prismáticas)"
            )
            img = mpimg.imread(os.path.join(ruta, "Cilindrico.png"))

        elif robot == "Esférico":
            self.label.setText(
                "Robot Esférico\n"
                "Articulaciones: 3\n"
                "Tipo: RRP (2 Rotacionales + 1 Prismática)"
            )
            img = mpimg.imread(os.path.join(ruta, "Esferico.png"))

        else:
            return

        ax.imshow(img)
        ax.axis("off")

          # 🔥 Limitar espacio de la imagen dentro del canvas
        self.fig.subplots_adjust(left=0.25, right=1.00, top=0.85, bottom=0.15)
        
        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
    