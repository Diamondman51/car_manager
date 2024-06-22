# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cars_uiYSNUYD.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(539, 527)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setSpacing(9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.menu_page = QWidget()
        self.menu_page.setObjectName(u"menu_page")
        self.verticalLayout_5 = QVBoxLayout(self.menu_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_19 = QLabel(self.menu_page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 60))
        self.label_19.setMaximumSize(QSize(16777215, 60))
        self.label_19.setStyleSheet(u"padding: 0 0 0 10;\n"
"font-size: 24px;")

        self.verticalLayout_2.addWidget(self.label_19)

        self.line_2 = QFrame(self.menu_page)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 20))
        self.line_2.setLineWidth(10)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.frame = QFrame(self.menu_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 40))
        self.label_20.setMaximumSize(QSize(30, 40))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_20.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_20)

        self.btn_list_cars = QPushButton(self.frame)
        self.btn_list_cars.setObjectName(u"btn_list_cars")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_list_cars.sizePolicy().hasHeightForWidth())
        self.btn_list_cars.setSizePolicy(sizePolicy1)
        self.btn_list_cars.setMinimumSize(QSize(0, 40))
        self.btn_list_cars.setMaximumSize(QSize(16777215, 40))
        self.btn_list_cars.setFont(font1)

        self.horizontalLayout_5.addWidget(self.btn_list_cars)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.menu_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 40))
        self.label_21.setMaximumSize(QSize(30, 40))
        self.label_21.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_21)

        self.btn_add_car = QPushButton(self.frame_2)
        self.btn_add_car.setObjectName(u"btn_add_car")
        sizePolicy1.setHeightForWidth(self.btn_add_car.sizePolicy().hasHeightForWidth())
        self.btn_add_car.setSizePolicy(sizePolicy1)
        self.btn_add_car.setMinimumSize(QSize(0, 40))
        self.btn_add_car.setMaximumSize(QSize(16777215, 40))
        self.btn_add_car.setFont(font1)

        self.horizontalLayout_6.addWidget(self.btn_add_car)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.menu_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 40))
        self.label_22.setMaximumSize(QSize(30, 40))
        self.label_22.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_22)

        self.btn_delete_car = QPushButton(self.frame_3)
        self.btn_delete_car.setObjectName(u"btn_delete_car")
        sizePolicy1.setHeightForWidth(self.btn_delete_car.sizePolicy().hasHeightForWidth())
        self.btn_delete_car.setSizePolicy(sizePolicy1)
        self.btn_delete_car.setMinimumSize(QSize(0, 40))
        self.btn_delete_car.setMaximumSize(QSize(16777215, 16777215))
        self.btn_delete_car.setFont(font1)

        self.horizontalLayout_7.addWidget(self.btn_delete_car)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.menu_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(30, 40))
        self.label_23.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_23)

        self.btn_update_car = QPushButton(self.frame_4)
        self.btn_update_car.setObjectName(u"btn_update_car")
        sizePolicy1.setHeightForWidth(self.btn_update_car.sizePolicy().hasHeightForWidth())
        self.btn_update_car.setSizePolicy(sizePolicy1)
        self.btn_update_car.setMinimumSize(QSize(0, 40))
        self.btn_update_car.setMaximumSize(QSize(16777215, 16777215))
        self.btn_update_car.setFont(font1)

        self.horizontalLayout_8.addWidget(self.btn_update_car)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.menu_page)
        self.car_list_page = QWidget()
        self.car_list_page.setObjectName(u"car_list_page")
        self.verticalLayout_3 = QVBoxLayout(self.car_list_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget = QTableWidget(self.car_list_page)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        font2 = QFont()
        font2.setPointSize(12)
        self.tableWidget.setFont(font2)
        self.tableWidget.setStyleSheet(u"alternate-background-color: rgb(123, 213, 255);\n"
"")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.widget_3 = QWidget(self.car_list_page)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.btn_back_to_menu_car_list = QPushButton(self.widget_3)
        self.btn_back_to_menu_car_list.setObjectName(u"btn_back_to_menu_car_list")
        self.btn_back_to_menu_car_list.setFont(font2)

        self.horizontalLayout_9.addWidget(self.btn_back_to_menu_car_list)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.car_list_page)
        self.add_car_page = QWidget()
        self.add_car_page.setObjectName(u"add_car_page")
        self.add_car_page.setStyleSheet(u"QLabel {\n"
"	padding: 0 0 0 2\n"
"}\n"
"\n"
"QLineEdit {\n"
"	padding: 0 0 0 5\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.add_car_page)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, -1, -1, 20)
        self.label_12 = QLabel(self.add_car_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.verticalLayout_4.addWidget(self.label_12)

        self.label_7 = QLabel(self.add_car_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setPointSize(14)
        self.label_7.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_7)

        self.id_lineEdit = QLineEdit(self.add_car_page)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        self.id_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.id_lineEdit.setFont(font3)

        self.verticalLayout_4.addWidget(self.id_lineEdit)

        self.label_8 = QLabel(self.add_car_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_8)

        self.brand_lineEdit = QLineEdit(self.add_car_page)
        self.brand_lineEdit.setObjectName(u"brand_lineEdit")
        self.brand_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.brand_lineEdit.setFont(font3)

        self.verticalLayout_4.addWidget(self.brand_lineEdit)

        self.label_9 = QLabel(self.add_car_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_9)

        self.car_model_lineEdit = QLineEdit(self.add_car_page)
        self.car_model_lineEdit.setObjectName(u"car_model_lineEdit")
        self.car_model_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.car_model_lineEdit.setFont(font3)

        self.verticalLayout_4.addWidget(self.car_model_lineEdit)

        self.label_10 = QLabel(self.add_car_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_10)

        self.production_year_lineEdit = QLineEdit(self.add_car_page)
        self.production_year_lineEdit.setObjectName(u"production_year_lineEdit")
        self.production_year_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.production_year_lineEdit.setFont(font3)

        self.verticalLayout_4.addWidget(self.production_year_lineEdit)

        self.label_11 = QLabel(self.add_car_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 30))
        self.label_11.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_11)

        self.is_convertable_comboBox = QComboBox(self.add_car_page)
        self.is_convertable_comboBox.addItem("")
        self.is_convertable_comboBox.addItem("")
        self.is_convertable_comboBox.addItem("")
        self.is_convertable_comboBox.setObjectName(u"is_convertable_comboBox")
        self.is_convertable_comboBox.setMaximumSize(QSize(16777215, 35))
        self.is_convertable_comboBox.setFont(font3)

        self.verticalLayout_4.addWidget(self.is_convertable_comboBox)

        self.widget = QWidget(self.add_car_page)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_back_to_menu_add = QPushButton(self.widget)
        self.btn_back_to_menu_add.setObjectName(u"btn_back_to_menu_add")
        self.btn_back_to_menu_add.setFont(font3)
        self.btn_back_to_menu_add.setStyleSheet(u"background-color: rgb(178, 178, 186);")

        self.horizontalLayout.addWidget(self.btn_back_to_menu_add)

        self.btn_ok = QPushButton(self.widget)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setFont(font3)
        self.btn_ok.setStyleSheet(u"background-color: rgb(91, 199, 79);")

        self.horizontalLayout.addWidget(self.btn_ok)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.widget)

        self.verticalLayout_4.setStretch(1, 5)
        self.stackedWidget.addWidget(self.add_car_page)
        self.update_car_page = QWidget()
        self.update_car_page.setObjectName(u"update_car_page")
        self.update_car_page.setStyleSheet(u"QLabel {\n"
"	padding: 0 0 0 2\n"
"}\n"
"\n"
"QLineEdit {\n"
"	padding: 0 0 0 5\n"
"}")
        self.verticalLayout = QVBoxLayout(self.update_car_page)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, -1, -1, 20)
        self.label_15 = QLabel(self.update_car_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout.addWidget(self.label_15)

        self.label_17 = QLabel(self.update_car_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 30))
        self.label_17.setFont(font3)

        self.verticalLayout.addWidget(self.label_17)

        self.update_id_lineEdit = QLineEdit(self.update_car_page)
        self.update_id_lineEdit.setObjectName(u"update_id_lineEdit")
        self.update_id_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_id_lineEdit.setFont(font3)

        self.verticalLayout.addWidget(self.update_id_lineEdit)

        self.label_18 = QLabel(self.update_car_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 30))
        self.label_18.setFont(font3)

        self.verticalLayout.addWidget(self.label_18)

        self.update_brand_lineEdit = QLineEdit(self.update_car_page)
        self.update_brand_lineEdit.setObjectName(u"update_brand_lineEdit")
        self.update_brand_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_brand_lineEdit.setFont(font3)

        self.verticalLayout.addWidget(self.update_brand_lineEdit)

        self.label_13 = QLabel(self.update_car_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setFont(font3)

        self.verticalLayout.addWidget(self.label_13)

        self.update_car_model_lineEdit = QLineEdit(self.update_car_page)
        self.update_car_model_lineEdit.setObjectName(u"update_car_model_lineEdit")
        self.update_car_model_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_car_model_lineEdit.setFont(font3)

        self.verticalLayout.addWidget(self.update_car_model_lineEdit)

        self.label_16 = QLabel(self.update_car_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 30))
        self.label_16.setFont(font3)

        self.verticalLayout.addWidget(self.label_16)

        self.update_production_year_lineEdit = QLineEdit(self.update_car_page)
        self.update_production_year_lineEdit.setObjectName(u"update_production_year_lineEdit")
        self.update_production_year_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_production_year_lineEdit.setFont(font3)

        self.verticalLayout.addWidget(self.update_production_year_lineEdit)

        self.label_14 = QLabel(self.update_car_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setFont(font3)

        self.verticalLayout.addWidget(self.label_14)

        self.update_is_convertable_comboBox = QComboBox(self.update_car_page)
        self.update_is_convertable_comboBox.addItem("")
        self.update_is_convertable_comboBox.addItem("")
        self.update_is_convertable_comboBox.addItem("")
        self.update_is_convertable_comboBox.setObjectName(u"update_is_convertable_comboBox")
        self.update_is_convertable_comboBox.setMaximumSize(QSize(16777215, 35))
        self.update_is_convertable_comboBox.setFont(font3)

        self.verticalLayout.addWidget(self.update_is_convertable_comboBox)

        self.widget_2 = QWidget(self.update_car_page)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btn_back_to_menu_update = QPushButton(self.widget_2)
        self.btn_back_to_menu_update.setObjectName(u"btn_back_to_menu_update")
        self.btn_back_to_menu_update.setFont(font3)
        self.btn_back_to_menu_update.setStyleSheet(u"background-color: rgb(178, 178, 186);")

        self.horizontalLayout_4.addWidget(self.btn_back_to_menu_update)

        self.btn_update = QPushButton(self.widget_2)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setFont(font3)
        self.btn_update.setStyleSheet(u"background-color: rgb(91, 199, 79);")

        self.horizontalLayout_4.addWidget(self.btn_update)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.widget_2)

        self.verticalLayout.setStretch(1, 5)
        self.stackedWidget.addWidget(self.update_car_page)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Vantage Cars Database", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Menu", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"1.", None))
        self.btn_list_cars.setText(QCoreApplication.translate("Form", u" List cars", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"2.", None))
        self.btn_add_car.setText(QCoreApplication.translate("Form", u"Add new car", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"3.", None))
        self.btn_delete_car.setText(QCoreApplication.translate("Form", u"Delete car", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"4.", None))
        self.btn_update_car.setText(QCoreApplication.translate("Form", u"Update car", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"brand", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"model", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"production year", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"convertible", None));
        self.btn_back_to_menu_car_list.setText(QCoreApplication.translate("Form", u"Back to Menu", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Add New Car", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Car ID", None))
        self.id_lineEdit.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"Car Brand", None))
        self.brand_lineEdit.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"Car Model", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Car production year", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Is this car convertible?", None))
        self.is_convertable_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Choose", None))
        self.is_convertable_comboBox.setItemText(1, QCoreApplication.translate("Form", u"YES", None))
        self.is_convertable_comboBox.setItemText(2, QCoreApplication.translate("Form", u"NO", None))

        self.btn_back_to_menu_add.setText(QCoreApplication.translate("Form", u"Back to Menu", None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"Ok", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Update Car", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Car ID", None))
        self.update_id_lineEdit.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"Car Brand", None))
        self.update_brand_lineEdit.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"Car Model", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Car production year", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Is this car convertible?", None))
        self.update_is_convertable_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Choose", None))
        self.update_is_convertable_comboBox.setItemText(1, QCoreApplication.translate("Form", u"YES", None))
        self.update_is_convertable_comboBox.setItemText(2, QCoreApplication.translate("Form", u"NO", None))

        self.btn_back_to_menu_update.setText(QCoreApplication.translate("Form", u"Back to Menu", None))
        self.btn_update.setText(QCoreApplication.translate("Form", u"Update", None))
    # retranslateUi

