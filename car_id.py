from PySide6.QtWidgets import QDialog

from car_id_ui import Ui_Dialog


class Car_id(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_ok.clicked.connect(lambda: self.accept())
        self.btn_cancel.clicked.connect(lambda: self.close())
        self.btn_ok.setDefault(True)