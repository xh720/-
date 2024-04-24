# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtGui import QBrush, QColor, QFont
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QSize
from PyQt5.QtGui import *


class itemjinzhi(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def createEditor(self, Parent, Option: QtWidgets.QStyleOptionViewItem, modeIndex: QtCore.QModelIndex):
        wdt = super().createEditor(Parent, Option, modeIndex)
        validator = QDoubleValidator(-10000.0, 10000.0, 3)
        wdt.setValidator(validator)
        return wdt

class ProvinceDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def createEditor(self, Parent, Option: QtWidgets.QStyleOptionViewItem, modeIndex: QtCore.QModelIndex):
        size = Option.rect.size()
        tb = Option.widget
        row = modeIndex.row()
        cellitem = tb.item(row, 0)
        Province = cellitem.text()
        _translate = QtCore.QCoreApplication.translate
        combobox = QtWidgets.QComboBox(Parent)
        combobox.addItem(_translate("Form", "系统操作"))
        combobox.addItem(_translate("Form","流程控制"))
        combobox.addItem(_translate("Form","输出口设置"))
        combobox.addItem(_translate("Form","回零运动"))
        combobox.addItem(_translate("Form","插补运动"))
        combobox.addItem(_translate("Form","独立运动"))
        combobox.setCurrentText(Province)
        combobox.setFixedSize(size)
        return combobox


class CityDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._translate = QtCore.QCoreApplication.translate

    def createEditor(self, Parent, Option: QtWidgets.QStyleOptionViewItem, modeIndex: QtCore.QModelIndex):
        tb = Option.widget
        row = modeIndex.row()
        cellitem = tb.item(row, 0)
        Province = cellitem.text()
        cellitem2 = tb.item(row, 1)
        City = cellitem2.text()
        size = Option.rect.size()
        combobox = QtWidgets.QComboBox(Parent)

        citys = {self._translate("Form", "系统操作"): [self._translate("Form", "停止"), self._translate("Form", "启动"),
                                                        self._translate("Form", "暂停"), self._translate("Form", "恢复"),
                                                        self._translate("Form", "延时等待"),
                                                        self._translate("Form", "等待电机完成"),
                                                        self._translate("Form", "停止电机运动"),
                                                        self._translate("Form", "常等待")],
                      self._translate("Form", "流程控制"): [self._translate("Form", "程序间跳转"),
                                                        self._translate("Form", "程序循环"),
                                                        self._translate("Form", "输入跳转"),
                                                        self._translate("Form", "开启输入中断"),
                                                        self._translate("Form", "关闭输入中断")],
                      self._translate("Form", "输出口设置"): [self._translate("Form", "输出口设置")],
                      self._translate("Form", "回零运动"): [self._translate("Form", "设置回零速度"),
                                                        self._translate("Form", "启动回零")],
                      self._translate("Form", "插补运动"): [self._translate("Form", "设置点位速度"),
                                                        self._translate("Form", "三轴相对运动"),
                                                        self._translate("Form", "单轴绝对运动"),
                                                        self._translate("Form", "XY绝对运动"),
                                                        self._translate("Form", "XZ绝对运动"),
                                                        self._translate("Form", "YZ绝对运动"),
                                                        self._translate("Form", "三轴绝对运动"),
                                                        self._translate("Form", "XY圆弧插补"),
                                                        self._translate("Form", "XZ圆弧插补"),
                                                        self._translate("Form", "YZ圆弧插补")],
                      self._translate("Form", "独立运动"): [self._translate("Form", "独立运动速度"),
                                                        self._translate("Form", "相对运动"),
                                                        self._translate("Form", "X绝对运动"),
                                                        self._translate("Form", "Y绝对运动"),
                                                        self._translate("Form", "Z绝对运动")]}
        if citys[Province] != None:
            citylist = citys[Province]
            combobox.addItems(citylist)
            combobox.setCurrentText(City)
        combobox.setFixedSize(size)
        return combobox

    def initUI(self):
        self.setWindowTitle('标题')
        # self.setWindowIcon(QIcon('C:/Users/Administrator/Desktop/icon.jpg'))
        self.show()

class PushButtonEx(QPushButton):  #控件  继承属性
    downpressed = pyqtSignal()
    uppressed = pyqtSignal()

    def __init__(self,parent):
        super(PushButtonEx, self).__init__(parent=parent)

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == Qt.LeftButton:
            self.downpressed.emit()

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == Qt.LeftButton:
            self.uppressed.emit()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        _translate = QtCore.QCoreApplication.translate
        Form.resize(820, 500)  # 整个界面的大小
        Form.setFixedSize(820, 515)

        # ---------------------------formGroupBox是串口设置子区域--------------------------------------
        # 打开按钮和关闭按钮以及两个按钮的排版格式
        self.open_button = QtWidgets.QPushButton(Form)
        self.open_button.setObjectName("open_button")
        self.open_button.setGeometry(QtCore.QRect(17, 20, 115, 35))
        self.open_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(225,127,83)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(124,252,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(220,220,220)}""")
        self.open_button.setFont(QFont("华文新魏", 16))

        self.stop_button = QtWidgets.QPushButton(Form)
        self.stop_button.setObjectName("stop_button")
        self.stop_button.setGeometry(QtCore.QRect(17, 75, 115, 35))
        self.stop_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(189,252,201)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,227,132)}""")
        self.stop_button.setFont(QFont("华文新魏", 16))

        self.Peizhi_button = QtWidgets.QPushButton(Form)  # 手动输入按钮
        self.Peizhi_button.setGeometry(QtCore.QRect(17, 130, 115, 35))
        self.Peizhi_button.setObjectName("self.Peizhi_button")
        self.Peizhi_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(212,180,83)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(245,222,179)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(61,145,64)}""")
        self.Peizhi_button.setFont(QFont("华文新魏", 16))


        self.Manual_input_button = QtWidgets.QPushButton(Form)  # 手动输入按钮
        self.Manual_input_button.setGeometry(QtCore.QRect(17, 185, 115, 35))
        self.Manual_input_button.setObjectName("self.Manual_input_button")
        self.Manual_input_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(64,224,208)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,3)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Manual_input_button.setFont(QFont("华文新魏", 16))



        self.Parameter_setting_button = QtWidgets.QPushButton(Form)  # 参数设置按钮
        self.Parameter_setting_button.setGeometry(QtCore.QRect(17, 240, 115, 35))
        self.Parameter_setting_button.setObjectName("Parameter_setting_button")
        self.Parameter_setting_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(56,196,110)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(245,222,179)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,248,220)}""")
        self.Parameter_setting_button.setFont(QFont("华文新魏", 16))

        self.Editing_program_button = QtWidgets.QPushButton(Form)  # 程序编辑按钮
        self.Editing_program_button.setGeometry(QtCore.QRect(17, 295, 115, 35))
        self.Editing_program_button.setObjectName("self.Manual_input_button")
        self.Editing_program_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,215,0)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(210,105,30)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(250,255,240)}""")
        self.Editing_program_button.setFont(QFont("华文新魏", 16))

        self.Line_Arc_button = QtWidgets.QPushButton(Form)
        self.Line_Arc_button.setObjectName("Line_Arc_button")
        self.Line_Arc_button.setGeometry(QtCore.QRect(17, 350, 115, 35))
        self.Line_Arc_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(225,127,83)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(252,230,201)}""")
        self.Line_Arc_button.setFont(QFont("华文新魏", 16))

        self.About_button = QtWidgets.QPushButton(Form)  # 程序编辑按钮
        self.About_button.setGeometry(QtCore.QRect(17, 405, 115, 35))
        self.About_button.setObjectName("self.About_button")
        self.About_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(135,206,235)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(130,255,255)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(252,230,201)}""")
        self.About_button.setFont(QFont("华文新魏", 16))

        self.s1__box_23 = QtWidgets.QComboBox(Form)
        self.s1__box_23.setObjectName("s1__box_23")
        self.s1__box_23.setGeometry(QtCore.QRect(17, 460, 115, 35))
        self.s1__box_23.setFont(QFont("华文楷书", 14))
        self.s1__box_23.setStyleSheet("border:4px groove gray;border-radius:10px;"
                                      "padding:4px 6px;background-color:rgb(255,250,240)")
        self.s1__box_23.addItem("")
        self.s1__box_23.addItem("")
        self.s1__box_23.addItem("")

        # ----------------------------------------todo 串口状态子区域（删除）--------------------------------------------

        # ------------------todo self.verticalGroupBox_1是接收区那个区（删除）--------------------------------

        # ---------------todo self.verticalGroupBox_2是发送区那个区（删除）--------------------------------

        # todo self.verticalGroupBox_3是手动操作那个子区--------------------------------
        self.s1__lb_42 = QtWidgets.QLabel(Form)  # 已连接控制器那个标签
        self.s1__lb_42.setObjectName("self.s1__lb_42")
        self.s1__lb_42.setGeometry(QtCore.QRect(175, 5, 300, 20))

        self.verticalGroupBox_3 = QtWidgets.QGroupBox(Form)  # 手动操作那个集群
        self.verticalGroupBox_3.setGeometry(QtCore.QRect(160, 30, 640, 460))
        self.verticalGroupBox_3.setObjectName("verticalGroupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalGroupBox_3)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # self.s1__lb_43 = QtWidgets.QLabel(self.verticalGroupBox_3)  # 未连接显示的那个标签
        # self.s1__lb_43.setObjectName("self.s1__lb_43")
        # self.s1__lb_43.setGeometry(QtCore.QRect(30, 25, 40, 20))

        self.CheckBox_19 = QtWidgets.QCheckBox(self.verticalGroupBox_3)  # 上电是否自动运行
        self.CheckBox_19.setGeometry(QtCore.QRect(60, 25, 100, 20))
        self.CheckBox_19.setObjectName("CheckBox_19")

        self.Para_save_button1 = QtWidgets.QPushButton(self.verticalGroupBox_3)
        self.Para_save_button1.setObjectName("Para_save_button1")
        self.Para_save_button1.setGeometry(QtCore.QRect(200, 30, 60, 35))
        self.Para_save_button1.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(176,224,230)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(130,255,255)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(252,230,201)}""")
        self.Para_save_button1.setFont(QFont("Times New Roman", 10.5))


        self.X_minus_button = PushButtonEx(self.verticalGroupBox_3)
        self.X_minus_button.setObjectName("X_minus_button")
        self.X_minus_button.setGeometry(QtCore.QRect(20, 62, 50, 40))
        self.X_minus_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(135,206,235)}
        
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        
        QPushButton:Clicked{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(176,224,230)}""")
        self.X_minus_button.setFont(QFont("Times New Roman", 10.5))

        self.X_plus_button = PushButtonEx(self.verticalGroupBox_3)
        self.X_plus_button.setObjectName("X_plus_button")
        self.X_plus_button.setGeometry(QtCore.QRect(82, 62, 50, 40))
        self.X_plus_button.setStyleSheet(
            "border:2px groove gray;border-radius:10px;"
            "padding:2px 4px;background-color:rgb(176,224,230)")
        self.X_plus_button.setFont(QFont("Times New Roman", 10.5))

        self.BackX_button = QtWidgets.QPushButton(self.verticalGroupBox_3)
        self.BackX_button.setObjectName("self.BackX_button")
        self.BackX_button.setGeometry(QtCore.QRect(144, 62, 50, 40))
        self.BackX_button.setStyleSheet(
            "border:2px groove gray;border-radius:10px;"
            "padding:2px 4px;background-color:rgb(176,224,230)")
        self.BackX_button.setFont(QFont("Times New Roman", 10.5))

        self.Y_minus_button = PushButtonEx(self.verticalGroupBox_3)
        self.Y_minus_button.setObjectName("Y_minus_button")
        self.Y_minus_button.setGeometry(QtCore.QRect(20, 117, 50, 40))
        self.Y_minus_button.setStyleSheet(
            "border:2px groove gray;border-radius:10px;"
            "padding:2px 4px;background-color:rgb(176,224,230)")
        self.Y_minus_button.setFont(QFont("Times New Roman", 10.5))

        self.Y_plus_button = PushButtonEx(self.verticalGroupBox_3)
        self.Y_plus_button.setObjectName("Y_plus_button")
        self.Y_plus_button.setGeometry(QtCore.QRect(82, 117, 50, 40))
        self.Y_plus_button.setStyleSheet(
            "border:2px groove gray;border-radius:10px;"
            "padding:2px 4px;background-color:rgb(176,224,230)")
        self.Y_plus_button.setFont(QFont("Times New Roman", 10.5))

        self.BackY_button = QtWidgets.QPushButton(self.verticalGroupBox_3)
        self.BackY_button.setObjectName("self.BackY_button")
        self.BackY_button.setGeometry(QtCore.QRect(144, 117, 50, 40))
        self.BackY_button.setStyleSheet(
            "border:2px groove gray;border-radius:10px;"
            "padding:2px 4px;background-color:rgb(176,224,230)")
        self.BackY_button.setFont(QFont("Times New Roman", 10.5))

        self.Z_minus_button = PushButtonEx(self.verticalGroupBox_3)
        self.Z_minus_button.setObjectName("Z_minus_button")
        self.Z_minus_button.setGeometry(QtCore.QRect(20, 172, 50, 40))
        self.Z_minus_button.setStyleSheet(
            "border:2px groove gray;border-radius:10px;"
            "padding:2px 4px;background-color:rgb(176,224,230)")
        self.Z_minus_button.setFont(QFont("Times New Roman", 10.5))

        self.Z_plus_button = PushButtonEx(self.verticalGroupBox_3)
        self.Z_plus_button.setObjectName("Z_plus_button")
        self.Z_plus_button.setGeometry(QtCore.QRect(82, 172, 50, 40))
        self.Z_plus_button.setStyleSheet(
            "border:2px groove gray;border-radius:10px;"
            "padding:2px 4px;background-color:rgb(176,224,230)")
        self.Z_plus_button.setFont(QFont("Times New Roman", 10.5))

        self.BackZ_button = QtWidgets.QPushButton(self.verticalGroupBox_3)
        self.BackZ_button.setObjectName("self.BackZ_button")
        self.BackZ_button.setGeometry(QtCore.QRect(144, 172, 50, 40))
        self.BackZ_button.setStyleSheet(
            "border:2px groove gray;border-radius:10px;"
            "padding:2px 4px;background-color:rgb(176,224,230)")
        self.BackZ_button.setFont(QFont("Times New Roman", 10.5))

        self.BackZero_button = QtWidgets.QPushButton(self.verticalGroupBox_3)
        self.BackZero_button.setObjectName("self.BackZero_button")
        self.BackZero_button.setGeometry(QtCore.QRect(210, 115, 50, 45))
        self.BackZero_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,70,70)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(130,180,177)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(90,230,201)}""")
        self.BackZero_button.setFont(QFont("华为楷书-加粗", 12))

        self.s1__lb_13 = QtWidgets.QLabel(self.verticalGroupBox_3)  # 这个是手动速度的标签
        self.s1__lb_13.setObjectName("self.s1__lb_13")
        self.s1__lb_13.setGeometry(QtCore.QRect(25, 230, 53, 40))

        # todo 按照self.lineEdit_4 设置文本框只能输入数字
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalGroupBox_3)  # 这个是手动速度标签的文本框
        self.lineEdit_4.setObjectName("self.lineEdit_4")
        self.lineEdit_4.setGeometry(QtCore.QRect(85, 234, 88, 30))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_4.setProperty("type", 1)

        self.dw_1 = QtWidgets.QLabel(self.verticalGroupBox_3)  # 这个是手动速度单位
        self.dw_1.setObjectName("self.dw_1")
        self.dw_1.setGeometry(QtCore.QRect(177, 234, 30, 30))

        # todo 按照self.Enter1_button设置按钮形状
        self.Enter1_button = QtWidgets.QPushButton(self.verticalGroupBox_3)  # 确定按钮
        self.Enter1_button.setObjectName("self.Enter1_button")
        self.Enter1_button.setGeometry(QtCore.QRect(222, 231, 40, 35))
        self.Enter1_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,230,160)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(130,180,177)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(90,230,201)}""")
        self.Enter1_button.setFont(QFont("Times New Roman", 10.5))

        self.CheckBox_20= QtWidgets.QCheckBox(self.verticalGroupBox_3)
        self.CheckBox_20.setGeometry(QtCore.QRect(25, 290, 13, 20))
        self.CheckBox_20.setObjectName("CheckBox_19")

        self.s1__lb_39 = QtWidgets.QLabel(self.verticalGroupBox_3)
        self.s1__lb_39.setGeometry(QtCore.QRect(42, 290, 53, 20))
        self.s1__lb_39.setObjectName("s1__lb_39")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalGroupBox_3)  # 步进文本框
        self.lineEdit_5.setObjectName("self.lineEdit_5")
        self.lineEdit_5.setGeometry(QtCore.QRect(103, 285, 70, 30))
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_5.setProperty("type", 1)

        self.dw_2 = QtWidgets.QLabel(self.verticalGroupBox_3)  # 步进单位
        self.dw_2.setObjectName("self.dw_2")
        self.dw_2.setGeometry(QtCore.QRect(177, 285, 30, 30))

        self.Enter2_button = QtWidgets.QPushButton(self.verticalGroupBox_3)  # 第二个确定按钮
        self.Enter2_button.setObjectName("self.Enter2_button")
        self.Enter2_button.setGeometry(QtCore.QRect(222, 284, 40, 35))
        self.Enter2_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,230,160)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(130,180,177)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(90,230,201)}""")
        self.Enter2_button.setFont(QFont("Times New Roman", 10.5))

        self.verticalGroupBox_6 = QtWidgets.QGroupBox(self.verticalGroupBox_3)  # 手动操作左半边下面的输出口选择
        self.verticalGroupBox_6.setGeometry(QtCore.QRect(25, 335, 225, 110))
        self.verticalGroupBox_6.setObjectName("verticalGroupBox_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalGroupBox_6)
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        # CheckBox_1---CheckBox_4表示的是输出口选择
        self.CheckBox_1 = QtWidgets.QCheckBox(self.verticalGroupBox_6)
        self.CheckBox_1.setGeometry(QtCore.QRect(30, 20, 50, 30))
        self.CheckBox_1.setObjectName("CheckBox_1")

        self.CheckBox_2 = QtWidgets.QCheckBox(self.verticalGroupBox_6)
        self.CheckBox_2.setGeometry(QtCore.QRect(125, 20, 50, 30))
        self.CheckBox_2.setObjectName("CheckBox_2")

        self.CheckBox_3 = QtWidgets.QCheckBox(self.verticalGroupBox_6)
        self.CheckBox_3.setGeometry(QtCore.QRect(30, 65, 50, 30))
        self.CheckBox_3.setObjectName("CheckBox_3")

        self.CheckBox_4 = QtWidgets.QCheckBox(self.verticalGroupBox_6)
        self.CheckBox_4.setGeometry(QtCore.QRect(125, 65, 50, 30))
        self.CheckBox_4.setObjectName("CheckBox_4")

        self.verticalGroupBox_7 = QtWidgets.QGroupBox(self.verticalGroupBox_3)  # 手动操作界面的右半边机器状态
        self.verticalGroupBox_7.setGeometry(QtCore.QRect(280, 20, 340, 425))
        self.verticalGroupBox_7.setObjectName("verticalGroupBox_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalGroupBox_7)
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.verticalGroupBox_13 = QtWidgets.QGroupBox(self.verticalGroupBox_7)
        self.verticalGroupBox_13.setGeometry(QtCore.QRect(17, 25, 310, 109))
        self.verticalGroupBox_13.setObjectName("verticalGroupBox_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalGroupBox_13)
        self.verticalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")

        self.s1__lb_14 = QtWidgets.QLabel(self.verticalGroupBox_13)  # X轴位置标签
        self.s1__lb_14.setObjectName("self.s1__lb_14")
        self.s1__lb_14.setGeometry(QtCore.QRect(20, 20, 55, 25))

        self.lineEdit_31 = QtWidgets.QLineEdit(self.verticalGroupBox_13)  # 显示X轴位置的文本框
        self.lineEdit_31.setObjectName("self.lineEdit_31")
        self.lineEdit_31.setGeometry(QtCore.QRect(80, 20, 60, 25))
        self.lineEdit_31.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_31.setStyleSheet("background-color:rgb(240,255,240)")
        self.s1__lb_44 = QtWidgets.QLabel(self.verticalGroupBox_13)  # 显示位置的标签
        self.s1__lb_44.setObjectName("self.s1__lb_44")
        self.s1__lb_44.setGeometry(QtCore.QRect(80, 20, 60, 25))
        self.s1__lb_44.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.s1__lb_15 = QtWidgets.QLabel(self.verticalGroupBox_13)  # Y轴位置标签
        self.s1__lb_15.setObjectName("self.s1__lb_15")
        self.s1__lb_15.setGeometry(QtCore.QRect(160, 20, 55, 25))

        self.lineEdit_32 = QtWidgets.QLineEdit(self.verticalGroupBox_13)  # 显示Y轴位置的文本框
        self.lineEdit_32.setObjectName("self.lineEdit_32")
        self.lineEdit_32.setGeometry(QtCore.QRect(220, 20, 60, 25))
        self.lineEdit_32.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_32.setStyleSheet("background-color:rgb(240,255,240)")
        self.s1__lb_45 = QtWidgets.QLabel(self.verticalGroupBox_13)  # 显示位置的标签
        self.s1__lb_45.setObjectName("self.s1__lb_45")
        self.s1__lb_45.setGeometry(QtCore.QRect(220, 20, 60, 25))
        self.s1__lb_45.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.s1__lb_16 = QtWidgets.QLabel(self.verticalGroupBox_13)  # Z轴位置标签
        self.s1__lb_16.setObjectName("self.s1__lb_16")
        self.s1__lb_16.setGeometry(QtCore.QRect(20, 68, 55, 25))

        self.lineEdit_33 = QtWidgets.QLineEdit(self.verticalGroupBox_13)  # 显示Z轴位置的文本框
        self.lineEdit_33.setObjectName("self.lineEdit_33")
        self.lineEdit_33.setGeometry(QtCore.QRect(80, 68, 60, 25))
        self.lineEdit_33.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_33.setStyleSheet("background-color:rgb(240,255,240)")
        self.s1__lb_46 = QtWidgets.QLabel(self.verticalGroupBox_13)  # 显示位置的标签
        self.s1__lb_46.setObjectName("self.s1__lb_46")
        self.s1__lb_46.setGeometry(QtCore.QRect(80, 68, 60, 25))
        self.s1__lb_46.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.verticalGroupBox_8 = QtWidgets.QGroupBox(self.verticalGroupBox_7)  # 手动操作界面右半边机器状态里边的输入口状态
        self.verticalGroupBox_8.setGeometry(QtCore.QRect(17, 153, 310, 92))
        self.verticalGroupBox_8.setObjectName("verticalGroupBox_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalGroupBox_8)
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.CheckBox_5 = QtWidgets.QCheckBox(self.verticalGroupBox_8)  # 5 7 8 9 10 11 是输入口状态里边的几个选择
        self.CheckBox_5.setGeometry(QtCore.QRect(30, 23, 45, 20))
        self.CheckBox_5.setObjectName("CheckBox_5")
        self.CheckBox_5.setDisabled(True)

        self.CheckBox_6 = QtWidgets.QCheckBox(self.verticalGroupBox_8)
        self.CheckBox_6.setGeometry(QtCore.QRect(95, 23, 45, 20))
        self.CheckBox_6.setObjectName("CheckBox_6")
        self.CheckBox_6.setDisabled(True)

        self.CheckBox_7 = QtWidgets.QCheckBox(self.verticalGroupBox_8)
        self.CheckBox_7.setGeometry(QtCore.QRect(160, 23, 45, 20))
        self.CheckBox_7.setObjectName("CheckBox_7")
        self.CheckBox_7.setDisabled(True)

        self.CheckBox_8 = QtWidgets.QCheckBox(self.verticalGroupBox_8)
        self.CheckBox_8.setGeometry(QtCore.QRect(225, 23, 45, 20))
        self.CheckBox_8.setObjectName("CheckBox_8")
        self.CheckBox_8.setDisabled(True)

        self.CheckBox_9 = QtWidgets.QCheckBox(self.verticalGroupBox_8)
        self.CheckBox_9.setGeometry(QtCore.QRect(45, 56, 50, 20))
        self.CheckBox_9.setObjectName("CheckBox_9")
        self.CheckBox_9.setDisabled(True)

        self.CheckBox_10 = QtWidgets.QCheckBox(self.verticalGroupBox_8)
        self.CheckBox_10.setGeometry(QtCore.QRect(120, 56, 50, 20))
        self.CheckBox_10.setObjectName("CheckBox_10")
        self.CheckBox_10.setDisabled(True)

        self.CheckBox_11 = QtWidgets.QCheckBox(self.verticalGroupBox_8)
        self.CheckBox_11.setGeometry(QtCore.QRect(195, 56, 50, 20))
        self.CheckBox_11.setObjectName("CheckBox_11")
        self.CheckBox_11.setDisabled(True)

        self.verticalGroupBox_9 = QtWidgets.QGroupBox(self.verticalGroupBox_7)  # 手动操作界面右半边机器状态里边的输入口状态
        self.verticalGroupBox_9.setGeometry(QtCore.QRect(17, 266, 310, 60))
        self.verticalGroupBox_9.setObjectName("verticalGroupBox_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalGroupBox_9)
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.CheckBox_12 = QtWidgets.QCheckBox(self.verticalGroupBox_9)
        self.CheckBox_12.setGeometry(QtCore.QRect(25, 26, 45, 20))
        self.CheckBox_12.setObjectName("CheckBox_12")
        self.CheckBox_12.setDisabled(True)

        self.CheckBox_13 = QtWidgets.QCheckBox(self.verticalGroupBox_9)
        self.CheckBox_13.setGeometry(QtCore.QRect(93, 26, 45, 20))
        self.CheckBox_13.setObjectName("CheckBox_13")
        self.CheckBox_13.setDisabled(True)

        self.CheckBox_14 = QtWidgets.QCheckBox(self.verticalGroupBox_9)
        self.CheckBox_14.setGeometry(QtCore.QRect(161, 26, 45, 20))
        self.CheckBox_14.setObjectName("CheckBox_14")
        self.CheckBox_14.setDisabled(True)

        self.CheckBox_15 = QtWidgets.QCheckBox(self.verticalGroupBox_9)
        self.CheckBox_15.setGeometry(QtCore.QRect(229, 26, 45, 20))
        self.CheckBox_15.setObjectName("CheckBox_15")
        self.CheckBox_15.setDisabled(True)

        self.verticalGroupBox_12 = QtWidgets.QGroupBox(self.verticalGroupBox_7)  # 手动操作界面右半边机器状态里边的输入口状态
        self.verticalGroupBox_12.setGeometry(QtCore.QRect(17, 344, 310, 63))
        self.verticalGroupBox_12.setObjectName("verticalGroupBox_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalGroupBox_9)
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")

        self.CheckBox_16 = QtWidgets.QCheckBox(self.verticalGroupBox_12)
        self.CheckBox_16.setGeometry(QtCore.QRect(25, 25, 70, 20))
        self.CheckBox_16.setObjectName("CheckBox_16")
        self.CheckBox_16.setDisabled(True)

        self.CheckBox_17 = QtWidgets.QCheckBox(self.verticalGroupBox_12)
        self.CheckBox_17.setGeometry(QtCore.QRect(120, 25, 70, 20))
        self.CheckBox_17.setObjectName("CheckBox_17")
        self.CheckBox_17.setDisabled(True)
        # a = self.CheckBox_17.palette()
        # b = a.color(QPalette.Normal,QPalette.Text)
        # print("b",b)
        # a.setColor(QPalette.Disabled,QPalette.Text,b)



        self.CheckBox_18 = QtWidgets.QCheckBox(self.verticalGroupBox_12)
        self.CheckBox_18.setGeometry(QtCore.QRect(215, 25, 70, 20))
        self.CheckBox_18.setObjectName("CheckBox_18")
        self.CheckBox_18.setDisabled(True)

        # -todo 下面是按钮以及前边显示的标签（删除）-------------------------------
        # todo 发送区那个文本框（写功能程序的时候需要用到）
        # #todo 接收区的文本框（写功能程序的时候需要用到）
        # --------------------------------todo 主界面的一些内容（删除）------------------------------------
        # todo 写新界面的功能程序的时候用下载程序按钮代替（写功能程序的时候改一下）

        # ------------todo 切换界面 -------------切换至参数设置界面----------------------
        self.GroupBoxPara = QtWidgets.QGroupBox(Form)
        self.GroupBoxPara.setGeometry(QtCore.QRect(160, 30, 640, 460))
        self.GroupBoxPara.setObjectName("GroupBoxPara")
        self.verticalLayout_para = QtWidgets.QVBoxLayout(self.GroupBoxPara)
        self.verticalLayout_para.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_para.setObjectName("verticalLayout_para")

        self.verticalGroupBox_10 = QtWidgets.QGroupBox(self.GroupBoxPara)  # 手动操作左半边下面的输出口选择
        self.verticalGroupBox_10.setGeometry(QtCore.QRect(13, 25, 610, 210))
        self.verticalGroupBox_10.setObjectName("verticalGroupBox_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalGroupBox_10)
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        self.verticalGroupBox_11 = QtWidgets.QGroupBox(self.GroupBoxPara)  # 手动操作左半边下面的输出口选择
        self.verticalGroupBox_11.setGeometry(QtCore.QRect(25, 255, 580, 120))
        self.verticalGroupBox_11.setObjectName("verticalGroupBox_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalGroupBox_11)
        self.verticalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")

        self.s1__lb_18 = QtWidgets.QLabel(self.verticalGroupBox_11)  # X轴系统加速度标签
        self.s1__lb_18.setObjectName("self.s1__lb_18")
        self.s1__lb_18.setGeometry(QtCore.QRect(30, 25, 85, 25))
        self.s1__lb_18.setFont(QFont("华文楷书", 9))
        self.s1__lb_18.setStyleSheet("color:rgb(8,12,84);")

        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalGroupBox_11)  # X轴系统加速度标签后面的文本框
        self.lineEdit_9.setObjectName("self.lineEdit_9")
        self.lineEdit_9.setGeometry(QtCore.QRect(125, 25, 80, 25))
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_9.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))

        self.dw_3 = QtWidgets.QLabel(self.verticalGroupBox_11)  # X轴系统加速度文本框后面的单位
        self.dw_3.setGeometry(QtCore.QRect(210, 25, 60, 25))
        self.dw_3.setObjectName("dw_3")

        self.s1__lb_40 = QtWidgets.QLabel(self.verticalGroupBox_11)  # Y轴 系统加速度标签
        self.s1__lb_40.setObjectName("self.s1__lb_40")
        self.s1__lb_40.setGeometry(QtCore.QRect(310, 25, 85, 25))
        self.s1__lb_40.setFont(QFont("华文楷书", 9))
        self.s1__lb_40.setStyleSheet("color:rgb(8,12,84);")

        self.lineEdit_29 = QtWidgets.QLineEdit(self.verticalGroupBox_11)  # Y轴系统加速度标签后面的文本框
        self.lineEdit_29.setObjectName("self.lineEdit_29")
        self.lineEdit_29.setGeometry(QtCore.QRect(405, 25, 80, 25))
        self.lineEdit_29.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_29.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))

        self.dw_4 = QtWidgets.QLabel(self.verticalGroupBox_11)  # Y轴系统加速度文本框后面的单位
        self.dw_4.setGeometry(QtCore.QRect(490, 25, 60, 25))
        self.dw_4.setObjectName("dw_4")

        self.s1__lb_41 = QtWidgets.QLabel(self.verticalGroupBox_11)  # Z轴系统加速度标签
        self.s1__lb_41.setObjectName("self.s1__lb_41")
        self.s1__lb_41.setGeometry(QtCore.QRect(30, 70, 85, 25))
        self.s1__lb_41.setFont(QFont("华文楷书", 9))
        self.s1__lb_41.setStyleSheet("color:rgb(8,12,84);")

        self.lineEdit_30 = QtWidgets.QLineEdit(self.verticalGroupBox_11)  # Z轴系统加速度标签后面的文本框
        self.lineEdit_30.setObjectName("self.lineEdit_30")
        self.lineEdit_30.setGeometry(QtCore.QRect(125, 70, 80, 25))
        self.lineEdit_30.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_30.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))

        self.dw_5 = QtWidgets.QLabel(self.verticalGroupBox_11)  # Z轴系统加速度文本框后面的单位
        self.dw_5.setGeometry(QtCore.QRect(210, 70, 60, 25))
        self.dw_5.setObjectName("dw_5")

        self.Para_read_button = QtWidgets.QPushButton(self.GroupBoxPara)  # 参数读取
        self.Para_read_button.setObjectName("Para_read_button")
        self.Para_read_button.setGeometry(QtCore.QRect(80, 395, 60, 40))
        self.Para_read_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(135,206,235)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(192,192,192)}""")
        self.Para_read_button.setFont(QFont("Times New Roman", 10.5))

        self.Para_write_button = QtWidgets.QPushButton(self.GroupBoxPara)  # 参数写入
        self.Para_write_button.setObjectName("Para_write_button")
        self.Para_write_button.setGeometry(QtCore.QRect(260, 395, 60, 40))
        self.Para_write_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(135,206,235)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(192,192,192)}""")
        self.Para_write_button.setFont(QFont("Times New Roman", 10.5))

        self.Para_save_button2 = QtWidgets.QPushButton(self.GroupBoxPara)  # 参数写入
        self.Para_save_button2.setObjectName("Para_save_button2")
        self.Para_save_button2.setGeometry(QtCore.QRect(440, 395, 60, 40))
        self.Para_save_button2.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(135,206,235)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(192,192,192)}""")
        self.Para_save_button2.setFont(QFont("Times New Roman", 10.5))

        # 标头在这段
        self.s1__lb_28 = QtWidgets.QLabel(self.verticalGroupBox_10)  # 标头标签  脉冲当量标签
        self.s1__lb_28.setObjectName("self.s1__lb_28")
        self.s1__lb_28.setGeometry(QtCore.QRect(35, 30, 47, 25))

        self.s1__lb_29 = QtWidgets.QLabel(self.verticalGroupBox_10)  #  =
        self.s1__lb_29.setObjectName("self.s1__lb_29")
        self.s1__lb_29.setGeometry(QtCore.QRect(95, 30, 15, 25))

        self.s1__lb_30 = QtWidgets.QLabel(self.verticalGroupBox_10)  #导程
        self.s1__lb_30.setObjectName("self.s1__lb_30")
        self.s1__lb_30.setGeometry(QtCore.QRect(122, 30, 40, 25))

        self.s1__lb_31 = QtWidgets.QLabel(self.verticalGroupBox_10)  #/
        self.s1__lb_31.setObjectName("self.s1__lb_31")
        self.s1__lb_31.setGeometry(QtCore.QRect(165, 30, 10, 25))

        self.s1__lb_32 = QtWidgets.QLabel(self.verticalGroupBox_10)  #细分数
        self.s1__lb_32.setObjectName("self.s1__lb_32")
        self.s1__lb_32.setGeometry(QtCore.QRect(188, 30, 52, 25))

        self.s1__lb_33 = QtWidgets.QLabel(self.verticalGroupBox_10)  #行程文本框
        self.s1__lb_33.setObjectName("self.s1__lb_33")
        self.s1__lb_33.setGeometry(QtCore.QRect(245, 30, 60, 25))

        self.s1__lb_34 = QtWidgets.QLabel(self.verticalGroupBox_10)  #回原点方向
        self.s1__lb_34.setObjectName("self.s1__lb_34")
        self.s1__lb_34.setGeometry(QtCore.QRect(317, 30, 60, 25))

        self.s1__lb_35 = QtWidgets.QLabel(self.verticalGroupBox_10)  #回原点速度
        self.s1__lb_35.setObjectName("self.s1__lb_35")
        self.s1__lb_35.setGeometry(QtCore.QRect(390, 30, 100, 25))

        self.s1__lb_36 = QtWidgets.QLabel(self.verticalGroupBox_10)  #原点回退距
        self.s1__lb_36.setObjectName("self.s1__lb_36")
        self.s1__lb_36.setGeometry(QtCore.QRect(500, 30, 100, 25))

        # -------------------------------------------------------------------------
        self.s1__lb_19 = QtWidgets.QLabel(self.verticalGroupBox_10)  # X轴的那个标签
        self.s1__lb_19.setObjectName("self.s1__lb_19")
        self.s1__lb_19.setGeometry(QtCore.QRect(8, 72, 17, 25))

        self.s1__lb_20 = QtWidgets.QLabel(self.verticalGroupBox_10)  # Y轴那个标签
        self.s1__lb_20.setObjectName("self.s1__lb_20")
        self.s1__lb_20.setGeometry(QtCore.QRect(8, 117, 17, 25))

        self.s1__lb_21 = QtWidgets.QLabel(self.verticalGroupBox_10)  # Z轴那个标签
        self.s1__lb_21.setObjectName("self.s1__lb_21")
        self.s1__lb_21.setGeometry(QtCore.QRect(8, 162, 17, 25))
        # ----------------------------------------------------------------------------------------------------------
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 脉冲当量（X轴）
        self.lineEdit_10.setObjectName("self.lineEdit_10")
        self.lineEdit_10.setGeometry(QtCore.QRect(32, 72, 54, 25))
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_10.setValidator(QDoubleValidator(-10000.000, 10000.000, 3))
        self.lineEdit_10.setFont(QFont("Times New Roman", 8))
        # todo lineEdit_10  lineEdit_13  lineEdit_16  lineEdit_19
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 脉冲当量（Y轴）
        self.lineEdit_11.setObjectName("self.lineEdit_11")
        self.lineEdit_11.setGeometry(QtCore.QRect(32, 117, 54, 25))
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_11.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_11.setFont(QFont("Times New Roman", 8))

        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 脉冲当量（Z轴）
        self.lineEdit_12.setObjectName("self.lineEdit_12")
        self.lineEdit_12.setGeometry(QtCore.QRect(32, 162, 54, 25))
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_12.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_12.setFont(QFont("Times New Roman", 8))
        # -----------------------------------------------------------------
        self.s1__lb_22 = QtWidgets.QLabel(self.verticalGroupBox_10)  # =标签（X轴）
        self.s1__lb_22.setObjectName("self.s1__lb_22")
        self.s1__lb_22.setGeometry(QtCore.QRect(95, 72, 15, 25))

        self.s1__lb_23 = QtWidgets.QLabel(self.verticalGroupBox_10)  # =标签（Y轴）
        self.s1__lb_23.setObjectName("self.s1__lb_23")
        self.s1__lb_23.setGeometry(QtCore.QRect(95, 117, 15, 25))

        self.s1__lb_24 = QtWidgets.QLabel(self.verticalGroupBox_10)  # =标签（Z轴）
        self.s1__lb_24.setObjectName("self.s1__lb_24")
        self.s1__lb_24.setGeometry(QtCore.QRect(95, 162, 15, 25))
        # -----------------------------------------------------------------
        self.lineEdit_13 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 导程文本框（X轴）
        self.lineEdit_13.setObjectName("self.lineEdit_13")
        self.lineEdit_13.setGeometry(QtCore.QRect(108, 72, 52, 25))
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_13.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_13.setFont(QFont("Times New Roman", 8))

        self.lineEdit_14 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 导程文本框（Y轴）
        self.lineEdit_14.setObjectName("self.lineEdit_14")
        self.lineEdit_14.setGeometry(QtCore.QRect(108, 117, 52, 25))
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_14.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_14.setFont(QFont("Times New Roman",8))

        self.lineEdit_15 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 导程文本框（Z轴）
        self.lineEdit_15.setObjectName("self.lineEdit_15")
        self.lineEdit_15.setGeometry(QtCore.QRect(108, 162, 52, 25))
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_15.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_15.setFont(QFont("Times New Roman", 8))
        # -------------------------------------------------------------------
        self.s1__lb_25 = QtWidgets.QLabel(self.verticalGroupBox_10)  # /号标签（X轴标签）
        self.s1__lb_25.setObjectName("self.s1__lb_25")
        self.s1__lb_25.setGeometry(QtCore.QRect(165, 72, 10, 25))

        self.s1__lb_26 = QtWidgets.QLabel(self.verticalGroupBox_10)  # /号标签（Y轴标签）
        self.s1__lb_26.setObjectName("self.s1__lb_26")
        self.s1__lb_26.setGeometry(QtCore.QRect(165, 117, 10, 25))

        self.s1__lb_27 = QtWidgets.QLabel(self.verticalGroupBox_10)  # /号标签（Z轴标签）
        self.s1__lb_27.setObjectName("self.s1__lb_27")
        self.s1__lb_27.setGeometry(QtCore.QRect(165, 162, 10, 25))
        # -----------------------------------------------------------------
        self.lineEdit_16 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 细分数文本框（X轴）
        self.lineEdit_16.setObjectName("self.lineEdit_16")
        self.lineEdit_16.setGeometry(QtCore.QRect(179, 72, 54, 25))
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_16.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_16.setFont(QFont("Times New Roman", 8))

        self.lineEdit_17 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 细分数文本框（Y轴）
        self.lineEdit_17.setObjectName("self.lineEdit_17")
        self.lineEdit_17.setGeometry(QtCore.QRect(179, 117, 54, 25))
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_17.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_17.setFont(QFont("Times New Roman", 8))

        self.lineEdit_18 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 细分数文本框（Z轴）
        self.lineEdit_18.setObjectName("self.lineEdit_18")
        self.lineEdit_18.setGeometry(QtCore.QRect(179, 162, 54, 25))
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_18.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_18.setFont(QFont("Times New Roman",8))
        # ------------------------------------------------------------------
        self.lineEdit_19 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 行程文本框（X轴）
        self.lineEdit_19.setObjectName("self.lineEdit_19")
        self.lineEdit_19.setGeometry(QtCore.QRect(240, 72, 65, 25))
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_19.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_19.setFont(QFont("Times New Roman", 8))

        self.lineEdit_20 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 行程文本框（Y轴）
        self.lineEdit_20.setObjectName("self.lineEdit_20")
        self.lineEdit_20.setGeometry(QtCore.QRect(240, 117, 65, 25))
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_20.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_20.setFont(QFont("Times New Roman", 8))

        self.lineEdit_21 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 行程文本框（Z轴）
        self.lineEdit_21.setObjectName("self.lineEdit_21")
        self.lineEdit_21.setGeometry(QtCore.QRect(240, 162, 65, 25))
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_21.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_21.setFont(QFont("Times New Roman", 8))
        # --------------------------------------------------------------
        self.s1__box_20 = QtWidgets.QComboBox(self.verticalGroupBox_10)  # 回原点方向下拉框（X轴）
        self.s1__box_20.setGeometry(QtCore.QRect(320, 72, 55, 25))
        self.s1__box_20.setFont(QFont("Times New Roman", 8))
        self.s1__box_20.setObjectName("s1__box_20")
        self.s1__box_20.addItem("")
        self.s1__box_20.addItem("")

        self.s1__box_21 = QtWidgets.QComboBox(self.verticalGroupBox_10)  # 回原点方向下拉框（Y轴）
        self.s1__box_21.setGeometry(QtCore.QRect(320, 117, 55, 25))
        self.s1__box_20.setFont(QFont("Times New Roman", 8))
        self.s1__box_21.setObjectName("s1__box_21")
        self.s1__box_21.addItem("")
        self.s1__box_21.addItem("")

        self.s1__box_22 = QtWidgets.QComboBox(self.verticalGroupBox_10)  # 回原点方向下拉框（Z轴）
        self.s1__box_22.setGeometry(QtCore.QRect(320, 162, 55, 25))
        self.s1__box_20.setFont(QFont("Times New Roman", 8))
        self.s1__box_22.setObjectName("s1__box_22")
        self.s1__box_22.addItem("")
        self.s1__box_22.addItem("")
        # -----------------------------------------------------------------------
        self.lineEdit_22 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 回原点速度文本框（X轴）
        self.lineEdit_22.setObjectName("self.lineEdit_22")
        self.lineEdit_22.setGeometry(QtCore.QRect(400, 72, 80, 25))
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_22.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_22.setFont(QFont("Times New Roman", 8))

        self.lineEdit_23 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 回原点速度文本框（Y轴）
        self.lineEdit_23.setObjectName("self.lineEdit_23")
        self.lineEdit_23.setGeometry(QtCore.QRect(400, 117, 80, 25))
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_23.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_23.setFont(QFont("Times New Roman", 8))

        self.lineEdit_24 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 回原点速度文本框（Z轴）
        self.lineEdit_24.setObjectName("self.lineEdit_24")
        self.lineEdit_24.setGeometry(QtCore.QRect(400, 162, 80, 25))
        self.lineEdit_24.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_24.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_24.setFont(QFont("Times New Roman", 8))
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------
        self.lineEdit_25 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 原点回退距文本框（X轴）
        self.lineEdit_25.setObjectName("self.lineEdit_25")
        self.lineEdit_25.setGeometry(QtCore.QRect(510, 72, 80, 25))
        self.lineEdit_25.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_25.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_25.setFont(QFont("Times New Roman", 8))

        self.lineEdit_26 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 原点回退距文本框（Y轴）
        self.lineEdit_26.setObjectName("self.lineEdit_26")
        self.lineEdit_26.setGeometry(QtCore.QRect(510, 117, 80, 25))
        self.lineEdit_26.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_26.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_26.setFont(QFont("Times New Roman", 8))

        self.lineEdit_27 = QtWidgets.QLineEdit(self.verticalGroupBox_10)  # 原点回退距文本框（Z轴）
        self.lineEdit_27.setObjectName("self.lineEdit_27")
        self.lineEdit_27.setGeometry(QtCore.QRect(510, 162, 80, 25))
        self.lineEdit_27.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_27.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_27.setFont(QFont("Times New Roman", 8))

        les = self.GroupBoxPara.findChildren(QLineEdit)
        for item in les:
            item.setProperty("type", 2)

        # ----------------------------------------------------------------------
        self.GroupBoxLine_arc = QtWidgets.QGroupBox(Form)
        self.GroupBoxLine_arc.setGeometry(QtCore.QRect(160, 30, 640, 460))
        self.GroupBoxLine_arc.setObjectName("GroupBoxLine_arc")
        self.verticalLayout_lineArc = QtWidgets.QVBoxLayout(self.GroupBoxLine_arc)
        self.verticalLayout_lineArc.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_lineArc.setObjectName("verticalLayout_lineArc")

        self.s1__lb_47 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_47.setObjectName("self.s1__lb_47")
        self.s1__lb_47.setGeometry(QtCore.QRect(20, 25, 65, 30))

        self.lineEdit_34 = QtWidgets.QLineEdit(self.GroupBoxLine_arc)
        self.lineEdit_34.setObjectName("self.lineEdit_34")
        self.lineEdit_34.setGeometry(QtCore.QRect(92, 25, 100, 35))
        self.lineEdit_34.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_34.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_34.setFont(QFont("Times New Roman", 10.5))

        self.dw_6 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.dw_6.setGeometry(QtCore.QRect(198, 27, 25, 25))
        self.dw_6.setObjectName("dw_6")

        self.Read_button = QtWidgets.QPushButton(self.GroupBoxLine_arc)
        self.Read_button.setObjectName("self.Read_button")
        self.Read_button.setGeometry(QtCore.QRect(245, 25, 85, 40))
        self.Read_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(110,240,123)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,227,132)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Read_button.setFont(QFont("Times New Roman", 11.5))

        self.line = QtWidgets.QFrame(self.GroupBoxLine_arc)
        self.line.setGeometry(QtCore.QRect(20, 68, 440, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.s1__lb_57 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_57.setObjectName("self.s1__lb_57")
        self.s1__lb_57.setGeometry(QtCore.QRect(25, 80, 70, 20))

        self.s1__lb_48 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_48.setObjectName("self.s1__lb_48")
        self.s1__lb_48.setGeometry(QtCore.QRect(15, 110, 70, 30))

        self.lineEdit_35 = QtWidgets.QLineEdit(self.GroupBoxLine_arc)
        self.lineEdit_35.setObjectName("self.lineEdit_35")
        self.lineEdit_35.setGeometry(QtCore.QRect(92, 110, 95, 35))
        self.lineEdit_35.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_35.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_35.setFont(QFont("Times New Roman", 10.5))

        self.dw_7 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.dw_7.setGeometry(QtCore.QRect(193, 112, 25, 25))
        self.dw_7.setObjectName("dw_7")

        self.s1__lb_49 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_49.setObjectName("self.s1__lb_49")
        self.s1__lb_49.setGeometry(QtCore.QRect(15, 168, 70, 30))

        self.lineEdit_36 = QtWidgets.QLineEdit(self.GroupBoxLine_arc)
        self.lineEdit_36.setObjectName("self.lineEdit_36")
        self.lineEdit_36.setGeometry(QtCore.QRect(92, 165, 95, 35))
        self.lineEdit_36.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_36.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_36.setFont(QFont("Times New Roman", 10.5))

        self.dw_8 = QtWidgets.QLabel(self.GroupBoxLine_arc)  # X轴系统加速度文本框后面的单位
        self.dw_8.setGeometry(QtCore.QRect(193, 167, 25, 25))
        self.dw_8.setObjectName("dw_8")

        self.s1__lb_50 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_50.setObjectName("self.s1__lb_50")
        self.s1__lb_50.setGeometry(QtCore.QRect(15, 226, 70, 30))

        self.lineEdit_37 = QtWidgets.QLineEdit(self.GroupBoxLine_arc)
        self.lineEdit_37.setObjectName("self.lineEdit_37")
        self.lineEdit_37.setGeometry(QtCore.QRect(92, 225, 95, 35))
        self.lineEdit_37.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_37.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_37.setFont(QFont("Times New Roman", 10.5))

        self.dw_9 = QtWidgets.QLabel(self.GroupBoxLine_arc)  # X轴系统加速度文本框后面的单位
        self.dw_9.setGeometry(QtCore.QRect(193, 227, 25, 25))
        self.dw_9.setObjectName("dw_9")

        self.s1__lb_51 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_51.setObjectName("self.s1__lb_51")
        self.s1__lb_51.setGeometry(QtCore.QRect(15, 281, 70, 30))

        self.lineEdit_38 = QtWidgets.QLineEdit(self.GroupBoxLine_arc)
        self.lineEdit_38.setObjectName("self.lineEdit_38")
        self.lineEdit_38.setGeometry(QtCore.QRect(92, 280, 95, 35))
        self.lineEdit_38.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_38.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_38.setFont(QFont("Times New Roman", 10.5))

        self.dw_10 = QtWidgets.QLabel(self.GroupBoxLine_arc)  # X轴系统加速度文本框后面的单位
        self.dw_10.setGeometry(QtCore.QRect(193, 282, 25, 25))
        self.dw_10.setObjectName("dw_10")

        self.s1__lb_52 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_52.setObjectName("self.s1__lb_52")
        self.s1__lb_52.setGeometry(QtCore.QRect(15, 336, 70, 30))

        self.lineEdit_39 = QtWidgets.QLineEdit(self.GroupBoxLine_arc)
        self.lineEdit_39.setObjectName("self.lineEdit_38")
        self.lineEdit_39.setGeometry(QtCore.QRect(92, 335, 95, 35))
        self.lineEdit_39.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_39.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_39.setFont(QFont("Times New Roman", 10.5))

        self.dw_11 = QtWidgets.QLabel(self.GroupBoxLine_arc)  # X轴系统加速度文本框后面的单位
        self.dw_11.setGeometry(QtCore.QRect(193, 337, 25, 25))
        self.dw_11.setObjectName("dw_11")

        self.s1__lb_53 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_53.setObjectName("self.s1__lb_53")
        self.s1__lb_53.setGeometry(QtCore.QRect(15, 391,70, 30))

        self.lineEdit_40 = QtWidgets.QLineEdit(self.GroupBoxLine_arc)
        self.lineEdit_40.setObjectName("self.lineEdit_40")
        self.lineEdit_40.setGeometry(QtCore.QRect(92, 390, 95, 35))
        self.lineEdit_40.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_40.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_40.setFont(QFont("Times New Roman", 10.5))

        self.dw_12 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.dw_12.setGeometry(QtCore.QRect(193, 392, 25, 25))
        self.dw_12.setObjectName("dw_12")

        self.Fast_Stop_button = QtWidgets.QPushButton(self.GroupBoxLine_arc)
        self.Fast_Stop_button.setObjectName("self.Fast_Stop_button")
        self.Fast_Stop_button.setGeometry(QtCore.QRect(245, 190, 85, 40))
        self.Fast_Stop_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(50,205,50)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Fast_Stop_button.setFont(QFont("Times New Roman", 11.5))

        self.s1__lb_58 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_58.setObjectName("self.s1__lb_58")
        self.s1__lb_58.setGeometry(QtCore.QRect(220, 260, 48, 25))

        self.lineEdit_44 = QtWidgets.QLineEdit(self.GroupBoxLine_arc)
        self.lineEdit_44.setObjectName("self.lineEdit_44")
        self.lineEdit_44.setGeometry(QtCore.QRect(272, 255, 65, 35))
        self.lineEdit_44.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_44.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_44.setFont(QFont("Times New Roman", 10.5))

        self.s1__lb_59 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_59.setObjectName("self.s1__lb_59")
        self.s1__lb_59.setGeometry(QtCore.QRect(325, 260, 45, 25))

        self.Enter4_button = QtWidgets.QPushButton(self.GroupBoxLine_arc)
        self.Enter4_button.setObjectName("self.Enter4_button")
        self.Enter4_button.setGeometry(QtCore.QRect(245, 320, 85, 40))
        self.Enter4_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,100,100)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Enter4_button.setFont(QFont("Times New Roman", 11.5))

        self.XY_Line_interpolation_button = QtWidgets.QPushButton(self.GroupBoxLine_arc)
        self.XY_Line_interpolation_button.setObjectName("self.XY_Line_interpolation_button")
        self.XY_Line_interpolation_button.setGeometry(QtCore.QRect(375, 80, 80, 40))
        self.XY_Line_interpolation_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(111,222,160)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.XY_Line_interpolation_button.setFont(QFont("Times New Roman", 10.5))

        self.XZ_Line_interpolation_button = QtWidgets.QPushButton(self.GroupBoxLine_arc)
        self.XZ_Line_interpolation_button.setObjectName("self.XZ_Line_interpolation_button")
        self.XZ_Line_interpolation_button.setGeometry(QtCore.QRect(375, 140, 80, 40))
        self.XZ_Line_interpolation_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(150,170,160)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.XZ_Line_interpolation_button.setFont(QFont("Times New Roman", 10.5))

        self.YZ_Line_interpolation_button = QtWidgets.QPushButton(self.GroupBoxLine_arc)
        self.YZ_Line_interpolation_button.setObjectName("self.YZ_Line_interpolation_button")
        self.YZ_Line_interpolation_button.setGeometry(QtCore.QRect(375, 200, 80, 40))
        self.YZ_Line_interpolation_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(211,120,100)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.YZ_Line_interpolation_button.setFont(QFont("Times New Roman", 10.5))

        self.XY_Arc_interpolation_button = QtWidgets.QPushButton(self.GroupBoxLine_arc)
        self.XY_Arc_interpolation_button.setObjectName("self.XY_Arc_interpolation_button")
        self.XY_Arc_interpolation_button.setGeometry(QtCore.QRect(375, 275, 80, 40))
        self.XY_Arc_interpolation_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(244,164,96)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.XY_Arc_interpolation_button.setFont(QFont("Times New Roman", 10.5))

        self.XZ_Arc_interpolation_button = QtWidgets.QPushButton(self.GroupBoxLine_arc)
        self.XZ_Arc_interpolation_button.setObjectName("self.XZ_Arc_interpolation_button")
        self.XZ_Arc_interpolation_button.setGeometry(QtCore.QRect(375, 335, 80, 40))
        self.XZ_Arc_interpolation_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(221,160,221)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.XZ_Arc_interpolation_button.setFont(QFont("Times New Roman", 10.5))

        self.YZ_Arc_interpolation_button = QtWidgets.QPushButton(self.GroupBoxLine_arc)
        self.YZ_Arc_interpolation_button.setObjectName("self.YZ_Arc_interpolation_button")
        self.YZ_Arc_interpolation_button.setGeometry(QtCore.QRect(375, 395, 80, 40))
        self.YZ_Arc_interpolation_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(64,224,208)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.YZ_Arc_interpolation_button.setFont(QFont("Times New Roman", 10.5))

        self.line_2 = QtWidgets.QFrame(self.GroupBoxLine_arc)
        self.line_2.setGeometry(QtCore.QRect(472, 10, 2, 430))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.s1__lb_54 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_54.setObjectName("self.s1__lb_54")
        self.s1__lb_54.setGeometry(QtCore.QRect(487, 30, 48, 30))

        self.lineEdit_41 = QtWidgets.QLineEdit(self.GroupBoxLine_arc)
        self.lineEdit_41.setObjectName("self.lineEdit_41")
        self.lineEdit_41.setGeometry(QtCore.QRect(540, 30, 85, 35))
        self.lineEdit_41.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_41.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_41.setFont(QFont("Times New Roman", 10.5))
        self.s1__lb_60 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_60.setObjectName("self.s1__lb_60")
        self.s1__lb_60.setGeometry(QtCore.QRect(560, 30, 65, 35))
        self.s1__lb_60.setFont(QFont("Times New Roman", 11))

        self.s1__lb_55 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_55.setObjectName("self.s1__lb_55")
        self.s1__lb_55.setGeometry(QtCore.QRect(487, 90, 48, 30))

        self.lineEdit_42 = QtWidgets.QLineEdit(self.GroupBoxLine_arc)
        self.lineEdit_42.setObjectName("self.lineEdit_42")
        self.lineEdit_42.setGeometry(QtCore.QRect(540, 90, 85, 35))
        self.lineEdit_42.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_42.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_42.setFont(QFont("Times New Roman", 10.5))
        self.s1__lb_61 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_61.setObjectName("self.s1__lb_61")
        self.s1__lb_61.setGeometry(QtCore.QRect(560, 90, 65, 35))
        self.s1__lb_61.setFont(QFont("Times New Roman", 11))

        self.s1__lb_56 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_56.setObjectName("self.s1__lb_56")
        self.s1__lb_56.setGeometry(QtCore.QRect(487, 150, 48, 30))

        self.lineEdit_43 = QtWidgets.QLineEdit(self.GroupBoxLine_arc)
        self.lineEdit_43.setObjectName("self.lineEdit_43")
        self.lineEdit_43.setGeometry(QtCore.QRect(540, 150, 85, 35))
        self.lineEdit_43.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_43.setValidator(QDoubleValidator(-10000.0, 10000.0, 3))
        self.lineEdit_43.setFont(QFont("Times New Roman", 10.5))
        self.s1__lb_62 = QtWidgets.QLabel(self.GroupBoxLine_arc)
        self.s1__lb_62.setObjectName("self.s1__lb_62")
        self.s1__lb_62.setGeometry(QtCore.QRect(560, 150, 65, 35))
        self.s1__lb_62.setFont(QFont("Times New Roman", 11))

        self.Basic_Para_button = QtWidgets.QPushButton(self.GroupBoxLine_arc)
        self.Basic_Para_button.setObjectName("self.Basic_Para_button")
        self.Basic_Para_button.setGeometry(QtCore.QRect(500, 230, 95, 40))
        self.Basic_Para_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(135,206,235)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(220,220,220)}""")
        self.Basic_Para_button.setFont(QFont("Times New Roman", 10.5))

        self.Return_main_interface_button = QtWidgets.QPushButton(self.GroupBoxLine_arc)
        self.Return_main_interface_button.setObjectName("self.Return_main_interface_button")
        self.Return_main_interface_button.setGeometry(QtCore.QRect(500, 360, 95, 40))
        self.Return_main_interface_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(135,206,235)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(220,220,220)}""")
        self.Return_main_interface_button.setFont(QFont("Times New Roman", 10.5))

        self.Para_save_button4 = QtWidgets.QPushButton(self.GroupBoxLine_arc)  # 参数写入
        self.Para_save_button4.setObjectName("Para_save_button4")
        self.Para_save_button4.setGeometry(QtCore.QRect(500, 295, 95, 40))
        self.Para_save_button4.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(135,206,235)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(220,220,220)}""")
        self.Para_save_button4.setFont(QFont("Times New Roman", 10.5))

        les = self.GroupBoxLine_arc.findChildren(QLineEdit)
        for item in les:
            item.setProperty("type", 4)

        # todo 切换界面3 ---------- 切换至程序编辑界面---------------------
        self.GroupBoxEditProgram = QtWidgets.QGroupBox(Form)
        self.GroupBoxEditProgram.setGeometry(QtCore.QRect(160, 30, 640, 460))
        self.GroupBoxEditProgram.setObjectName("GroupBoxEditProgram")
        self.verticalLayout_editProgram = QtWidgets.QVBoxLayout(self.GroupBoxEditProgram)
        self.verticalLayout_editProgram.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_editProgram.setObjectName("verticalLayout_editProgram")
        # 程序编辑界面的表格
        self.TableWidget = QTableWidget(self.GroupBoxEditProgram)
        self.TableWidget.setRowCount(666)
        self.TableWidget.setColumnCount(7)
        self.TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.TableWidget.setGeometry(15, 20, 505, 427)

        self.TableWidget.resizeColumnsToContents()
        # 这个就是添加的联动效果的下拉框
        self.provincedeldeate = ProvinceDelegate()
        self.citydelegate = CityDelegate()
        self.jinzhiitemdelegate = itemjinzhi()
        self.TableWidget.setItemDelegateForColumn(0, self.provincedeldeate)
        self.TableWidget.setItemDelegateForColumn(1, self.citydelegate)
        self.TableWidget.setItemDelegateForColumn(2, self.jinzhiitemdelegate)
        self.TableWidget.setItemDelegateForColumn(3, self.jinzhiitemdelegate)
        self.TableWidget.setItemDelegateForColumn(4, self.jinzhiitemdelegate)
        self.TableWidget.setItemDelegateForColumn(5, self.jinzhiitemdelegate)
        self.TableWidget.setItemDelegateForColumn(6, self.jinzhiitemdelegate)

        # 设置水平方向的表头标签与垂直方向上的表头标签，注意要在初始化行列之后进行，否则，没有用
        # self.TableWidget("QHeaderView::section{background-color:transparent;font:13pt '宋体';color: red;}")
        self.TableWidget.setHorizontalHeaderLabels(
            [_translate("Form", '指令集'), '指令', '  参数1  ', '  参数2  ', '  参数3  ', ' 参数4 ', '参数5'])

        # Todo 优化 1 设置垂直方向的表头标签
        self.TableWidget.setVerticalHeaderLabels([])

        self.TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.TableWidget.setColumnWidth(0, 200)

        # TODO 优化 2 设置水平方向表格为自适应的伸缩模式
        self.TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 水平方向可以根据表格的多少伸缩

        # TODO 优化 3 将表格变为禁止编辑
        # TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # TODO 优化 4 设置表格整行选中
        self.TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # TODO 优化 6 表格头的显示与隐藏
        # TableWidget.verticalHeader().setVisible(False)
        # TableWidget.horizontalHeader().setVisible(False)
        # TOdo 优化7 在  单元格  内放置控件
        # print(self.TableWidget.cellWidget(96, 1).currentText())  # 获取(x,y)的值
        # todo 在这个位置添加一个标签或者文本框  显示行数

        self.s1__lb_37 = QtWidgets.QLabel(self.GroupBoxEditProgram)
        self.s1__lb_37.setObjectName("s1__lb_37")
        self.s1__lb_37.setGeometry(QtCore.QRect(533, 20, 40, 27))

        self.lineEdit_28 = QtWidgets.QLineEdit(self.GroupBoxEditProgram)  # 原点回退距文本框（Z轴）
        self.lineEdit_28.setObjectName("self.lineEdit_28")
        self.lineEdit_28.setGeometry(QtCore.QRect(580, 20, 40, 27))
        self.lineEdit_28.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.lineEdit_28.setFocusPolicy(QtCore.Qt.NoFocus)

        self.lineEdit_28.setStyleSheet("background-color:rgb(240,255,240)")

        self.Line_up_button = QtWidgets.QPushButton(self.GroupBoxEditProgram)  # 指定行上移按钮
        self.Line_up_button.setObjectName("Line_up_button")
        self.Line_up_button.setGeometry(QtCore.QRect(533, 57, 90, 27))
        self.Line_up_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(192,192,192)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Line_up_button.setFont(QFont("Times New Roman", 10.5))

        self.Line_down_button = QtWidgets.QPushButton(self.GroupBoxEditProgram)  # 指定行下移按钮
        self.Line_down_button.setObjectName("Line_down_button")
        self.Line_down_button.setGeometry(QtCore.QRect(533, 93, 90, 27))
        self.Line_down_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(176,224,230)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Line_down_button.setFont(QFont("Times New Roman", 10.5))

        self.Come_in_button = QtWidgets.QPushButton(self.GroupBoxEditProgram)  # 插入代码行按钮
        self.Come_in_button.setObjectName("Come_in_button")
        self.Come_in_button.setGeometry(QtCore.QRect(533, 129, 90, 27))
        self.Come_in_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(189,252,201)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Come_in_button.setFont(QFont("Times New Roman", 10.5))

        self.Delete_1_button = QtWidgets.QPushButton(self.GroupBoxEditProgram)  # 删除代码行按钮
        self.Delete_1_button.setObjectName("Delete_1_button")
        self.Delete_1_button.setGeometry(QtCore.QRect(533, 165, 90, 27))
        self.Delete_1_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(135,206,235)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Delete_1_button.setFont(QFont("Times New Roman", 10.5))

        self.Copy_button = QtWidgets.QPushButton(self.GroupBoxEditProgram)  # 复制程序按钮
        self.Copy_button.setObjectName("Copy_button")
        self.Copy_button.setGeometry(QtCore.QRect(533, 201, 90, 27))
        self.Copy_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,125,64)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Copy_button.setFont(QFont("Times New Roman", 10.5))

        self.Paste_button = QtWidgets.QPushButton(self.GroupBoxEditProgram)  # 粘贴程序按钮
        self.Paste_button.setObjectName("Paste_button")
        self.Paste_button.setGeometry(QtCore.QRect(533, 237, 90, 27))
        self.Paste_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(0,255,127)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Paste_button.setFont(QFont("Times New Roman", 10.5))

        self.New_program_button = QtWidgets.QPushButton(self.GroupBoxEditProgram)  # 新建程序按钮
        self.New_program_button.setObjectName("New_program_button")
        self.New_program_button.setGeometry(QtCore.QRect(533, 273, 90, 27))
        self.New_program_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(0,199,140)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.New_program_button.setFont(QFont("Times New Roman", 10.5))

        self.Save_program_button = QtWidgets.QPushButton(self.GroupBoxEditProgram)  # 保存程序按钮
        self.Save_program_button.setObjectName("Save_program_button")
        self.Save_program_button.setGeometry(QtCore.QRect(533, 309, 90, 27))
        self.Save_program_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(0,255,255)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Save_program_button.setFont(QFont("Times New Roman", 10.5))

        self.Delete_program_button = QtWidgets.QPushButton(self.GroupBoxEditProgram)  # 删除程序按钮
        self.Delete_program_button.setObjectName("Delete_program_button")
        self.Delete_program_button.setGeometry(QtCore.QRect(533, 345, 90, 27))
        self.Delete_program_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(221,160,221)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Delete_program_button.setFont(QFont("Times New Roman", 10.5))

        self.Download_program_button = QtWidgets.QPushButton(self.GroupBoxEditProgram)  # 下载程序按钮
        self.Download_program_button.setObjectName("Download_program_button")
        self.Download_program_button.setGeometry(QtCore.QRect(533, 381, 90, 27))
        self.Download_program_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,230,160)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Download_program_button.setFont(QFont("Times New Roman", 10.5))

        self.Open_program_button = QtWidgets.QPushButton(self.GroupBoxEditProgram)  # 打开工程按钮
        self.Open_program_button.setObjectName("Open_program_button")
        self.Open_program_button.setGeometry(QtCore.QRect(533, 417, 90, 27))
        self.Open_program_button.setStyleSheet("""
        QPushButton{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(227,207,120)}
        QPushButton:hover{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(255,97,0)}
        QPushButton:pressed{border:2px groove gray; border-radius:10px;padding:2px 4px;
        background-color:rgb(240,255,255)}""")
        self.Open_program_button.setFont(QFont("Times New Roman", 10.5))
        # todo 新添加MODBUS CRC校验按钮----------------
        self.verticalGroupBox_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # ------------------------------------------------------------
    def addNum(self):
        # 这里获取的是String,不是什么QString
        s = self.lineEdit_13.text()
        # 不能用 interval = s.toInt()
        interval = int(s)

    # -----------------------------------------------------------
    # 左侧一栏的显示区
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.stop_button.setText(_translate("Form", "断开控制器"))
        self.open_button.setText(_translate("Form", "连接控制器"))
        self.Peizhi_button.setText(_translate("Form", "串口配置"))
        # self.close_button.setText(_translate("Form", "关闭控制器"))
        self.Para_save_button1.setText(_translate("Form", "参数保存"))
        self.Para_save_button2.setText(_translate("Form", "参数保存"))
        self.Para_save_button4.setText(_translate("Form", "参数保存"))
        self.X_minus_button.setText(_translate("Form", "X-"))
        self.X_plus_button.setText(_translate("Form", "X+"))
        self.BackX_button.setText(_translate("Form", "X归零"))
        self.Y_minus_button.setText(_translate("Form", "Y-"))
        self.Y_plus_button.setText(_translate("Form", "Y+"))
        self.BackY_button.setText(_translate("Form", "Y归零"))
        self.Z_minus_button.setText(_translate("Form", "Z-"))
        self.Z_plus_button.setText(_translate("Form", "Z+"))
        self.BackZ_button.setText(_translate("Form", "Z归零"))
        self.BackZero_button.setText(_translate("Form", "停止"))
        self.Enter1_button.setText(_translate("Form", "确定"))
        self.Enter2_button.setText(_translate("Form", "确定"))
        self.Enter4_button.setText(_translate("Form", "确 定"))
        self.s1__lb_13.setText(_translate("Form", "手动速度："))
        self.s1__lb_14.setText(_translate("Form", "X轴位置："))
        self.s1__lb_15.setText(_translate("Form", "Y轴位置："))
        self.s1__lb_16.setText(_translate("Form", "Z轴位置："))
        # self.s1__lb_17.setText(_translate("Form", "控制卡内程序："))
        self.s1__lb_18.setText(_translate("Form", "X轴系统加速度："))
        self.s1__lb_40.setText(_translate("Form", "Y轴系统加速度："))
        self.s1__lb_41.setText(_translate("Form", "Z轴系统加速度："))
        self.s1__lb_19.setText(_translate("Form", "X轴"))
        self.s1__lb_20.setText(_translate("Form", "Y轴"))
        self.s1__lb_21.setText(_translate("Form", "Z轴"))
        self.s1__lb_22.setText(_translate("Form", "="))
        self.s1__lb_23.setText(_translate("Form", "="))
        self.s1__lb_24.setText(_translate("Form", "="))
        self.s1__lb_25.setText(_translate("Form", "/"))
        self.s1__lb_26.setText(_translate("Form", "/"))
        self.s1__lb_27.setText(_translate("Form", "/"))
        self.s1__lb_28.setText(_translate("Form", "脉冲当量"))
        self.s1__lb_29.setText(_translate("Form", "="))
        self.s1__lb_30.setText(_translate("Form", "导程"))
        self.s1__lb_31.setText(_translate("Form", "/"))
        self.s1__lb_32.setText(_translate("Form", "细分数"))
        self.s1__lb_33.setText(_translate("Form", "行程（mm）"))
        self.s1__lb_34.setText(_translate("Form", "回原点方向"))
        self.s1__lb_35.setText(_translate("Form", "回原点速度(mm/s)"))
        self.s1__lb_36.setText(_translate("Form", "原点回退距离(mm)"))
        self.s1__lb_37.setText(_translate("Form", "  行数："))
        self.s1__lb_42.setText(_translate("Form", "当前状态：未连接控制器"))
        # self.s1__lb_43.setText(_translate("Form", "未连接"))
        # self.s1__lb_43.setStyleSheet("color:rgb(250,0,0);")

        self.s1__lb_47.setText(_translate("Form", "插补速度："))
        self.s1__lb_48.setText(_translate("Form", "X轴终点坐标："))
        self.s1__lb_49.setText(_translate("Form", "Y轴终点坐标："))
        self.s1__lb_50.setText(_translate("Form", "Z轴终点坐标："))
        self.s1__lb_51.setText(_translate("Form", "X轴段点坐标："))
        self.s1__lb_52.setText(_translate("Form", "Y轴段点坐标："))
        self.s1__lb_53.setText(_translate("Form", "Z轴段点坐标："))
        self.s1__lb_54.setText(_translate("Form", "X轴位置："))
        self.s1__lb_55.setText(_translate("Form", "Y轴位置："))
        self.s1__lb_56.setText(_translate("Form", "Z轴位置："))
        self.s1__lb_57.setText(_translate("Form", "插补"))
        self.s1__lb_57.setFont(QFont("黑体", 11.5))
        self.s1__lb_58.setText(_translate("Form", "圆弧方向"))

        self.Fast_Stop_button.setText(_translate("Form", "急 停"))
        self.XY_Line_interpolation_button.setText(_translate("Form", "XY直线插补"))
        self.XZ_Line_interpolation_button.setText(_translate("Form", "XZ直线插补"))
        self.YZ_Line_interpolation_button.setText(_translate("Form", "YZ直线插补"))
        self.XY_Arc_interpolation_button.setText(_translate("Form", "XY圆弧插补"))
        self.XZ_Arc_interpolation_button.setText(_translate("Form", "XZ圆弧插补"))
        self.YZ_Arc_interpolation_button.setText(_translate("Form", "YZ圆弧插补"))

        self.Basic_Para_button.setText(_translate("Form", "基本参数界面"))
        self.Return_main_interface_button.setText(_translate("Form", "主界面"))
        self.Read_button.setText(_translate("Form", "数据读取"))

        # self.Delete_button.setText(_translate("Form", "删除程序"))
        self.Para_read_button.setText(_translate("Form", "参数读取"))
        self.Para_write_button.setText(_translate("Form", "参数写入"))

        self.Line_up_button.setText(_translate("Form", "指定行上移"))
        self.Line_down_button.setText(_translate("Form", "指定行下移"))
        self.Come_in_button.setText(_translate("Form", "插入代码行"))
        self.Delete_1_button.setText(_translate("Form", "删除代码行"))
        self.Copy_button.setText(_translate("Form", "复制代码行"))
        self.Paste_button.setText(_translate("Form", "粘贴代码行"))
        self.New_program_button.setText(_translate("Form", "新建工程"))
        self.Save_program_button.setText(_translate("Form", "保存工程"))
        self.Delete_program_button.setText(_translate("Form", "删除工程"))
        self.Download_program_button.setText(_translate("Form", "下载工程"))
        self.Open_program_button.setText(_translate("Form", "打开工程"))
        self.lineEdit_4.setText(_translate("Form", ""))
        self.lineEdit_5.setText(_translate("Form", ""))

        self.lineEdit_9.setText(_translate("Form", ""))
        self.lineEdit_10.setText(_translate("Form", ""))
        self.lineEdit_11.setText(_translate("Form", ""))
        self.lineEdit_12.setText(_translate("Form", ""))
        self.lineEdit_13.setText(_translate("Form", ""))
        self.lineEdit_14.setText(_translate("Form", ""))
        self.lineEdit_15.setText(_translate("Form", ""))
        self.lineEdit_16.setText(_translate("Form", ""))
        self.lineEdit_17.setText(_translate("Form", ""))
        self.lineEdit_18.setText(_translate("Form", ""))
        self.lineEdit_19.setText(_translate("Form", ""))
        self.lineEdit_20.setText(_translate("Form", ""))
        self.lineEdit_21.setText(_translate("Form", ""))
        self.lineEdit_22.setText(_translate("Form", ""))
        self.lineEdit_23.setText(_translate("Form", ""))
        self.lineEdit_24.setText(_translate("Form", ""))

        # self.s1__box_18.setItemText(0, _translate("Form", "请输入程序"))
        # self.s1__box_18.setItemText(1, _translate("Form", "程序1"))
        # self.s1__box_18.setItemText(2, _translate("Form", "程序2"))

        self.s1__box_20.setItemText(0, _translate("Form", "N"))
        self.s1__box_20.setItemText(1, _translate("Form", "Y"))
        self.s1__box_21.setItemText(0, _translate("Form", "N"))
        self.s1__box_21.setItemText(1, _translate("Form", "Y"))
        self.s1__box_22.setItemText(0, _translate("Form", "N"))
        self.s1__box_22.setItemText(1, _translate("Form", "Y"))

        self.s1__box_23.setItemText(0, _translate("Form", "Language"))
        self.s1__box_23.setItemText(1, _translate("Form", "中文"))
        self.s1__box_23.setItemText(2, _translate("Form", "ENGLISH"))

        self.verticalGroupBox_3.setTitle(_translate("Form", "手动操作"))

        self.GroupBoxPara.setTitle(_translate("Form", "参数设置"))
        self.GroupBoxEditProgram.setTitle(_translate("Form", "程序编辑"))
        self.verticalGroupBox_6.setTitle(_translate("Form", "输出口选择"))
        self.verticalGroupBox_7.setTitle(_translate("Form", "机器状态"))
        self.verticalGroupBox_8.setTitle(_translate("Form", "输入口状态"))
        self.verticalGroupBox_9.setTitle(_translate("Form", "输出口状态"))
        self.verticalGroupBox_12.setTitle(_translate("Form", "电机状态"))
        self.verticalGroupBox_13.setTitle(_translate("Form", "三轴位置"))
        self.verticalGroupBox_10.setTitle(_translate("Form", "轴参数"))
        self.verticalGroupBox_11.setTitle(_translate("Form", "其他参数"))

        #         self.TableWidget.row[0:10].setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        # "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        # "p, li { white-space: pre-wrap; }\n"
        # "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        # "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请输入要发送数据</p></body></html>"))
        # 发送区的发送、清除、Hex发送

        self.s1__lb_39.setText(_translate("Form", "步进距离："))  # 将这个改为标签
        self.CheckBox_1.setText(_translate("Form", "OUT1"))  # CheckBox_1至CheckBox_4是输出口选择
        self.CheckBox_2.setText(_translate("Form", "OUT2"))
        self.CheckBox_3.setText(_translate("Form", "OUT3"))
        self.CheckBox_4.setText(_translate("Form", "OUT4"))
        self.CheckBox_5.setText(_translate("Form", "IN1"))  # CheckBox_5至CheckBox_11是输入口状态
        self.CheckBox_6.setText(_translate("Form", "IN2"))
        self.CheckBox_7.setText(_translate("Form", "IN3"))
        self.CheckBox_8.setText(_translate("Form", "IN4"))
        self.CheckBox_9.setText(_translate("Form", "ORG1"))
        self.CheckBox_10.setText(_translate("Form", "ORG2"))
        self.CheckBox_11.setText(_translate("Form", "ORG3"))
        self.CheckBox_12.setText(_translate("Form", "OUT1"))  # CheckBox_12至CheckBox_15是输出口状态
        self.CheckBox_13.setText(_translate("Form", "OUT2"))
        self.CheckBox_14.setText(_translate("Form", "OUT3"))
        self.CheckBox_15.setText(_translate("Form", "OUT4"))
        self.CheckBox_16.setText(_translate("Form", "X轴电机"))
        self.CheckBox_17.setText(_translate("Form", "Y轴电机"))
        self.CheckBox_18.setText(_translate("Form", "Z轴电机"))
        self.CheckBox_19.setText(_translate("Form", "上电自动运行"))
        self.Line_Arc_button.setText(_translate("Form", "直线圆弧"))
        self.Manual_input_button.setText(_translate("Form", "手动操作"))
        self.Parameter_setting_button.setText(_translate("Form", "参数设置"))
        self.Editing_program_button.setText(_translate("Form", "程序编辑"))
        self.About_button.setText(_translate("Form", " 关  于 "))
        self.dw_1.setText(_translate("Form", "mm/s"))
        self.dw_2.setText(_translate("Form", "mm"))
        self.dw_3.setText(_translate("Form", "(mm/s^2)"))
        self.dw_4.setText(_translate("Form", "(mm/s^2)"))
        self.dw_5.setText(_translate("Form", "(mm/s^2)"))

        self.dw_6.setText(_translate("Form", "mm/s"))
        self.dw_7.setText(_translate("Form", "mm"))
        self.dw_8.setText(_translate("Form", "mm"))
        self.dw_9.setText(_translate("Form", "mm"))
        self.dw_10.setText(_translate("Form", "mm"))
        self.dw_11.setText(_translate("Form", "mm"))
        self.dw_12.setText(_translate("Form", "mm"))
        self.TableWidget.setHorizontalHeaderLabels(
            [self._translate("Form", '指令集'), self._translate("Form", '指令'), self._translate("Form", '  参数1  '),
             self._translate("Form", '  参数2  '), self._translate("Form", '  参数3  '), self._translate("Form", ' 参数4 '),
             self._translate("Form", ' 参数5 ')])
