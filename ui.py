from PyQt5.QtWidgets import QMainWindow, QSlider, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class EqualizerUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parametric EQ")
        self.setGeometry(100, 100, 300, 400)
        self.bands = [(100, 0, 1.0), (500, 0, 1.0), (1000, 0, 1.0), (5000, 0, 1.0)]
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.sliders = []
        self.labels = []

        for i, (f, g, q) in enumerate(self.bands):
            label = QLabel(f\"{f} Hz: {g} dB\", self)
            slider = QSlider(Qt.Horizontal)
            slider.setMinimum(-12)
            slider.setMaximum(12)
            slider.setValue(g)
            slider.valueChanged.connect(lambda val, i=i: self.slider_changed(i, val))
            layout.addWidget(label)
            layout.addWidget(slider)
            self.labels.append(label)
            self.sliders.append(slider)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def slider_changed(self, index, value):
        freq, _, q = self.bands[index]
        self.bands[index] = (freq, value, q)
        self.labels[index].setText(f\"{freq} Hz: {value} dB\")

    def eq_settings(self):
        return self.bands