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

vstup = QtWidgets.QLineEdit()
layout.addWidget(vstup)
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
    

button.clicked.connect(change_label)

# Spuštění
main.show()
app.exec()