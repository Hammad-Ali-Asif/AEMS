from PyQt5.QtWidgets import QApplication
from login_page import Ui_Form  # Replace with your actual module name

class MyApplication(Ui_Form):
    def __init__(self, Form):
        super(MyApplication, self).__init__()
        self.setupUi(MainWindow)
        # Add your application logic here

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MyApplication()
    MainWindow.show()
    sys.exit(app.exec_())
