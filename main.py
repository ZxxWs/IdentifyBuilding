
import sys
from PyQt5.QtWidgets import QApplication

from Code.MainUI import MainUI

if __name__ == '__main__':

    app = QApplication(sys.argv)

    myapp = MainUI()

    myapp.show()

    sys.exit(app.exec_())