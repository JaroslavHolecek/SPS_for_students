from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

# Hlavní okno
main = QtWidgets.QWidget()
main.setWindowTitle('Hello Qt')

# Layout pro hlavní okno
layout = QtWidgets.QHBoxLayout()
main.setLayout(layout)

layout_vertical = QtWidgets.QVBoxLayout()


# Nápis
label = QtWidgets.QLabel('Click the button to change me')
# Přidáním do layoutu se nápis automaticky stane potomkem hlavního okna
layout.addWidget(label)

layout.addLayout(layout_vertical)

# Tlačítko
button = QtWidgets.QPushButton('Click me')
layout_vertical.addWidget(button)

buttonDva = QtWidgets.QPushButton("Cudlik 2")
layout_vertical.addWidget(buttonDva)

vstup = QtWidgets.QLineEdit()
layout.addWidget(vstup)

vstupDva = QtWidgets.QLineEdit()
layout.addWidget(vstupDva)
# vstup.text()
# Funkcionalita



def change_label():
    celytext = vstup.text()
    print(celytext)
    rozdelenepole = celytext.split(" ")
    print(rozdelenepole)
    y = 0
    for i in rozdelenepole:
        y += int(i)

    z = sum(map(int, vstup.text().split(" ")))
    
    label.setText(f"{y} je stejné jako {z}")


def change_labelDva():
    celytext = vstupDva.text()
    print(celytext)
    rozdelenepole = celytext.split(" ")
    print(rozdelenepole)
    y = 0
    for i in rozdelenepole:
        y += int(i)
    
    z = sum(map(int, vstupDva.text().split(" ")))
    
    label.setText(f"{y} je stejné jako {z}")

button.clicked.connect(change_label)

buttonDva.clicked.connect(change_labelDva)

# Spuštění
main.show()
app.exec()