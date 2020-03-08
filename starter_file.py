from PyQt5 import QtWidgets
# from SoundEquilizer import Ui_MainWindow
# from ChangeItWindow import Ui_ChangeItWindow
from Welcome import Ui_Welcome
import sys


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_Welcome()
        self.ui.setupUi(self)
     


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()