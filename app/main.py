import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('app/ui/mainwindow.ui', self)
        self.setWindowTitle('Windows App Template')
        self.setWindowIcon(QIcon('app/icons/app-icon.ico'))
        self.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        self.label.setText("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
