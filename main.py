from ui import EqualizerUI
from audio import AudioEngine
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EqualizerUI()
    audio = AudioEngine(window.eq_settings)
    audio.start()
    window.show()
    sys.exit(app.exec_())