import sys
import numpy as np
from PyQt5 import QtWidgets

from calculadora_ui import Ui_Form

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# 🎨 Canvas
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        self.ax = fig.add_subplot(111)
        super().__init__(fig)


# 🧩 App
class MainApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 📊 Canvas en widget
        self.canvas = MplCanvas(self)
        self.layout_plot = QtWidgets.QVBoxLayout()
        self.widget_plot.setLayout(self.layout_plot)
        self.layout_plot.addWidget(self.canvas)

        # 🎚️ Conectar sliders
        self.slider_R.valueChanged.connect(self.actualizar)
        self.slider_C.valueChanged.connect(self.actualizar)
        self.slider_V.valueChanged.connect(self.actualizar)

        # Primera gráfica
        self.actualizar()

    def actualizar(self):
        # Valores
        R = self.slider_R.value()
        C_micro = self.slider_C.value()
        V = self.slider_V.value()

        # Evitar errores
        if R == 0 or C_micro == 0:
            return

        # Convertir a Faradios
        C = C_micro * 1e-6

        # Labels
        self.label_R.setText(f"RESISTENCIA: {R} Ω")
        self.label_C.setText(f"CAPACITANCIA: {C_micro} µF")
        self.label_V.setText(f"VOLTAJE: {V} V")

        # 🔥 TIEMPO FIJO (CLAVE)
        t = np.linspace(0, 5, 1000)

        # Ecuaciones RC
        carga = V * (1 - np.exp(-t / (R * C)))
        descarga = V * np.exp(-t / (R * C))

        # Limpiar gráfica
        self.canvas.ax.clear()

        # Graficar
        self.canvas.ax.plot(t, carga, label="Carga")
        self.canvas.ax.plot(t, descarga, linestyle='--', label="Descarga")

        # Configuración
        self.canvas.ax.set_title(f"Circuito RC | R={R}Ω C={C_micro}µF V={V}V")
        self.canvas.ax.set_xlabel("Tiempo (s)")
        self.canvas.ax.set_ylabel("Voltaje (V)")
        self.canvas.ax.legend()
        self.canvas.ax.grid()

        # Constante de tiempo
        tau = R * C
        self.canvas.ax.text(
            0.05, 0.9,
            f"τ = {tau:.6f} s",
            transform=self.canvas.ax.transAxes
        )

        # 🔥 Actualizar gráfica en tiempo real
        self.canvas.draw_idle()


# 🚀 Ejecutar
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())