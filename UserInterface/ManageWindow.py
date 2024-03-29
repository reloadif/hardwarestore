# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ManageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os, os.path

class Ui_Manage(object):
    def setupUi(self, Manage):
        Manage.setObjectName("Manage")
        Manage.setEnabled(True)
        Manage.resize(1000, 600)
        Manage.setMinimumSize(QtCore.QSize(1000, 600))
        Manage.setMaximumSize(QtCore.QSize(1000, 600))
        icondir = ""
        if hasattr(sys, "_MEIPASS"): icondir = os.path.join(sys._MEIPASS, './icons/mainIcon.png')
        else: icondir = './UserInterface/icons/mainIcon.png'
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icondir), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Manage.setWindowIcon(icon)
        Manage.setStyleSheet("background-color: #5d5c60;")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Manage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 521, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("font-size: 14px; color: white;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.TableNameComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.TableNameComboBox.setEnabled(True)
        self.TableNameComboBox.setStyleSheet("border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px; color: white;")
        self.TableNameComboBox.setObjectName("TableNameComboBox")
        self.TableNameComboBox.addItem("")
        self.TableNameComboBox.addItem("")
        self.TableNameComboBox.addItem("")
        self.TableNameComboBox.addItem("")
        self.TableNameComboBox.addItem("")
        self.horizontalLayout.addWidget(self.TableNameComboBox)
        self.TableOfRecordWidget = QtWidgets.QTableWidget(Manage)
        self.TableOfRecordWidget.setGeometry(QtCore.QRect(220, 120, 751, 441))
        self.TableOfRecordWidget.setStyleSheet("background: white;\n"
"\n"
"")
        self.TableOfRecordWidget.setObjectName("TableOfRecordWidget")
        self.TableOfRecordWidget.setColumnCount(0)
        self.TableOfRecordWidget.setRowCount(0)
        self.verticalLayoutWidget = QtWidgets.QWidget(Manage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 100, 160, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vecticalButtonLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vecticalButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.vecticalButtonLayout.setObjectName("vecticalButtonLayout")
        self.TapeFormButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.TapeFormButton.setEnabled(True)
        self.TapeFormButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TapeFormButton.setStyleSheet("background-color: #557a95; border: none;color: white;padding: 5px;text-align: center;  text-decoration: none;  font-size: 14px;\n"
"outline: none;")
        self.TapeFormButton.setObjectName("TapeFormButton")
        self.vecticalButtonLayout.addWidget(self.TapeFormButton)
        self.AddRecordButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.AddRecordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AddRecordButton.setStyleSheet("background-color: #557a95; border: none;color: white;padding: 5px;text-align: center;  text-decoration: none;  font-size: 14px;\n"
"outline: none;")
        self.AddRecordButton.setObjectName("AddRecordButton")
        self.vecticalButtonLayout.addWidget(self.AddRecordButton)
        self.DeleteRecordButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.DeleteRecordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DeleteRecordButton.setStyleSheet("background-color: #557a95; border: none;color: white;padding: 5px;text-align: center;  text-decoration: none;  font-size: 14px;\n"
"outline: none;")
        self.DeleteRecordButton.setObjectName("DeleteRecordButton")
        self.vecticalButtonLayout.addWidget(self.DeleteRecordButton)
        self.SearchRecordButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SearchRecordButton.setEnabled(True)
        self.SearchRecordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SearchRecordButton.setStyleSheet("background-color: #557a95; border: none;color: white;padding: 5px;text-align: center;  text-decoration: none;  font-size: 14px;\n"
"outline: none;")
        self.SearchRecordButton.setObjectName("SearchRecordButton")
        self.vecticalButtonLayout.addWidget(self.SearchRecordButton)
        self.ComposeBarGraphButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ComposeBarGraphButton.setEnabled(True)
        self.ComposeBarGraphButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ComposeBarGraphButton.setStyleSheet("background-color: #557a95; border: none;color: white;padding: 5px;text-align: center;  text-decoration: none;  font-size: 14px;\n"
"outline: none;")
        self.ComposeBarGraphButton.setObjectName("ComposeBarGraphButton")
        self.vecticalButtonLayout.addWidget(self.ComposeBarGraphButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Manage)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(630, 11, 161, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FirstCellButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FirstCellButton.setEnabled(True)
        self.FirstCellButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FirstCellButton.setStyleSheet("background-color: #7395ae;  border: none;  color: white;  padding: 5px;  text-align: center; text-decoration: none;  font-size: 14px;outline: none;")
        self.FirstCellButton.setObjectName("FirstCellButton")
        self.verticalLayout.addWidget(self.FirstCellButton)
        self.LastCellButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.LastCellButton.setEnabled(True)
        self.LastCellButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LastCellButton.setStyleSheet("background-color: #7395ae;  border: none;  color: white;  padding: 5px;  text-align: center; text-decoration: none;  font-size: 14px;outline: none;")
        self.LastCellButton.setObjectName("LastCellButton")
        self.verticalLayout.addWidget(self.LastCellButton)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Manage)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(810, 11, 160, 81))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.NextCellButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.NextCellButton.setEnabled(True)
        self.NextCellButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NextCellButton.setStyleSheet("background-color: #7395ae;  border: none;  color: white;  padding: 5px;  text-align: center; text-decoration: none;  font-size: 14px;outline: none;")
        self.NextCellButton.setObjectName("NextCellButton")
        self.verticalLayout_2.addWidget(self.NextCellButton)
        self.PreviousCellButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.PreviousCellButton.setEnabled(True)
        self.PreviousCellButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PreviousCellButton.setStyleSheet("background-color: #7395ae;  border: none;  color: white;  padding: 5px;  text-align: center; text-decoration: none;  font-size: 14px;outline: none;")
        self.PreviousCellButton.setObjectName("PreviousCellButton")
        self.verticalLayout_2.addWidget(self.PreviousCellButton)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Manage)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 460, 160, 121))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ComposeReportButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ComposeReportButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ComposeReportButton.setStyleSheet("background-color: #557a95; border: none;color: white;padding: 5px;text-align: center;  text-decoration: none;  font-size: 14px;\n"
"outline: none;")
        self.ComposeReportButton.setObjectName("ComposeReportButton")
        self.verticalLayout_3.addWidget(self.ComposeReportButton)
        self.ReturnBackButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ReturnBackButton.setEnabled(True)
        self.ReturnBackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ReturnBackButton.setStyleSheet("background-color: #557a95; border: none;color: white;padding: 5px;text-align: center;  text-decoration: none;  font-size: 14px;\n"
"outline: none;")
        self.ReturnBackButton.setObjectName("ReturnBackButton")
        self.verticalLayout_3.addWidget(self.ReturnBackButton)

        self.retranslateUi(Manage)
        self.TableNameComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Manage)

    def retranslateUi(self, Manage):
        _translate = QtCore.QCoreApplication.translate
        Manage.setWindowTitle(_translate("Manage", "Управление строительным магазином"))
        self.label.setText(_translate("Manage", "Выберете таблицу "))
        self.TableNameComboBox.setItemText(0, _translate("Manage", "Клиенты"))
        self.TableNameComboBox.setItemText(1, _translate("Manage", "Заказы"))
        self.TableNameComboBox.setItemText(2, _translate("Manage", "Товары"))
        self.TableNameComboBox.setItemText(3, _translate("Manage", "Сотрудники"))
        self.TableNameComboBox.setItemText(4, _translate("Manage", "Должности"))
        self.TableOfRecordWidget.setSortingEnabled(True)
        self.TapeFormButton.setText(_translate("Manage", "Ленточная форма"))
        self.AddRecordButton.setText(_translate("Manage", "Добавить"))
        self.DeleteRecordButton.setText(_translate("Manage", "Удалить"))
        self.SearchRecordButton.setText(_translate("Manage", "Поиск"))
        self.ComposeBarGraphButton.setText(_translate("Manage", "Гистограмма"))
        self.FirstCellButton.setText(_translate("Manage", "Первая ячейка"))
        self.LastCellButton.setText(_translate("Manage", "Последняя ячейка"))
        self.NextCellButton.setText(_translate("Manage", "Следующая ячейка"))
        self.PreviousCellButton.setText(_translate("Manage", "Предыдущая ячейка"))
        self.ComposeReportButton.setText(_translate("Manage", "Отчет"))
        self.ReturnBackButton.setText(_translate("Manage", "Назад"))
