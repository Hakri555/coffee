import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Coffe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.coffe = self.comboBox.currentText()
        self.con = sqlite3.connect("coffe.db")
        cur = self.con.cursor()
        info = cur.execute(f"""SELECT * FROM coffee_varieties WHERE name = '{self.coffe}'""").fetchall()
        info = info[0]
        self.lineEdit.setText(f'{info[0]}')
        self.lineEdit_2.setText(f'{info[2]}')
        self.lineEdit_3.setText(f'{info[3]}')
        self.lineEdit_4.setText(f'{info[4]}')
        self.lineEdit_5.setText(f'{info[5]}')
        self.lineEdit_6.setText(f'{info[6]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffe()
    ex.show()
    sys.exit(app.exec_())
