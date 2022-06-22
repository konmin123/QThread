from PySide2 import QtWidgets, QtCore

from form import Ui_Form
from timer import Timer


class QThread(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.timer_theard = Timer()
        # self.ui.spinBox
        self.ui.pushButton.clicked.connect(self.handler_timer)
        # self.ui.lcdNumber

    def handler_timer(self):
        self.ui.lcdNumber.setText(str(self.ui.spinBox.value()))
        self.timer_theard.set_timer(self.ui.spinBox.value())
        self.timer_theard.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    myapp = QThread()
    myapp.show()

    app.exec_()
