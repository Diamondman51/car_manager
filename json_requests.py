import json

import requests
from PySide6.QtWidgets import QMessageBox

hh ={
    "id": "1",
    "brand": "Porsche",
    "model": "911",
    "production_year": 1963,
    "convertible": False
}

ctp = {'Content-Type': 'application/json'}

# data = requests.post('http://localhost:3000/cars/', headers=ctp, data=json.dumps(hh))
#
# print(data.text)

class JSON:
    head = {'Content-Type': 'application/json'}

    def __init__(self, jj):
        self.jj = jj

    def add(self):
        data = self.get_data()

        id_ = self.jj.id_lineEdit.text()
        sp = [d['id'] for d in data]
        if id_ not in sp:
            brand = self.jj.brand_lineEdit.text()
            model = self.jj.car_model_lineEdit.text()
            production_year = self.jj.production_year_lineEdit.text()
            convertible = self.jj.is_convertable_comboBox.currentText()
            if convertible == 'YES':
                convertible = True
            elif convertible == 'NO':
                convertible = False

            if convertible != 'Choose':
                data = {
                    "id": id_,
                    "brand": brand,
                    "model": model,
                    "production_year": production_year,
                    "convertible": convertible
                }
                res = requests.post('http://localhost:3000/cars/', headers=self.head, data=json.dumps(data)).status_code
                print(res)
                if res == requests.codes.created:
                    print('Success')
                    QMessageBox(self.jj).information(self.jj, 'Message', f'Successfully added: id {id_}')
                else:
                    QMessageBox(self.jj).warning(self.jj, 'Warning', f'Id not added, check your internet connection: id {id_}')

        else:
            QMessageBox(self.jj).warning(self.jj, 'Warning', f'This id is already exists: id {id_}')

    def update(self):

        # TODO Check is there same ID in the data
        id_ = self.jj.update_id_lineEdit.text()
        brand = self.jj.update_brand_lineEdit.text()
        model = self.jj.update_car_model_lineEdit.text()
        production_year = self.jj.update_production_year_lineEdit.text()
        convertible = self.jj.update_is_convertable_comboBox.currentText()
        if convertible == 'YES':
            convertible = True
        elif convertible == 'NO':
            convertible = False
        print(convertible != 'Choose')
        print(convertible)
        if convertible != 'Choose':
            data = {
                "id": id_,
                "brand": brand,
                "model": model,
                "production_year": production_year,
                "convertible": convertible
            }
            response = requests.put(f'http://localhost:3000/cars/{id_}', headers=self.head, data=json.dumps(data))
            print(id_)
            print(response.status_code)
            if response.status_code == 200:
                print('Success')
                QMessageBox(self.jj).information(self.jj, 'Message', f'Successfully added: id {id_}')
            else:
                QMessageBox(self.jj).warning(self.jj, 'Warning', f'Id not added, check your internet connection: id {id_}')

    def delete(self, id):
        res = requests.delete(f"http://localhost:3000/cars/{id}")
        print(res.status_code)
        if res.status_code == 200:
            return True
            # msg = QMessageBox(self.jj)
            # msg.setWindowTitle('Message')
            # msg.setText('Car deleted successfully')
            # msg.show()
        elif res.status_code == 404:
            return False

        else:
            raise AssertionError

    def get_data(self):
        response = requests.get('http://localhost:3000/cars/')
        if response.status_code == 200:
            # print(response.text)
            return json.loads(response.text)
        else:
            return False

# f = JSON(45)
# text = f.get_data()
#
# for i in text:
#     print(i)