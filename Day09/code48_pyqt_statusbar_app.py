import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, Qt, QTime


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 메뉴바 - 액션
        actExit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)
        actExit.setShortcut('Ctrl+Q')  # 단축키지정
        actExit.setStatusTip('앱 종료')
        actExit.triggered.connect(qApp.quit)

        actSave = QAction(QIcon('./Day09/save.png'), 'Save', self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 툴바
        toolbar = self.addToolBar('MainToolBar')    # Toolbar 타이틀은 없어도됨
        toolbar.addAction(actSave)
        toolbar.addAction(actExit)

        # 상태바
        now = QDate.currentDate()   # 현재 날짜
        time = QTime.currentTime()  # 현재 시간
        # print(now.toString('d.M.yy'))
        # print(now.toString('dd.MM.yyyy'))
        # print(now.toString('ddd.MMMM.yyyy'))
        # print(now.toString(Qt.ISODate))
        # print(now.toString(Qt.DefaultLocaleLongDate))
        # self.statusBar().showMessage(now.toString(Qt.DefaultLocaleLongDate))
        self.statusBar().showMessage(now.toString('yyyy-MM-dd') + ' ' + time.toString('hh:mm:ss'))
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        # GUI 화면 설정
        self.setWindowTitle('Bar Window')

        # self.move(1920 // 2 - 200, 1080 // 2 - 100)       # 정중앙 표시
        self.resize(400, 200)
        self.setCenter()
        self.show()     # 핵심

    # 화면 중심 셋팅
    def setCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

