import time

from PySide2 import QtCore


class Timer(QtCore.QThread):
    time_left_signal = QtCore.Signal(int)

    def set_timer(self, count):
        self.__timer_count = count

    def run(self):
        self.status = True

        while self.status:
            if not self.__timer_count == 0:
                self.__timer_count -= 1
                time.sleep(1)
                self.time_left_signal.emit(self.__timer_count)
            else:
                self.status = False
