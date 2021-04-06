# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lap1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from operator import eq

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
import cv2
import cv2 as cv

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(1, 1, 1, 1))
        self.textEdit.setObjectName("textEdit")
        self.groupButton = QtWidgets.QGroupBox(self.centralwidget)
        self.groupButton.setGeometry(QtCore.QRect(30, 20, 201, 511))
        self.groupButton.setObjectName("groupButton")
        self.pushButton = QtWidgets.QPushButton(self.groupButton)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupButton)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 70, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupButton)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 120, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupButton)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 170, 131, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupButton)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 220, 131, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupButton)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 270, 131, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupButton)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 320, 131, 31))
        self.pushButton_7.setObjectName("pushButton_7")
       # self.pushButton_8 = QtWidgets.QPushButton(self.groupButton)
       # self.pushButton_8.setGeometry(QtCore.QRect(30, 370, 131, 31))
       # self.pushButton_8.setObjectName("pushButton_8")
       # self.pushButton_9 = QtWidgets.QPushButton(self.groupButton)
       # self.pushButton_9.setGeometry(QtCore.QRect(30, 420, 131, 31))
       # self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_OriImg = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_OriImg.setGeometry(QtCore.QRect(270, 20, 471, 271))
        self.groupBox_OriImg.setObjectName("groupBox_OriImg")
        self.label_3 = QtWidgets.QLabel(self.groupBox_OriImg)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 451, 231))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("2021-04-02_205149.png"))
        self.label_3.setObjectName("label_3")
        self.groupBox_ImgProcess = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ImgProcess.setGeometry(QtCore.QRect(270, 320, 481, 241))
        self.groupBox_ImgProcess.setObjectName("groupBox_ImgProcess")
        self.label_2 = QtWidgets.QLabel(self.groupBox_ImgProcess)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 471, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("2021-04-02_205149.png"))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Image = QtWidgets.QAction(MainWindow)
        self.actionOpen_Image.setObjectName("actionOpen_Image")

        self.pushButton.clicked.connect(self.OpenFile)
        self.pushButton_2.clicked.connect(self.Reverse_Image)
        self.pushButton_3.clicked.connect(self.logarit_transform)
        self.pushButton_4.clicked.connect(self.constrast_streching)
        self.pushButton_5.clicked.connect(self.Gamma)
        self.pushButton_6.clicked.connect(self.Image_Bleding)
        self.pushButton_7.clicked.connect(self.Brightness_Constrast)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupButton.setTitle(_translate("MainWindow", "Group Button"))
        self.pushButton.setText(_translate("MainWindow", "Open Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Reverse Image"))
        self.pushButton_3.setText(_translate("MainWindow", "Logarit Transform"))
        self.pushButton_4.setText(_translate("MainWindow", "Contrast Streching"))
        self.pushButton_5.setText(_translate("MainWindow", "Gamma"))
        self.pushButton_6.setText(_translate("MainWindow", "Image Blending"))
        self.pushButton_7.setText(_translate("MainWindow", "Brightness & Constrast"))
        self.groupBox_OriImg.setTitle(_translate("MainWindow", "Original Image"))
        self.groupBox_ImgProcess.setTitle(_translate("MainWindow", "Image processed"))
        self.actionOpen_Image.setText(_translate("MainWindow", "Open Image"))

    def OpenFile(self):
        root = tk.Tk()
        root.withdraw()
        self.file_path = filedialog.askopenfilename()
        if (self.file_path):
            self.label_3.setPixmap(QtGui.QPixmap(self.file_path))
            self.textEdit.setText(self.file_path)
        else:
            self.label_3.setPixmap(QtGui.QPixmap("2021-04-02_205149.png"))

    def Reverse_Image(self):
        filepath = self.textEdit.toPlainText()
        if (filepath == ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error!!!")
            msg.setInformativeText("Please! Choose an Image")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            self.image = cv2.imread(filepath)
            self.reverse_img = 255 - self.image
            self.show_image(self.reverse_img)

    def logarit_transform(self):
        filepath = self.textEdit.toPlainText()
        if (filepath == ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error!!!")
            msg.setInformativeText("Please! Choose an Image")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            self.image = cv.imread(filepath)
            c = 255 / np.log(1 + np.max(self.image))
            self.log_image = c * (np.log(self.image + 1))
            self.log_image = np.array(self.log_image, dtype=np.uint8)
            self.show_image(self.log_image)

    def constrast_streching(self):
        filepath = self.textEdit.toPlainText()
        if (filepath == ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error!!!")
            msg.setInformativeText("Please! Choose an Image")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            self.image = cv.imread(filepath)
            r1 = 70
            s1 = 0
            r2 = 140
            s2 = 255

            def pixelVal(pix, r1, s1, r2, s2):
                if (0 <= pix and pix <= r1):
                    return (s1 / r1) * pix
                elif (r1 < pix and pix <= r2):
                    return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
                else:
                    return ((255 - s2) / (255 - r2)) * (pix - r2) + s2

            # Vectorize the function to apply it to each value in the Numpy array.
            pixelVal_vec = np.vectorize(pixelVal)

            # Apply contrast stretching.
            contrast_stretched = pixelVal_vec(self.image, r1, s1, r2, s2)
            self.log_image = np.array(contrast_stretched, dtype=np.uint8)
            self.show_image(self.log_image)

    def Gamma(self):
        def control(gamma=0.1):
            # getTrackbarPos returns the current
            # position of the specified trackbar.
            gamma = cv2.getTrackbarPos('gamma=N/5',
                                            'GEEK')
            gamma=gamma/5
            result = np.array(255 * (img / 255) ** gamma, dtype='uint8')

            # The function imshow displays an image
            # in the specified window
            self.log_image = np.array(result, dtype=np.uint8)
            self.show_image(self.log_image)
        filepath = self.textEdit.toPlainText()
        if (filepath == ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error!!!")
            msg.setInformativeText("Please! Choose an Image")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            original = cv2.imread(filepath, 1)
            img = original.copy()
            cv2.namedWindow('GEEK')
            cv2.createTrackbar('gamma=N/5',
                               'GEEK', 1, 10,
                               control)
            control(0)
            cv2.waitKey(0)





    def Image_Bleding(self):
        filepath = self.textEdit.toPlainText()
        img1 = cv2.imread(filepath, 1)
        root = tk.Tk()
        root.withdraw()
        self.file_path2 = filedialog.askopenfilename()
        if (self.file_path2):
            img2 = cv2.imread(self.file_path2, 1)
        else:
            img2 = cv2.imread('71.jpg')

        img2 = cv2.resize(img2, img1.shape[1::-1])
        gamma = 0
        dst = cv2.addWeighted(img1, 0.5, img2, 0.5, gamma)
        self.log_image = np.array(dst, dtype=np.uint8)
        self.show_image(self.log_image)

    def Brightness_Constrast(self):

        def controller(img, brightness=255,
                       contrast=127):
            brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))

            contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))

            if brightness != 0:

                if brightness > 0:

                    shadow = brightness

                    max = 255

                else:

                    shadow = 0
                    max = 255 + brightness

                al_pha = (max - shadow) / 255
                ga_mma = shadow

                # The function addWeighted calculates
                # the weighted sum of two arrays
                cal = cv2.addWeighted(img, al_pha,
                                      img, 0, ga_mma)

            else:
                cal = img

            if contrast != 0:
                Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
                Gamma = 127 * (1 - Alpha)

                # The function addWeighted calculates
                # the weighted sum of two arrays
                cal = cv2.addWeighted(cal, Alpha,
                                      cal, 0, Gamma)

            return cal

        def BrightnessContrast(brightness=0):
            # getTrackbarPos returns the current
            # position of the specified trackbar.
            brightness = cv2.getTrackbarPos('Brightness',
                                            'GEEK')

            contrast = cv2.getTrackbarPos('Contrast',
                                          'GEEK')

            effect = controller(img, brightness,
                                contrast)

            # The function imshow displays an image
            # in the specified window
            self.log_image = np.array(effect, dtype=np.uint8)
            self.show_image(self.log_image)

        filepath = self.textEdit.toPlainText()
        original = cv2.imread(filepath, 1)
        img = original.copy()
        cv2.namedWindow('GEEK')
        cv2.createTrackbar('Brightness',
                           'GEEK', 255, 2 * 255,
                           BrightnessContrast)

        # Contrast range -127 to 127
        cv2.createTrackbar('Contrast', 'GEEK',
                           127, 2 * 127,
                           BrightnessContrast)

        BrightnessContrast(0)
        cv2.waitKey(0)

    @QtCore.pyqtSlot()
    def show_image(self, img):
        self.image = img
        self.image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0],
                                  QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.image))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
