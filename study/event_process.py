# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt


class MyWiget(QWidget):
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


def main():
    app = QApplication(sys.argv)

    window = MyWiget()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()