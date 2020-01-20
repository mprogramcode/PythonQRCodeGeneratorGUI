
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qrcode
from PIL import Image
from PIL.ImageQt import ImageQt

#Generates QRCodes
def QRCodeLookup(QRDATA):

    # Create qr code instance
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 8,
        border = 1,
    )

    # Add data
    qr.add_data(QRDATA)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    #Convert Pilimag Image to Qmap
    ConvtQRImg = ImageQt(img)

    return ConvtQRImg

#Exits the program
def BtnExitClicked():
    sys.exit()

def test():
    print("test")

class Ui_QRCODEAPP(object):
    def setupUi(self, QRCODEAPP):
        QRCODEAPP.setObjectName("QRCODEAPP")
        QRCODEAPP.resize(245, 466)
        self.centralwidget = QtWidgets.QWidget(QRCODEAPP)
        self.centralwidget.setObjectName("centralwidget")
        self.Lookup = QtWidgets.QPushButton(self.centralwidget)
        self.Lookup.setGeometry(QtCore.QRect(60, 290, 121, 61))
        self.Lookup.setObjectName("Lookup")
        self.APP_Quit = QtWidgets.QPushButton(self.centralwidget)
        self.APP_Quit.setGeometry(QtCore.QRect(60, 370, 121, 61))
        self.APP_Quit.setObjectName("APP_Quit")
        self.InputBox = QtWidgets.QLineEdit(self.centralwidget)
        self.InputBox.setGeometry(QtCore.QRect(60, 250, 121, 20))
        self.InputBox.setObjectName("InputBox")
        self.QRDisplayBox = QtWidgets.QLabel(self.centralwidget)
        self.QRDisplayBox.setGeometry(QtCore.QRect(30, 30, 184, 184))
        self.QRDisplayBox.setText("")
        self.QRDisplayBox.setScaledContents(True)
        self.QRDisplayBox.setObjectName("QRDisplayBox")
        QRCODEAPP.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QRCODEAPP)
        self.statusbar.setObjectName("statusbar")
        QRCODEAPP.setStatusBar(self.statusbar)
        self.retranslateUi(QRCODEAPP)
        QtCore.QMetaObject.connectSlotsByName(QRCODEAPP)

    def UpdateQRCode(self):
        #Get Data from QRCODE function and displays it on screen
        self.QRDisplayBox.setPixmap(QtGui.QPixmap.fromImage(QRCodeLookup(self.InputBox.text())))

    def retranslateUi(self, QRCODEAPP):
        _translate = QtCore.QCoreApplication.translate
        QRCODEAPP.setWindowTitle(_translate("QRCODEAPP", "QR Lookup"))
        self.Lookup.setText(_translate("QRCODEAPP", "Lookup QR Code"))
        self.APP_Quit.setText(_translate("QRCODEAPP", "Quit"))

#Start APP Loop
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    QRCODEAPP = QtWidgets.QMainWindow()
    ui = Ui_QRCODEAPP()
    ui.setupUi(QRCODEAPP)

    #Quits the app when the quit button is pressed
    ui.APP_Quit.clicked.connect(BtnExitClicked)

    #Gets data and converts it to a barcode
    ui.Lookup.clicked.connect(ui.UpdateQRCode)

    QRCODEAPP.show()
    sys.exit(app.exec_())


