# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quanly.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_quanly(object):
    def setupUi(self, quanly):
        quanly.setObjectName("quanly")
        quanly.resize(1106, 667)
        self.centralwidget = QtWidgets.QWidget(quanly)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1421, 891))
        self.label.setStyleSheet("background-color: rgb(226, 234, 221);\n"
"border-raidus:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1421, 211))
        self.label_2.setStyleSheet("background-color: rgb(40, 109, 87);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.p_thongke = QtWidgets.QPushButton(self.centralwidget)
        self.p_thongke.setGeometry(QtCore.QRect(530, 150, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.p_thongke.setFont(font)
        self.p_thongke.setStyleSheet("QPushButton#p_thongke{\n"
"background-color: qlineargradient(spread:pad, x1:0.0199005, y1:0.204, x2:0.726, y2:0.7105, stop:0.19403 rgba(63, 183, 186, 255), stop:0.900498 rgba(115, 214, 139, 255));\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton#p_thongke::hover{\n"
"    background-color:rgb(255, 170, 0);\n"
"}\n"
"")
        self.p_thongke.setObjectName("p_thongke")
        self.p_trangchu = QtWidgets.QPushButton(self.centralwidget)
        self.p_trangchu.setGeometry(QtCore.QRect(20, 150, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.p_trangchu.setFont(font)
        self.p_trangchu.setStyleSheet("QPushButton#p_trangchu{\n"
"background-color: qlineargradient(spread:pad, x1:0.0199005, y1:0.204, x2:0.726, y2:0.7105, stop:0.19403 rgba(63, 183, 186, 255), stop:0.900498 rgba(115, 214, 139, 255));\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton#p_trangchu::hover{\n"
"    background-color:rgb(255, 170, 0);\n"
"}\n"
"")
        self.p_trangchu.setObjectName("p_trangchu")
        self.p_quanly = QtWidgets.QPushButton(self.centralwidget)
        self.p_quanly.setGeometry(QtCore.QRect(360, 150, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.p_quanly.setFont(font)
        self.p_quanly.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0199005, y1:0.204, x2:0.726, y2:0.7105, stop:0.19403 rgba(50, 148, 150, 255), stop:0.900498 rgba(81, 152, 98, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px ;\n"
"")
        self.p_quanly.setObjectName("p_quanly")
        self.p_muonvatra = QtWidgets.QPushButton(self.centralwidget)
        self.p_muonvatra.setGeometry(QtCore.QRect(180, 150, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.p_muonvatra.setFont(font)
        self.p_muonvatra.setStyleSheet("QPushButton#p_muonvatra{\n"
"background-color: qlineargradient(spread:pad, x1:0.0199005, y1:0.204, x2:0.726, y2:0.7105, stop:0.19403 rgba(63, 183, 186, 255), stop:0.900498 rgba(115, 214, 139, 255));\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton#p_muonvatra::hover{\n"
"    background-color:rgb(255, 170, 0);\n"
"}\n"
"")
        self.p_muonvatra.setObjectName("p_muonvatra")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1100, 10, 311, 201))
        self.label_3.setStyleSheet("image: url(:/newPrefix/HinhAnh/background-trangchu1-removebg-preview.png);")
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 101, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 330, 111, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 379, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 439, 111, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 499, 81, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tb_quanly = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_quanly.setGeometry(QtCore.QRect(330, 250, 751, 331))
        self.tb_quanly.setStyleSheet("background-color: rgb(159, 159, 159);")
        self.tb_quanly.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tb_quanly.setAlternatingRowColors(True)
        self.tb_quanly.setRowCount(0)
        self.tb_quanly.setObjectName("tb_quanly")
        self.tb_quanly.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tb_quanly.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tb_quanly.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tb_quanly.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tb_quanly.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tb_quanly.setHorizontalHeaderItem(4, item)
        self.tb_quanly.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_quanly.horizontalHeader().setDefaultSectionSize(132)
        self.tb_quanly.horizontalHeader().setSortIndicatorShown(False)
        self.tb_quanly.horizontalHeader().setStretchLastSection(True)
        self.txt_ms = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_ms.setGeometry(QtCore.QRect(150, 259, 121, 31))
        self.txt_ms.setObjectName("txt_ms")
        self.txt_tensach = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_tensach.setGeometry(QtCore.QRect(150, 319, 121, 31))
        self.txt_tensach.setObjectName("txt_tensach")
        self.txt_soluong = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_soluong.setGeometry(QtCore.QRect(150, 378, 121, 31))
        self.txt_soluong.setObjectName("txt_soluong")
        self.txt_Nhaxuatban = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_Nhaxuatban.setGeometry(QtCore.QRect(150, 428, 121, 31))
        self.txt_Nhaxuatban.setObjectName("txt_Nhaxuatban")
        self.txt_tacgia = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_tacgia.setGeometry(QtCore.QRect(150, 490, 121, 31))
        self.txt_tacgia.setObjectName("txt_tacgia")
        self.p_them = QtWidgets.QPushButton(self.centralwidget)
        self.p_them.setGeometry(QtCore.QRect(20, 550, 93, 28))
        self.p_them.setObjectName("p_them")
        self.p_sua = QtWidgets.QPushButton(self.centralwidget)
        self.p_sua.setGeometry(QtCore.QRect(150, 550, 93, 28))
        self.p_sua.setObjectName("p_sua")
        self.p_xoa = QtWidgets.QPushButton(self.centralwidget)
        self.p_xoa.setGeometry(QtCore.QRect(70, 590, 93, 28))
        self.p_xoa.setObjectName("p_xoa")
        self.p_tim = QtWidgets.QPushButton(self.centralwidget)
        self.p_tim.setGeometry(QtCore.QRect(360, 600, 93, 28))
        self.p_tim.setObjectName("p_tim")
        self.txt_timkiemqly = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_timkiemqly.setGeometry(QtCore.QRect(490, 600, 581, 31))
        self.txt_timkiemqly.setObjectName("txt_timkiemqly")
        self.p_dx = QtWidgets.QPushButton(self.centralwidget)
        self.p_dx.setGeometry(QtCore.QRect(700, 150, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.p_dx.setFont(font)
        self.p_dx.setStyleSheet("QPushButton#p_dx{\n"
"background-color: qlineargradient(spread:pad, x1:0.0199005, y1:0.204, x2:0.726, y2:0.7105, stop:0.19403 rgba(63, 183, 186, 255), stop:0.900498 rgba(115, 214, 139, 255));\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton#p_dx::hover{\n"
"    background-color:rgb(255, 170, 0);\n"
"}\n"
"")
        self.p_dx.setObjectName("p_dx")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(40, 30, 891, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:rgb(255, 255, 255),\n"
"")
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(890, 40, 201, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("Hinhanh/logo1.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        quanly.setCentralWidget(self.centralwidget)

        self.retranslateUi(quanly)
        QtCore.QMetaObject.connectSlotsByName(quanly)

    def retranslateUi(self, quanly):
        _translate = QtCore.QCoreApplication.translate
        quanly.setWindowTitle(_translate("quanly", "MainWindow"))
        self.p_thongke.setText(_translate("quanly", "Thống kê"))
        self.p_trangchu.setText(_translate("quanly", "Trang chủ"))
        self.p_quanly.setText(_translate("quanly", "Quản lý sách"))
        self.p_muonvatra.setText(_translate("quanly", "Mượn và trả"))
        self.label_4.setText(_translate("quanly", "Mã sách"))
        self.label_5.setText(_translate("quanly", "Tên sách"))
        self.label_6.setText(_translate("quanly", "Số lượng"))
        self.label_7.setText(_translate("quanly", "Nhà xuất bản"))
        self.label_8.setText(_translate("quanly", "Tên tác giả"))
        item = self.tb_quanly.horizontalHeaderItem(0)
        item.setText(_translate("quanly", "Mã sách"))
        item = self.tb_quanly.horizontalHeaderItem(1)
        item.setText(_translate("quanly", "tên sách"))
        item = self.tb_quanly.horizontalHeaderItem(2)
        item.setText(_translate("quanly", "Số lượng"))
        item = self.tb_quanly.horizontalHeaderItem(3)
        item.setText(_translate("quanly", "Nhà xuất bản"))
        item = self.tb_quanly.horizontalHeaderItem(4)
        item.setText(_translate("quanly", "Tên tác giả"))
        self.p_them.setText(_translate("quanly", "Thêm"))
        self.p_sua.setText(_translate("quanly", "Sửa"))
        self.p_xoa.setText(_translate("quanly", "Xóa"))
        self.p_tim.setText(_translate("quanly", "Tìm kiếm"))
        self.p_dx.setText(_translate("quanly", "Đăng xuất"))
        self.label_15.setText(_translate("quanly", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">HỆ THỐNG THƯ VIỆN SÁCH ĐIỆN TỬ</span></p></body></html>"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    quanly = QtWidgets.QMainWindow()
    ui = Ui_quanly()
    ui.setupUi(quanly)
    quanly.show()
    sys.exit(app.exec_())
