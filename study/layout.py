# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    button1 = QPushButton('1')
    button2 = QPushButton('2')
    button3 = QPushButton('3')

    hbox = QHBoxLayout()

    hbox.addWidget(button1)

    vbox = QVBoxLayout()
    vbox.addWidget(button2)
    vbox.addWidget(button3)
    hbox.addLayout(vbox)

    window.setLayout(hbox)

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()