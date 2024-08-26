import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from  PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("34°C", self)
        self.emoji_label = QLabel("☀", self)
        self.description_label = QLabel("Sunny", self)

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QIcon("C:\\Users\\pappm\\Pictures\\Saved Pictures\\sun_icon.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())