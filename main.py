import sys
from threading import Thread

from PyQt5.QtWidgets import QApplication

from Code.MainUI import MainUI
# from Code.navigate import Navigate
from Code.mark import Mark
from Code.navigate import Navigate


# def


if __name__ == '__main__':
    app = QApplication(sys.argv)

    myapp = MainUI("building")
    # myapp = Navigate()
    # myapp.show()

    # myapp=Mark("building")
    myapp.show()

    sys.exit(app.exec_())
