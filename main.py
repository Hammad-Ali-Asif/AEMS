from PySide6.QtWidgets import QApplication, QMainWindow
from login_page import Ui_Login_page  # Assuming 'temp' is the name of your UI module

class MyLoginPage(QMainWindow, Ui_Login_page):
    def __init__(self):
        super(MyLoginPage, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = MyLoginPage()
    window.show()
    app.exec_()
