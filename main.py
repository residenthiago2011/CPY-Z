if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets
    import CPY_Z
    from Load import Loop

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CPY_Z.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    Thread = Loop()
    Thread.start()
    Thread.print_CPU(ui)
    Thread.print_Cache(ui)
    app.exec_()

