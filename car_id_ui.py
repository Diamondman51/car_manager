# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'car_idEAwIzA.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(150, 125)
        Dialog.setMinimumSize(QSize(150, 80))
        Dialog.setMaximumSize(QSize(150, 9999))
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"padding: 0 0 0 2")

        self.verticalLayout.addWidget(self.label)

        self.car_id_LineEdit = QLineEdit(Dialog)
        self.car_id_LineEdit.setObjectName(u"car_id_LineEdit")
        self.car_id_LineEdit.setMinimumSize(QSize(0, 30))
        self.car_id_LineEdit.setStyleSheet(u"padding: 0 0 0 5")
        self.car_id_LineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.car_id_LineEdit)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_cancel = QPushButton(self.widget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(65, 0))
        self.btn_cancel.setFont(font)

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_ok = QPushButton(self.widget)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setFont(font)

        self.horizontalLayout.addWidget(self.btn_ok)


        self.verticalLayout.addWidget(self.widget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Enter car id", None))
        self.car_id_LineEdit.setText("")
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"Ok", None))
    # retranslateUi

