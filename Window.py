from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

from car_id import Car_id
from cars_ui import Ui_Form
from json_requests import JSON


class Window(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Vantage Cars')
        self.btn_list_cars.clicked.connect(self.cars_list_page)
        self.btn_add_car.clicked.connect(self.add_page)
        self.btn_update_car.clicked.connect(self.update_page)
        self.btn_delete_car.clicked.connect(self.show_delete_dialog)
        self.btn_back_to_menu_car_list.clicked.connect(self.move_to_menu_page)
        self.btn_back_to_menu_add.clicked.connect(self.move_to_menu_page)
        self.btn_back_to_menu_update.clicked.connect(self.move_to_menu_page)
        self.js = JSON(self)

    def move_to_menu_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def cars_list_page(self):
        data = self.js.get_data()
        hh = ['id', 'brand', 'model', 'production_year', 'convertible']
        self.tableWidget.setColumnCount(len(hh))
        self.tableWidget.setColumnWidth(0, 10)
        self.tableWidget.setColumnWidth(1, 160)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 80)

        self.tableWidget.setHorizontalHeaderLabels(hh)
        for row_index, dat in enumerate(data):
            self.tableWidget.insertRow(row_index)
            # print(dat)
            for col_index, cell_data in enumerate(dat):
                # print(dat[cell_data])
                item = QTableWidgetItem(str(dat[cell_data]))
                self.tableWidget.setItem(row_index, col_index, item)

        self.stackedWidget.setCurrentIndex(1)

    def add_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.btn_ok.clicked.connect(self.js.add)

    def update_page(self):
        self.stackedWidget.setCurrentIndex(3)
        self.btn_update.clicked.connect(self.js.update)

    def show_delete_dialog(self):
        dialog = Car_id()
        res = dialog.exec()
        if res == Car_id.Accepted:
            try:
                if self.js.delete(dialog.car_id_LineEdit.text()):
                    msg = QMessageBox(self)
                    msg.setWindowTitle('Message')
                    msg.setText('Car deleted successfully')
                    msg.exec()
                else:
                    QMessageBox(self).warning(self, 'Not found', 'There is no such id')
                    self.show_delete_dialog()
                    # Seems these were not need

                    # msg.setWindowTitle('Message')
                    # msg.setText('Car deleted successfully')
                    # msg.show()

            except AssertionError:
                self.show_delete_dialog()