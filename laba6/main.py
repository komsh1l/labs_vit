import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        symbols = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', '.', '=', '/']
        self.buttons = [[] for i in range(5)]
        for bt in range(len(symbols)):
            button = QPushButton(symbols[bt])
            if symbols[bt] != '=':
                button.clicked.connect(self.buttonClicked)
            else:
                button.clicked.connect(self.equalClicked)
            self.buttons[bt // 4 + 1].append(button)
        else:
            button = QPushButton('C')
            button.clicked.connect(self.clearClicked)
            self.buttons[0].append(button)
            self.result = QLineEdit()
            self.buttons[0].append(self.result)

        vbox = QVBoxLayout()
        for i in self.buttons:
            hbox = QHBoxLayout()
            for j in i:
                hbox.addWidget(j)
            vbox.addLayout(hbox)

        self.setLayout(vbox)

    def buttonClicked(self):
        button = self.sender()
        value = button.text()
        current_value = self.result.text()
        self.result.setText(current_value + value)

    def clearClicked(self):
        self.result.setText('')

    def equalClicked(self):
        try:
            result = str(eval(self.result.text()))
        except:
            result = 'Error'
        self.result.setText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

