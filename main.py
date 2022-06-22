import time

from PySide2 import QtWidgets, QtCore

from form import Ui_Form


class QThread(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.timerThread = Timer()



class Url(QtCore.QThread):
    pass


class Sistem_info(QtCore.QThread):
    pass


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    myapp = QThread()
    myapp.show()

    app.exec_()
