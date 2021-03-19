from PyQt5.QtWidgets import QDialog

# from GUI.Ui_warning import Ui_Warning
from GUI.Ui_alert import Ui_Alert


class Alert(QDialog, Ui_Alert):

    def __init__(self, tag,parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)


