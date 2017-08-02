# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    button = QPushButton('button', window) # ボタンを埋め込み
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()