from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

# Hlavní okno
main = QtWidgets.QWidget()
main.setWindowTitle('Hello Qt')

# Layout pro hlavní okno
layout = QtWidgets.QHBoxLayout()
main.setLayout(layout)

# Nápis
label = QtWidgets.QLabel('Click the button to change me')
# Přidáním do layoutu se nápis automaticky stane potomkem hlavního okna
layout.addWidget(label)

# Tlačítko
button = QtWidgets.QPushButton('Click me')
layout.addWidget(button)

# Funkcionalita
def change_label():
    label.setText('Good job. +100 points.')

button.clicked.connect(change_label)

# Spuštění
main.show()
app.exec()